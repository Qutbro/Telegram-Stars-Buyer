import asyncio
import logging
from client import FragmentClient
from by_satrs.transaction import TonTransaction

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

async def main():
    # Здесь задаём переменные вручнуюЫ
    USERNAME = "@qut_bro"  # Ник получателя
    QUANTITY = 50              # Количество звёзд

    client = FragmentClient()
    recipient = await client.fetch_recipient(USERNAME)
    if recipient:
        req_id = await client.fetch_req_id(recipient, QUANTITY)
        if req_id:
            recipient, amount_nano, la = await client.fetch_buy_link(recipient, req_id, QUANTITY)
            if recipient and amount_nano and la:
                amount_decimal = int(amount_nano) / 1_000_000_000
                logging.info(f"Сумма для отправки: {amount_decimal:.4f} TON")
                transaction = TonTransaction()
                await transaction.send_ton_transaction(recipient, amount_decimal, la, USERNAME)

if __name__ == "__main__":
    asyncio.run(main())
