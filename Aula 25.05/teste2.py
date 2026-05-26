'''Teste de Datetime'''
import datetime
from zoneinfo import ZoneInfo

fuso_BR = ZoneInfo("Australia/Sydney")
x = datetime.datetime.now(fuso_BR)

print(x.strftime("%H:%H"))