import socket

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("", port))
            return True
        except OSError:
            return False

if __name__ == "__main__":
    port = int(input("Enter the port number to check: "))
    
    if check_port(port):
        print(f"Port {port} is available.")
    else:
        print(f"Port {port} is in use.")
    
    input("Press Enter to exit...")  # Keeps the window open
