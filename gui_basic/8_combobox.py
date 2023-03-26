import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

#   combobox는 확장식으로 됨
values = [str(i) + "일" for i in range(1,32)]   # 1~31 까지 수 생성
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # combobox 제목 설정

combobox1 = ttk.Combobox(root, height=10, values=values, state="readonly")
combobox1.current(0)    # 기본0번째 인덱스 값 선택
combobox1.pack()        # readonly이기 때문에 글 입력 불가

def btncmd():
    print(combobox.get())


btn = Button(root, text="선택하기", command=btncmd)
btn.pack()

root.mainloop() #꺼지지 않도록 루프


