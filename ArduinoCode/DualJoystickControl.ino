/*
 * Andrew Laurin, Nick Oglive, Zechariah Rosal
 * EE151-05
 * Week 5
 * Arduino Project #7:"Dual Joystick Robot Motor Control"
 */

int motorR1 = 4;  //MotorR1 is assigned to pin 4
int motorR2 = 5;  //MotorR1 is assigned to pin 5
int motorL1 = 6;  //MotorR1 is assigned to pin 6
int motorL2 = 7;  //MotorR1 is assigned to pin 7
const int JoystickLCenterValue = 127;  //The center value for the joysticks are 518
const int JoystickRCenterValue = 127;

 void setup() {
  pinMode(motorR1, OUTPUT);  //Set motor pins to output
  pinMode(motorR2, OUTPUT);
  pinMode(motorL1, OUTPUT);
  pinMode(motorL2, OUTPUT);
 }

void loop() {
  JoystickL();  //Run the two joystick functions defined below
  JoystickR();
}

 void MoveFRS() {
  //Move right wheel forward slow
  digitalWrite(motorR1, LOW);
  analogWrite(motorR2, 128);
  delay(50);
 }

 void MoveFRF() {
  //Move right wheel forward fast
  digitalWrite(motorR1, LOW);
  analogWrite(motorR2, 220);
  delay(50);
 }

void MoveBRS() {
  //Move right wheel backward slow
  digitalWrite(motorR2, LOW);
  analogWrite(motorR1, 128);
  delay(50);
 }

 void MoveBRF() {
  //Move right wheel backwards fast
  digitalWrite(motorR2, LOW);
  analogWrite(motorR1, 220);
  delay(50);
 }

 void MoveFLS() {
  //Move left wheel forwards slow
  digitalWrite(motorL1, LOW);
  analogWrite(motorL2, 120);
  delay(50);
 }

 void MoveFLF() {
  //Moveleft wheel forwards fast
  digitalWrite(motorL1, LOW);
  analogWrite(motorL2, 209);
  delay(50);
 }

 void MoveBLS() {
  //Move left wheel backwards slow
  digitalWrite(motorL2, LOW);
  analogWrite(motorL1, 120);
  delay(50);
 }

 void MoveBLF() {
  //Move left wheel backwards fast
  digitalWrite(motorL2, LOW);
  analogWrite(motorL1, 209);
  delay(50);
 }

 void StopR() {
  //All motors stop
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, LOW);
  delay(50);
 }

 void StopL() {
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, LOW);
  delay(50);
 }

void JoystickL() {
  if(analogRead(A0) < (JoystickLCenterValue-110)) {     //If left joystick is all the way forwards, move forward fast
    MoveFLF();
  }
  else if(analogRead(A0) < (JoystickLCenterValue-15)) { //If left joystick is pushed half forwards, move forward slow
    MoveFLS();
  }
  else if((JoystickLCenterValue-10) < analogRead(A0) < (JoystickLCenterValue+10)) {  //If left Joystick is in center, stop
    StopL();
  }
  else if((JoystickLCenterValue+15) < analogRead(A0) < (JoystickLCenterValue+110)) {  //If left joystick is pushed half backwards, move backward slow
    MoveBLS();
  }
  else if(analogRead(A0) > (JoystickLCenterValue+115)) {  //If left joystick is pushed all the way backwards, move backward fast
    MoveBLF();
  }
  else {
    
  }
}

void JoystickR() {
  if(analogRead(A1) < (JoystickRCenterValue-110)) {  //If right joystick is pushed all the way forward, left wheel turns faster
    MoveFRF();
  }
  else if(analogRead(A1) < (JoystickRCenterValue-15)) { //If right joystick is pushed half forward, left wheel turns slightly faster
    MoveFRS();
  }
  else if((JoystickRCenterValue-10) < analogRead(A1) < (JoystickRCenterValue+10)) {  //If right Joystick is in center, stop
    StopR();
  }
  else if((JoystickRCenterValue+15) < analogRead(A1) > (JoystickRCenterValue+110)) { //If right joystick is pushed half forward, right wheel turns slightly faster
    MoveBRS();
  }
  else if(analogRead(A1) > (JoystickRCenterValue+115)) { //If right joystick is pushed all the way forward, right wheel turns faster
    MoveBRF();
  }
  else {
    
  }
}
 
