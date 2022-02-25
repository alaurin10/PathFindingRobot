import RPi.GPIO as GPIO
import time

# Set the GPIO mode for the Jetson Nano. GPIO.BOARD will allow pins to be called by their pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define pin numbers for each of the four motor ports
motorR1 = 29
motorR2 = 32
motorL1 = 31
motorL2 = 33

# Set up all motor pins to output
GPIO.setup(motorR1, GPIO.OUT)
GPIO.setup(motorR2, GPIO.OUT)
GPIO.setup(motorL1, GPIO.OUT)
GPIO.setup(motorL2, GPIO.OUT)

# Set up R2 and L2 to utilize PWM. Initialize them at 100 Hz
motorR2_pwm = GPIO.PWM(motorR2, 100)
motorL2_pwm = GPIO.PWM(motorL2, 100)


# Function to make the robot stop
def stop():
    GPIO.output(motorR1, GPIO.LOW)  # Sets R1 to low
    motorR2_pwm.stop()  # Stops the output of PWM to R2
    GPIO.output(motorL1, GPIO.LOW)  # Sets L1 to low
    motorL2_pwm.stop()  # Stops the output of PWM to L2


# Function to make the robot move forward
def move_forward():
    GPIO.output(motorR1, GPIO.LOW)  # Sets R1 to low
    motorR2_pwm.start(50)  # Sets R2 to 50% duty cycle
    GPIO.output(motorL1, GPIO.LOW)  # Sets L1 to low
    motorL2_pwm.start(50)  # Sets L2 to 50% duty cycle


# Main Loop
def main():
    # Have the robot move forward and stop a total of 3 times
    for i in range(3):
        move_forward()
        time.sleep(1)
        stop()
        time.sleep(2)


# Run the main loop
if __name__ == '__main__':
    main()
