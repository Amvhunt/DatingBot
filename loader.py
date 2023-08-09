from typing import Any

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from glQiwiApi import QiwiWrapper
from nudenet import NudeDetector, NudeClassifier

from data.config import load_config
from functions.main_app.language_ware import setup_middleware
from utils.YandexMap.api import Client
from utils.db_api.postgres import Database

bot = Bot(token=load_config().tg_bot.token, parse_mode=types.ParseMode.HTML)
storage = RedisStorage2() if load_config().tg_bot.use_redis else MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
client = Client(api_key=load_config().misc.yandex_api_key)
wallet = QiwiWrapper(
    api_access_token=load_config().misc.qiwi_key,
    phone_number=load_config().misc.phone_number,
    secret_p2p=load_config().misc.secret_p2p_key
)
job_defaults = dict(coalesce=False, max_instances=3)
scheduler = AsyncIOScheduler(
    timezone=load_config().tg_bot.timezone,
    job_defaults=job_defaults
)

detector = NudeDetector()
classifier = NudeClassifier()

i18n = setup_middleware(dp)
_: Any = i18n.gettext
