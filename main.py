import cv2

img = cv2.imread('imagensTeste/imgMelhor1.jpeg', cv2.IMREAD_COLOR)
img = cv2.resize(img, (800, 600))

cv2.imshow("Imagem", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('cinza', img_gray)

bordas = cv2.Canny(img_gray, 100, 200)
cv2.imshow("bordas", bordas)


cv2.waitKey(0)
cv2.destroyAllWindows()