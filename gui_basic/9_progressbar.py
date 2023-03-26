import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

#   다운로드바 같이 생긴거 생성
# progressbar =ttk.Progressbar(root, maximum=100, mode ="indeterminate")
    # indeterminate 는 불확정 
# progressbar =ttk.Progressbar(root, maximum=100, mode ="determinate")
#     # determinate 이어짐
# progressbar.start() # 괄호 속 수가 속도 10 -> 10ms마다 움직임(작을수록 빠름)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # 작동 중지

p_var2 = DoubleVar()    # 올라가는 값 실수도 사용
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)    # 0.01초 대기

        p_var2.set(i)   # 1 부터 100까지 가는거 보여주려고 만듦
        progressbar2.update()   # 0.01초 마다 갱신
        print(p_var2.get())

btn = Button(root, text="선택하기", command=btncmd2)
btn.pack()

root.mainloop() #꺼지지 않도록 루프

