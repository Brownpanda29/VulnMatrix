import socket
import requests

def scan_ports(ip, ports):
    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))

        if result == 0:
            service_info = get_service_info(ip, port)
            open_ports.append((port, service_info))

        sock.close()

    return open_ports

def get_service_info(ip, port):
    # Implement a method to retrieve service details based on the port (e.g., using banners)
    # Extract software version from service details
    software_version = "Your-Software-Version-Here"
    return software_version

def search_cve_for_version(version):
    base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"
    search_url = f"{base_url}?cpeMatchString=:{version}"

    response = requests.get(search_url)

    if response.status_code == 200:
        data = response.json()
        if data['totalResults'] == 0:
            print(f"Software Version: {version}")
            print("Bingo! This software is good to go with no known CVEs.")
        else:
            print(f"Software Version: {version}")
            for cve_entry in data['result']['CVE_Items']:
                cve_id = cve_entry['cve']['CVE_data_meta']['ID']
                description = cve_entry['cve']['description']['description_data'][0]['value']
                print(f"CVE ID: {cve_id}")
                print(f"Description: {description}\n")
    else:
        print("Error: Unable to fetch CVE data.")

def main():
    target_ip = input("Enter the target IP address: ")
    target_ports = range(1, 1025)  # Scan common ports

    open_ports = scan_ports(target_ip, target_ports)

    if open_ports:
        for port, service_info in open_ports:
            print(f"Port {port}: {service_info}")

            print(f"Now scanning CVE database for {service_info}")
            search_cve_for_version(service_info)
    else:
        print("No open ports found on", target_ip)

if __name__ == "__main__":
    main()
