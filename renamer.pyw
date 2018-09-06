import os, time
from tkinter import *


scriptInfo = {'scriptName'    : 'Renamer',
              'authorName'    : 'Pavel_Blend',
              'modifDate'     : (2014, 9, 6),
              'scriptVersion' : (0, 0, 1)}


def author():
    authorText = 'Автор: {0}\nВерсия: {1}.{2}.{3}\n\n{4}.{5:0>2}.{6:0>2}'.format(
    scriptInfo['authorName'],
    scriptInfo['scriptVersion'][0],
    scriptInfo['scriptVersion'][1],
    scriptInfo['scriptVersion'][2],
    scriptInfo['modifDate'][0],
    scriptInfo['modifDate'][1],
    scriptInfo['modifDate'][2])
    authorWin = Toplevel(root, width=200, height=200)
    authorWin.focus()
    authorWin.minsize(width=200, height=200)
    authorWin.maxsize(width=200, height=200)
    authorWin.resizable(width=False, height=False)
    authorWin.title('О программе')
    authorWin.transient(root)
    authorWin.geometry("+%d+%d"%(root.winfo_rootx()+220, root.winfo_rooty()+30))
    nameLab = Label(authorWin, text=scriptInfo['scriptName'], font=('courier', 14, 'bold'))
    nameLab.pack(pady=24)
    authorLab = Label(authorWin, text=authorText, font=('courier', 11, 'bold'))
    authorLab.pack()


def rename_number(event):
    name = entName.get()
    try:
        i = int(ent_num.get())
    except:
        i = 1
    try:
        step = int(entNumStep.get())
    except:
        step = 1
    try:
        count_number = int(labCountNum.get())
    except:
        count_number = 3
    for f in os.listdir():
        ext = os.path.splitext(f)[1]
        if ext not in pass_ext and f not in pass_name:
            try:
                s = str(i)
                se = startEnd.get()
                nules = (count_number - len(s)) * '0'
                if se == 0:
                    new_name = name + nules + s + ext
                elif se == 1:
                    new_name = nules + s + name + ext
                os.rename(f, new_name)
                i += step
            except:
                print('Не переименован %s' % (f))


def rename_date(event):
    for f in os.listdir():
        tm = time.localtime(os.path.getmtime(f))
        name, ext = os.path.splitext(f)
        if ext not in pass_ext and f not in pass_name:
            try:
                new_name = time.strftime('%Y_%m_%d %H-%M-%S', tm) + ext
                os.rename(f, new_name)
                print('Файл %s переименован в %s' % (name + ext, new_name))
            except:
                print('Не переименован %s' % (name + ext))


def save_names(event):
    save = open('renamer_save.txt', 'w')
    for i in os.listdir():
        if i not in pass_name:
            save.write(i + '\n')
    save.close()


pass_ext = ('.py', '.pyw', '.pyc')
pass_name = ('readme_renamer.txt',
             'renamer_save.txt',
             'Thumbs.db',
             'renamer.py',
             'renamer.pyw')
root = Tk()
root.title('Rename Files')
root.minsize(width=640, height=320)
root.maxsize(width=640, height=320)
root.resizable(width=False, height=False)
x = (root.winfo_screenwidth()) / 2
y = (root.winfo_screenheight()) / 2
root.geometry('+%d+%d' % (x - 320, y - 200))
helpMenu = Menu(root)
root.config(menu=helpMenu)
docMenu = Menu(helpMenu)
helpMenu.add_cascade(label="Помощь", menu=docMenu)
docMenu.add_command(label="О программе", command=author)
labName = Label(root, text='Имя')
labName.grid(column=0, row=0)
entName = Entry(root,  width=24, bd=4, font='f 8')
entName.grid(column=1, row=0)
startEnd = IntVar()
startEnd.set(0)
radStart = Radiobutton(root, text="В начале", variable=startEnd, value=0, font='font 8')
radEnd = Radiobutton(root, text="В конце", variable=startEnd, value=1, font='font 8')
radStart.grid(column=2, row=0)
radEnd.grid(column=3, row=0)
butRenameNumber = Button(root, text='Номер', font='font 8', height=1, width=16)
butRenameNumber.bind('<Button-1>', rename_number)
butRenameNumber.grid(column=0, row=1)
labStartNum = Label(root, text='Начать с:')
labStartNum .grid(column=1, row=1)
entNum = Entry(root,  width=10, bd=4, font='f 8')
entNum.grid(column=2, row=1)
labStepNum = Label(root, text='Шаг:')
labStepNum.grid(column=3, row=1)
entNumStep = Entry(root,  width=10, bd=4, font='f 8')
entNumStep.grid(column=4, row=1)
labCountNum = Label(root, text='Цифр:')
labCountNum.grid(column=5, row=1)
entCountNum = Entry(root,  width=10, bd=4, font='f 8')
entCountNum.grid(column=6, row=1)
butRenameDate = Button(root, text='Дата создания', font='font 8', height=1, width=16)
butRenameDate.bind('<Button-1>', rename_date)
butRenameDate.grid(column=0, row=2)
butSaveName = Button(root, text='Сохранить имена', height=1, width=16)
butSaveName.bind('<Button-1>', save_names)
butSaveName.grid(column=0, row=3)
root.mainloop()

