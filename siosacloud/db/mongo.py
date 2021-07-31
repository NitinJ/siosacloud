import motor.motor_asyncio
from config.settings import DATABASE

db_client: motor.motor_asyncio.AsyncIOMotorClient = None

async def get_db_client():
    global db_client
    if db_client is None:
        await connect_db()
    return db_client

async def connect_db():
    global db_client
    db_url = DATABASE['default']['url']
    db_client = motor.motor_asyncio.AsyncIOMotorClient(db_url)

async def close_db():
    global db_client
    await db_client.close()
