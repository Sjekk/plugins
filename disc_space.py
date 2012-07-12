#!/usr/bin/env python
from optparse import OptionParser
import subprocess
import re
 
parser = OptionParser()
parser.add_option("-w", "--warning", dest="Warning", help="Prozent when the Status is Warning")
parser.add_option("-c", "--critical", dest="Critical", help="Percent when the Status is Critical")
parser.add_option("-d", "--disc", dest="Disc", help="The Name of the Disc")
(optionen, args) = parser.parse_args()
 
p = subprocess.Popen('df | grep "'+optionen.Disc+'"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
firstline = "Unbekannt"
for line in p.stdout.readlines():
        if(firstline=="Unbekannt"):
                firstline = line
regex = re.compile("([0-9]{1,2})\%")
er = regex.findall(firstline)
frei =  int(er[0])
status = "ok"
if(frei > int(optionen.Warning)):
        status="warning"
if(frei > int(optionen.Critical)):
        status="critical"
print "{\"status\": \""+status+"\", \"msg\": \"Used Disc:"+str(frei)+"\"}"
