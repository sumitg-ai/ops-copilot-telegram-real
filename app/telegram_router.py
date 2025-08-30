from .services.slack_service import get_recent_messages
from .services.notion_service import get_recent_tasks
from .services.digest_service import build_digest
from .nlp.promise_detector import detect_promises

async def handle_update(update: dict) -> str:
    text = (update.get("message", {}).get("text") or "").strip().lower()
    if text.startswith("/start"):
        return "Bot up and running 🚀"
    if text.startswith("/slacktest"):
        msgs = get_recent_messages()
        return f"Slack messages: {len(msgs)}"
    if text.startswith("/notiontest"):
        tasks = get_recent_tasks()
        return f"Notion tasks: {len(tasks)}"
    if text.startswith("/promises"):
        msgs = get_recent_messages()
        detections = [d for m in msgs for d in detect_promises(m['text'], author=m['user'])]
        return f"Promises detected: {len(detections)}"
    if text.startswith("/digest"):
        return build_digest()
    return "Unknown command."
