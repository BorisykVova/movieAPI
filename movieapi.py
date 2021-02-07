import uvicorn
from fastapi import FastAPI

from api.shared import logger
from database import database, configs

logger.logger_configure()
log = logger.get_logger('Movie')

app = FastAPI()


@app.on_event('startup')
async def startup():
    log.info('Setting up database...')
    await database.setup(config=configs.MYSQL_CONFIG)


@app.on_event('shutdown')
async def startup():
    log.info('Shutting down database...')
    await database.shutdown()


if __name__ == '__main__':
    uvicorn.run('movieapi:app', reload=True, port=8001)
