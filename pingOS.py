#!/usr/bin/env python3
 
#Every OS has a different TTL for their ICMP packets, so we can use that value to determine the host's operating system.
#But that value can be changed so this method of judgment is not necessarily accurate.

 
import sys, subprocess, re
 
def pingTo(targetIP):
 
   pingToTarget = subprocess.Popen([f"ping -c 1 {targetIP} 2>/dev/null"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
   output, errors = pingToTarget.communicate()
 
   return output.decode("utf-8"), errors
 
def whichOS(targetPingOutput):
   ttlWithLetters = str(re.findall("ttl=\d{1,3}", targetPingOutput))
 
   if ttlWithLetters == "[]":
       return "Host unreachable!"
 
   else:
       try:
           ttl = int(re.findall("\d{1,3}", ttlWithLetters)[0])
      
       except IndexError:
           print("index error at whichOS function")
           return "Insert a valid IP address!"
 
   if ttl <= 254 and ttl > 128:
       return f"Target host is running Solaris/AIX.\nTTL = {ttl}"
      
   elif ttl <= 64 and ttl > 1:
       return f"Target host is running Linux/Unix.\nTTL = {ttl}"
  
   elif ttl <=128 and ttl > 64:
       return f"Target host is running Windows ttl.\nTTL = {ttl}"
 
try : #Program start
   targetIP = sys.argv[1]  #If IP address was passed to the script assign it to a variable
 
   if re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", targetIP): #check if its a correct IP address with regex
 
       try:
           pingOutput = pingTo(targetIP)[0]   #Store output of ping command to the target IP
           print(whichOS(pingOutput))
 
       except IndexError:
           print("Insert a valid IP address!")
 
   else:
       print("Insert a valid IP address!")
 
except IndexError:
   print("Usage -> python3 pingOS.py <ipAddress>")