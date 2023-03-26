# 그리드란 격자 의미
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100")    # 크기 설정 알파뱃 'x'사용 + 열리는 x,y 좌표 위치

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # btn1.pack(side="left")
# # btn2.pack(side="right")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

## 반복 구절이 많은 부분
## sticky=N+E+W+S 에 con + C 한 후에 con + f 하면 한번에 덧붙이기 가능

# 숫자 패드 만들기
# 맨 윗줄
btn_f16 = Button(root, text="F16", width=5,height=2)    # padx = 버튼 크기 설정
btn_f17 = Button(root, text="F17", width=5,height=2)
btn_f18 = Button(root, text="F18", width=5,height=2)
btn_f19 = Button(root, text="F19", width=5,height=2)
btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)   # sticky 버튼 최대 공간으로 확장
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)   # grid에 padx,y를 넣으면 버튼사이 공백생김
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

#clear 줄
btn_clear = Button(root, text="clear")
btn_eqeal = Button(root, text="=")
btn_div = Button(root, text="/")
btn_mul = Button(root, text="*")
btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_eqeal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 789-
btn_7 = Button(root, text="7")
btn_8 = Button(root, text="8")
btn_9 = Button(root, text="9")
btn_mi = Button(root, text="-")
btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mi.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 456+
btn_4 = Button(root, text="4")
btn_5 = Button(root, text="5")
btn_6 = Button(root, text="6")
btn_pl = Button(root, text="+")
btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_pl.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 123en
btn_1 = Button(root, text="1")
btn_2 = Button(root, text="2")
btn_3 = Button(root, text="3")
btn_en = Button(root, text="enter") # 세로로 합쳐짐
btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_en.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) # 행 합치기

btn_0 = Button(root, text="0")
btn_dot = Button(root, text=".")
btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_dot.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop() #꺼지지 않도록 루프
