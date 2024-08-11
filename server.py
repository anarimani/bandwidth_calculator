import socket
import time

def send_packet(host, port, packet_size, num_packets):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        packet = b'a' * packet_size  # Create a packet of the specified size
        
        start_time = time.time()  # Start timing
        
        for _ in range(num_packets):
            client_socket.sendto(packet, (host, port))
        
        end_time = time.time()  # End timing
        
        client_socket.close()
        
        # Calculate bandwidth
        total_data_sent = packet_size * num_packets  # Total data sent in bytes
        duration = end_time - start_time  # Time in seconds
        bandwidth = (total_data_sent / duration) / (1024 * 1024)  # Bandwidth in MBps
        
        print(f'Total data sent: {total_data_sent} bytes')
        print(f'Time taken: {duration:.4f} seconds')
        print(f'Bandwidth: {bandwidth:.4f} MBps')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        host = input("Enter the client IP address: ")
        port = int(input("Enter the client port: "))
        packet_size = int(input("Enter the packet size in bytes: "))
        num_packets = int(input("Enter the number of packets to send: "))
        
        send_packet(host, port, packet_size, num_packets)
    except Exception as e:
        print(f"An error occurred during input: {e}")
        input("Press Enter to exit...")
