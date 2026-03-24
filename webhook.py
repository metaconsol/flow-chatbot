from flow import handle_message

async def process_webhook(data, background_tasks):

    value = data["entry"][0]["changes"][0]["value"]

    if "messages" not in value:
        return

    message = value["messages"][0]
    sender = message["from"]

    if message["type"] == "interactive":
        interactive = message["interactive"]

        if "button_reply" in interactive:
            user_msg = interactive["button_reply"]["id"]
            print(f"👤 BUTTON: {user_msg}")

        elif "list_reply" in interactive:
            user_msg = interactive["list_reply"]["id"]
            print(f"👤 LIST: {user_msg}")

        else:
            return

    else:
        user_msg = message["text"]["body"]
        print(f"👤 TEXT: {user_msg}")

    background_tasks.add_task(handle_message, sender, user_msg)