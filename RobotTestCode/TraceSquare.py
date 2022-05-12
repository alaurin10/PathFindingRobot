import time
import board
import busio
import digitalio
import Jetson.GPIO as GPIO
import adafruit_pca9685
 
# Initialize i2c bus and connect to servo driver board
i2c = busio.I2C(board.SCL, board.SDA)       # i2c = busio.I2C(board.D3, board.D2)
pca = adafruit_pca9685.PCA9685(i2c)
 
# Set frequency to 60 Hz
pca.frequency = 100
 
# Initialize PWM channels
ENA = pca.channels[0]
ENB = pca.channels[1]


# Initialize motor control pins
IN1 = digitalio.DigitalInOut(board.D12)
IN1.direction = digitalio.Direction.OUTPUT

IN2 = digitalio.DigitalInOut(board.D13)
IN2.direction = digitalio.Direction.OUTPUT

IN3 = digitalio.DigitalInOut(board.D19)
IN3.direction = digitalio.Direction.OUTPUT

IN4 = digitalio.DigitalInOut(board.D26)
IN4.direction = digitalio.Direction.OUTPUT
 
# Function to move right wheel
def move_right_wheel(speed):
    pwm = int(0xFFFF * speed)
 
    # Move forward
    if speed > 0:
        IN1.value = True
        IN2.value = False

        ENA.duty_cycle = pwm
 
    # Move backward
    elif speed < 0:
        IN1.value = False
        IN2.value = True
        
 
        ENA.duty_cycle = pwm
 
    # Stop motors
    elif speed == 0:
        IN1.value = False
        IN2.value = False 

# Function to move left wheel
def move_left_wheel(speed):
    pwm = int(0xFFFF * speed)

 
    # Move forward
    if speed > 0:
        IN4.value = True
        IN3.value = False        
 
        ENB.duty_cycle = pwm
 
    # Move backward
    elif speed < 0:
        IN4.value = False
        IN3.value = True 
        ENB.duty_cycle = pwm
 
    # Stop motors
    elif speed == 0:
        IN4.value = False
        IN3.value = False        
 
# Function setmode
def stop():
    move_right_wheel(0)
    move_left_wheel(0)
 
# Function to make the robot move forward
def move_forward(speed):
    move_right_wheel(speed)
    move_left_wheel(speed)
 
# Function to make the robot pivot right
def pivot_right(speed):
    move_right_wheel(0)
    move_left_wheel(speed)
 
# Function to make the robot trace a square
def move_square():
    # Move forward and pivot right four times, tracing a square
    for i in range(4):
        move_forward(0.5)
        time.sleep(1)
        pivot_right(0.2)
        time.sleep(0.8)
        print(f'Iteration {i}')
    stop()
 
# Main function
def main():
    move_square()

# Run the main loop
if __name__ == '__main__':
    main()
