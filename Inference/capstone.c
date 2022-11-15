String x;
int moves;

void setup() {
    Serial.begin(115200);
    Serial.setTimeout(1);
}

void loop() {
    while (!Serial.available());
        x = Serial.readString();
        moves = moves + 1;
        Serial.print(x);
}
