import os
import random
import sys
import subprocess
from datetime import datetime
from time import sleep

logTag = ['ERR','DEBUG','INFO']

while True:
    currentEvent = random.choice(logTag)
    now = str(datetime.now())
    sys.stdout = open('app.log','a')
    print now + ' ' + currentEvent + ' : sSekarang sedang ' + currentEvent +' pesan kesalahan'
    sleep(1)