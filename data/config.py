from dataclasses import dataclass
from pathlib import Path
from typing import List

from environs import Env


# Параметр frozen=True защищает экземпляры класса от случайного изменения
@dataclass(frozen=True)
class DataBaseConfig:
    user: str
    password: str
    host: str
    database: str


@dataclass(frozen=True)
class TgBot:
    token: str
    admin_ids: List[int]
    support_ids: List[int]
    timezone: str
    ip: str
    I18N_DOMAIN: str


@dataclass(frozen=True)
class Miscellaneous:
    secret_key: str
    yandex_api_key: str
    qiwi_key: str
    phone_number: str
    secret_p2p_key: str


@dataclass(frozen=True)
class Config:
    tg_bot: TgBot
    db: DataBaseConfig
    misc: Miscellaneous


def load_config() -> Config:
    env = Env()
    env.read_env()

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            support_ids=list(map(int, env.list("SUPPORTS"))),
            ip=env.str("IP"),
            timezone=env.str("TIMEZONE"),
            I18N_DOMAIN='dating'
        ),
        db=DataBaseConfig(
            user=env.str('DB_USER'),
            password=env.str('DB_PASS'),
            host=env.str('DB_HOST'),
            database=env.str('DB_NAME'),
        ),
        misc=Miscellaneous(
            secret_key=env.str("SECRET_KEY"),
            yandex_api_key=env.str('API_KEY'),
            qiwi_key=env.str("QIWI_KEY"),
            phone_number=env.str("PHONE_NUMBER"),
            secret_p2p_key=env.str("SECRET_P2"),
        )
    )


BASE_DIR = Path(__file__).parent.parent
LOCALES_DIR = BASE_DIR / 'locales'
