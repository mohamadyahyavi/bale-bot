class BaleClient:

    async def send_message(self, user_id: str, text: str):
          print(f"[Bale] {user_id}: {text}")