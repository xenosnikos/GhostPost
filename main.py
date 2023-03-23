import asyncio
from app import app
from database import persist_todb
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

async def main():
    await persist_todb()
    print("Data generated successfully!")


if __name__ == "__main__":
    asyncio.run(main())
