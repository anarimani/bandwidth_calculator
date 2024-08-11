import socket
import time
import os

def send_file(host, port, file_path, chunk_size=65536):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        with open(file_path, 'rb') as file:
            start_time = time.time()  # Start timing
            
            while chunk := file.read(chunk_size):
                client_socket.sendto(chunk, (host, port))
            
            end_time = time.time()  # End timing
        
        client_socket.close()
        
        # Calculate bandwidth
        total_data_sent = os.path.getsize(file_path)  # Total data sent in bytes
        duration = end_time - start_time  # Time in seconds
        bandwidth = (total_data_sent / duration) / (1024 * 1024)  # Bandwidth in MBps
        
        print(f'Total data sent: {total_data_sent} bytes')
        print(f'Time taken: {duration:.4f} seconds')
        print(f'Bandwidth: {bandwidth:.4f} MBps')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        input("Press Enter to exit...")  # Keeps the window open

if __name__ == "__main__":
    try:
        host = input("Enter the client IP address: ")
        port = int(input("Enter the client port: "))
        file_path = input("Enter the file path to send: ")
        
        send_file(host, port, file_path)
    except Exception as e:
        print(f"An error occurred during input: {e}")
        input("Press Enter to exit...")  # Keeps the window open
