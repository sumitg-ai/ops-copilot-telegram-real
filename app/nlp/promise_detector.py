import re
def detect_promises(text: str, author: str = "unknown"):
    if re.search(r"i'll|due by|by eod", text, re.I):
        return [{"owner": author, "title": text[:50], "due": None}]
    return []
