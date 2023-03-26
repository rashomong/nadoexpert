import os
from tkinter import *   # __all__에다가 정의를 하지 않으면 서브모듈은 import하지 않음
import tkinter.messagebox as msgbox
import tkinter.ttk as ttk
from tkinter import filedialog  # 서브모듈이기 때문에 *로 못가져옴
from PIL import Image

root=Tk()
root.title("Nado GUI")

# 파일 추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", \
        filetypes=(("PNG 파일", "*.png"),("모든 파일", "*.*" )), \
         initialdir=r"nadoexpert")
    # 모든 확장자 파일을 선택가능하며, 최초경로를 지정해 줄 수 있다.
    # r 을 앞에 붙이면 /r /d /t 같은 줄이나 공백 무시한다.

    # 사용자가 선택한 파일 목록을 리스트에 넣는다
    for file in files:
        list_file.insert(END, file)

# 선택 삭제 함수
def del_file():
    # print(list_file.currentselection) # 인덱스 반환 해줌    # 하지만 이런 식으로 지우면 0번을 지운후 1번이 0번으로 갱신되어 복잡해짐
    for index in reversed(list_file.curselection()):
        list_file.delete(index)
        # 선택 삭제를 누르면 맨 뒤에꺼 먼저 지운다.

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    print(folder_selected)
    txt_dest_path.delete(0, END)    #entry 이므로 0으로. txt였다면 '0.1' 로 했어야 함
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합 함수
def merge_image():
    print("가로넓이 : " , cmb_width.get())
    print("간격 : " , cmb_space.get())
    print("포맷 : ", cmb_format.get())

    # 가로
    img_width = cmb_width.get()
    if img_width == "원본유지":
        img_width = -1  # -1일때는 원본유지로 따로 작업 없어도됨
    else:
        img_width = int(img_width)

    # 간격
    img_space = cmb_space.get()
    if img_space == "좁게":
        img_space = 30
    elif img_space == "보통":
        img_space = 60
    elif img_space == "넓게":
        img_space = 90
    elif img_space == "없음":
        img_space = 0

    # 포맷
    img_format = cmb_format.get().lower()   # PNG,JPG,BMP 값 가져와서 소문자로 변경

    #######################
    # print(list_file.get(0,END))   # 잘 불러왔나 확인용
    images = [Image.open(x) for x in list_file.get(0,END)]  # list_file 을 list []로 저장.
    # size -> size[0] : width, size[1] : height
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]
    # print("width : ", widths)
    # print("height : " ,heights)

    images_sizes = []  
    if img_width > -1 :
        image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
    else:
        images_sizes = [(x.size[0], x.size[1]) for x in images]

    # unzip 활용하기 (x.size[0] for x in images) 는 [(10,10) ,(20,20) ...] 꼴로 저장됨.
    widths, heights = zip(*(image_sizes))

    max_width, total_height = max(widths), sum(heights)
    # print("max width :", max_width) 
    # print("total height :", total_height)

    # 스케치북 준비
    if img_space > 0:
        total_height += (img_space * (len(images -1)))

        
    result_img = Image.new("RGB", (max_width, total_height), (255,255,255)) # 배경은 흰색
    y_offset = 0    # y 위치
    # for img in images:
    #     result_img.paste(img, (0,y_offset)) # images에 있는 사진들을 특정 위치에 삽입 paste = 붙여넣다
    #     y_offset += img.size[1]  # height값 만큼 더해주어서 다음 이미지 삽입
    
    # 위처럼 해도 되나, progress 바 갱신을 위해서 idx 변수도 추가해서 다시 씀
    for idx, img in enumerate(images) : 
        result_img.paste(img, (0,y_offset))
        y_offset += img.size[1]

        progress = (idx + 1) / len(images) * 100
        p_var.set(progress)
        progress_bar.update()


    dest_path = os.path.join(txt_dest_path.get(), "nado_photo.jpg") # 결과물의 경로
    result_img.save(dest_path)
    msgbox.showinfo("알림", "작업이 완료되었습니다.")


def start ():
    # 각 옵션들 값 확인
    # print("가로넓이 : " , cmb_width.get())
    # print("간격 : " , cmb_space.get())
    # print("포맷 : ", cmb_format.get())

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0 :
        msgbox.showwarning("경고", "저장 경로를 선택하세요")
        return

    # 이미지 합치기 작업
    merge_image()


# 파일 프레임
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)   #   fill=x 를 하면 가로영역을 모두 차지한다.

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left")  # fill=x 를 했으므로 왼쪽 끝에 붙게됨(안하면 가운데에서 왼쪽)

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="선택 삭제", command=del_file)
btn_del_file.pack(side="right")


# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)    # fill을 통해 프레임 크기 지정

Scrollbar = Scrollbar(list_frame)
Scrollbar.pack(side="right",fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=Scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
Scrollbar.config(command=list_file.yview)


###### 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)   #entry 줄바꿈이 불가능한 txt
txt_dest_path.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)  # ipad 는 inner 안쪽 영역

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
btn_dest_path.pack(side="right", padx=5, pady=5)


######옵션 프레임
frame_option = LabelFrame(root, text="옵션")
frame_option.pack(padx=5, pady=5,ipady=5)


# 1. '가로 넓이'를 지정해주는 박스
# 가로 넓이 레이블
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left")

# 가로 넓이 콤보박스
opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly", values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side="left", padx=5, pady=5)

# 2. '간격 옵션'을 지정해주는 부분
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = ttk.Combobox(frame_option, state="readonly", values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side="left", padx=5, pady=5)

# 3. 파일 포맷(확장자) 지정
lbl_space = Label(frame_option, text="포맷", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly", values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side="left", padx=5, pady=5)


### 진행 상황 progress bar
frame_progress = LabelFrame(root, text="진행상황")
frame_progress.pack(fill="x", padx=5, pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)


### 시작 , 닫기 실행프레임
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text="닫기", width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text="시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)



root.resizable(False,False)  # 크기 조절 불가
root.mainloop()