#include  <SoftwareSerial.h>SoftwareSerial BTSerial(10, 11);const int led = 8;const int laser = 13;char value;const byte trig = 11;const byte echo = 2;const int dangerDistance = 580; //10cm * 58const int leftSpeed = 220;const int rightSpeed = 220;const byte motorLeft_1 = 9;const byte motorLeft_2 = 6;const byte motorRight_1 = 5;const byte motorRight_2 = 3;const int SLeft = 4;const int SMiddle = 7;const int SRight = 12;long distance;byte direction = 0; // 0 -> Forward  1 -> Rightbyte sensorStatus = 0;void setup() {    Serial.begin(9600);    BTSerial.begin(9600);    pinMode(led, OUTPUT);    pinMode(laser, OUTPUT);        pinMode(motorLeft_1, OUTPUT);    pinMode(motorLeft_2, OUTPUT);    pinMode(motorRight_1, OUTPUT);        pinMode(motorRight_2, OUTPUT);    pinMode(trig, OUTPUT);    pinMode(echo, INPUT);        pinMode(SLeft, INPUT);    pinMode(SMiddle, INPUT);    pinMode(SRight, INPUT);        analogWrite(motorLeft_1, 0);    analogWrite(motorLeft_2, 0);    analogWrite(motorRight_1, 0);    analogWrite(motorRight_2, 0);}void loop() {  if (BTSerial.available()){    value = BTSerial.read();    //Serial.write(value);    //BTSerial.println(value);    switch(value){      case 'a':        Forward(255);        Serial.println("a -> forward");        break;      case 'b':        Back(255);        Serial.println("b -> back");        break;      case 'c':        Right(255);        Serial.println("c -> right");        break;      case 'd':        Left(255);        Serial.println("d -> left");        break;      case 'e':        digitalWrite(laser, HIGH);        break;      case 'f':        digitalWrite(laser, LOW);        break;      case 'g': //循跡模式        IRsensor();        break;      case 'h': //循跡 + 超音波        Car();        break;      case 's':        Stop(0);        break;    }  }    /*  if (Serial.available())    {      BTSerial.write(Serial.read());    }    */}void Forward(byte speed){  analogWrite(motorLeft_1, speed);  analogWrite(motorLeft_2, 0);  analogWrite(motorRight_1, speed);  analogWrite(motorRight_2, 0);  Serial.println("forward");}void Back(byte speed){  analogWrite(motorLeft_1, 0);  analogWrite(motorLeft_2, speed);  analogWrite(motorRight_1, 0);  analogWrite(motorRight_2, speed);  Serial.println("back");}void Left(byte speed){  analogWrite(motorRight_1, speed);  analogWrite(motorRight_2, 0);  analogWrite(motorLeft_1, 0);  analogWrite(motorLeft_2, 0);  Serial.println("left");}void Right(byte speed){  analogWrite(motorLeft_1, speed);  analogWrite(motorLeft_2, 0);  analogWrite(motorRight_1, 0);  analogWrite(motorRight_2, 0);  Serial.println("right");}void Stop(byte speed){  analogWrite(motorLeft_1, speed);  analogWrite(motorLeft_2, speed);  analogWrite(motorRight_1, speed);  analogWrite(motorRight_2, speed);  Serial.println("stop");}long ping(){  digitalWrite(trig, HIGH);  delayMicroseconds(5);  digitalWrite(trig, LOW);    return pulseIn(echo, HIGH);}void driveMotor(byte status){  switch(status){    case 7:      Stop(0);      break;    case 6:      Left(255);      break;    case 5:      Stop(255);      break;    case 4:      Left(255);      break;    case 3:      Right(255);      break;    case 2:      Forward(255);      break;    case 1:      Right(255);      break;    case 0:      Forward(255);  }}void Car(){  int IRstatus;    sensorStatus = 0;    digitalWrite(led, LOW);        IRstatus = digitalRead(SLeft);    if(IRstatus == 1)     sensorStatus = (sensorStatus | (0x01 << 2));         IRstatus = digitalRead(SMiddle);    if(IRstatus == 1)     sensorStatus = (sensorStatus | (0x01 << 1));         IRstatus = digitalRead(SRight);    if(IRstatus == 1)     sensorStatus = (sensorStatus | 0x01);         driveMotor(sensorStatus);  //-------------------------------------------------    distance = ping();    if(distance > dangerDistance){      if(direction != 0){        direction = 0;        Stop(0);        delay(500);      }      Forward(220);      //Left(150);      //Back(120);          }else{      digitalWrite(led, HIGH);      if(direction != 1){        direction = 1;        Stop(0);        delay(500);      }      Right(220);      Back(220);    }        delay(1000);}void IRsensor(){  int IRstatus;    sensorStatus = 0;        IRstatus = digitalRead(SLeft);    if(IRstatus == 1)     sensorStatus = (sensorStatus | (0x01 << 2));         IRstatus = digitalRead(SMiddle);    if(IRstatus == 1)     sensorStatus = (sensorStatus | (0x01 << 1));         IRstatus = digitalRead(SRight);    if(IRstatus == 1)     sensorStatus = (sensorStatus | 0x01);         driveMotor(sensorStatus);}