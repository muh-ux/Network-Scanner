import nmap
import re

nm = nmap.PortScanner()
target = input("Enter the target IP address: ")
options = '-sV -sC'

if not re.match(r'^\d{1,3}(\.\d{1,3}){3}$', target):
    print("Invalid IP format. Example: 192.168.1.1")
else:
    try:
        nm.scan(target, '1-1024', arguments=options)

        if not nm.all_hosts():
            print("No hosts found. Check the IP address and try again.")
        else:
            for host in nm.all_hosts():
                print('Host : %s (%s)' % (host, nm[host].hostname()))
                print('State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                    print('Protocol : %s' % proto)
                    for port in nm[host][proto].keys():
                        state = nm[host][proto][port]['state']
                        print('port : %s\tstate : %s' % (port, state))

    except nmap.PortScannerError as e:
        print(f"Scan error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        