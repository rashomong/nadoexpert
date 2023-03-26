from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1")   # 버튼 생성
btn1.pack()     # 버튼을 프로그램에 포함시킴

btn2 = Button(root, padx=5, pady=10, text="버튼2")  #버튼 글자 기준으로 공간 확보
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼4")   # 버튼 크기 설정 (택스트가 길면 짤림)
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="image.png")        #window에서는 gui_basic/image.png 해야 된다
btn6 = Button(root, image=photo) 
btn6.pack()

def btncmd():
    print("버튼이 출력되었어요.")
      
btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() #꺼지지 않도록 루프




