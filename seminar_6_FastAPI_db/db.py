import sqlalchemy
import databases
from sqlalchemy import create_engine
from settings import settings

DATABASE_URL = settings.DATABASE_URL
# В лекции было так:
# DATABASE_URL = "sqlite:///mydatabase.db"
# сейчас же ЭТО внесено в файл .env (его создали вручную),
# а уже из него тянет информацию load_dotenv() в файле settings, а из него уже импорт сюда.
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(32)),
    sqlalchemy.Column("password", sqlalchemy.String(32)),
)
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)
