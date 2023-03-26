import time
from PIL import ImageGrab

time.sleep(5)   # 5초 대기

for i in range(1,11):   # 10번 반복
    img = ImageGrab.grab()  # 이미지 가지고 와서
    img.save("image{}.png".format(i))   # 파일로 저장
    time.sleep(2)   # 2초 쉬고