/*
 * Andrew Laurin, Nickolas Ogilvie, Zechariah Rosal
 * EE151-05
 * Project Final Code
 */

int motorR1 = 4;  //MotorR1 is assigned to pin 4
int motorR2 = 5;  //MotorR1 is assigned to pin 5
int motorL1 = 6;  //MotorR1 is assigned to pin 6
int motorL2 = 7;  //MotorR1 is assigned to pin 7

const int SteeringGain = 60;
const int DesiredSpeed = 100;

#include <Servo.h> //servo library
Servo myservo; // create servo object to control servo
const int ServoPin = 11; //Servo connection
Servo ServoEgg; //create servo object to control egg dropper
int ServoPinEgg = 9; //set servo pin for egg dropper to pin 9
int pos; //create variable for rotational position for egg dropper servo

int SensorPointingAngle;
int PointStraightAheadAngle = 81;
int PointingGain = 30;

const int Threshold = 113;


// Pins used for digital input of obstacle sensors 
const int RangeTriggerPin = 40; // Rangefinder Trigger input pin
const int RangeEchoPin = 41; // Rangefinder Echo Sensor output pin
const unsigned long RangeTimeout = 4000; //usec = 4 millisec. timeout value. 

unsigned long EchoDelay = 0;
float Distance = 0.0; 

float WithinInches;

void setup() {
  
  pinMode(motorR1, OUTPUT);  //Set motor pins to output
  pinMode(motorR2, OUTPUT);
  pinMode(motorL1, OUTPUT);
  pinMode(motorL2, OUTPUT);

  pinMode(43, OUTPUT);
  pinMode(45, OUTPUT);
  pinMode(47, OUTPUT);
  pinMode(49, OUTPUT);
  pinMode(51, OUTPUT);

  
  pinMode(RangeTriggerPin, OUTPUT);
  pinMode(RangeEchoPin, INPUT); 
  
  digitalWrite(motorR1, LOW); //disable motor driver
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, LOW); 

  pinMode(50, OUTPUT); //set up digital pin 50 as output
  
  Serial.begin(9600);
  myservo.attach(ServoPin); // attach servo on pin 11 to servo object
  myservo.write(PointStraightAheadAngle);  

  ServoEgg.attach(ServoPinEgg); //attach servo for egg dropper
  ServoEgg.write(90); //starts egg dropper servo to 0 degrees
//  for(int i = 0; i < 32; i++){
//   float PathError = SensePathPositionError(i);
//   if(PathError > -3 && PathError < 3){
//    SensorPointingAngle = UpdatePointingAngle(PathError);
//    Serial.print("Sensor State Code: ");
//    Serial.print(i, BIN);
//    Serial.print(" ");
//    AdjustMotorSpeeds(PathError);
//    Serial.print("SensePathPositionError: ");
//    Serial.print(SensePathPositionError);
//    Serial.print("  ");
//    Serial.print("LeftMotorSpeed: ");
//    Serial.print(LeftMotorSpeed);
//    Serial.print("  ");
//    Serial.print("RightMotorSpeed: ");
//    Serial.print(RightMotorSpeed);
//    Serial.print("  ");    
//    Serial.print("SensorPointingAngle = ");
//    Serial.print(SensorPointingAngle);    
//    Serial.println(" "); 
//   }
//    else {
//      Serial.print("Sensor State Code: ");
//      Serial.println(i, BIN);
//    }
//     delay(1000);
//  }
}

void loop(){
  byte PathSensorStates = GetPathSensorStates(); 
  float PathError = SensePathPositionError(PathSensorStates);
  if(PathError > -3 && PathError < 3){
    AdjustMotorSpeeds(PathError);
    SensorPointingAngle = UpdatePointingAngle(PathError);
    if (ObstacleDetected(WithinInches) == true) {
    Stop();
    Siren();
    }
    else {}
  }
  else {}

}

int ReadLineSensor(int SensorAnalogInPin, int SensorDigitalOutPin){
  int AnalogValue = analogRead(SensorAnalogInPin);
//  Serial.print(AnalogValue);
//  Serial.print("  ");
  if (AnalogValue > Threshold){
    digitalWrite(SensorDigitalOutPin, HIGH);
    return 1;
  }
  else{
    digitalWrite(SensorDigitalOutPin, LOW);
    return 0;
  }
}

byte GetPathSensorStates(){
  int FarLeftSensorDigitalValue = ReadLineSensor(A15, 43);
  int LeftSensorDigitalValue = ReadLineSensor(A14, 45);
  int MiddleSensorDigitalValue = ReadLineSensor(A13, 47);
  int RightSensorDigitalValue = ReadLineSensor(A12, 49);
  int FarRightSensorDigitalValue = ReadLineSensor(A11, 51);
  byte SensorCode = 0;
  bitWrite(SensorCode, 4, FarLeftSensorDigitalValue);
  bitWrite(SensorCode, 3, LeftSensorDigitalValue);
  bitWrite(SensorCode, 2, MiddleSensorDigitalValue);
  bitWrite(SensorCode, 1, RightSensorDigitalValue);
  bitWrite(SensorCode, 0, FarRightSensorDigitalValue);
//  Serial.println(SensorCode, BIN);
  return SensorCode;
}

int UpdatePointingAngle(float PathError) {
  SensorPointingAngle = PointStraightAheadAngle + PointingGain * PathError;
  myservo.attach(ServoPin); // attach servo on pin 11 to servo object
  myservo.write(SensorPointingAngle);
  return SensorPointingAngle;
}

float SensePathPositionError(byte PathSensorStates) {
  float value;
  switch(PathSensorStates) {
    case 0b00001:
      value = 2;
      return value;
      break;
    case 0b00011:
      value = 1.5;
      return value;
      break;
    case 0b00010:
      value = 1;
      return value;
      break;
    case 0b00110:
      value = 0.5;
      return value;
      break;
    case 0b00100: 
      value = 0;
      return value;
      break;
    case 0b01100:
      value = -0.5;
      return value;
      break;
    case 0b01000:
      value = -1;
      return value;
      break;
    case 0b11000:
      value = -1.5;
      return value;
      break;
    case 0b10000:
      value = -2;
      return value;
      break;
    case 0b00000:
    case 0b00101:
    case 0b00111:
    case 0b01001:
    case 0b01010:
    case 0b01011:
    case 0b01101:
    case 0b01110:
    case 0b01111:
    case 0b10001:
    case 0b10010:
    case 0b10011:
    case 0b10100:
    case 0b10101:
    case 0b10110:
    case 0b10111:
    case 0b11001:
    case 0b11010:
    case 0b11011:
    case 0b11100:
    case 0b11101:
    case 0b11110:
    case 0b11111:
      value = 999.99; //impossible value
      return value;
      break;
  }
}

void AdjustMotorSpeeds(float SensePathPositionError){
  int SpeedAdjustmentPercent = SteeringGain*SensePathPositionError;
  int RightMotorSpeed = (100-SpeedAdjustmentPercent)*DesiredSpeed/100;
  RightMotorSpeed = constrain (RightMotorSpeed, 0, 255);
  int LeftMotorSpeed = (100+SpeedAdjustmentPercent)*DesiredSpeed/100;
  LeftMotorSpeed = constrain (LeftMotorSpeed, 0, 255);
  Move(LeftMotorSpeed, RightMotorSpeed);
}

void Move(int LeftMotorSpeed, int RightMotorSpeed){
  digitalWrite(motorR1, LOW);
  analogWrite(motorR2, RightMotorSpeed);  
  digitalWrite(motorL1, LOW);       
  analogWrite(motorL2, LeftMotorSpeed);  
}  

void Stop() {
  digitalWrite(motorR1, LOW); //disable motor driver
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, LOW);  
}

bool ObstacleDetected(float WithinInches) {
  if(ObstacleDistance(WithinInches) < 2 &&
     ObstacleDistance(WithinInches) > 0) {
    return true;
  } 
  else {
    return false;
  }
}

float ObstacleDistance(float WithinInches) {
  digitalWrite(RangeTriggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(RangeTriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(RangeTriggerPin, LOW); 

  EchoDelay = pulseIn(RangeEchoPin, HIGH, RangeTimeout);
  Distance = (EchoDelay / 74.0) / 2.0;

  if (EchoDelay < 300) {
    Distance = 0;
  }

//  if (Distance < 20 && Distance > 0) {  //if distance is between 0 and 20
//    tone(50,frequency(Distance), 500);  //output tone as function of distance
//    if (Distance < 6) {
//      digitalWrite(LED, HIGH);
//    } 
//    else {
//      digitalWrite(LED, LOW);
//    }
//  }

  delay(10);  
  return Distance;
}

void Siren() {
  tone(50, 1319, 167); 
  delay(167);         //wait until above note finishes playing
  tone(50, 1047, 167); 
  delay(167);
  tone(50, 1319, 167); 
  delay(167);
  tone(50, 1047, 500); 
  delay(500); 
}

void Dropper() {
  for (pos = 0; pos <= 90; pos += 1) {  //for loop to increment degrees by 1
    ServoEgg.write(pos);
    delay(100); //increment one degree every .1 seconds
  }
  delay(1000);
}
