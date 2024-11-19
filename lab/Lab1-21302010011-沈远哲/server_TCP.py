import socket
import threading

# 定义处理单个客户端连接的函数
def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)  # 接收客户端发送的数据，最多接收1024字节
        if not data:  # 如果没有数据，退出循环
            break
        modified_data = data.decode().upper()  # 将接收到的数据解码为字符串，然后转换为大写字母
        client_socket.send(modified_data.encode())  # 发送修改后的数据给客户端
    client_socket.close()  # 关闭与客户端的连接套接字

# 主函数
def main():
    server_host = '127.0.0.1'  # 服务器主机地址
    server_port = 12345  # 服务器监听的端口

    # 创建服务器套接字，使用IPv4和TCP协议
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定套接字到指定主机地址和端口
    server_socket.bind((server_host, server_port))

    # 设置服务器套接字为监听模式，允许最多5个等待连接的客户端
    server_socket.listen(5)

    print(f"Server is listening on {server_host}:{server_port}")

    while True:
        # 接受客户端连接请求，返回新的客户端套接字和客户端地址
        client_socket, client_address = server_socket.accept()

        # 打印客户端连接信息
        print(f"Connection from {client_address}")

        # 对每个客户端连接创建一个新线程，调用handle_client函数处理
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()  # 启动新线程来处理客户端连接

if __name__ == "__main__":
    main()  # 启动服务器主函数
