from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import PlainTextResponse
import httpx


app = FastAPI()

ACCESS_TOKEN = "EAAa0QlEc0yoBQwEzZCeeuZCkHQIKcvv0sKkviQd46LZB2QPM68uv28gjVIzVbGZCpOGWZBHvj3AZCkdbFK4UCGLVN5HPmo6GD5xZBccBOywtI0DAZBFUK9l2Q6u75ZBVHwpIIhcZCNVQvxbbVf7VBwmauVf4FFteWkdyIxgknbdkqc7FisAlOwMsMINcHLSd7U1Nr2jpCxSRhI3HTczQZAZASaF3LxDMhAy7emVJubzomR7rldjAnCbWUpM3ssLLaKMyQq4MfzpOcZBh9awhYnIbNlZA54LCp5"
PHONE_NUMBER_ID = "1039662792560419"
VERIFY_TOKEN = "my_verify_token"

WHATSAPP_URL = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}



 



# ---------------- SEND FUNCTIONS (ASYNC) ---------------- #

async def send_request(payload):
    async with httpx.AsyncClient() as client:
        res = await client.post(WHATSAPP_URL, headers=headers, json=payload)

        # ✅ SUCCESS / ERROR CHECK
        if res.status_code != 200:
            print("❌ ERROR FROM WHATSAPP:")
            print(res.text)
        else:
            print("✅ MESSAGE SENT")

        # ✅ CLEAN BOT OUTPUT LOG
        if payload["type"] == "text":
            print(f"🤖 BOT TEXT: {payload['text']['body']}")

        elif payload["type"] == "interactive":
            print(f"🤖 BOT INTERACTIVE: {payload['interactive']['body']['text']}")

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
                        "reply": {
                            "id": b["id"],
                            "title": b["title"]
                        }
                    } for b in buttons
                ]
            }
        }
    }
    return payload

def send_list(to, text, sections):
    print("📤 SENDING LIST MESSAGE")
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
    return payload
    
def send_text(to, text):
    return {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }

# ---------------- VERIFY ---------------- #

@app.get("/webhook")
def verify(mode: str = None, token: str = None, challenge: str = None):
    if token == VERIFY_TOKEN:
        return PlainTextResponse(challenge)
    return PlainTextResponse("Error")

# ---------------- MAIN HANDLER ---------------- #

async def handle_message(sender, user_msg):

    user_msg = user_msg.strip()

    # -------- LANGUAGE -------- #
    if user_msg.lower() in ["hi", "hello", "start", "hey"]:
        await send_request(send_buttons(sender,
            "Hello! 🙏\nPlease choose your preferred language / कृपया अपनी भाषा चुनें:",
            [
                {"id": "english", "title": "English"},
                {"id": "hindi", "title": "हिन्दी"}
            ]))

    # -------- ENGLISH -------- #

    elif user_msg == "english":
        await send_request(send_list(sender,
    """Welcome to Mrignayanee – An Initiative of Government of Madhya Pradesh 🇮🇳
Explore 100% authentic handloom & handicraft products made by our skilled artisans.
How can I assist you today?""",
    [{
        "title": "Main Menu",
        "rows": [
            {"id": "explore_en", "title": "🛍 Explore Products"},
            {"id": "crafts_en", "title": "🎨 Learn About Crafts"},
            {"id": "reviews_en", "title": "🎥 Watch Reviews"},
            {"id": "order_en", "title": "📦 How to Order"},
            {"id": "gift_en", "title": "🎁 Corporate Gifting"},
            {"id": "seller_en", "title": "🧵 Become Seller"},
            {"id": "support_en", "title": "📞 Support"}
        ]
    }]
))

    elif user_msg == "explore_en":
        await send_request(send_list(sender,
            "Explore a wide range of authentic products:",
            [{
                "title": "Categories",
                "rows": [
                    {"id": "sarees_en", "title": "Sarees & Fabrics"},
                    {"id": "handicraft_en", "title": "Handicrafts"},
                    {"id": "jewelry_en", "title": "Jewelry"},
                    {"id": "decor_en", "title": "Home Decor"},
                    {"id": "all_en", "title": "View All"}
                ]
            }]))

    elif user_msg in ["sarees_en", "handicraft_en", "jewelry_en", "decor_en", "all_en"]:
        await send_request(send_text(sender, "👉 Shop here: https://themrignayanee.com/"))

    elif user_msg == "crafts_en":
        await send_request(send_text(sender,
            "Discover the rich heritage of artisans:\nhttps://www.youtube.com/@MrignayaneeFanClub"))

    elif user_msg == "reviews_en":
        await send_request(send_text(sender,
            "Watch customer reviews:\nhttps://www.youtube.com/@MrignayaneeFanClub"))

    elif user_msg == "order_en":
        await send_request(send_text(sender,
            "1. Visit website\n2. Select product\n3. Add to cart\n4. Checkout\n👉 https://themrignayanee.com/"))

    elif user_msg == "gift_en":
        await send_request(send_text(sender,
            "We offer corporate gifting solutions.\nVisit website for details."))

    elif user_msg == "seller_en":
        await send_request(send_text(sender,
            "Become a seller with us. Visit website for more info."))

    elif user_msg == "support_en":
        await send_request(send_text(sender,
            "Need help? Contact us via website support section."))

    # -------- HINDI -------- #

    elif user_msg == "hindi":
     await send_request(send_list(sender,
        """आपका स्वागत है मृगनयनी में 🇮🇳
मैं आपकी कैसे सहायता कर सकता हूँ?""",
        [{
            "title": "मेनू",
            "rows": [
                {"id": "explore_hi", "title": "🛍 उत्पाद देखें"},
                {"id": "crafts_hi", "title": "🎨 शिल्प जानकारी"},
                {"id": "reviews_hi", "title": "🎥 वीडियो देखें"},
                {"id": "order_hi", "title": "📦 ऑर्डर कैसे करें"},
                {"id": "gift_hi", "title": "🎁 कॉर्पोरेट गिफ्टिंग"},
                {"id": "seller_hi", "title": "🧵 विक्रेता बनें"},
                {"id": "support_hi", "title": "📞 सहायता"}
            ]
        }]
    ))

    elif user_msg == "explore_hi":
        await send_request(send_list(sender,
            "प्रमाणिक उत्पाद देखें:",
            [{
                "title": "श्रेणियाँ",
                "rows": [
                    {"id": "sarees_hi", "title": "साड़ियाँ"},
                    {"id": "handicraft_hi", "title": "हस्तशिल्प"},
                    {"id": "jewelry_hi", "title": "आभूषण"},
                    {"id": "decor_hi", "title": "होम डेकोर"},
                    {"id": "all_hi", "title": "सभी देखें"}
                ]
            }]))

    elif user_msg in ["sarees_hi", "handicraft_hi", "jewelry_hi", "decor_hi", "all_hi"]:
        await send_request(send_text(sender, "👉 यहाँ खरीदें: https://themrignayanee.com/"))

    elif user_msg == "crafts_hi":
        await send_request(send_text(sender,
            "शिल्पकारों की कहानियाँ देखें:\nhttps://www.youtube.com/@MrignayaneeFanClub"))

    elif user_msg == "reviews_hi":
        await send_request(send_text(sender,
            "ग्राहकों की समीक्षा देखें:\nhttps://www.youtube.com/@MrignayaneeFanClub"))

    elif user_msg == "order_hi":
        await send_request(send_text(sender,
            "1. वेबसाइट पर जाएँ\n2. उत्पाद चुनें\n3. कार्ट में जोड़ें\n4. ऑर्डर करें\n👉 https://themrignayanee.com/"))

    elif user_msg == "gift_hi":
        await send_request(send_text(sender,
            "हम कॉर्पोरेट गिफ्टिंग सेवाएँ प्रदान करते हैं।"))

    elif user_msg == "seller_hi":
        await send_request(send_text(sender,
            "विक्रेता बनने के लिए वेबसाइट देखें।  \n 👉 https://themrignayanee.com/"))

    elif user_msg == "support_hi":
        await send_request(send_text(sender,
            "सहायता के लिए वेबसाइट पर संपर्क करें। \n 👉 https://themrignayanee.com/"))

    # -------- SMART TRIGGERS -------- #

    elif "buy" in user_msg.lower():
        await send_request(send_text(sender, "👉 https://themrignayanee.com/"))

    elif "review" in user_msg.lower():
        await send_request(send_text(sender, "👉 https://www.youtube.com/@MrignayaneeFanClub"))

    # -------- INVALID -------- #

    else:
        await send_request(send_buttons(sender,
            "❌ Invalid input. Please choose an option:",
            [
                {"id": "english", "title": "English"},
                {"id": "hindi", "title": "हिन्दी"}
            ]))

# ---------------- WEBHOOK ---------------- #

@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    data = await request.json()

    try:
        value = data["entry"][0]["changes"][0]["value"]

        if "messages" not in value:
            return {"status": "ignored"}

        message = value["messages"][0]
        sender = message["from"]

        if message["type"] == "interactive":

            interactive = message["interactive"]

            if "button_reply" in interactive:
                user_msg = interactive["button_reply"]["id"]
                print(f"\n👤 USER CLICKED BUTTON: {user_msg}")

            elif "list_reply" in interactive:
                user_msg = interactive["list_reply"]["id"]
                print(f"\n👤 USER SELECTED LIST: {user_msg}")

            else:
                print("⚠️ Unknown interactive type")
                return {"status": "ignored"}
        else:
            user_msg = message["text"]["body"]

        background_tasks.add_task(handle_message, sender, user_msg)

    except Exception as e:
        print("Error:", e)

    return {"status": "ok"}