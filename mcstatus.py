import os
import requests
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_server_status(address, server_type):
    clear_screen()

    if server_type == 'normal':
        url = f"https://api.mcsrvstat.us/3/{address}"
    elif server_type == 'bedrock':
        url = f"https://api.mcsrvstat.us/bedrock/3/{address}"
    else:
        print(Fore.RED + "Invalid server type selection.")
        return

    try:
        response = requests.get(url)
        data = response.json()

        if data['online']:
            print(Fore.GREEN + f"Server {data['ip']}:{data['port']} ({data['hostname'] if 'hostname' in data else ''}) is online:")
            print(Fore.YELLOW + f"Version: {data['version']} ({data['protocol']['name']})")
            print(Fore.CYAN + f"Players Online: {data['players']['online']}/{data['players']['max']}")
            if 'motd' in data:
                print(Fore.WHITE + "MOTD:")
                for line in data['motd']['clean']:
                    print(Style.BRIGHT + line)
            if 'plugins' in data:
                print(Fore.MAGENTA + "Plugins:")
                for plugin in data['plugins']:
                    print(Style.BRIGHT + f"- {plugin['name']} v{plugin['version']}")
            if 'mods' in data:
                print(Fore.BLUE + "Mods:")
                for mod in data['mods']:
                    print(Style.BRIGHT + f"- {mod['name']} v{mod['version']}")
        else:
            print(Fore.RED + f"Server {data['ip']}:{data['port']} is currently offline.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"Error fetching server status: {e}")

    input("\nPress Enter to continue...")
    main()

def main():
    clear_screen()
    print(Fore.CYAN + "Welcome to Minecraft Server Status Checker")
    print(Fore.YELLOW + "Choose server type:")
    print(Fore.GREEN + "1. Normal (Java Edition)")
    print("2. Bedrock")
    print(Fore.RED + "Type 'exit' to quit")
    user_input = input(Fore.WHITE + "Enter your choice: ").strip().lower()
    
    
    if user_input == 'exit':
        clear_screen()
        print(Fore.YELLOW + "Exiting Minecraft Server Status Checker. Goodbye!")
        print(Fore.GREEN + "mcsrvstat.us")

        return
    elif user_input == '1':
        server_type = 'normal'
    elif user_input == '2':
        server_type = 'bedrock'
    else:
        print(Fore.RED + "Invalid choice.")
        main()
        return

    if user_input in ['1', '2']:
        ip_address = input(Fore.WHITE + "Enter the IP address of the Minecraft server: ").strip()
        get_server_status(ip_address, server_type)
    else:
        main()

if __name__ == "__main__":
    main()
