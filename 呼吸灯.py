from machine import Pin, PWM
import time

PWM_led = PWM(Pin(2, Pin.OUT))
PWM_led.freq(1000)   # 设置频率为 1kHz   范围（1Hz, 40MHz）

while True:
    for i in range(0, 1024, 1):
        PWM_led.duty(i)  # 设置PWM的占空比   占空比越大 灯越亮
        time.sleep_ms(1)  # 设置呼吸灯的周期
    
    for i in range(1023, -1, -1):
        PWM_led.duty(i)  # 设置PWM的占空比   占空比越大 灯越亮
        time.sleep_ms(1)  # 设置呼吸灯的周期