from pathlib import Path
import discord
import logging
from discord.ext import commands
import asyncpg
import asyncio
import sys
import traceback

if not Path("./config.py").exists():
  print("[WARNING] Configuration file not found. Please generate it by running the config generator.")
  sys.exit(1)
else:
  import config

intents = discord.Intents.default()
intents.message_content = True


if not config.prefix:
  print("[WARNING] Bot text prefix is missing. Please set it in config.py.")
  sys.exit(1)
bot = commands.Bot(command_prefix=config.prefix, intents=intents)
bot.db_pool = asyncpg.Pool = None

async def init_db():
  if not config.database_url:
    print("[WARNING] Database URL not found! Please set it in config.py.")
    sys.exit(1)
  else:
    try:
        bot.db_pool = await asyncpg.create_pool(dsn=config.database_url)
        print("[INFO] Database is ready.")
    except Exception as e:
        print("[ERROR] Failed to connect to database.")
        traceback.print_exception(type(e), e, e.__traceback__, file=sys.stderr)
        sys.exit(1) 
