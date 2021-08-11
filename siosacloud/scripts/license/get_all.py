from db.mongo import connect_db, get_db_client, close_db
from pprint import pprint
import uuid

async def get_licenses(count: int = 1):
    client = await get_db_client()
    licenses = {'muid': {'$exists': False}}
    db = client.test
    l = await db.license.find(licenses).limit(count).to_list(count)
    pprint(l)
    client.close()
