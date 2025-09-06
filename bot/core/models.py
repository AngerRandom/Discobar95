from tortoise import exceptions, fields, models, signals, timezone, validators
from enum import IntEnum
from datetime import datetime, timedelta
import discord

class OperatingSystemType(IntEnum):
  PROGRESSBAR = 1
  BAROS = 2
  PROGRESSBAR_SERVER = 3
  HIDDEN = 4
  EIGHT_BIT = 5

class OperatingSystem(models.Model):
  id = fields.IntField(primary_key=True)
  name = fields.CharField(max_length=64, description="Name of the operating system")
  type = fields.IntEnumField(
    OperatingSystemType,
    description="Type of the operating system",
    default=OperatingSystemType.PROGRESSBAR
  )
  custom = fields.BooleanField(
    description="If enabled, the oprerating system will be listed in custom operating systems.", 
    default=False
  )
  
  
