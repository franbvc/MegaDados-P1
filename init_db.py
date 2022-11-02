from sqlalchemy import create_engine
from orm import Base
import os
from dotenv import load_dotenv

load_dotenv()

engine = create_engine(os.environ["DB_URL"], echo=True)

Base.metadata.create_all(engine)
