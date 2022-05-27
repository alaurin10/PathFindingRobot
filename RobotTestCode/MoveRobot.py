import board
import busio
import digitalio
import threading
import adafruit_pca9685


class Move:

    def __init__(self):

        self.MOVE_1FT = 0.64
        self.ROTATE_360 = 1.88

        # Initialize i2c bus and connect to servo driver board
        i2c = busio.I2C(board.SCL, board.SDA)       # i2c = busio.I2C(board.D3, board.D2)
        pca = adafruit_pca9685.PCA9685(i2c)
        
        # Set frequency to 60 Hz
        pca.frequency = 100
        
        # Initialize PWM channels
        self.ENA = pca.channels[0]
        self.ENB = pca.channels[1]


        self.IN1 = digitalio.DigitalInOut(board.D12)
        self.IN1.direction = digitalio.Direction.OUTPUT

        self.IN2 = digitalio.DigitalInOut(board.D13)
        self.IN2.direction = digitalio.Direction.OUTPUT

        self.IN3 = digitalio.DigitalInOut(board.D19)
        self.IN3.direction = digitalio.Direction.OUTPUT

        self.IN4 = digitalio.DigitalInOut(board.D26)
        self.IN4.direction = digitalio.Direction.OUTPUT
    
    # Function to move right wheel
    def move_right_wheel(self, speed):
        pwm = int(0xFFFF * abs(speed))
    
        # Move forward
        if speed > 0:

            self.IN1.value = True
            self.IN2.value = False

            self.ENA.duty_cycle = pwm
    
        # Move backward
        elif speed < 0:

            self.IN1.value = False
            self.IN2.value = True
            
    
            self.ENA.duty_cycle = pwm
    
        # Stop motors
        elif speed == 0:

            self.IN1.value = False
            self.IN2.value = False 

    # Function to move left wheel
    def move_left_wheel(self, speed):
        pwm = int(0xFFFF * abs(speed))

    
        # Move forward
        if speed > 0:
    
            self.IN4.value = True
            self.IN3.value = False        
    
            self.ENB.duty_cycle = pwm
    
        # Move backward
        elif speed < 0:
    
            self.IN4.value = False
            self.IN3.value = True 
            self.ENB.duty_cycle = pwm
    
        # Stop motors
        elif speed == 0:

            self.IN4.value = False
            self.IN3.value = False        
    
    # Function setmode
    def stop(self):
        self.move_right_wheel(0)
        self.move_left_wheel(0)
    
    # Function to make the robot move forward
    def move(self, speed, dist):
        delay = self.MOVE_1FT * dist / 12
        timer = threading.Timer(delay, self.stop)
        timer.start()

        self.move_right_wheel(speed)
        self.move_left_wheel(speed)


    
    # Function to make the robot pivot right
    def turn_right(self, speed, angle):
        delay = self.ROTATE_360 * angle / 360
        timer = threading.Timer(delay, self.stop)
        timer.start()

        self.move_right_wheel(-1 * speed)
        self.move_left_wheel(speed)
    
    # Function to make the robot pivot right
    def turn_left(self, speed, angle):
        delay = self.ROTATE_360 * angle / 360
        timer = threading.Timer(delay, self.stop)
        timer.start()

        self.move_right_wheel(speed)
        self.move_left_wheel(-1 * speed)
