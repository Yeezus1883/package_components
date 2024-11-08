from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class PackageComponentBase(BaseModel):
    component_name: str

class PackageComponentCreate(PackageComponentBase):
    pass

class PackageComponent(PackageComponentBase):
    id: int
    package_id: int

    class Config:
        from_attributes = True

class PackageBase(BaseModel):
    package_name: str
    display_description: str
    status: str
    candidate_type: str
    check_type: str
    rack_id: int
    created_at: datetime
    updated_at: datetime

class PackageCreate(PackageBase):
    components: List[PackageComponentCreate]

class Package(PackageBase):
    id: int
    components: List[PackageComponent]

    class Config:
        from_attributes = True