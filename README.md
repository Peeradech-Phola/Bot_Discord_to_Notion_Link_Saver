```markdown
# Notion Link Saver Bot

This project is a Discord bot that captures URLs shared in a Discord channel and saves them to a Notion database. The bot also captures additional text messages and saves them along with the link.

## Features
- Detects URLs shared in Discord messages.
- Saves the link along with the associated text content to a Notion database.
- Logs the current date and time when the link is saved.

## Prerequisites
Before using the bot, make sure you have the following:
- A Discord bot token.
- A Notion API key and a Notion database ID.

## Installation

### Step 1: Clone the repository
Clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/notion-link-saver.git
cd notion-link-saver
```

### Step 2: Install dependencies
Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### Step 3: Configure environment variables
Create a `.env` file in the root directory of the project and add your Discord bot token and Notion API details:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
NOTION_API_KEY=your_notion_api_key
NOTION_DATABASE_ID=your_notion_database_id
```

### Step 4: Run the bot
Run the bot using the following command:

```bash
python bot.py
```

Once the bot is running, it will listen for any messages containing a URL and will save the link along with the associated text content to your Notion database.

## How it works
1. The bot listens for messages in Discord channels.
2. When a message containing a URL is detected, the bot:
   - Extracts the URL from the message.
   - Extracts any content following the URL.
   - Saves both the URL and the content to a Notion database.
   - Saves the current date and time when the link is saved.
   
## Notion Database Setup
In order for this bot to work, you need to create a database in Notion with the following properties:
- **Title** (Type: Title)
- **Link** (Type: URL)
- **Date** (Type: Date)
- **Content** (Type: Rich Text)

## Troubleshooting
- **Error: Failed to save the link to Notion**  
  Ensure that your Notion API key and database ID are correct. Double-check the database property names in Notion to ensure they match the bot's expectations.
