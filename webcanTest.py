import cv2

cam = cv2.VideoCapture(0)

ultimo_quadrado = None
frames_sem_deteccao = 0

while True:
    success, frame = cam.read()

    if not success:
        print("Não foi possível acessar a câmera.")
        break

    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    desfoque = cv2.GaussianBlur(frame_cinza, (3, 3), 0)

    bordas = cv2.Canny(desfoque, 50, 150)

    contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    melhor_contorno = None
    maior_area = 0


    for c in contornos:

        perimetro = cv2.arcLength(c, True)
        aprox = cv2.approxPolyDP(c, 0.03 * perimetro, True)


        if len(aprox) == 4 and cv2.isContourConvex(aprox):

            area = cv2.contourArea(aprox)

            if area > 5000 and area > maior_area:

                maior_area = area
                melhor_contorno = aprox

    if melhor_contorno is not None:
        cv2.drawContours(frame, [melhor_contorno], -1, (0, 255, 0), 3)

        for ponto in melhor_contorno:
            x, y = ponto[0]
            cv2.circle(frame, (x, y), 7, (0, 0, 255), -1)

    cv2.imshow("bordas", bordas)
    cv2.imshow("cubo", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
