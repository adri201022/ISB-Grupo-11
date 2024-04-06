/*************************************
 Curso: ISB-UPCH
 Date: 29/03/2023
 Autor: Moises Meza
**************************************/

unsigned long lastMsg = 0;
float F = 5;                   // 1 hz
double Fs = 10 * F;               // 10 hz
double Ts_ms = (1 / Fs) * 1000;  // 100 ms
int valor;                        // Variable global

void setup() {
  Serial.begin(9600);
  while (!Serial);
}

void loop() {
  unsigned long now = millis();

  if (now - lastMsg > Ts_ms) {
    lastMsg = now;

    int r1 = random(10);
    int r2 = random(10);
    valor = analogRead(A0);  // Lee el valor analógico en cada iteración
    Serial.print("Señal2:");
    Serial.println(valor);
  }
}
