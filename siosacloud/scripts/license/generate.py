from db.mongo import connect_db, get_db_client, close_db
import uuid

async def generate_licenses(count: int = 1):
    client = await get_db_client()
    licenses = [
        {'license_key': str(uuid.uuid4())}
        for _ in range(count)
    ]
    db = client.test
    l = await db.license.insert_many(licenses)
    client.close()
