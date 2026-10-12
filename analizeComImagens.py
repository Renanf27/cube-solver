import cv2

img = cv2.imread("imagensTeste/imgMelhor1.jpeg", cv2.IMREAD_COLOR)
img = cv2.resize(img, (800, 900))

img_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.GaussianBlur(img_cinza, (5, 5), 0)

bordas = cv2.Canny(img_blur, 50, 150)

contornos, _ = cv2.findContours(bordas, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_contornos = img.copy()

cv2.drawContours(img_contornos, contornos, -1, (0, 255, 0), 2)

melhor_contorno = None
maior_area = 0

if melhor_contorno is not None:
        cv2.drawContours(img, [melhor_contorno], -1, (0, 255, 0), 3)

        for ponto in melhor_contorno:
            x, y = ponto[0]
            cv2.circle(img, (x, y), 7, (0, 0, 255), -1)

cv2.imshow("foto", bordas)

cv2.waitKey(0)
cv2.destroyAllWindows()