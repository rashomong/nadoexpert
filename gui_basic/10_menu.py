from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="open file...")
menu_file.add_separator()
menu_file.add_command(label="Save ALL", state="disable")   #비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit",  command=root.quit)   #종료
menu.add_cascade(label="파일", menu=menu_file)

# menu.add_cascade(label="Edit")  똑같이 했는데 안나옴

# radiobutton
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="language", menu=menu_lang)

# checkbox
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop() #꺼지지 않도록 루프
