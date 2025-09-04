from pathlib import Path
import discord
import logging
from discord.ext import commands
import asyncpg
import asyncio

if not Path("config.py").exists():
  print("[WARNING] Configuration file not found. Please generate it by running the config generator.")
else:
  import config

intents = discord.Intents.default()
intents.message_content = True


if not config.prefix:
  print("[WARNING] Bot text prefix is missing. Please set it in config.py.")
  return
