import cv2
import numpy as np

cam = cv2.VideoCapture(1)

pontos = None

frame_anterior = None

while True:

    success, frame = cam.read()

    if not success:
        print("Não foi possível acessar a câmera.")
        break

    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if pontos is not None and frame_anterior is not None:

        novos_pontos, status, erro = cv2.calcOpticalFlowPyrLK(frame_anterior, frame_cinza, pontos, None)

        if novos_pontos is not None:

            pontos_validos = novos_pontos[status == 1]

            if len(pontos_validos) == 4:

                pontos = novos_pontos

                for ponto in pontos:
                    x, y = ponto.ravel()

                    cv2.circle(frame, (int(x), int(y)), 8, (0, 0, 255), -1)

                cv2.polylines(frame, [pontos.astype(int)], True, (0, 255, 0), 3)

    if pontos is None:

        desfoque = cv2.GaussianBlur(frame_cinza, (3, 3), 0)

        bordas = cv2.Canny(desfoque, 50, 150)

        contornos, hierarquia = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for c in contornos:

            perimetro = cv2.arcLength(c, True)

            aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)

            if len(aprox) == 4 and cv2.isContourConvex(aprox):

                area = cv2.contourArea(aprox)

                if area > 5000:

                    pontos = aprox.astype(np.float32)
                    break


    frame_anterior = frame_cinza.copy()

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cam.release()
cv2.destroyAllWindows()