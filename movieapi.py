import uvicorn
from fastapi import FastAPI

from database import database, configs


app = FastAPI()


@app.on_event('startup')
async def startup():
    await database.setup(config=configs.MYSQL_CONFIG)


@app.on_event('shutdown')
async def startup():
    await database.shutdown()


if __name__ == '__main__':
    uvicorn.run('movieapi:app', reload=True, port=8001)
