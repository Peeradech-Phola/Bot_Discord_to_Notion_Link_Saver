import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from notion_api import save_to_notion
import re
from datetime import datetime  # สำหรับวันที่

# โหลดค่าจากไฟล์ .env
load_dotenv()

# ดึงค่า Token และ Key จาก .env
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# สร้าง intents
intents = discord.Intents.default()
intents.message_content = True

# ตั้งค่าบอท Discord
bot = commands.Bot(command_prefix="!botstn ", intents=intents)

# ฟังก์ชันช่วยแยกเฉพาะ URL จากข้อความ
def extract_url(message_content):
    """
    ดึง URL จากข้อความ
    """
    url_pattern = r'(https?://[^\s]+)'  # Regular Expression สำหรับจับ URL
    match = re.search(url_pattern, message_content)
    return match.group(0) if match else None

# ฟังก์ชันช่วยแยกข้อความ (Content) หลังจาก URL
def extract_content(message_content, url):
    """
    ดึงข้อความที่เหลือหลังจาก URL
    """
    if url:
        return message_content.replace(url, "").strip()
    return message_content.strip()

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now running!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return  # ไม่ตอบสนองต่อข้อความจากบอท

    # ดึงเฉพาะ URL จากข้อความ
    link = extract_url(message.content)
    if link:  # ตรวจสอบว่าเจอ URL หรือไม่
        author = message.author.name
        content = extract_content(message.content, link)  # ดึงข้อความที่เหลือ
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # วันที่และเวลา

        try:
            # บันทึกข้อมูลทั้งหมดลงใน Notion
            save_to_notion(author, link, content, date)
            await message.channel.send(f"✅ Link from {author} has been saved to Notion.")
        except Exception as e:
            await message.channel.send(f"❌ Failed to save the link to Notion. Error: {e}")

# รันบอท
bot.run(DISCORD_BOT_TOKEN)
