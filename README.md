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

---

Test Commands (Mock or Real mode)

**1. `/start` — sanity check**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/start"}}' \
  | jq -r '.message'
```

**2. `/slacktest` — last 10 Slack messages**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/slacktest"}}' \
  | jq -r '.message'
```

**3. `/notiontest` — last 5 Notion tasks**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/notiontest"}}' \
  | jq -r '.message'
```

**4. `/promises` — detect commitments**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/promises"}}' \
  | jq -r '.message'
```

**5. `/digest today` — daily digest summary**

```bash
curl -s -X POST http://127.0.0.1:8000/telegram/webhook \
  -H "Content-Type: application/json" \
  -d '{"message":{"chat":{"id":"123"},"text":"/digest today"}}' \
  | jq -r '.message'
```

```
*Digest (Today)*

- Slack Promises: 10
   • @alice: I'll send the report by Friday
   • @bob: Will push new code by EOD
   • @carol: Due by 9/15
   … and 7 more

- Overdue Notion Tasks: 2
   • Update Campaign Metrics (due: 8/29)
   • Review SOP Draft (due: 8/28)

- Recent #Kandy messages:
   • @dave: Any blockers on deployment?
   • @emma: Running tests now
   • @frank: PR merged 
   … and 7 more
```

---




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
