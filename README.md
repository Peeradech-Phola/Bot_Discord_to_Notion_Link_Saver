```markdown
# Discord Bot with Notion Integration

This project is a Discord bot that integrates with Notion to save shared URLs, context, tags, and timestamps. It uses Google's Gemini API to generate accurate tags from the content.

## Features
- Detects URLs shared in Discord messages.
- Extracts tags using AI-powered tagging (Google Gemini API).
- Saves content, tags, and URLs to a Notion database.
- Automatically includes the timestamp.

---

## Requirements

Make sure you have Python installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file with the following variables:

```plaintext
DISCORD_BOT_TOKEN=your_discord_token
NOTION_API_KEY=your_notion_api_key
NOTION_DATABASE_ID=your_notion_database_id
GENAI_API_KEY=your_gemini_api_key
```

1. Get DISCORD_BOT_TOKEN:

To get your Discord bot token, follow these steps:

    Go to the Discord Developer Portal.
    Click on New Application and give it a name.
    Under your application, navigate to the Bot section.
    Click on Add Bot and then Yes, do it! to confirm.
    Scroll down to Token, click Copy. This is your DISCORD_BOT_TOKEN.

2. Get NOTION_API_KEY:

To get your Notion API key, follow these steps:

    Go to the Notion Developers Portal.
    Click on Create new integration.
    Give your integration a name and save.
    After creating the integration, you will get an Integration Token. This is your NOTION_API_KEY.
    Make sure the integration has access to your workspace.

3. Get NOTION_DATABASE_ID:

To get your Notion database ID, follow these steps:

    Open your Notion workspace and navigate to the database you want to use.
    In the URL, you will see a long string after your workspace name. This string is your database ID.
        For example, in the URL https://www.notion.so/yourworkspace/Database-Name-123abc456def, the database ID is 123abc456def.

4. Get GENAI_API_KEY:

To get your Gemini API key, follow these steps:

    Go to the Google Generative AI API Portal.
    Enable the Gemini API for your Google Cloud project.
    Create an API key by following the instructions on the API documentation page.
    Copy the API key and set it as GENAI_API_KEY.
    
Replace the placeholders with your actual tokens and IDs.

---

## Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/discord-notion-bot.git
cd discord-notion-bot
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run the Bot

```bash
python bot1.py
```

---

## Usage

1. Invite the bot to your Discord server.
2. Send a message containing a URL in any channel the bot has access to.
3. The bot will:
   - Extract the URL.
   - Generate tags using the content of the URL or message.
   - Save the data (URL, tags, content, and timestamp) to your Notion database.

Example Discord Message:
```plaintext
Check out this amazing tool! https://example.com 
```

Result in Notion:
- **Title**: Link shared by Username
- **Content**: `Check out this amazing tool!`
- **Link**: `https://example.com`
- **Tags**: `AI`, `Tech`
- **Date**: Timestamp of when the message was sent.

---
