import asyncio
import random
import tornado.web
import tornado.websocket

clients = set()
fruits = ["Táo", "Cam", "Xoài", "Chuối", "Nho", "Dưa hấu"]


class FruitWebSocket(tornado.websocket.WebSocketHandler):
    def check_origin(self, origin):
        return True

    def open(self):
        clients.add(self)
        print(f"[SERVER] Client connected. Total: {len(clients)}")

    def on_close(self):
        clients.discard(self)
        print(f"[SERVER] Client disconnected. Total: {len(clients)}")

    def on_message(self, message):
        print(f"[SERVER] Received: {message}")


def make_app():
    return tornado.web.Application([
        (r"/ws", FruitWebSocket),
    ])


async def send_fruits():
    while True:
        fruit = random.choice(fruits)
        print(f"[SERVER] Sending: {fruit}")

        disconnected = []
        for client in clients:
            try:
                client.write_message(fruit)
            except Exception:
                disconnected.append(client)

        for client in disconnected:
            clients.discard(client)

        await asyncio.sleep(3)


async def main():
    app = make_app()
    app.listen(8888)
    print("[SERVER] Running at ws://localhost:8888/ws")

    asyncio.create_task(send_fruits())
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())