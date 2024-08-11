import socket
import time

def send_packet(host, port, packet_size, num_packets):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    packet = b'a' * packet_size  # Create a packet of the specified size
    
    start_time = time.time()  # Start timing
    
    for _ in range(num_packets):
        client_socket.sendto(packet, (host, port))
    
    end_time = time.time()  # End timing
    
    client_socket.close()
    import socket

def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind(("", port))
            return True
        except OSError:
            return False

port = 12345  # Replace with your preferred port
if check_port(port):
    print(f"Port {port} is available.")
else:
    print(f"Port {port} is in use.")

    # Calculate bandwidth
    total_data_sent = packet_size * num_packets  # Total data sent in bytes
    duration = end_time - start_time  # Time in seconds
    bandwidth = (total_data_sent / duration) / (1024 * 1024)  # Bandwidth in MBps
    
    print(f'Total data sent: {total_data_sent} bytes')
    print(f'Time taken: {duration} seconds')
    print(f'Bandwidth: {bandwidth} MBps')

if __name__ == "__main__":
    host = input("Enter the client IP address: ")
    port = int(input("Enter the client port: "))
    packet_size = int(input("Enter the packet size in bytes: "))
    num_packets = int(input("Enter the number of packets to send: "))
    
    send_packet(host, port, packet_size, num_packets)
    input("Press Enter to exit...")
