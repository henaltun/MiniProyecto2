# MiniProyecto2
Mini proyecto 2 de inteligencia artificial UMG

🧠 Resumen del Proyecto
Este proyecto detecta cuántos dedos tienes levantados frente a la cámara, usando MediaPipe y OpenCV en Python, y luego envía ese número a un Arduino por puerto serial. El Arduino muestra el número en un display de 7 segmentos.

💻 Parte en Python (PC)
Cámara + MediaPipe: Se usa cv2.VideoCapture(0) para capturar video en tiempo real. MediaPipe analiza cada fotograma para detectar una mano y localizar sus puntos clave (landmarks).

Contador de Dedos:

El pulgar se verifica por su posición en eje X.

Los otros dedos (índice a meñique) se verifican por el eje Y: si la punta del dedo está más arriba (más cerca del borde superior del frame) que la articulación intermedia, se considera levantado.

Comunicación Serial:

Si el número de dedos levantados cambió respecto al anterior, se envía por el puerto serial (arduino.write()).

Ejemplo: si detecta 3 dedos, envía "3\n".

🔌 Parte en Arduino
Recepción Serial:

El Arduino recibe datos como texto (por ejemplo, "3\n"), lo convierte a número con .toInt() y lo guarda como int numero.

Display de 7 segmentos:

Un array numeros[6][7] para definir qué segmentos deben encenderse para cada número del 0 al 5.

El mostrarNumero() enciende los pines correspondientes del display según el número recibido.

Tipo de Display:

Usando un display de ánodo común, se enciende un segmento escribiendo LOW, y se apaga con HIGH.

📦 Conexión General
PC → Python: Detecta dedos y envía número por USB.

USB → Arduino: Recibe el número y actualiza el display.

Arduino → Display: Muestra visualmente cuántos dedos estás levantando (0 a 5).
