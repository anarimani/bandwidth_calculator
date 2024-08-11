import socket

def receive_file(port, save_path, chunk_size=65536):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind(('', port))
        
        print(f'Starting server on port {port}... Waiting for data...')
        
        with open(save_path, 'wb') as file:
            while True:
                data, addr = server_socket.recvfrom(chunk_size)
                if not data:
                    break
                file.write(data)
        
        print("File received successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server_socket.close()
        input("Press Enter to exit...")  # Keeps the window open

if __name__ == "__main__":
    try:
        port = int(input("Enter the port to listen on: "))
        save_path = input("Enter the file path to save the received file: ")
        
        receive_file(port, save_path)
    except Exception as e:
        print(f"An error occurred during input: {e}")
        input("Press Enter to exit...")  # Keeps the window open
