from api.config import settings
from databases import Database

database = Database(settings.DATABASE_URL)
