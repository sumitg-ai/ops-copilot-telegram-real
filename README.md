Got it 👍 — here’s the cleaned-up, well-formatted **README.md content** for your **real repo**. I’ve applied all the formatting fixes, consistent section titles, and clarified dev vs client usage.

---

# Ops Co-Pilot — Telegram MVP (Slack + Notion Digest)

This project demonstrates a Telegram MVP bot that integrates Slack + Notion and produces a daily digest.

---

## Run in Real Mode (Slack + Notion APIs)

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

3. **Integration Requirements**

   * **Slack**

     * The Slack app must have scopes: `channels:history`, `channels:read`, `users:read`.
     * The bot user must be invited to the target channel (e.g., `#Kandy`).
   * **Notion**

     * The Notion integration must be shared with the database.
     * The database must include at least: `Name` (title), `Status` (select).
     * `Due` (date) and `Owner` (people) are optional but recommended.

---

### Run

```bash
uvicorn app.main:app --reload --port 8000
curl http://localhost:8000/healthz
```

---

### Bot Commands (Real Mode)

These are the commands end-users can run directly inside the Telegram app:

* `/slacktest` → last 10 Slack messages
* `/notiontest` → last 5 Notion tasks
* `/promises` → detect commitments + task creation
* `/digest today` → daily digest summary

---

### Curl Test Commands (Developer Only)

These commands are for developers/IT to test the backend locally.
In real mode, the outputs depend on live Slack and Notion data.

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

Example output:

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

### End-to-End Flow (with Telegram UI)

The client interacts **only through Telegram UI** (on phone or desktop app).

Example flow in production:

1. User opens Telegram, types `/digest today` in the chat with the bot.
2. Telegram → sends a webhook POST to your FastAPI server (`/telegram/webhook`).
3. Your code processes it → calls Slack API + Notion API → generates digest.
4. Response goes back to Telegram → user sees digest in chat.

---

### Deployment Note

Deploy your FastAPI app on a **public HTTPS-capable host** (AWS ECS, App Runner, or EC2 with SSL).
Ensure port `8000` (or whichever you configure) is accessible over HTTPS.

---

### Telegram Webhook Setup

Once the FastAPI app is deployed on a public HTTPS endpoint, register the webhook with Telegram:

1. Make sure you have your **Telegram Bot Token** (from BotFather).
2. Deploy your FastAPI app and note the public URL. Example:

   ```
   https://yourdomain.com/telegram/webhook
   ```
3. Register the webhook:

   ```bash
   curl -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/setWebhook \
     -d "url=https://yourdomain.com/telegram/webhook"
   ```
4. Verify webhook is set:

   ```bash
   curl https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/getWebhookInfo
   ```

   You should see your webhook URL and `last_error_date` = 0 if successful.

---

### Pro Tips

* If you redeploy to a different host, re-run the `setWebhook` command with the new URL.
* To disable the webhook temporarily:

  ```bash
  curl -X POST https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/deleteWebhook
  ```
* End-users must **open the bot in Telegram and click “Start”** once before using commands.

---

Would you like me to also prepare the **Mock repo README** in the same polished style (so both repos look consistent when your IT team reads them)?
