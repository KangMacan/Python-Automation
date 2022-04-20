# $language = "python"
# $interface = "1.0"

# This python script is to automate our manual config stuff

# Author : KangMacan - IP RAN
# Modified by : KangMacan
# 2022-04 | Mark-02

import datetime
import os

# Add timestamp on file
dtn = datetime.datetime.now().strftime("%d%m%Y_%H-%M")


# Credential & Bypass RSA Key
user = "cisco"
passwd = "cisco123!"
rsa_key = "-o StrictHostKeyChecking=no "

# List IP Address/Hostname from file
Hosts = open("device.txt","r").readlines()

# Command List read from file
Command_XE = open('command_xe.txt','r').readlines()
Command_XR = open('command_xr.txt','r').readlines()
Command_NX = open('command_nx.txt','r').readlines()

# Pop Up Dialog Window
Action = crt.Dialog.Prompt ("Choose Script Type: \n 1 ==> Running Script IOS-XE \n 2 ==> Running Script IOS-XR \n 3 ==> Running Script NX-OS")

# -----------------------------------------------------------------------------

def main():
    if Action == "1":
        for host_name in Hosts:
            crt.Session.LogFileName = "D:\Python\Logg SecureCRT\%s_%s.log" % (host_name.strip(), dtn)
            crt.Session.Log (True)
            crt.Screen.Synchronous = True
            crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
            crt.Screen.WaitForString("Password:")
            crt.Screen.Send(passwd + chr(13))
            crt.Screen.WaitForString(">")
            crt.Screen.Send("enable" + chr(13))
            crt.Screen.WaitForString("Password:")
            crt.Screen.Send(passwd + chr(13))
            crt.Screen.WaitForString("#")
            crt.Screen.Send("ter len 0" + chr(13))    
            crt.Screen.WaitForString("#")
            for command_iosxe in Command_XE:
                crt.Screen.Send(command_iosxe + chr(13))
                crt.Screen.WaitForString("#")
            crt.Screen.Send("exit" + chr(13))
            crt.Screen.WaitForString("$")
            crt.Session.Log (False)
            

    if Action == "2":
        for host_name in Hosts:
            crt.Session.LogFileName = "D:\Python\Logg SecureCRT\%s_%s.log" % (host_name.strip(), dtn)
            crt.Session.Log(True)
            crt.Screen.Synchronous = True
            crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
            crt.Screen.WaitForString("Password:")
            crt.Screen.Send(passwd + chr(13))
            crt.Screen.WaitForString("#")
            crt.Screen.Send("ter len 0" + chr(13))    
            crt.Screen.WaitForString("#")
            for command_iosxr in Command_XR:
                crt.Screen.Send(command_iosxr + chr(13))
                crt.Screen.WaitForString("#")
            crt.Screen.Send("exit" + chr(13))
            crt.Screen.WaitForString("$")
            crt.Session.Log (False)


    if Action == "3":
        for host_name in Hosts:
            crt.Session.LogFileName = "D:\Python\Logg SecureCRT\%s_%s.log" % (host_name.strip(), dtn)
            crt.Session.Log(True)
            crt.Screen.Synchronous = True
            crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
            crt.Screen.WaitForString("Password:")
            crt.Screen.Send(passwd + chr(13))
            crt.Screen.WaitForString("#")
            crt.Screen.Send("ter len 0" + chr(13))    
            crt.Screen.WaitForString("#")
            for command_nxos in Command_NX:
                crt.Screen.Send(command_nxos + chr(13))
                crt.Screen.WaitForString("#")
            crt.Screen.Send("exit" + chr(13))
            crt.Screen.WaitForString("$")
            crt.Session.Log (False)
main()