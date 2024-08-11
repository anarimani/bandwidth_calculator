import socket

def check_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("", port))
                return True
            except OSError:
                return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

if __name__ == "__main__":
    try:
        port = int(input("Enter the port number to check: "))
        
        if check_port(port):
            print(f"Port {port} is available.")
        else:
            print(f"Port {port} is in use.")
    except Exception as e:
        print(f"An error occurred during input: {e}")
    finally:
        input("Press Enter to exit...")
