import time
import network
import socket
from machine import Pin

led = Pin(2, Pin.OUT) # 定义一个led灯

def do_connect():  # 连接网络  采用UDP协议连接
    wlan = network.WLAN(network.STA_IF)  # 工作在STA_IF模式
    wlan.active(True)
    if not wlan.isconnected():   
        wlan.connect('11111111', '11111111')
        while not wlan.isconnected():
            print('正在连接网络...')
            time.sleep(1)
            
    print('连接网络成功...')         
    print('network config:', wlan.ifconfig())

def create_udp_socket():  # 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("0.0.0.0", 7788))  # 绑定一个固定的端口
    
    return udp_socket

def main():
    do_connect()
    udp_socket = create_udp_socket()
    while True:  # 接受UDP数据
        recv_data, sender_info = udp_socket.recvfrom(1024)  # 返回的是一个元组，可以进行拆包
        # print("{}发送的数据：{}".format(sender_info, recv_data))
        # 对收到的数据进行解码
        recv_data_str = recv_data.decode("utf-8")
        # print(recv_data_str)
        if recv_data_str == "light on":
            led.on()
        elif recv_data_str == "light off":
            led.off()
        

if __name__ == "__main__":
    main()