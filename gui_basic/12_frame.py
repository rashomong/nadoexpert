from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame_burger = Frame(root, relief="solid", bd=1)  # 태두리 모양, 외곽선
frame_burger.pack()

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack()
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()

root.mainloop() #꺼지지 않도록 루프
