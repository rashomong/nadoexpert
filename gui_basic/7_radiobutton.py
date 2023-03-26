from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="메뉴를 선택하세요").pack()

# radiobutton은 여러 값 중에 하나만 선택 가능
burger_var = IntVar()  
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable = burger_var)
btn_burger1.select()    # 기본 선택값
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable = burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

label2 = Label(root, text="음료를 선택하세요").pack()
drinkvar = StringVar()  # 문자열 var
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable = drinkvar)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable = drinkvar)
btn_drink1.pack()
btn_drink2.pack()

def btncmd():
    print(burger_var.get()) # 선택한 value 출력
    print(drinkvar.get())

btn = Button(root, text="주문하기", command=btncmd)
btn.pack()

root.mainloop() #꺼지지 않도록 루프


