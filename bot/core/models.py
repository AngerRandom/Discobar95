from tortoise import exceptions, fields, models, signals, timezone, validators
from enum import IntEnum
from datetime import datetime, timedelta
import discord

class DiscordSnowflakeValidator(validators.Validator):
    def __call__(self, value: int):
        if not 17 <= len(str(value)) <= 19:
            raise exceptions.ValidationError("Discord IDs are between 17 and 19 characters long")

class OperatingSystemType(IntEnum):
  PROGRESSBAR = 1
  BAROS = 2
  PROGRESSBAR_SERVER = 3
  HIDDEN = 4
  EIGHT_BIT = 5

class OperatingSystem(models.Model):
  id = fields.IntField(primary_key=True)
  name = fields.CharField(
    max_length=64, 
    description="Name of the operating system",
    unique=True
  )
  type = fields.IntEnumField(
    OperatingSystemType,
    description="Type of the operating system",
    default=OperatingSystemType.PROGRESSBAR
  )
  custom = fields.BooleanField(
    description="If enabled, the oprerating system will be listed in custom operating systems.", 
    default=False
  )
  pro_level = fields.IntField(
    description="Amount of levels required to reach Pro rank",
    validators=[validators.MaxValueValidator(99), validators.MinValueValidator(1)],
  )
  bonus_points = fields.IntField(
    description="Bonus points an operating system can give per level clear",
    default=0
  )
  box_image = fields.CharField(
    max_length=200,
    description="Image asset of the box"
  )
  logo_image = fields.CharField(
    max_length=200,
    description="Image asset of the logo"
  )
  wallpapers = fields.JSONField(
    description="JSON object of wallpapers of the operaring system",
    default={},
    null=True
  )

class Player(models.Model):
  discord_id = fields.BigIntField(
    description="Discord user ID of the player",
    unique=True,
    validators=[DiscordSnowflakeValidator()]
  )
  
  
