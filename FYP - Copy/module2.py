import scapy.all as scapy
from termcolor import colored

def scan(ip, timeout=3):  # Increased timeout to 5 seconds
    try:
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list, _ = scapy.srp(arp_request_broadcast, timeout=timeout, verbose=False)

        client_list = []
        for _, element in answered_list:
            client_dict = {"ip": element.psrc, "mac": element.hwsrc}
            client_list.append(client_dict)
        return client_list
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))
        return []

def print_result(result_list):
    if result_list:
        print("Discovered Devices:")
        print("IP Address\t\tMAC Address")
        print("---------------------------------------")
        for result in result_list:
            print(result["ip"], "\t\t", result["mac"])
    else:
        print(colored("No devices found.", "yellow"))

if __name__ == "__main__":
    target_ip = "192.168.0.0/24"
    print("Scanning network...")
    scan_result = scan(target_ip)
    print_result(scan_result)
