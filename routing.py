# mysite/routing.py
from channels.auth import AuthMiddlewareStack # (Channels docs tutorial, page 19)
from channels.routing import ProtocolTypeRouter, URLRouter # (Channels docs tutorial, page 19)
import chat.routing # (Channels docs tutorial, page 19)

"""
The root routing configuration below ('websocket') specifies that when a connection is made to the Channels development server, the
ProtocolTypeRouter will first inspect the type of connection. If it is a WebSocket connection (ws:// or wss://),
the connection will be given to the AuthMiddlewareStack.
"""

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack( # (Channels docs tutorial, page 20)
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})