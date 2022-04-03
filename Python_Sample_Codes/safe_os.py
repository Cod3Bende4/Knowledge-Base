'''
Applications that execute operating system commands or execute commands that interact with the underlying system should neutralize any externally-provided values used in those commands. Failure to do so could allow an attacker to include input that executes unintended commands or exposes sensitive data.

The problem could be mitigated in any of the following ways:

Using subprocess module without the shell=true. In this case subprocess expects an array where command and arguments are clearly separated.
Escaping shell argument with shlex.quote

https://rules.sonarsource.com/python/RSPEC-2076

'''
'''
Non-Complaint Code
from flask import request
import subprocess

@app.route('/ping')
def ping():
    address = request.args.get("address")
    cmd = "ping -c 1 %s" % address
    subprocess.Popen(cmd, shell=True) # Noncompliant; using shell=true is unsafe
'''

''''Valid Code
import subprocess

user_input_string = "ping "+input()

subprocess.Popen(user_input_string,
    shell=True,
    stdin=subprocess.PIPE
).communicate(user_input_string.encode())

'''

import subprocess

def isValidIP(s):
 
    # check number of periods
    if s.count('.') != 3:
        return False

    l = list(map(str, s.split('.')))
 
    # check range of each number between periods
    for ele in l:
        if int(ele) < 0 or int(ele) > 255 or (l[0]=='0' and len(l)!=1):
            return False
    return True

def ping():
    address = input("give me an IP: ")
    if isValidIP(address):
        args = ["ping", "-c1", address]
        subprocess.Popen(args) # Compliant
    else:
        print("Enter a valid IP!")

ping()