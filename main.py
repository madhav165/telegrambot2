import asyncio
import telegram
from dotenv import load_dotenv

def configure():
    load_dotenv()

async def main():
    configure
    bot = telegram.Bot("TOKEN")
    async with bot:
        print(await bot.get_me())


if __name__ == '__main__':
    asyncio.run(main())