#include <esp_now.h>
#include <WiFi.h>
#include <esp_wifi.h>

#define SENSOR_ID 1 
#define LDRPIN 33
#define CURRENTPIN 34
uint8_t S4Address[] = {0xE8, 0x6B, 0xEA, 0xDE, 0xC5, 0x00};

int value = 0;
int mVperAmp = 100; // 66 mV/A output sensitivity
int ACSoffset = 5500 / 2;

typedef struct struct_message {
  uint8_t sensorId=NULL;
  int ldrValue=NULL; 
  float current=NULL;
   
} struct_message;
struct_message myData;

struct_message receivedData[1];

constexpr char WIFI_SSID[] = "Debangshu";

int32_t getWiFiChannel(const char *ssid) {
  int32_t n = WiFi.scanNetworks();
  if (n > 0) {
    for (uint8_t i = 0; i < n; i++) {
      if (strcmp(ssid, WiFi.SSID(i).c_str()) == 0) {
        return WiFi.channel(i);
      }
    }
  }
  return 0;
}

esp_now_peer_info_t peerInfo;

void OnDataSent(const uint8_t *mac_addr, esp_now_send_status_t status) {
  Serial.print("\r\nLast Packet Send Status:\t");
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Delivery Success" : "Delivery Fail");
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  int32_t channel = getWiFiChannel(WIFI_SSID);
  Serial.print("Channel:");
  Serial.println(channel);

  if (channel == 0) {
    Serial.println("Failed to get Wi-Fi channel.");
    return;
  }

  esp_wifi_set_channel(channel, WIFI_SECOND_CHAN_NONE);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  esp_now_register_send_cb(OnDataSent);

  memcpy(peerInfo.peer_addr, S4Address, 6);
  peerInfo.channel = 0;  
  peerInfo.encrypt = false;
         
  if (esp_now_add_peer(&peerInfo) != ESP_OK){
    Serial.println("Failed to add peer");
    return;
  }
}

void loop() {

  int ldrValue = analogRead(LDRPIN);
  float current = getCurrent(); // Function to calculate current using ACS712

  myData.sensorId = SENSOR_ID;
  myData.ldrValue = ldrValue;
  myData.current = current;

  receivedData[value++] = myData;

  esp_err_t result = esp_now_send(S4Address, (uint8_t *) &value, sizeof(value));

  if (result == ESP_OK) {
    for(int i=0;i<value;i++){
      esp_err_t result2 = esp_now_send(S4Address, (uint8_t *) &receivedData[i], sizeof(receivedData[i]));
      if(result2 == ESP_OK){
        
        Serial.println(myData.sensorId);
        Serial.println(myData.ldrValue);
        Serial.println(myData.current);
      }else {
      Serial.println("Error sending the data");
    }
    }
    value=0;
    myData.sensorId = NULL;
    myData.ldrValue = NULL;
    myData.current = NULL;
  }

  delay(3000);
}

float getCurrent() {
  int RawValue = analogRead(CURRENTPIN);
  float Voltage = (RawValue / 4096.0) * 5000; // mV
  float Amps = ((Voltage - ACSoffset) / mVperAmp);
  return Amps;
}