import socket

def scan_host(ip, start_port, end_port):
    # Define a socket timeout
    socket.setdefaulttimeout(1)
    
    # List of open ports
    open_ports = []
    
    # Scan the ports in the specified range
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
            print(f"swewdcdww {port} is open.")
        s.close()
    
    return open_ports

# Example usage
if __name__ == "__main__":
    target_ip = "192.168.1.1"  # Change to the target IP you want to scan
    start_port = 1
    end_port = 1024
    open_ports = scan_host(target_ip, start_port, end_port)
    print("Open ports:", open_ports)
