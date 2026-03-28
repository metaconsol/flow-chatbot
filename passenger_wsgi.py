import sys, os
from asgiref.wsgi import WsgiToAsgi

# Set correct python path
INTERP = "/home/themrignayanee/pulic_html/chatbot/flow-chatbot/venv/bin/python"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Import your FastAPI app
from main import app

# Convert ASGI → WSGI
application = WsgiToAsgi(app)