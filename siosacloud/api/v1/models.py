from uuid import UUID
from pydantic import BaseModel

class LicenseModel(BaseModel):
    license_key: UUID
    muid: str