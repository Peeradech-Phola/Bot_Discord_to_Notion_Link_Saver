from datetime import datetime
import os  # เพิ่มการนำเข้า datetime หากยังไม่ได้
import requests

def save_to_notion(author, link, content, tags, date):
    """
    บันทึก URL, ข้อความ, tag และวันที่ลงใน Notion
    """
    NOTION_API_KEY = os.getenv("NOTION_API_KEY")
    NOTION_DATABASE_ID = os.getenv("NOTION_DATABASE_ID")
    notion_api_url = "https://api.notion.com/v1/pages"
    headers = {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"  # ใช้ API เวอร์ชันล่าสุด
    }

    # เปลี่ยนวันที่ให้เป็นรูปแบบที่ Notion รองรับ
    formatted_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # รูปแบบของวันที่ที่ Notion รองรับ
    valid_tags = [tag for tag in tags if len(tag) <= 100]

    # สร้างข้อมูลสำหรับบันทึกลงในฐานข้อมูล
    page_data = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Title": {  # Property ชื่อ Title
                "title": [
                    {
                        "text": {"content": f"Link shared by {author}"}
                    }
                ]
            },
            "Link": {  # Property ชื่อ Link
                "url": link
            },
            "Date": {  # Property ชื่อ Date
                "date": {"start": formatted_date}  # แก้ไขให้ใช้วันที่ที่ถูกต้อง
            },
            "Content": {  # Property ชื่อ Content
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": content}
                    }
                ]
            },
            "Tags": {  # Property ชื่อ Tags
                "multi_select": [{"name": tag} for tag in valid_tags]   # แปลง tag เป็น list ของ dictionary
            }
        }
    }

    # ส่งข้อมูลไปยัง Notion API
    response = requests.post(notion_api_url, headers=headers, json=page_data)

    # ตรวจสอบผลลัพธ์
    if response.status_code == 200:
        print("Successfully saved to Notion!")
    else:
        raise Exception(f"Failed to save to Notion. Error: {response.text}")
