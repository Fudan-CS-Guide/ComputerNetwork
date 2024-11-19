import socket

def main():
    # 定义服务器主机地址和端口
    server_host = '127.0.0.1'  # 使用本地主机地址
    server_port = 12345

    # 创建客户端套接字，使用IPv4和TCP协议
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器的主机地址和端口
    client_socket.connect((server_host, server_port))

    # 输入要发送的字符串
    message = input("Enter a string: ")

    # 发送用户输入的字符串给服务器
    client_socket.send(message.encode())

    # 接收服务器返回的数据
    modified_message = client_socket.recv(1024)

    # 打印服务器返回的大写字符串
    print(f"Received from server: {modified_message.decode()}")

    # 关闭客户端套接字
    client_socket.close()

if __name__ == "__main__":
    main()
