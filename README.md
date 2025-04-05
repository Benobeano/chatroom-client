# chatroom-client
"""
Cross‑platform command‑line client for the chat server.

Defaults:
    HOST = 129.213.136.50
    PORT = 5500

You can still override on the command line:

    python3 client.py                # use defaults
    python3 client.py 1.2.3.4        # custom host
    python3 client.py 1.2.3.4 6500   # custom host + port

Type /quit to exit. Other commands are passed through to the server.
"""

Server repository: https://github.com/Benobeano/chatroom-server
