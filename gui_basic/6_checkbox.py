from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# 체크박스. 팝업창 뛰우기
chkvar = IntVar()   #chkvar 에 int형으로 값 저장
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
chkbox.select()     # 기본으로 체크되어있음.
# chkbox.deselect()   # 기본으로 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0이면 체크 해제, 1이면 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #꺼지지 않도록 루프


