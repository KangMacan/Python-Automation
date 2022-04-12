# $language = "python"
# $interface = "1.0"

# This python script is to automate our manual config stuff

# Author : KangMacan - IP RAN
# Modified by : KangMacan
# 2022-04 | Mark-01

import datetime
import os

dtn = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

# // OSSERA Variables //
#host = "10.175.1.150"
# host = "10.175.1.151"
# -----------------------------------------------------------------------------
# user = "20337132"
# passwd = "NTTfit89!"
rsa_key = "-o StrictHostKeyChecking=no "

# Credential Lab
user = "cisco"
passwd = "cisco123!"

Host = """ 
192.168.239.130
192.168.239.131
192.168.239.132
""".strip().splitlines()


# Command_XE = open('command_xe.txt','r')
# Command_XR = open('command_xr.txt')
# Command_NX = open('command_nx.txt')

Command_XE = ["show platform", "show cdp neig","show clock"]
Command_XR = ["show interface desc", "show interface brief", "show cdp neig", "show arp","show clock"]
Command_NX = ["show interface desc", "show ip interface brief", "show interface status", "show cdp neig", "show ip arp","show clock"]

Script_Type = crt.Dialog.Prompt ("Choose Script Type: \n 1= Running Script IOS-XE \n 2= Running Script IOS-XR \n 3= Running Script NX-OS")

# -----------------------------------------------------------------------------
def Main():
    vPossibleResponses = [\
        "-->",
        "$",
        "(yes/no)?",
        "(yes/no/[fingerprint])?",
        "name:",
        "ogin:",
        "sword:",
        ">",
        "Permission denied",
        "incorrect",
        "No route to host"]


    crt.Screen.Synchronous = True
    for host_name in Host:
        # cmd = "/SSH2 /L %s /PASSWORD %s /C 3DES /M MD5 %s" % (user, passwd, host)
        # crt = crt.Session.ConnectInTab(cmd)
        
        crt.Screen.Send("ssh " +rsa_key+user+"@" + host_name + chr(13))
        while True:
            crt.Screen.WaitForStrings(vPossibleResponses)
            if crt.Screen.MatchIndex > 0:
                strStringFound = vPossibleResponses[crt.Screen.MatchIndex - 1]

            if crt.Screen.MatchIndex == 1 or crt.Screen.MatchIndex == 2:
                return True

            elif crt.Screen.MatchIndex == 3 or crt.Screen.MatchIndex == 4:
                crt.Screen.Send("yes\r")
                
            elif crt.Screen.MatchIndex == 5 or crt.Screen.MatchIndex == 6:
                crt.Screen.Send(user + "\r")

            elif crt.Screen.MatchIndex == 7:
                crt.Screen.Send(passwd + "\r")
                crt.Screen.Send("enable\r")
                crt.Screen.WaitForString("word:")
                crt.Screen.Send(passwd + "\r")
                crt.Screen.Send("\r\r\r")
                return True
                
            elif crt.Screen.MatchIndex == 8:
                crt.Screen.Send("enable\r")
                crt.Screen.WaitForString("word:")
                crt.Screen.Send(passwd + "\r")
                crt.Screen.Send("\r\r\r")

            elif crt.Screen.MatchIndex == 9:
                crt.Screen.Send("\003")
            else:
                crt.Session.SetStatusText("Unhandled " + strStringFound)
                crt.Screen.SendSpecial("MENU_SCRIPT_CANCEL")
            return True

        if Script_Type == "1":
            crt.Screen.WaitForString("#")
            for command_iosxe in Command_XE:
                crt.Screen.Send(command_iosxe + chr(13))
                crt.Screen.WaitForString("#")
        
        if Script_Type == "2":
            for command_iosxr in Command_XR:
                crt.Screen.Send(command_iosxr + chr(13))
                crt.Screen.WaitForString("#")

        if Script_Type == "3":
            for command_nxos in Command_NX:
                crt.Screen.Send(command_nxos + chr(13))
                crt.WaitForString("#")
        crt.Screen.Send("exit" + chr(13))
        crt.Screen.WaitForString("$")
Main()

# if Script_Type == "1":
#     for host_name in Host:
#         # crt.Session.LogFileName = "D:\TSEL\Activity\Logg SecureCRT\%s_%s.log" % (host_name, dtn)
#         # crt.Session.Log(True)
#         crt.Screen.Synchronous = True
#         crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
#         crt.Screen.WaitForString("Password:")
#         crt.Screen.Send(passwd + chr(13))
#         crt.Screen.WaitForString(">")
#         crt.Screen.Send("enable" + chr(13))
#         crt.Screen.WaitForString("Password:")
#         crt.Screen.Send(passwd + chr(13))
#         crt.Screen.WaitForString("#")
#         crt.Screen.Send("ter len 0" + chr(13))    
#         crt.Screen.WaitForString("#")
#         for command_iosxe in Command_XE:
#             crt.Screen.Send(command_iosxe + chr(13))
#             crt.Screen.WaitForString("#")
#         crt.Screen.Send("exit" + chr(13))
#         crt.Screen.WaitForString("$")

# if Script_Type == "2":
#     for host_name in Host:
#         # crt.Session.LogFileName = "D:\TSEL\Activity\Logg SecureCRT\%s_%s.log" % (host_name, dtn)
#         # crt.Session.Log(True)
#         crt.Screen.Synchronous = True
#         crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
#         crt.Screen.WaitForString("Password:")
#         crt.Screen.Send(passwd + chr(13))
#         crt.Screen.WaitForString("#")
#         for command_iosxr in Command_XR:
#             crt.Screen.Send(command_iosxr + chr(13))
#             crt.Screen.WaitForString("#")

# if Script_Type == "3":
#     for host_name in Host:
#         # crt.Session.LogFileName = "D:\TSEL\Activity\Logg SecureCRT\%s_%s.log" % (host_name, dtn)
#         # crt.Session.Log(True)
#         crt.Screen.Synchronous = True
#         crt.Screen.Send("ssh "+rsa_key+user+"@" + host_name + chr(13))
#         crt.Screen.WaitForString("Password:")
#         crt.Screen.Send(passwd + chr(13))
#         crt.Screen.WaitForString("#")
#         for command_nxos in Command_NX:
#             crt.Screen.Send(command_nxos + chr(13))
#             crt.Screen.WaitForString("#")