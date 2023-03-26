from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480+300+100")    # 크기 설정 알파뱃 'x'사용 + 열리는 x,y 좌표 위치

frame = Frame(root)
frame.pack()

Scrollbar = Scrollbar(frame)
Scrollbar.pack(side="right", fill="y") # 스크롤바는 오른쪽에

listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand = Scrollbar.set)
#yscrollcommand 를 넣어줘야지 스크롤시 작동함

for i in range(1,32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

Scrollbar.config(command=listbox.yview)

root.mainloop() #꺼지지 않도록 루프


