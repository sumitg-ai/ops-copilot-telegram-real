from .slack_service import get_recent_messages
from .notion_service import get_recent_tasks
from app.nlp.promise_detector import detect_promises

def build_digest() -> str:
    slack_msgs = get_recent_messages(limit=10)
    notion_tasks = get_recent_tasks(limit=5)

    promises = [d for m in slack_msgs for d in detect_promises(m['text'], author=m['user'])]
    num_promises = len(promises)
    overdue_tasks = [t for t in notion_tasks if t['status'] == "Todo"]
    num_overdue = len(overdue_tasks)
    recent = slack_msgs[:3]

    lines = ["*Digest (Today)*", ""]
    lines.append(f"- Slack Promises: {num_promises}")
    for p in promises[:3]:
        lines.append(f"   • @{p['owner']}: {p['title']}")
    if num_promises > 3:
        lines.append(f"   … and {num_promises - 3} more")
    lines.append("")
    lines.append(f"- Overdue Notion Tasks: {num_overdue}")
    for t in overdue_tasks[:2]:
        lines.append(f"   • {t['title']} (due: mock-date)")
    if num_overdue > 2:
        lines.append(f"   … and {num_overdue - 2} more")
    lines.append("")
    lines.append(f"- Recent #Kandy messages:")
    for m in recent:
        lines.append(f"   • @{m['user']}: {m['text']}")
    if len(slack_msgs) > 3:
        lines.append(f"   … and {len(slack_msgs) - 3} more")
    return "\n".join(lines)
