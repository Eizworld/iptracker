import requests
import os
import sys
import socket
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)

def banner():
    os.system("clear")
    ascii_banner = pyfiglet.figlet_format("EIZ IP TRACKER PRO")
    print(Fore.CYAN + ascii_banner)
    print(Fore.YELLOW + "1. Track IP")
    print(Fore.YELLOW + "2. Track My IP")
    print(Fore.YELLOW + "3. Track Multiple IPs")
    print(Fore.YELLOW + "4. Domain → IP Lookup")
    print(Fore.YELLOW + "5. Exit\n")

def fetch_ip_data(ip):
    try:
        url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(url, timeout=10)
        return response.json()
    except:
        return None

def show_data(data, save=False, filename="report.txt"):
    if not data or "error" in data:
        print(Fore.RED + "\n[!] Failed to fetch IP data\n")
        return

    info = f"""
========== RESULT ==========
IP Address     : {data.get('ip')}
City           : {data.get('city')}
Region         : {data.get('region')}
Country        : {data.get('country_name')}
Postal Code    : {data.get('postal')}
Latitude       : {data.get('latitude')}
Longitude      : {data.get('longitude')}
Timezone       : {data.get('timezone')}
ISP / Org      : {data.get('org')}
ASN            : {data.get('asn')}

Google Maps    : https://maps.google.com/?q={data.get('latitude')},{data.get('longitude')}
=============================
"""
    print(Fore.GREEN + info)

    if save:
        with open(filename, "a") as f:
            f.write(info + "\n")

def domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(Fore.CYAN + f"\nDomain {domain} → IP: {ip}\n")
        return ip
    except:
        print(Fore.RED + "[!] Failed to resolve domain")
        return None

def main():
    while True:
        banner()
        choice = input(Fore.YELLOW + "Select option: ")

        if choice == "1":
            ip = input(Fore.CYAN + "\nEnter IP Address: ")
            data = fetch_ip_data(ip)
            show_data(data)

        elif choice == "2":
            data = fetch_ip_data("")
            show_data(data)

        elif choice == "3":
            filename = input(Fore.CYAN + "\nEnter filename to save report (e.g., report.txt): ")
            file_list = input("Enter IPs separated by comma: ").split(",")
            for ip in file_list:
                ip = ip.strip()
                data = fetch_ip_data(ip)
                show_data(data, save=True, filename=filename)
            print(Fore.GREEN + f"\nAll data saved to {filename}")

        elif choice == "4":
            domain = input(Fore.CYAN + "\nEnter domain: ")
            ip = domain_to_ip(domain)
            if ip:
                data = fetch_ip_data(ip)
                show_data(data)

        elif choice == "5":
            print(Fore.GREEN + "Goodbye!")
            sys.exit()

        else:
            print(Fore.RED + "Invalid option")
        input(Fore.YELLOW + "Press Enter to continue...")

if __name__ == "__main__":
    main()
