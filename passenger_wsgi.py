import sys
import os

INTERP = "/home/themrignayanee/public_html/chatbot/flow-chatbot/env_mrignayanee/bin/python"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add project path
sys.path.insert(0, "/home/themrignayanee/public_html/chatbot/flow-chatbot")

# Import FastAPI app
from main import app

# Convert ASGI → WSGI
from asgiref.wsgi import AsgiToWsgi

application = AsgiToWsgi(app)