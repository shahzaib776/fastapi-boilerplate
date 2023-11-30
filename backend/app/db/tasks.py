from fastapi import FastAPI
from databases import Database
from app.core.config import DATABASE_URL
import logging
 
"""
Initializes a logger with the name of the current module (__name__). 
This logger will be used to output log messages during database connection and disconnection.
"""
logger = logging.getLogger(__name__)
 
async def connect_to_db(app: FastAPI) -> None:
    database = Database(DATABASE_URL, min_size=2, max_size=10)  # these can be configured in config as well
 
    try:
        await database.connect()
        app.state._db = database
    except Exception as e:
        logger.warn("--- DB CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DB CONNECTION ERROR ---")
 
 
async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.disconnect()
    except Exception as e:
        logger.warn("--- DB DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DB DISCONNECT ERROR ---")