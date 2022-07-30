#include <OneWire.h> 
#include <DallasTemperature.h>
#include <WiFiClientSecure.h>
#define tempPin0 14
#define tempPin1 26
OneWire oneWire0(tempPin0); 
OneWire oneWire1(tempPin1); 
DallasTemperature sensor0(&oneWire0);
DallasTemperature sensor1(&oneWire1);

//////////// user changes here
const char* ssid     = "SSIDname";     // your network SSID (name of wifi network)
const char* password = "SSIDpassword"; // your network password
const char * udpAddress = "192.168.1.100"; // IP address of local syslog server
const int udpPort = 3333; // listening port on syslog server
WiFiUDP udp;  // send udp or tcp 
//////////// no changes below this line
boolean connected = false; //start in disconnected state
void setup() {
 //Initialize serial and wait for port to open:
 Serial.begin(115200);
 delay(100);
 sensor0.begin(); 
 sensor1.begin(); 

  Serial.print("Attempting to connect to SSID: ");
  Serial.println(ssid);
  connectToWiFi(ssid, password);
  // attempt to connect to Wifi network:
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }

  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("My IP is: "); 
  Serial.println(WiFi.localIP());
}

void loop() {
sensor0.requestTemperatures();  // send command 
sensor1.requestTemperatures();  // send command 
float temp0C = sensor0.getTempCByIndex(0);
float temp0F = (temp0C*9/5) + 32;
float temp1C = sensor1.getTempCByIndex(0);
float temp1F = (temp1C*9/5) + 32;

 Serial.print("Temperature #0 is: "); 
 Serial.print(temp0C);
 Serial.print(" C / "); 
 Serial.print(temp0F);
 Serial.println(" F"); 

 Serial.print("Temperature #1 is: "); 
 Serial.print(temp1C);
 Serial.print(" C / "); 
 Serial.print(temp1F);
 Serial.println(" F"); 
 Serial.println(""); 

// send to listening server
if(connected){
    //Send data to syslog server
    udp.beginPacket(udpAddress,udpPort);
    udp.print(temp0F);  // for Celcius, change F to C
    udp.print(",");
    udp.print(temp1F);  // for Celcius, change F to C
    udp.endPacket();
  }

 delay(60 000); 
}

void connectToWiFi(const char * ssid, const char * pwd){
  Serial.println("Connecting to WiFi network: " + String(ssid));
  WiFi.disconnect(true);
  WiFi.onEvent(WiFiEvent);
  WiFi.begin(ssid, password);
  Serial.println("Waiting for WIFI connection...");
}
void WiFiEvent(WiFiEvent_t event){
    switch(event) {
      case ARDUINO_EVENT_WIFI_STA_GOT_IP:
          //When connected set 
          Serial.print("WiFi connected! IP address: ");
          Serial.println(WiFi.localIP());  
          //initializes the UDP state
          //This initializes the transfer buffer
          udp.begin(WiFi.localIP(),udpPort);
          connected = true;
          break;
      case ARDUINO_EVENT_WIFI_STA_DISCONNECTED:
          Serial.println("WiFi lost connection");
          connected = false;
          break;
      default: break;
    }
}
