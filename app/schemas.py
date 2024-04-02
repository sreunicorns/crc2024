from pydantic import BaseModel


class ApplicationSchema(BaseModel):
    id: str
    app_name: str
    app_version: str
    ip_address: str
    release_date: str


class HealthCheck(BaseModel):
    status: str
