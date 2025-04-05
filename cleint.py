import socket
import threading
import sys

DEFAULT_HOST = "129.213.136.50"
DEFAULT_PORT = 5500

HOST = DEFAULT_HOST
PORT = DEFAULT_PORT

# Allow optional overrides
if len(sys.argv) >= 2:
    HOST = sys.argv[1]
if len(sys.argv) >= 3:
    PORT = int(sys.argv[2])


def receive_loop(sock: socket.socket):
    """Continuously receive messages from server and print them."""
    try:
        while True:
            data = sock.recv(1024)
            if not data:
                print("\n*** Disconnected from server ***")
                break
            print(data.decode("utf-8"), end="")
    except OSError:
        pass


def send_loop(sock: socket.socket):
    """Read user input from stdin and send to server."""
    try:
        while True:
            try:
                line = input()
            except EOFError:
                break
            if line.strip() == "/quit":
                sock.sendall(b"/quit\n")
                break
            sock.sendall((line + "\n").encode("utf-8"))
    finally:
        sock.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.connect((HOST, PORT))
        except ConnectionRefusedError:
            print("Unable to connect – is the server running?")
            return
        print(f"Connected to {HOST}:{PORT}. Type /join <room> to get started.")

        # start threads
        threading.Thread(target=receive_loop, args=(sock,), daemon=True).start()
        send_loop(sock)
        print("Connection closed.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
