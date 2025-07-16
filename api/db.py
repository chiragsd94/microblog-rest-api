from api.config import settings
from databases import Database
from sqlalchemy import MetaData

database = Database(settings.DATABASE_URL)

metadata = MetaData()
