# 16/04/2025
# Aussawin Saksawaddikul
# Survey Quesiton Tkinter Format Program
# Thai version

from tkinter import *
from tkinter import ttk, messagebox
import csv

# ฟอนต์ตัวอักษร
font_title = ('Aria',14,'bold')
font_1 = ('Aria',12,'normal')

LIST_USER = []

# หน้าเริ่มต้นโปรแกรม
def start_program():
    start_ui = Tk()
    start_ui.title('Application Name')
    start_ui.geometry('320x200')

    # ฟังก์ชั่นปุ่มกดเปิดหน้ากรอกข้อมูล และปิดหน้าจอหลัก
    def button():
        start_ui.destroy()
        user_gui()

    Label(start_ui,text='Application Name',font=('Arial',20,'bold')).pack(pady=25)
    Button(start_ui,text='เริ่มทำแบบสอบถาม',font=('Aria',14,'bold'),bg='steelblue1',fg='white',command=button).pack()
    start_ui.mainloop()


# ฟังก์ชั่นสร้างหน้ากรอกข้อมูล
def user_gui():

    main = Tk()
    main.title('Application Name')
    main.geometry('450x320')

    # สร้าง Frame
    frame = Frame(main,padx=10,pady=10,width=10,highlightbackground='black',highlightthickness=2)
    frame.pack(expand=False)

    # แสดงผลข้อความ
    Label(frame,text='Application Name',font=font_title).grid(row=0,columnspan=3,pady=10)
    Label(frame,text='เพศ',font=font_1).grid(row=1,column=0,pady=10)
    Label(frame,text='อายุ',font=font_1).grid(row=2,column=0,pady=10)
    Label(frame,text='แพลตฟอร์ม',font=font_1).grid(row=3,column=0,pady=10)
    Label(frame,text='จำนวนชั่วโมง',font=font_1).grid(row=4,column=0,pady=10)

    # ช่องใส่ข้อมูล
    gender_entry = ttk.Combobox(frame,width=28,font=font_1,state='readonly',values=['เพศชาย','เพศหญิง'])
    age_entry = Entry(frame, width=30,font=font_1)
    platform_entry = ttk.Combobox(frame,width=28,font=font_1,state='readonly',values=['Facebook','Tiktok','Instragram','Youtube','Line','อื่นๆ'])
    hr_entry = Entry(frame,width=30,font=font_1)

    # กำหนดช่องแสดงผล
    gender_entry.grid(row=1,column=1,sticky='e')
    age_entry.grid(row=2,column=1,sticky='e')
    platform_entry.grid(row=3,column=1,sticky='e')
    hr_entry.grid(row=4,column=1,sticky='e')

    # ฟังก์ชั่นกดปุ่มเริ่มทำแบบทดสอบ
    def go_question():
        try:
            gender = gender_entry.get()
            age = age_entry.get()
            platform = platform_entry.get()
            hr = hr_entry.get()
            if gender == '' or age == '' or platform == '' or hr == '':
                messagebox.showinfo(title='กรอกข้อมูลไม่ถูกต้อง',message='กรุณากรอกข้อมูลให้ครบถ้วน')
            else:
                #เปลี่ยนค่า age hr เป็นตัวเลข
                age = int(age)
                hr = int(hr)

                # เพิ่มเพศ,อายุ,แพลต์ฟอร์ม,จำนวนชั่วโมง ใน LIST_USER
                LIST_USER.append(gender)
                LIST_USER.append(f'{age} ปี')
                LIST_USER.append(platform)
                LIST_USER.append(f'{hr} ชั่วโมง')
                # ปิดหน้าจอหลัก
                main.destroy()
                # เปิดหน้าคำถาม
                create_survey_gui()
        except:
            messagebox.showinfo(title='กรอกข้อมูลไม่ถูกต้อง',message='กรอกอายุ/จำนวนชั่วโมง เป็นตัวเลขจำนวนเต็มเท่านั้น')

        
    Button(frame,text='เริ่มทำแบบทดสอบ',font=('Aria',12,'bold'),bg='springgreen2',fg='white',command=go_question).grid(row=5,columnspan=3,pady=10)
    main.mainloop()


# ฟังก์ชั่นสร้างหน้าต่างคำถาม
def create_survey_gui():

    root = Tk()
    root.title('Application Name')

    # Style และ Font
    style = ttk.Style()
    # Font ปุ่ม Radiobutton
    style.configure('Select.TRadiobutton',font=('Aria',12,'normal'))
    # Font ปุ่ม submit
    style.configure('submit.TButton',font=('Aria',14,'bold'))

    # โจทย์คำถาม
    questions = [
        '1. คำถามที่ 1',
        '2. คำถามที่ 2',
        '3. คำถามที่ 3',
        '4. คำถามที่ 4',
        '5. คำถามที่ 5',
        '6. คำถามที่ 6',
        '7. คำถามที่ 7',
        '8. คำถามที่ 8',
        '9. คำถามที่ 9',
        '10. คำถามที่ 10'
    ]

    # ตัวเลือกคำตอบ 4 ระดับ 
    options = ['มากที่สุด', 'มาก', 'เล็กน้อย', 'ไม่เลย']

    # เก็บคำถามและคำตอบในรูปแบบ dictionary
    responses = {}

    # สร้าง frame แต่ละคำถาม
    for i, question in enumerate(questions):
        frame = ttk.Frame(root, padding='10')
        frame.grid(row=i, column=0, sticky=(W, E))

        # โจทย์คำถาม
        question_label = ttk.Label(frame,text=question,width=50,anchor=W)
        question_label.config(font=('Aria',12,'normal'))
        question_label.grid(row=0, column=0, sticky=W)

        response_var = StringVar()
        responses[i] = response_var  # เก็บข้อมูลลงใน responses

        # สร้างปุ่มระดับจาก options
        for j, option in enumerate(options):
            radio_button = ttk.Radiobutton(frame, text=option, variable=response_var, value=option, style='Select.TRadiobutton')
            radio_button.grid(row=0, column=j + 1, padx=5)
        

    # ปุ่มกด submit คำตอบ
    def submit_survey():
        point=0
        for i, question in enumerate(questions):
            # คำนวณคะแนน ตามเกณฑ์
            response=responses[i].get()
            if response=='มากที่สุด':
                point+=4 
            elif response=='มาก':
                point+=3
            elif response=='เล็กน้อย':
                point+=2
            elif response=='ไม่เลย':
                point+=1
            else:
                # หากตอบคำถามไม่ครบ รีคะแนนเป็นศูนย์และหยุดคิดคะแนน
                point=0 
                break
                
        # กรอกคำถามไม่ครบ ให้ขึ้นแจ้งเตือน
        if point==0:
            messagebox.showinfo(title='คำตอบไม่ครบ',message='กรุณากรอกคำตอบให้ครบทุกข้อ')
        else:
            # ปิดหน้าจอคำถาม
            root.destroy()
            # เปิดหน้าสรุปผล
            summary_gui(p=point)

    # ปุ่มกดส่งคำตอบ
    submit_button = ttk.Button(root, text='ส่งคำตอบ', style='submit.TButton', command=submit_survey)
    submit_button.grid(row=len(questions), column=0, columnspan=len(options) + 1, pady=10)

    # ลูปหน้าจอให้หน้าจอแสดงผล
    root.mainloop()


# ฟังก์ชั่นสร้างหน้าสรุปผล
def summary_gui(p):

    summary = Tk()
    summary.title('Application Name')
    summary.geometry('400x450')

    Label(summary,text=f'คะแนนของคุณ คือ {p}',font=font_title).pack(pady=10)

    # เช็คคะแนน พร้อมทั้งบอกระดับ สีตัวอักษร และคำแนะนำ
    if p >= 30:
        rank = 'ระดับดี'
        color_font = 'green'
        suggest = '''คำแนะนำ\n
บรรทัดที่ 1\n
บรรทัดที่ 2\n      
'''
    elif p >= 20:
        rank = 'ปกติ'
        color_font = 'turquoise3'
        suggest = '''คำแนะนำ\n
บรรทัดที่ 1\n
บรรทัดที่ 2\n      
'''
    else :
        rank = 'ต่ำ'
        color_font = 'red'
        suggest = '''คำแนะนำ\n
บรรทัดที่ 1\n
บรรทัดที่ 2\n      
'''

    # เพิ่มคะแนนกับระดับใน LIST_USER
    LIST_USER.append(f'{p} คะแนน')
    LIST_USER.append(rank)
    
    # เก็บข้อมูลผู้ใช้ลงในไฟล์ Result.csv
    with open('Result.csv','a',encoding='utf-8',newline='') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerow(LIST_USER)

    # เคลียร์ list
    LIST_USER.clear()

    # แสดงข้อความ
    Label(summary,text=f'คุณอยู่ในระดับ{rank}',font=font_title,fg=color_font).pack()
    Label(summary,text='_'*100,font=font_title).pack()
    Label(summary,text='คำแนะนำ',font=font_title).pack(pady=10)
    Label(summary,text=suggest,font=font_1).pack(pady=5)

    # ฟังก์ชั่นปุ่มกด เพื่อปิดหน้าต่างและเริ่มโปรแกรมใหม่
    def button():
        summary.destroy()
        start_program()

    Button(summary,text='กลับหน้าเมนู',font=font_title,command=button).pack(pady=10)

    summary.mainloop()


# เริ่มต้นโปรแกรม
start_program()