from tortoise import Tortoise, run_async
from connection import connect_to_db


async def main():
    await connect_to_db()
    await Tortoise.generate_schemas()

if __name__ == '__main__':
    run_async(main())
