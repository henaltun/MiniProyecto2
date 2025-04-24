import cv2
import mediapipe as mp
import serial
import time

# Configura el puerto serial 
puerto = 'COM3'  # Puerto Arduino
arduino = serial.Serial(puerto, 9600)
time.sleep(2)  # Espera a que el Arduino se reinicie

# Inicializa MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

# Variables auxiliares
dedos_previos = -1

# Detección de cámara
cap = cv2.VideoCapture(0)

# Detección de dedos (índices: [pulgar, índice, medio, anular, meñique])
dedos_ids = [4, 8, 12, 16, 20]

while True:
    ret, frame = cap.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = hands.process(frame_rgb)

    dedos_arriba = 0

    if resultados.multi_hand_landmarks:
        for mano in resultados.multi_hand_landmarks:
            lm = mano.landmark

            # Pulgar (eje X)
            if lm[dedos_ids[0]].x < lm[dedos_ids[0] - 1].x:
                dedos_arriba += 1

            # Otros dedos (eje Y)
            for id in range(1, 5):
                if lm[dedos_ids[id]].y < lm[dedos_ids[id] - 2].y:
                    dedos_arriba += 1

            # Dibuja la mano
            mp_draw.draw_landmarks(frame, mano, mp_hands.HAND_CONNECTIONS)

    # Solo envía si cambió el número
    if dedos_arriba != dedos_previos:
        print(f"Dedos: {dedos_arriba}")
        arduino.write(f"{dedos_arriba}\n".encode())
        dedos_previos = dedos_arriba

    # Muestra el video
    cv2.imshow("Contador de Dedos", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Presionar ESC para salir
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
