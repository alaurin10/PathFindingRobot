import time
import board
import busio
import adafruit_pca9685

# Initialize i2c bus and connect to servo driver board
i2c = busio.I2C(board.SCL, board.SDA)       # i2c = busio.I2C(board.D3, board.D2)
pca = adafruit_pca9685.PCA9685(i2c)

# Set frequency to 60 Hz
pca.frequency = 60

# Initialize which channels each motor is connencted to
motorR1 = pca.channels[0]
motorR2 = pca.channels[1]

motorL1 = pca.channels[2]
motorL2 = pca.channels[3]

motor_channels = [motorR1, motorR2, motorL1, motorL2]


# Function to make the robot stop
def stop():
    for channel in motor_channels:
        channel.duty_cycle = 0

# Function to make the robot move forward
def move_forward():
    motorR1.duty_cycle = 0          # Set R1 to low
    motorR2.duty_cycle = 0x7FFF     # Set R2 to 50% duty cycle
    motorL1.duty_cycle = 0          # Set L1 to low
    motorL2.duty_cycle = 0x7FFF     # Set L2 to 50% duty cycle

# Function to make the robot pivot right
def pivot_right():
    motorR1.duty_cycle = 0x7FFF     # Set R1 to 50% duty cycle
    motorR2.duty_cycle = 0          # Set R2 to low
    motorL1.duty_cycle = 0          # Set L1 to low
    motorL2.duty_cycle = 0x7FFF     # Set L2 to 50% duty cycle

# Function to make the robot trace a square
def move_square():
    # Move forward and pivot right four times, tracing a square
    for i in range(4):
        move_forward()
        time.sleep(1)
        pivot_right()
        time.sleep(0.53)
    stop()


# Main function
def main():
    move_square()


# Run the main loop
if __name__ == '__main__':
    main()
