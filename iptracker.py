import requests
import os
import sys
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

def banner():
    os.system("clear")
    ascii_banner = pyfiglet.figlet_format("EIZ IP TRACKER")
    print(Fore.CYAN + ascii_banner)
    print(Fore.YELLOW + "1. Track IP")
    print(Fore.YELLOW + "2. Track My IP")
    print(Fore.YELLOW + "3. Exit\n")

def fetch_ip_data(ip):
    try:
        url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(url, timeout=10)
        return response.json()
    except:
        return None

def show_data(data):
    if not data or "error" in data:
        print(Fore.RED + "\n[!] Failed to fetch IP data\n")
        return

    print(Fore.GREEN + "\n========== RESULT ==========\n")

    print(Fore.CYAN + "IP Address     : " + Fore.WHITE + str(data.get('ip')))
    print(Fore.CYAN + "City           : " + Fore.WHITE + str(data.get('city')))
    print(Fore.CYAN + "Region         : " + Fore.WHITE + str(data.get('region')))
    print(Fore.CYAN + "Country        : " + Fore.WHITE + str(data.get('country_name')))
    print(Fore.CYAN + "Postal Code    : " + Fore.WHITE + str(data.get('postal')))
    print(Fore.CYAN + "Latitude       : " + Fore.WHITE + str(data.get('latitude')))
    print(Fore.CYAN + "Longitude      : " + Fore.WHITE + str(data.get('longitude')))
    print(Fore.CYAN + "Timezone       : " + Fore.WHITE + str(data.get('timezone')))
    print(Fore.CYAN + "ISP / Org      : " + Fore.WHITE + str(data.get('org')))
    print(Fore.CYAN + "ASN            : " + Fore.WHITE + str(data.get('asn')))

    lat = data.get("latitude")
    lon = data.get("longitude")

    if lat and lon:
        print(Fore.MAGENTA + "\nGoogle Maps:")
        print(Fore.WHITE + f"https://maps.google.com/?q={lat},{lon}")

    print(Fore.GREEN + "\n=============================\n")

def main():
    while True:
        banner()
        choice = input(Fore.YELLOW + "Select option: ")

        if choice == "1":
            ip = input(Fore.CYAN + "\nEnter IP Address: ")
            data = fetch_ip_data(ip)
            show_data(data)
            input(Fore.YELLOW + "Press Enter to continue...")

        elif choice == "2":
            data = fetch_ip_data("")
            show_data(data)
            input(Fore.YELLOW + "Press Enter to continue...")

        elif choice == "3":
            print(Fore.GREEN + "Goodbye!")
            sys.exit()

        else:
            print(Fore.RED + "Invalid option")
            input("Press Enter...")

if __name__ == "__main__":
    main()
