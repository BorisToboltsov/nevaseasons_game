from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class Sentry:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    sentry: Sentry


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(token=env("API_TOKEN_TELEGRAM")),
        sentry=Sentry(token=env("API_TOKEN_SENTRY")),
    )
