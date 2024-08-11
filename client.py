import socket

def receive_packets(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('', port))
        
        print(f'Starting server on port {port}... Waiting for packets...')
        
        while True:
            data, addr = server_socket.recvfrom(65535)
            print(f'Received packet of size {len(data)} bytes from {addr}')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        port = int(input("Enter the port to listen on: "))
        
        receive_packets(port)
    except Exception as e:
        print(f"An error occurred during input: {e}")
        input("Press Enter to exit...")
