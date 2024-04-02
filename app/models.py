from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Application(Base):
    __tablename__ = "applications"
    id = Column(String, primary_key=True)
    app_name = Column(String)
    app_version = Column(String)
    ip_address = Column(String)
    release_date = Column(String)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id}, name={self.app_name}, version={self.app_version}, ip={self.ip_address}, release={self.release_date})>"
