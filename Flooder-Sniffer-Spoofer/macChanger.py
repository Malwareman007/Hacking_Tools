import subprocess
import optparse
import re
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC")
    parser.add_option("-m", "--mac", dest="MAC", help="New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-]Please specify an interface, use --help for more info")
    elif not options.MAC:
        parser.error("[-]Please specify a MAC, use --help for more info")
    return options
def change_mac(interface, MAC):
    print("[+]Changing Mac address for", interface, "to", MAC)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", MAC])
    subprocess.call(["ifconfig", interface, "up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")



options = get_arguments()

current_mac = get_current_mac(options.interface)
print("current MAC= " +str(current_mac))
change_mac(options.interface, options.MAC)
current_mac = get_current_mac(options.interface)
if current_mac == options.MAC:
    print("[+] MAC address was successfully changed to " +current_mac)
else:
    print("[-] MAC address did not changed.")
