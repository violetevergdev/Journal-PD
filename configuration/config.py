import sys
import os
from dynaconf import Dynaconf
from dotenv import load_dotenv

# Функция для получения окружения, если мы в production, то берется из MEIPASS, в develop берется из configuration
def get_env(name):
    load_dotenv()
    env = os.getenv(name)

    if env is None:
        env_path = os.path.join(sys._MEIPASS, '.env')
        load_dotenv(env_path)

        env = os.getenv('ENV_FOR_DYNACONF')
    return env


# Получаем значение окружения
env = get_env('ENV_FOR_DYNACONF')

# Указываем пути конфиг. файлов в зависимости от значения env
if env == 'prod':
    settings_files = ['W:\\!VIOLETTA!\\!fw!\\journal\\settings.toml', 'W:\\!VIOLETTA!\\!fw!\\journal\\.secrets.toml']
else:
    settings_files = ['./configuration/settings.toml', './configuration/.secrets.toml']

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    load_dotenv=True,
    environments=True,
    settings_files=settings_files
)

