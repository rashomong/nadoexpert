from tkinter import *

root = Tk()
root.title("제목없음 - mac 메모장")
root.geometry("640x480")

# 프레임 
frame = Frame(root)
frame.pack()

# 스크롤바
Scrollbar = Scrollbar(frame)
Scrollbar.pack(side="right", fill="y") # 스크롤바는 오른쪽에

# 본문
txt = Text(frame, yscrollcommand = Scrollbar.set)
txt.pack()

# def open_file():


# 메뉴
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기")
menu_file.add_command(label="저장")
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)
menu_edit = Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=menu_edit)
menu_su = Menu(menu, tearoff=0)
menu.add_cascade(label="서식", menu=menu_su)

# 본문

Scrollbar.config(command=txt.yview)
root.config(menu=menu)
root.mainloop() #꺼지지 않도록 루프