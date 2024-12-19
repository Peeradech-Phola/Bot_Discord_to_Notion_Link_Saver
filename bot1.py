import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from notion_api import save_to_notion
import re
import google.generativeai as genai
from bs4 import BeautifulSoup
from datetime import datetime  # สำหรับวันที่
import requests

# โหลดค่าจากไฟล์ .env
load_dotenv()

API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")

# ตั้งค่า Google Generative AI
genai.configure(api_key=API_KEY)

# ดึงค่า Token และ Key จาก .env
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# สร้าง intents
intents = discord.Intents.default()
intents.message_content = True

# ตั้งค่าบอท Discord
bot = commands.Bot(command_prefix="!botstn ", intents=intents)

def extract_tags_with_ai_google(message_content, url=None):
    """
    สร้างแท็กอัตโนมัติโดยใช้ Google Gemini Model และเนื้อหา URL (ถ้ามี)
    """
    import requests
    from bs4 import BeautifulSoup

    # เก็บแท็กจากข้อความที่มีอยู่
    predefined_tags = re.findall(r'#\w+', message_content)

    # ดึงเนื้อหา URL ถ้ามี
    url_content = ""
    if url:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                title = soup.title.string if soup.title else ""
                meta_desc = soup.find('meta', attrs={"name": "description"})
                meta_desc_content = meta_desc["content"] if meta_desc else ""
                url_content = f"Title: {title}\nDescription: {meta_desc_content}"
        except Exception as e:
            print(f"Error fetching URL content: {e}")

    # รวมข้อความและเนื้อหา URL เพื่อส่งให้โมเดล AI
    combined_content = (
        f"Message: {message_content}\n"
        f"URL Content: {url_content}\n\n"
        "Generate 3-5 concise, relevant, and descriptive tags for this content, separated by commas."
    )

    try:
        # เรียกใช้ Google Generative AI
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(combined_content)

        # แปลงข้อความที่ AI สร้างเป็นลิสต์ของแท็ก
        ai_generated_tags = response.text.split(",")  # แยกตามเครื่องหมายจุลภาค
        ai_generated_tags = [tag.strip() for tag in ai_generated_tags if tag.strip()]  # ลบช่องว่างและฟิลเตอร์
        ai_generated_tags = [tag[:100] for tag in ai_generated_tags if len(tag) <= 100]  # จำกัดความยาวแท็ก
    except Exception as e:
        print(f"Error generating tags with Google AI: {e}")
        ai_generated_tags = []

    # รวมแท็กทั้งหมด (ลบซ้ำ)
    all_tags = list(set(predefined_tags + ai_generated_tags))
    return all_tags[:5]  # จำกัดจำนวนแท็กที่ส่งออก


# ฟังก์ชันช่วยแยกข้อความที่ไม่ใช่ tag
def extract_content_without_tags(message_content, tags):
    """
    ลบ tag และ URL ออกจากข้อความและคืนข้อความที่เหลือ
    """
    # ลบ tags
    for tag in tags:
        message_content = message_content.replace(tag, "")  # ลบ tag

    # ลบ URL ออกจากข้อความ
    url_pattern = r'(https?://[^\s]+)'  # Regular Expression สำหรับจับ URL
    message_content = re.sub(url_pattern, "", message_content)

    return message_content.strip()  # คืนข้อความที่เหลือหลังจากลบ tag และ URL


# ฟังก์ชันช่วยแยก URL จากข้อความ
def extract_url(message_content):
    """
    ดึง URL จากข้อความ
    """
    url_pattern = r'(https?://[^\s]+)'  # Regular Expression สำหรับจับ URL
    match = re.search(url_pattern, message_content)
    return match.group(0) if match else None

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # ไม่ตอบสนองต่อข้อความจากบอท

    # ดึง URL จากข้อความ
    link = extract_url(message.content)
    if link:  # ตรวจสอบว่าเจอ URL หรือไม่
        author = message.author.name
        tags = extract_tags_with_ai_google(message.content, link)  # ใช้ฟังก์ชันใหม่
        content = extract_content_without_tags(message.content, tags)  # ดึงข้อความที่เหลือหลังจากลบ tag
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # วันที่และเวลา

        try:
            # บันทึกข้อมูลทั้งหมดลงใน Notion
            save_to_notion(author, link, content, tags, date)
            await message.channel.send(f"✅ Link from {author} has been saved to Notion.")
        except Exception as e:
            await message.channel.send(f"❌ Failed to save the link to Notion. Error: {e}")


# รันบอท
bot.run(DISCORD_BOT_TOKEN)

