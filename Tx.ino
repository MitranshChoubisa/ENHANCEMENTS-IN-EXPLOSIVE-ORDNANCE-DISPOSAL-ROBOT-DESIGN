#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <RF24_config.h>
const char data[30];
RF24 radio(7,8); //CNS,CE

const byte address[6] = "abcde";
void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(address); 
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}

void loop() {
  data[] = "Enhancements in Explosive Ordnance Disposal Robot design";
  radio.write(&data,sizeof(data));
  delay(1000);
}
