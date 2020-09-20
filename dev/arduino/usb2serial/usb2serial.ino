/**********************************************
 *
 * MIT License, Kevin J. Walchko (c) 2020
 *
 *********************************************/
#include <stdint.h>

#define usleep delayMicroseconds
#define msleep delay
#define DD_W HIGH
#define DD_R LOW
#define PIN 1
#define BAUDRATE 1000000

uint8_t buffer[256];

void setup() {
    Serial.begin(115200);
    Serial.setTimeout(1);
    Serial1.begin(BAUDRATE);
    Serial1.setTimeout(1);
    pinMode(PIN, OUTPUT);
}

void loop() {
    // USB => AX-12
  int size = Serial.available();
  if (size > 5) {
//    Serial1.readBytes(buffer, 256); // flush input?
    digitalWrite(PIN, DD_W);
    Serial.readBytes(reinterpret_cast<char*>(buffer), size);
    Serial1.write(buffer, size);
    usleep((size << 3) + 20); // wait for write complete, bits at 1Mb DR
    digitalWrite(PIN, DD_R);
    usleep(500 + 200); // default packet hold time before response
  }
  
  // AX-12 => USB
  size = Serial1.available();
  if (size > 5) {
    Serial1.readBytes(buffer, size);
    Serial.write(buffer, size);
  }

  msleep(1);
}
