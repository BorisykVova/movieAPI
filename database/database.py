from tortoise import Tortoise

from config_schemes import DataBaseConfig


async def setup(config: DataBaseConfig):
    await Tortoise.init(config=config.dict())
    await Tortoise.generate_schemas()


async def shutdown():
    await Tortoise.close_connections()
