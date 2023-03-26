from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Listbox = Listbox(root, selectmode="extended", height=0)
    # "single"이면 하나만 선택 가능
    # height가 0이면 전부 보여주고, 3이면 3줄만 보여준다.
Listbox.insert(0, "사과")
Listbox.insert(1, "딸기")
Listbox.insert(2, "바나나")
Listbox.insert(END, "수박")     # 순서 생각 없이 끝에 추가.
Listbox.insert(END, "포도") 
Listbox.pack()

def btncmd():
    # Listbox.delete(END)   # 뒤에서 부터 삭제
    # Listbox.delete(0)     # 앞에서부터 삭제

    # 갯수 확인
    # print("리스트에는", Listbox.size(), "개가 있어요")

    # 항목 확인 
    # print("1번째부터 3번째 까지의 항목 : ", Listbox.get(0,2))

    # 선택된 항목 확인
    # print("선택된 항목은 : " ,Listbox.curselection())
    pass



btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() #꺼지지 않도록 루프


