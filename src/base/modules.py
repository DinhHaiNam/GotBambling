# -------------------------------------------------------
# Got Bambling Discord Bot
# Copyright (C) Dinh Hai Nam 2026
# License: GPL 3.0
# For more information, see README.md and LICENSE
# -------------------------------------------------------

import os
import sys
import math
import discord
import random
import json
from dotenv import load_dotenv
from discord.ext import commands
from pymongo import *
from pymongo.server_api import ServerApi
from datetime import timedelta, datetime