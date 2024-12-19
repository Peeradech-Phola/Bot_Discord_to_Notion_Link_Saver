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
- **Link**: `https://example.com`
- **Tags**: `AI`, `Tech`
- **Content**: `Check out this amazing tool!`
- **Date**: Timestamp of when the message was sent.

---

## Development

Feel free to modify the bot's behavior by editing `bot1.py` or the Notion API integration. 

### Notes
1. Replace `yourusername/discord-notion-bot` with the actual repository name.
2. Include clear instructions for setting up and running the bot.
3. Add badges (optional) for build status, license, or other useful information.
