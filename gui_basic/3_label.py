from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="image.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="또만나요.")

    global photo2                # global을 선언 해주어야 바뀐다.
    photo2 = PhotoImage(file="image2.png")
    label2.config(image=photo2)


btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop() #꺼지지 않도록 루프
 