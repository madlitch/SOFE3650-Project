from tables import metadata
from sqlalchemy import text

import databases
import sqlalchemy
import constants

DATABASE_URL = "postgresql://{}:{}@localhost:{}/{}".format(
    constants.DATABASE_USER,
    constants.DATABASE_KEY,
    constants.DATABASE_PORT,
    constants.DATABASE_DB)


database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL, echo=False)
metadata.create_all(engine)




