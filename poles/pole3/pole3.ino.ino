#include <esp_now.h>
#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "Debangshu";
const char* password = "123456789";
const char* serverUrl = "http://192.168.182.133/UserMade_esp_receive/pole3_handlerNew.php";

#define THRESHOLD_LDR 2000 // Example threshold for LDR
#define THRESHOLD_CURRENT 15 // Example threshold for Current
#define SENSOR_ID 3
#define LDRPIN 33 
#define CURRENTPIN 34


int value=0; 
int currentIndex =0; 
int mVperAmp = 100; // 66 mV/A output sensitivity 
int ACSoffset = 5500 / 2;

typedef struct struct_message {
  uint8_t sensorId=NULL;
  int ldrValue=NULL;
  float current=NULL;
} struct_message;
struct_message myData;

struct_message receivedData[3]; // Array to store data from Pole 1, Pole 2, and Pole 3

void OnDataRecv(const esp_now_recv_info_t *recv_info, const uint8_t *data, int data_len){ 
  const uint8_t *mac_addr = recv_info->src_addr;
  if (data_len == sizeof(int)) { 
    value=*data; 
  } 
  if (data_len == sizeof(struct_message)) { 
    struct_message *incomingData = (struct_message *)data; 
    receivedData[currentIndex].sensorId = incomingData->sensorId; 
    receivedData[currentIndex].ldrValue = incomingData->ldrValue; 
    receivedData[currentIndex++].current = incomingData->current; 
  }
}

void sendDataToServer(const char* id, int v1, int v2) {
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  HTTPClient http;
  http.begin(serverUrl);
  http.addHeader("Content-Type", "application/x-www-form-urlencoded");

  // Construct the POST data
  String postData = "id=";
  postData += id;
  postData += "&val1=";
  postData += v1;
  postData += "&val2=";
  postData += v2;

  int httpResponseCode = http.POST(postData);
  Serial.println(postData);

  if (httpResponseCode > 0) {
    String response = http.getString();
    Serial.println("Server response: " + response);
  } else {
    Serial.print("Error on HTTP request. Error code: ");
    Serial.println(httpResponseCode);
  }

  http.end();
  WiFi.disconnect(true);
  WiFi.mode(WIFI_STA);
}

void setup() {
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  if (esp_now_init() != ESP_OK) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  esp_now_register_recv_cb(OnDataRecv);
}

void loop() {
  int ldrValue = analogRead(LDRPIN); 
  float current = getCurrent(); // Function to calculate current using ACS712 
 
  myData.sensorId = SENSOR_ID; 
  myData.ldrValue = ldrValue; 
  myData.current = current; 
 
  receivedData[value++] = myData;

  // Print header
  Serial.println("Pole\tLDR\tCurrent");

    for (int i = 0; i < 3; i++) {
      const char* id = "";
      int v1 = 0;
      int v2 = 0;

      if (receivedData[i].sensorId == 1) {
        id = "Pole1";
      } else if (receivedData[i].sensorId == 2) {
        id = "Pole2";
      } else if (receivedData[i].sensorId == 3) {
        id = "Pole3";
      }

      // Check thresholds and set v1 and v2 accordingly
      v1 = (receivedData[i].ldrValue < THRESHOLD_LDR) ? 1 : 0;
      v2 = (receivedData[i].current <= THRESHOLD_CURRENT) ? 1 : 0;

      // Print the values in a tabular format
      Serial.print(id);
      Serial.print("\t");
      Serial.print(v1);
      Serial.print("\t");
      Serial.println(v2);

      sendDataToServer(id, v1, v2);
    }
  value=0; 
  currentIndex =0; 
  myData.sensorId = NULL; 
  myData.ldrValue = NULL; 
  myData.current = NULL; 
  delay(3000); 
} 
 
float getCurrent() { 
  int RawValue = analogRead(CURRENTPIN); 
  float Voltage = (RawValue / 4096.0) * 5000; // mV 
  float Amps = ((Voltage - ACSoffset) / mVperAmp); 
  return Amps; 
}