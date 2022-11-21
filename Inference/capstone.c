#include <Servo.h>
Servo fist, elbow, shoulder;
String x;
float move_number=0;

float grab_limit=10, release_limit=110;
float elbow_up_limit=110, elbow_down_limit=50;
float shoulder_left_limit=50, shoulder_right_limit=150;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);

  fist.attach(9);
  elbow.attach(8);
  shoulder.attach(11);
}

void loop() {
  while (!Serial.available());
  x = Serial.readString();
  Serial.print(x);
  
  if (x=="release")
  {
    fist.write(release_limit);
  }
  if (x=="grab")
  {
    fist.write(grab_limit);
  }
  if (x=="shoulder_left")
  {
    for (float pos=150; pos>=shoulder_left_limit; pos-=1) {
      shoulder.write(pos);
      delay(10);
    }
  }
  if (x=="shoulder_right")
  {
    for (float pos=50; pos<=shoulder_right_limit; pos+=1) {
      shoulder.write(pos);
      delay(10);
    }
  }
  if (x=="elbow_down")
  {
    for (float pos=110; pos>=elbow_down_limit; pos-=1) {
      elbow.write(pos);
      delay(10);
    }
  }
  if (x=="elbow_up")
  {
    for (float pos=50; pos<=elbow_up_limit; pos+=1) {
      elbow.write(pos);
      delay(10);
    }
  }
}