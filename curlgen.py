# generated curl commands from secret

import re
from datetime import datetime, timedelta

with open('secret.txt', 'r') as file:
    curl = file.read()

years = 9
days = years * 365
step = 90
steps = days / step

def format(d):
    return d.strftime('%Y-%m-%d')

def out(d):
    s = curl.replace('curl', 'curl -s')
    s = re.sub(r"end_date=\d{4}-\d{2}-\d{2}", 'end_date=%s' % format(d), s)
    s = re.sub(r"start_date=\d{4}-\d{2}-\d{2}", 'start_date=%s' % format(d - timedelta(days=step)), s)
    print repr(s)

start = datetime.now()
out(start)

for i in range(0, steps):
    start -= timedelta(days=step)
    out(start)
