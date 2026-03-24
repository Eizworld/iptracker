import requests
import os
import sys

def banner():
    os.system("clear")
    print("""
====================================
        EIZ IP TRACKER TOOL
====================================
1. Track IP
2. Track My IP
3. Exit
""")

def fetch_ip_data(ip):
    try:
        url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data
    except:
        return None

def show_data(data):
    if not data or "error" in data:
        print("\n[!] Failed to fetch IP data\n")
        return

    print("\n========== RESULT ==========\n")

    print(f"IP Address     : {data.get('ip')}")
    print(f"City           : {data.get('city')}")
    print(f"Region         : {data.get('region')}")
    print(f"Country        : {data.get('country_name')}")
    print(f"Postal Code    : {data.get('postal')}")
    print(f"Latitude       : {data.get('latitude')}")
    print(f"Longitude      : {data.get('longitude')}")
    print(f"Timezone       : {data.get('timezone')}")
    print(f"ISP / Org      : {data.get('org')}")
    print(f"ASN            : {data.get('asn')}")

    lat = data.get("latitude")
    lon = data.get("longitude")
    if lat and lon:
        print("\nGoogle Maps:")
        print(f"https://maps.google.com/?q={lat},{lon}")

    print("\n=============================\n")

def main():
    while True:
        banner()
        choice = input("Select option: ")

        if choice == "1":
            ip = input("\nEnter IP Address: ")
            data = fetch_ip_data(ip)
            show_data(data)
            input("Press Enter to continue...")

        elif choice == "2":
            data = fetch_ip_data("")
            show_data(data)
            input("Press Enter to continue...")

        elif choice == "3":
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid option")
            input("Press Enter...")

if __name__ == "__main__":
    main()
