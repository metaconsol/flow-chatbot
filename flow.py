from send_fuction import send_request, send_buttons, send_list,send_text
from send_fuction import handle_rag,send_image,extract_phone
from db import check_order_in_db

async def handle_message(sender, user_msg):

    user_msg = user_msg.strip()

    # -------- LANGUAGE -------- #

    if user_msg.lower() in ["hi", "hello", "start", "hey"]:

    # 1. Send image first
        await send_request(send_image(
            sender,
            "https://res.cloudinary.com/dxdm610bp/image/upload/v1774256791/WhatsApp_Image_2026-03-23_at_2.25.34_PM_edd4qu_krevqq.jpg",  # <-- replace this
            "Welcome to Mrignayanee! 🇮🇳\nAuthentic Handloom & Handicrafts"
        ))

        # 2. Then send buttons
        await send_request(send_buttons(sender,
            "Please choose your preferred language / कृपया अपनी भाषा चुनें:",
            [
                {"id": "english", "title": "English"},
                {"id": "hindi", "title": "हिन्दी"}
            ]))

    # -------- ENGLISH -------- #

    elif user_msg == "english":
        await send_request(send_list(sender,
    """Welcome to Mrignayanee An Initiative of Government of Madhya Pradesh 🇮🇳
Explore 100% authentic handloom & handicraft products made by our skilled artisans.
How can I assist you today?""",
    [{
        "title": "Main Menu",
        "rows": [
            {"id": "explore_en", "title": "🛍 Explore Products"},
            {"id": "crafts_en", "title": "🎨 Learn About Crafts"},
            {"id": "reviews_en", "title": "🎥 Watch Reviews"},
            {"id": "order_en", "title": "📦 How to Order"},
            {"id":"track_order","title":"🛍 track order"},
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
    
    elif user_msg == "track_order":
        await send_request(send_text(sender,
            "👉 Please enter your 10 digit registered number"))

    elif user_msg == "gift_en":
        await send_request(send_text(sender,
            "We offer corporate gifting solutions.\nVisit website for details."))

    elif user_msg == "seller_en":
        await send_request(send_text(sender,
            "Become a seller with us. Visit website for more info."))

    elif user_msg == "support_en":
        await send_request(send_text(sender,
            "Need help? Contact us via website support section.\n👉 https://themrignayanee.com/contact"))

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


      
    elif extract_phone(user_msg):

        phone = extract_phone(user_msg)
        print("FINAL PHONE:", phone)

        order = check_order_in_db(phone)

        if order:
            order_id = order["id"]

            recent_order_url = f"https://themrignayanee.com/account/orders/{order_id}"
            all_orders_url = "https://themrignayanee.com/account/orders"

            # 🔥 Direct links (clickable in WhatsApp)
            await send_request(send_text(sender,
                f"""Track your order!

    📦 Recent Order:
    {recent_order_url}

    📋 All Orders:
    {all_orders_url}
    """))

        else:
            await send_request(send_text(sender,
                "No order found with this number. Please try again."))

    # -------- INVALID -------- #
    else:
        rag_response = handle_rag(user_msg)

        if rag_response:
            await send_request(send_text(sender, rag_response))

            await send_request(send_list(sender,
    "If you want to go back select option 👇",
    [
        {
            "title": "Main Menu",
            "rows": [
                {"id": "english", "title": "English"},
                {"id": "hindi", "title": "हिन्दी"}
            ]
        }
    ]
))

        else:
            await send_request(send_buttons(sender,
                "Invalid input. Please choose an option:",
                [
                    {"id": "english", "title": "English"},
                    {"id": "hindi", "title": "हिन्दी"}
                ]))





