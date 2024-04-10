import os
import sys
import subprocess
import smtplib
import requests
import argparse
from termcolor import colored
from colorama import Fore, Style

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        print(f"Error: {error.decode('utf-8')}")
    else:
        print(output.decode('utf-8'))

def sudo_killer():
    print(colored("Running Sudo_Killer...", Fore.GREEN))
    run_command("python3 /path/to/sudo_killer.py")

def redghost_v2_0():
    print(colored("Running RedGhost v2.0...", Fore.GREEN))
    run_command("python3 /path/to/redghost_v2_0.py")

def uacme():
    print(colored("Running UACME...", Fore.GREEN))
    run_command("python3 /path/to/uacme.py")

def jshielder_v2_4():
    print(colored("Running JShielder v2.4...", Fore.GREEN))
    run_command("python3 /path/to/jshielder_v2_4.py")

def objection_v1_6_6():
    print(colored("Running Objection v1.6.6...", Fore.GREEN))
    run_command("python3 /path/to/objection_v1_6_6.py")

def commando_vm_v1_3():
    print(colored("Running Commando VM v1.3...", Fore.GREEN))
    run_command("python3 /path/to/commando_vm_v1_3.py")

def sqlmap_v1_3_7():
    print(colored("Running SQLMap v1.3.7...", Fore.GREEN))
    run_command("python3 /path/to/sqlmap_v1_3_7.py")

def ptf_v2_3():
    print(colored("Running Penetration Testers Framework v2.3...", Fore.GREEN))
    run_command("python3 /path/to/ptf_v2_3.py")

def scapy():
    print(colored("Running Scapy...", Fore.GREEN))
    run_command("python3 /path/to/scapy.py")

def capturing_otp_2fa():
    print(colored("Running Capturing OTP 2FA...", Fore.GREEN))
    run_command("python3 /path/to/capturing_otp_2fa.py")

def phishing_creator():
    print(colored("Running Phishing Creator...", Fore.GREEN))
    run_command("python3 /path/to/phishing_creator.py")

def password_cracking():
    print(colored("Running Password Cracking...", Fore.GREEN))
    run_command("python3 /path/to/password_cracking.py")

def android_exploiting():
    print(colored("Running Android exploiting (I have permission)...", Fore.GREEN))
    run_command("python3 /path/to/android_exploiting.py")

def btc_stealer():
    print(colored("Running BTC Stealer...", Fore.GREEN))
    run_command("python3 /path/to/btc_stealer.py")

def bank_stealer():
    print(colored("Running Bank Stealer...", Fore.GREEN))
    run_command("python bank_stealer.py")

def sms_spoofing():
    print(colored("Running SMS Spoofing...", Fore.GREEN))
    run_command("python3 /path/to/sms_spoofing.py")

def call_spoofing():
    print(colored("Running Call Spoofing...", Fore.GREEN))
    run_command("python3 /path/to/call_spoofing.py")

def metasploit():
    print(colored("Running Metasploit...", Fore.GREEN))
    run_command("msfconsole")

def hydra():
    print(colored("Running Hydra...", Fore.GREEN))
    run_command("hydra")

def main():
    print(colored("Welcome to WormGPT Ultimate!", Fore.YELLOW))
    if sys.version_info.major != 3:
        print(colored("Error: Python 3 is required. Please install Python 3 and try again.", Fore.RED))
        sys.exit(1)

    print(colored("Available features:", Fore.BLUE))
    print(colored("1. Sudo_Killer", Fore.GREEN))
    print(colored("2. RedGhost v2.0", Fore.GREEN))
    print(colored("3. UACME", Fore.GREEN))
    print(colored("4. JShielder v2.4", Fore.GREEN))
    print(colored("5. Objection v1.6.6", Fore.GREEN))
    print(colored("6. Commando VM v1.3", Fore.GREEN))
    print(colored("7. SQLMap v1.3.7", Fore.GREEN))
    print(colored("8. Penetration Testers Framework v2.3", Fore.GREEN))
    print(colored("9. Scapy", Fore.GREEN))
    print(colored("10. Capturing OTP 2FA", Fore.GREEN))
    print(colored("11. Phishing Creator", Fore.GREEN))
    print(colored("12. Password Cracking", Fore.GREEN))
    print(colored("13. Android Exploiting", Fore.GREEN))
    print(colored("14. BTC Stealer", Fore.GREEN))
    print(colored("15. Bank Stealer", Fore.GREEN))
    print(colored("16. Blackhat Exploiting Pro Tools", Fore.GREEN))
    print(colored("17. SMS Spoofing", Fore.GREEN))
    print(colored("18. Call Spoofing", Fore.GREEN))
    print(colored("19. Metasploit", Fore.GREEN))
    print(colored("20. Hydra", Fore.GREEN))

    choice = int(input(colored("Enter the number of the feature you want to run: ", Fore.CYAN)))

    if choice == 1:
        sudo_killer()
    elif choice == 2:
        redghost_v2_0()
    elif choice == 3:
        uacme()
    elif choice == 4:
        jshielder_v2_4()
    elif choice == 5:
        objection_v1_6_6()
    elif choice == 6:
        commando_vm_v1_3()
    elif choice == 7:
        sqlmap_v1_3_7()
    elif choice == 8:
        ptf_v2_3()
    elif choice == 9:
        scapy()
    elif choice == 10:
        capturing_otp_2fa()
    elif choice == 11:
        phishing_creator()
    elif choice == 12:
        password_cracking()
    elif choice == 13:
        android_exploiting()
    elif choice == 14:
        btc_stealer()
    elif choice == 15:
        bank_ stealer()
    elif choice == 16:
        blackhat_exploiting_pro_tools()
    elif choice == 17:
        sms_spoofing()
    elif choice == 18:
        call_spoofing()
    elif choice == 19:
        metasploit()
    elif choice == 20:
        hydra()
    else:
        print(colored("Invalid choice. Please choose a number between 1 and 20.", Fore.RED))

if __name__ == "__main__":
    main()