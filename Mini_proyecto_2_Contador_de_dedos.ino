// Segmentos del display conectados a pines digitales
const int segmentos[] = {2, 3, 4, 5, 6, 7, 8};

// Formato: A, B, C, D, E, F, G (1 = encendido, 0 = apagado)
// Lógica original (pensada para cátodo común)
const byte numeros[6][7] = {
  {1,1,1,1,1,1,0},  // 0
  {0,1,1,0,0,0,0},  // 1
  {1,1,0,1,1,0,1},  // 2
  {1,1,1,1,0,0,1},  // 3
  {0,1,1,0,0,1,1},  // 4
  {1,0,1,1,0,1,1}   // 5
};

String dato = "";

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < 7; i++) {
    pinMode(segmentos[i], OUTPUT);
    digitalWrite(segmentos[i], HIGH); // Apagar todo al inicio (ánodo común)
  }
}

void loop() {
  if (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      int numero = dato.toInt();
      if (numero >= 0 && numero <= 5) {
        mostrarNumero(numero);
      }
      dato = "";
    } else {
      dato += c;
    }
  }
}

void mostrarNumero(int n) {
  for (int i = 0; i < 7; i++) {
    digitalWrite(segmentos[i], numeros[n][i] ? LOW : HIGH);
    // LOW enciende (por ánodo común), HIGH apaga
  }
}
