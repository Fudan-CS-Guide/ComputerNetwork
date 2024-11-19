import socket

def main():
    server_host = '127.0.0.1'  # 服务器地址
    server_port = 12345       # 服务器端口

    # 创建UDP套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定套接字到服务器地址和端口
    server_socket.bind((server_host, server_port))

    print(f"Server is listening on {server_host}:{server_port}")

    while True:
        # 接收客户端数据和地址
        data, client_address = server_socket.recvfrom(1024)

        # 打印客户端连接信息
        print(f"Connection from {client_address}")

        # 将接收到的数据转换为大写字母
        modified_data = data.decode().upper()

        # 发送修改后的数据回客户端
        server_socket.sendto(modified_data.encode(), client_address)

if __name__ == "__main__":
    main()
