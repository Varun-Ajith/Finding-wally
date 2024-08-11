import cv2

image = cv2.imread("nnn.jpg")
wally = cv2.imread("nnn1.png", 0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(gray, wally, cv2.TM_CCOEFF)
min_vel, max_vel, min_loc, max_loc = cv2.minMaxLoc(result)

print(max_loc)

top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)

cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 5)
cv2.imshow("img", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
