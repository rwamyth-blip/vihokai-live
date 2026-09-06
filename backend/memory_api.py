from fastapi import FastAPI
from datetime import datetime, timedelta

app = FastAPI()

# Mock DB - replace with Supabase
conversations = [
  {"id":"1","title":"แก้ปัญหาแคปหน้าจอ","user_id":"user1","updated_at": datetime.now()},
  {"id":"2","title":"Debug meta_ai.py syntax error","user_id":"user1","updated_at": datetime.now()},
]

@app.get("/api/conversations")
def get_convs(user_id: str, q: str = ""):
    # Grouping logic - เหมือนรูป
    now = datetime.now()
    result = {"today": [], "yesterday": [], "7days": [], "30days": []}
    for c in conversations:
        if q and q not in c["title"]:
            continue
        diff = (now - c["updated_at"]).days
        if diff == 0:
            result["today"].append(c)
        elif diff == 1:
            result["yesterday"].append(c)
        elif diff <= 7:
            result["7days"].append(c)
        else:
            result["30days"].append(c)
    return result

@app.post("/api/conversations")
def create_conv(title: str, user_id: str):
    # Auto title from first message - เหมือน ChatGPT
    return {"id": "new-id", "title": title[:40], "powered_by": "Vihok AI"}
