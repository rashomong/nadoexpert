from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

e = Entry(root, width=30)       # entry  는 엔터(줄바꿈) 불가능
e.pack()
e.insert(0, "글자는 한줄만 입력해요")

def btncmd():
    print(txt.get("1.0",END))   # 1은 1번째 줄부터, 0은 줄의 첫번째. 즉 제일 처음 단어를 가지고옴. END는 끝까지. 
    print(e.get())

    txt.delete("1.0",END)       # 입력한 문자를 가지고 오고 전부 삭제
    e.delete(0,END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #꺼지지 않도록 루프


