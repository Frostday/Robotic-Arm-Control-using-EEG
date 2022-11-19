#include <Servo.h>

Servo fist, shoulder, elbow;
String x;
int moves;
int fist_pos=0, shoulder_pos=0, elbow_pos=0;
int batch=32

void setup() {
    Serial.begin(115200);
    Serial.setTimeout(1);
    fist.attach(9);
    shoulder.attach(10);
    elbow.attach(11);
}

void loop() {
    for(int i=0;i<batch;i++)
    {
        while (!Serial.available());
        x = Serial.readString();
        moves = moves + 1;
        // add into array
    }
    // take highest occuring array value
    Serial.print(x);
    if(strcmp(x,"rest")==0)
    {
        // stop all movement
    }
    if(strcmp(x,"grab")==0)
    {
        for (pos=fist_pos; pos<=fist_pos+10; pos+=1)
        {
            fist.write(pos);
            delay(15);
        }
        fist_pos = pos;
    }
    if(strcmp(x,"release")==0)
    {
        
    }
    if(strcmp(x,"elbow_up")==0)
    {
        
    }
    if(strcmp(x,"elbow_down")==0)
    {
        
    }
    if(strcmp(x,"wrist_supination")==0)
    {
        
    }
    if(strcmp(x,"wrist_pronation")==0)
    {
        
    }
    if(strcmp(x,"shoulder_right")==0)
    {
        
    }
    if(strcmp(x,"shoulder_left")==0)
    {
        
    }
}
