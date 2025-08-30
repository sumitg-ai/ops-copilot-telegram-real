from notion_client import Client
import os

notion = Client(auth=os.getenv("NOTION_API_KEY"))
DB_ID = os.getenv("NOTION_DATABASE_ID")

def get_recent_tasks(limit: int = 5):
    results = notion.databases.query(database_id=DB_ID, page_size=limit)
    tasks = []
    for r in results["results"]:
        title = ""
        if "Name" in r["properties"] and r["properties"]["Name"]["title"]:
            title = r["properties"]["Name"]["title"][0]["text"]["content"]
        status = None
        if "Status" in r["properties"] and r["properties"]["Status"]["select"]:
            status = r["properties"]["Status"]["select"]["name"]
        tasks.append({"id": r["id"], "title": title, "status": status})
    return tasks
