#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
#include <RF24_config.h>
const char data[10];
RF24 radio(7,8); //CNS,CE

const byte address[6] = "abcde";
void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0,address); 
  radio.setPALevel(RF24_PA_MIN);
  radio.startListening();
}


void loop() {
  // put your main code here, to run repeatedly:
  if (radio.available()){
    char data[32] ="";
    radio.read(&data , sizeof(data));
    Serial.println(data);
  }
}
