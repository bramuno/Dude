#!/bin/python
import os, sys, json, subprocess, smtplib, datetime, time, pdb
from email.message import EmailMessage
# pull conifg data from config.json file
f = open("/home/brain/config.json", "r")
try:
    get = json.load(f)
except:
    sys.exit("Config.json load failed.\n")
#
f.close()
petName = get['petName']
folderName =  get['folderName']
logfileName =  get['logfileName']
statusFileName =  get['statusFileName']
max =  int(get['maxF'])
min =  int(get['minF'])
maxDuration =  int(get['maxDuration'])
emailDestination =  get['emailDestination']
SMTPuser =  get['SMTPuser']
SMTPpass =  get['SMTPpass']
SMTPserver =  get['SMTPserver']
SMTPport =  int(get['SMTPport'])
SMS =  get['SMS']
SMScarrier =  int(get['SMScarrier'])
#
debug = 0
car=["@vtext.com","@txt.att.net","@sms.myboostmobile.com","@tmomail.net","@sms.cricketwireless.net","@messaging.sprintpcs.com" ]
smsEmailDest = SMS+car[SMScarrier]
logfile = folderName+"/"+logfileName
statusFile = folderName+"/"+statusFileName
cmd = "mkdir -p "+str(folderName)
subprocess.check_output(cmd, shell=True)

f = open(statusFile, "r")
try:
    get = json.load(f)
    try:
        oldState =  int(get['state'])
        oldDur = float(get['duration'])
        lastSeen = int(get['lastSeen'])
        newfile = 0
    except:
        print("nope")
except:
    get = ""
    oldStatus = ""
    oldState =  ""
    oldDur = ""
    lastSeen = 0
    dur = 0
    if debug == 1:
        print("JSON load failed.\n")

if oldDur < 0:
    oldDur = 0

oldStatus = f.read()
f.close()
if oldStatus == "" and oldState == "" and oldDur == "":
    newfile = 1

if debug == 1: 
    print("oldState = "+str(oldState))
    print("oldDur = "+str(oldDur))
    print("max = ",str(max))
    print("min = ",str(min))
    print("maxDuration = ",str(maxDuration))
    print("newfile = ",str(newfile))

# open data log
f = open(logfile, "r")
read = f.read()
f.close()
# clear data log
f = open(logfile, "w")
f.write("")
f.close()
#
state = 1
data = read.split("\n")
lines = len(data)
now = datetime.datetime.now()
lastEvent = data[lines-2]
nowEpoch = int(datetime.datetime.now().timestamp())
chk = lastEvent.split(" ")
readTime = chk[0]+" "+chk[1]+" "+chk[2]
mo=str(chk[0])
months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
a = mo.strip()[:3].lower()
year = now.year
minute = now.strftime('%M')
month = months[a]
day=int(chk[1])
splTime = chk[2].split(":")
hour=int(splTime[0])
min=int(splTime[1])
sec=int(splTime[2])
logEpoch = int(datetime.datetime(year, month,day, hour, min, sec).timestamp())
diffEpoch = nowEpoch - lastSeen
secSinceLastLog = nowEpoch - logEpoch
minsSinceLastLog = round((secSinceLastLog/60),1)
if diffEpoch < 0:
    diffEpoch = 0;

if int(secSinceLastLog) < 0:
    secSinceLastLog = 0

diffMins = float(round(diffEpoch/60,2))
temp=chk[4].split(",")
if ( float(temp[0]) > float(max) and float(temp[1]) > float(max) ) or ( float(temp[0]) < float(min) and float(temp[1]) < float(min) )  :
    state = 0

avg = ( float(temp[0]) + float(temp[1]) ) /2
avg = round(avg,1)
if int(state) == 1:
    newDur = round(diffMins, 1)
else:
    newDur = round((oldDur + diffMins), 1)

# offline sensor alert
if round(minsSinceLastLog,0) > 5 and int(minute)%5 == 0:
    msgMissing = EmailMessage()
    msgMissing.set_content("No contact from temperature sensor harness in "+str(minsSinceLastLog)+" minutes.\nPlease check it is online and batteries are charged.\nReboot if needed.\n\nsent:"+str(year)+"-"+str(month)+"-"+str(day)+" "+str(hour)+":"+str(minute)+":"+str(sec)+"\n")
    msgMissing['Subject'] = "No contact from temperature sensor"
    msgMissing['From'] = emailDestination
    msgMissing['To'] = emailDestination+","+smsEmailDest
    server = smtplib.SMTP_SSL(SMTPserver, SMTPport)
    server.connect(SMTPserver,SMTPport)
    server.ehlo()
    server.login(SMTPuser, SMTPpass)
    server.send_message(msgMissing)
    server.quit()
    if debug == 1:
        print(">>>>> email alert sent")  

########## critical temperature alert begin
if ( int(oldState) == 0 and int(oldDur) > float(maxDuration-1) ) :
    alert = 1
    msgCritical = EmailMessage()
    msgCritical.set_content("\nHarness temperature outside desired threshold for at least "+str(oldDur)+" minutes.\nsensorA="+str(float(temp[0]))+"\nsensorB:"+str(float(temp[1]))+"\n\n"+str(oldState)+"==0 &&"+str(oldDur)+">"+str(maxDuration)+"\n")
    msgCritical['Subject'] = petName+" has been in ~"+str(avg)+" temperature for at least "+str(oldDur)+" minutes!"
    msgCritical['From'] = emailDestination
    msgCritical['To'] = emailDestination+","+smsEmailDest
    server = smtplib.SMTP_SSL(SMTPserver, SMTPport)
    server.connect(SMTPserver,SMTPport)
    server.ehlo()
    server.login(SMTPuser, SMTPpass)
    server.send_message(msgCritical)
    server.quit()
    if debug == 1:
        print(">>>>> email alert sent")  
########## critical temperature alert end
#
## alert sensor online but reading incorrectly
if float(temp[0]) < -60 or float(temp[1]) < -60:
    glitchMSG = EmailMessage()
    glitchMSG.set_content("\nA sensor is not reading correctly:\nsensorA="+str(float(temp[0]))+"\nsensorB:"+str(float(temp[1]))+"\n")
    glitchMSG['Subject'] = 'A sensor is not reading correctly'
    glitchMSG['From'] = "alert@temperatureMon.org"
    glitchMSG['To'] = emailDestination+","+smsEmailDest
    server = smtplib.SMTP_SSL(SMTPserver, SMTPport)
    server.connect(SMTPserver,SMTPport)
    server.ehlo()
    server.login(SMTPuser, SMTPpass)
    server.send_message(glitchMSG)    
    server.quit()
#
if debug == 1:
    print("temp[0] = ",str(temp[0]))
    print("temp[1] = ",str(temp[1]))
    print("state = ",str(state))
    print("nowEpoch = ",str(nowEpoch))
    print("lastSeen = ",str(lastSeen))
    print("diffEpoch = ",str(diffEpoch))
    print("diffMins = ",str(diffMins))
    print("newDur = ",str(newDur))
    print("minsSinceLastLog = ",str(minsSinceLastLog))
    print("minute = ",str(minute))
#
if newfile == 1:
    output = '{"lastSeen":"'+str(nowEpoch)+'","state":"'+str(state)+'","duration":"0" }'
    if debug == 1:
        print("\nnewfile\n")
else:
    if state == 0:
        output = '{"lastSeen":"'+str(logEpoch)+'","state":"'+str(state)+'","duration":"'+str(newDur)+'" }'
    else:
        output = '{"lastSeen":"'+str(logEpoch)+'","state":"'+str(state)+'","duration":"0"}'
#
if debug == 1:
    print(output)
#
f = open(statusFile, "w")
f.write(output)
f.close()
sys.exit()
