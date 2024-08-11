import socket

def receive_packets(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('', port))
    
    print(f'Starting server on port {port}... Waiting for packets...')
    
    while True:
        data, addr = server_socket.recvfrom(65535)
        print(f'Received packet of size {len(data)} bytes from {addr}')
        
if __name__ == "__main__":
    PORT = 12345  # The port on which the server will send packets
    
    receive_packets(PORT)

    input("Press Enter to exit...")