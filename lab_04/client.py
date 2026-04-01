import asyncio
from tornado.websocket import websocket_connect


async def main():
    url = "ws://localhost:8888/ws"
    print(f"[CLIENT] Connecting to {url}...")

    conn = await websocket_connect(url)
    print("[CLIENT] Connected.")

    while True:
        msg = await conn.read_message()
        if msg is None:
            print("[CLIENT] Connection closed.")
            break
        print(f"[CLIENT] Received: {msg}")


if __name__ == "__main__":
    asyncio.run(main())