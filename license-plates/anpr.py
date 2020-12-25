import json
from openalpr import Alpr

alpr = Alpr("us", "/etc/openalpr/openalpr.conf", "/usr/share/openalpr/runtimedata")
results = alpr.recognizefile("/home/pi/ea7the.jpg")
print(json.dumps(results, indent=4))
alpr.unload()