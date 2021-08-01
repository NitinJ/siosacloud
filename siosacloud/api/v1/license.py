from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from pydantic.types import Json
from starlette.status import HTTP_201_CREATED
from . import models
import logging
from db.mongo import get_db_client

logger = logging.getLogger('fastapi')

license_router = APIRouter(
    prefix="/licenses"
)

@license_router.post("/register")
async def register_client(body: models.LicenseModel):
    client = await get_db_client()
    db = client.test
    license_key = str(body.license_key)
    record = await db.license.find_one(
        {
            'license_key': license_key,
            'muid': {'$exists': False}
        }
    )
    if not record:
        return JSONResponse(
            {
                "message": "license_key is invalid"
            },
            status_code=status.HTTP_400_BAD_REQUEST
        )
    record = await db.license.update_one(
        {'license_key': license_key},
        {
            "$set": {
                "muid": body.muid,
                "valid_until": ""
            }
        }
    )
    print(record)
    return JSONResponse(
        {
            "message": "Registration Successful"
        },
        status_code=HTTP_201_CREATED
    )

@license_router.post("/verify")
async def verfiy_client(body: models.LicenseModel):
    client = await get_db_client()
    db = client.test
    license = str(body.license_key)
    record = await db.license.find_one({
        'license_key': license,
        'muid': body.muid
    })
    if record:
        return {"verified": True}
    return JSONResponse(
        {
            "verified": False
        },
        status_code=status.HTTP_401_UNAUTHORIZED
    )
