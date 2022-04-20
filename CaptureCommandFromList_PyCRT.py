# $language = "python"
# $interface = "1.0"

# This python script is to automate our manual config stuff

# Author : KangMacan
# Modified by : KangMacan
# 2022-04 | Mark-01

import datetime
import os

dtn = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")


# Credential & Bypass RSA Key
user = "cisco"
passwd = "cisco123!"
rsa_key = "-o StrictHostKeyChecking=no "

Host = """ 
192.168.239.130
192.168.239.131
192.168.239.132
""".strip().splitlines()


Command_XE = ["show interface desc", "show ip interface brief", "show platform", "show cdp neig", "show ip arp", "show clock"]
Command_XR = ["show interface desc", "show interface brief", "show cdp neig", "show arp","show clock"]
Command_NX = ["show interface desc", "show ip interface brief", "show interface status", "show cdp neig", "show ip arp","show clock"]

Script_Type = crt.Dialog.Prompt ("Choose Script Type: \n 1= Running Script IOS-XE \n 2= Running Script IOS-XR \n 3= Running Script NX-OS")

# -----------------------------------------------------------------------------

if Script_Type == "1":
    for host_name in Host:
        crt.Session.LogFileName = "D:\Python\Logg SecureCRT\%s_%s.log" % (host_name, dtn) #Need to be edited with your own path
        crt.Session.Log(True)
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

if Script_Type == "2":
    for host_name in Host:
        crt.Session.LogFileName = "D:\TSEL\Activity\Logg SecureCRT\%s_%s.log" % (host_name, dtn) #Need to be edited with your own path
        crt.Session.Log(True)
        crt.Screen.Synchronous = True
        crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
        crt.Screen.WaitForString("Password:")
        crt.Screen.Send(passwd + chr(13))
        crt.Screen.WaitForString("#")
        for command_iosxr in Command_XR:
            crt.Screen.Send(command_iosxr + chr(13))
            crt.Screen.WaitForString("#")

if Script_Type == "3":
    for host_name in Host:
        crt.Session.LogFileName = "D:\TSEL\Activity\Logg SecureCRT\%s_%s.log" % (host_name, dtn) #Need to be edited with your own path
        crt.Session.Log(True)
        crt.Screen.Synchronous = True
        crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
        crt.Screen.WaitForString("Password:")
        crt.Screen.Send(passwd + chr(13))
        crt.Screen.WaitForString("#")
        for command_nxos in Command_NX:
            crt.Screen.Send(command_nxos + chr(13))
            crt.Screen.WaitForString("#")
