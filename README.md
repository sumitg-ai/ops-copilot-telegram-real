# Ops Co-Pilot — Telegram MVP (Slack + Notion Digest)

This project demonstrates a Telegram MVP bot that integrates Slack + Notion and produces a daily digest.

## 1. Run in Mock Mode (No Credentials Needed)
Mock mode simulates Slack and Notion APIs for demo purposes.

### Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
curl http://localhost:8000/healthz
```

### Test Commands
Use curl POST requests with `/start`, `/slacktest`, `/notiontest`, `/promises`, `/digest today`.

## 2. Run in Real Mode (Slack + Notion APIs)
Real mode calls Slack + Notion APIs using credentials provided in `.env`.

### Setup
1. Copy `.env.sample` → `.env`
2. Fill in values for:
   ```ini
   TELEGRAM_BOT_TOKEN=123456:your-telegram-token
   SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
   SLACK_CHANNEL_ID=C123456789
   NOTION_API_KEY=secret_xxxxx
   NOTION_DATABASE_ID=aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
   ```
3. Ensure Slack bot is invited to the channel and Notion integration has DB access.

### Run
```bash
uvicorn app.main:app --reload --port 8000
curl http://localhost:8000/healthz
```

### Commands (real mode)
- `/slacktest` → last 10 Slack messages
- `/notiontest` → last 5 Notion tasks
- `/promises` → detect commitments + task creation
- `/digest today` → daily digest summary
