import os
import json
import urllib2
import socket
import psutil
import time

# Import Requests Library
import requests
 
# Import Blinka
from board import SCL, SDA
import busio
import adafruit_ssd1306

# Import Python Imaging Library
from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw
from font_fredoka_one import FredokaOne

# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load graphic

img = Image.open("./logo.png")
draw = ImageDraw.Draw(img)

# system monitoring from here :
  IP = socket.gethostbyname(socket.gethostname())
  cpu = psutil.cpu_percent()
  memory = psutil.virtual_memory().available * 100 / psutil.virtual_memory().total

# get api data

try:
  f = urllib2.urlopen('http://pi.hole/admin/api.php')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  adsblocked = parsed_json['ads_blocked_today']
  r = requests.get(api_url)
  data = json.loads(r.text)
  DNSQUERIES = data['dns_queries_today']
  ADSBLOCKED = data['ads_blocked_today']
  CLIENTS = data['unique_clients']
  f.close()

except:
  queries = '?'
  adsblocked = '?'
  ratio = '?'

font = ImageFont.truetype(FredokaOne, 20)
font2 = ImageFont.truetype(FredokaOne, 16)

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

draw.text((20,10), "IP: " + str(IP), inky_display.BLACK, font2)
draw.text((00,20), "Clients: " + str(CLIENTS), inky_display.BLACK, font2)
draw.text((10,20), "DNS Queries: " + str(DNSQUERIES), inky_display.BLACK, font2)
draw.text((00,65), "CPU: " + str(cpu), inky_display.BLACK, font2)
draw.text((20,65), "RAM: " + str(memory), inky_display.BLACK, font2)
draw.text((20,20), "Ads Blocked: " + str(adsblocked), inky_display.BLACK, font)
draw.text((40,20), str("%.1f" % round(ratioblocked,2)) + "%", inky_display.BLACK, font)



inky_display.set_image(img)

inky_display.show()
