import sys
import os

# Set correct Python path (your venv)
INTERP = "/home/themrignayanee/public_html/chatbot/flow-chatbot/venv/bin/python"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Import FastAPI app
from main import app

# Convert ASGI -> WSGI
from asgiref.compatibility import guarantee_single_callable
from asgiref.wsgi import AsgiToWsgi

application = AsgiToWsgi(app)