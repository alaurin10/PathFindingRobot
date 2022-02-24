/*
 * Andrew Laurin, Nick Oglive, Zechariah Rosal
 * EE151-05
 * Week 5
 * Arduino Project #3: Loopy Squares
 */

 int motorR1 = 4;
 int motorR2 = 5;
 int motorL1 = 6;
 int motorL2 = 7;

 void setup () {
  pinMode(motorR1, OUTPUT);
  pinMode(motorR2, OUTPUT);
  pinMode(motorL1, OUTPUT);
  pinMode(motorL2, OUTPUT); 
//Set digital pin 13 as an input
  pinMode(13, OUTPUT);
  
 }

void loop() {
   //Trace out a square path
  TracelSide();
  PivotRight();
  TracelSide();
  PivotRight();
  TracelSide();
  PivotRight();
  TracelSide();
  PivotRight();

  //All motors stop
  digitalWrite(motorR1, LOW);
  digitalWrite(motorR2, LOW);
  digitalWrite(motorL1, LOW);
  digitalWrite(motorL2, LOW);

  FlashLED();
  FlashLED();
  FlashLED();
  FlashLED();

  delay(3000);
}

 void TracelSide() {
  //Move forward at medium speed
  digitalWrite (motorR1, LOW); 
  analogWrite (motorR2, 128); 
  digitalWrite (motorL1, LOW); 
  analogWrite (motorL2, 120);
  delay(2000); 
  
 }

void PivotRight() {
  //Pivot right 90 degrees
  analogWrite (motorR1, 128); 
  digitalWrite (motorR2, LOW); 
  digitalWrite (motorL1, LOW); 
  analogWrite (motorL2, 120); 
  delay (540);  //takes about 0.53 seconds to make a 90 degree turn
}

void FlashLED() {
  digitalWrite(13,HIGH);
  delay(300);        //0.1 second flash intervals
  digitalWrite(13, LOW);
  delay(300);
}

