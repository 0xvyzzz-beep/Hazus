import os
import subprocess
import colorama
import time

def clear():
    if os.name == "nt":
        subprocess.Popen("cls", shell=True)
        time.sleep(0.1)
    else:
        print("\033c")
        time.sleep(0.1)

def menu():
    print (colorama.Fore.RED + """
                        __   __ __   __  ____
                        \ \ / / \ \ / / |_  /
                         \ V /   \ V /   / / 
                          \_/     |_|   /___|
                                             """)
    print ("https://discord.gg/udUpvtMzb8")

async def asynccprint(text, type):
    if type == 0:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.GREEN + "Success" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 1:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Error" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 2:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.YELLOW + "Warn" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 3:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Hazus" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)

def cprint(text, type):
    if type == 0:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.GREEN + "Success" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 1:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Error" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 2:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.YELLOW + "Warn" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 3:

        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Hazus" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
