import httpx
from config import WHATSAPP_URL, HEADERS
import re
from db import check_order_in_db

client = httpx.AsyncClient()

async def send_request(payload):
    res = await client.post(WHATSAPP_URL, headers=HEADERS, json=payload)

    if res.status_code != 200:
        print("❌ ERROR:", res.text)
    else:
        print("✅ SENT")

def send_text(to, text):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    print(f"🤖 BOT: {text}")
    return (payload)

def send_buttons(to, text, buttons):
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "button",
            "body": {"text": text},
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": b
                    } for b in buttons
                ]
            }
        }
    }
    print(f"🤖 BOT BUTTON: {text}")
    return (payload)

def send_list(to, text, sections):
    print("📤 LIST SENT")

    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "interactive",
        "interactive": {
            "type": "list",
            "body": {"text": text},
            "action": {
                "button": "View Options",
                "sections": sections
            }
        }
    }
    print(f"🤖 BOT LIST: {text}")
    return (payload)


from rag import get_context ,initialize_vector_db
from agent import generate_response

def send_image(to, image_url, caption=""):
    return {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "image",
        "image": {
            "link": image_url,
            "caption": caption
        }
    }


vector_db = initialize_vector_db()

def handle_rag(user_msg):
    try:
        context = get_context(vector_db, user_msg)

        # Safety check
        if not context or len(context.strip()) < 20:
            return None

        response = generate_response(
            user_message=user_msg,
            order_data="",
            context=context
        )

        return response

    except Exception as e:
        print("RAG Error:", e)
        return None
    




def extract_phone(msg):
    msg = msg.strip()
    
    # allow only digits
    if msg.isdigit() and len(msg) == 10:
        return "+91" + msg  

    return None


