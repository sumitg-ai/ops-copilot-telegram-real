from slack_sdk import WebClient
import os

client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))

def get_recent_messages(channel_id: str = None, limit: int = 10):
    if not channel_id:
        channel_id = os.getenv("SLACK_CHANNEL_ID")
    response = client.conversations_history(channel=channel_id, limit=limit)
    return [{"user": m.get("user", "unknown"), "text": m.get("text", ""), "ts": m.get("ts")} for m in response["messages"]]
