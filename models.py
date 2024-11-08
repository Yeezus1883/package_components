# app/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base

class Package(Base):
    __tablename__ = "packages"
    
    id = Column(Integer, primary_key=True, index=True)
    package_name = Column(String, index=True)
    display_description = Column(String)
    status = Column(String)
    candidate_type = Column(String)
    check_type = Column(String)
    rack_id = Column(Integer)
    created_at = Column(String)
    updated_at = Column(String)

    components = relationship("PackageComponent", back_populates="package")


class PackageComponent(Base):
    __tablename__ = "package_components"
    
    id = Column(Integer, primary_key=True, index=True)
    package_id = Column(Integer, ForeignKey("packages.id"))
    component_name = Column(String)

    package = relationship("Package", back_populates="components")
