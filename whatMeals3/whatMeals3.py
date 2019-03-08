import tkinter
from music import *
'''
if __name__ == '__main__':
    root = tkinter.Tk()
    x = 1
    mm = music()
    
    b = tkinter.Button(root,text = "music",command = mm.play).pack()
    root.mainloop()
'''
from tkinter import *           # 导入 Tkinter 库
from tkinter import ttk
import time
def command_history(root,pp):
    #添加搜索项
    year_label = Label(root,text = "year")
    year_label.place(x = 20,y = 100)
    year_entry = Entry(root,bd = 2,width = 4,text = "2019")
    year_entry.place(x = 55,y = 100)
    month_label = Label(root,text = "month")
    month_label.place(x = 105,y = 100)
    month_entry = Entry(root,bd = 2,width = 4,text = "3")
    month_entry.place(x = 155,y = 100)
    day_label = Label(root,text = "day")
    day_label.place(x = 210,y = 100)
    day_entry = Entry(root,bd = 2,width = 4,text = "8")
    day_entry.place(x = 240,y = 100)
    #添加搜索按钮
    search_button = Button(root,height = 20,width = 20,image = pp,command = lambda:command_search_button(year_entry.get(),month_entry.get(),day_entry.get()))
    search_button.place(x = 300,y= 95)
    return
def command_game():
    return
def command_help():
    help_tk = Tk()
    help_tk.title("help message!")
    help_tk.iconbitmap(r'graph\little.ico')
    help_tk["height"] = 30
    help_tk["width"] = 50
    help_tk.geometry("500x200+250+150")
    help_message = ""
    help_message = help_message + "The music button in the side_frame:\n\tuse it to open BGM, or you can use it to change to another music\n"
    help_message = help_message + "The control menu in the menubar:\n\tuse it to close the music\n"
    help_message = help_message + "The option menu in the menubar:\n\t\"history\" can help you know the history meals of you\n"
    help_message = help_message + "\t\"game\" is a small game, and it can help you choose you next meal\n"
    help_message = help_message + "\t\"help\" shows this window\n"
    help_message = help_message + "The exit command equals to the quit this window\n"
    label = Label(help_tk,text = help_message,justify = "left")
    label.place(x = 0,y = 0)
    help_tk.mainloop()
    help_tk.quit()
    return
def command_run(meal_text,place_text):
    meal_text.delete("0.0",END)
    place_text.delete("0.0",END)
    #接下来是要选取哪一顿饭
    IO_breakfast = open("1早饭.txt","r")
    IO_lunch = open("2午饭.txt","r")
    IO_dinner= open("3晚饭.txt","r")
    IO_night = open("4夜宵.txt","r")
    list_breakfast = IO_breakfast.readlines()
    list_lunch = IO_lunch.readlines()
    list_dinner = IO_dinner.readlines()
    list_night = IO_night.readlines()
    print("\n\n\nSir,do you want to know which meal of today?")
    key_word = input("1 releates to breakfast\n2 releates to lunch\n3 releates to dinner\n4 releates to night\nand that 0 means all of them:\n")
    key_word = int(key_word)
    import Meal
    if key_word == 1:
        name_place = Meal.Find(list_breakfast)
    if key_word == 2:
        name_place = Meal.Find(list_lunch)
    if key_word == 3:
        name_place = Meal.Find(list_dinner)
    if key_word == 4:
        name_place = Meal.Find(list_night)
    IO_breakfast.close()
    IO_lunch.close()
    IO_dinner.close()
    IO_night.close()
    #IO操作结束了，接下来就要更改GUI界面上的值了
    meal_text.insert(INSERT,name_place[0])
    place_text.insert(INSERT,name_place[1])
    return
def command_search_button(year,month,day):
    path = "data/history/%s-%s-%s.txt"%(year,month,day)
    try:
        file = open(path,"r")
    except IOError:
        win = Tk()
        win.geometry("500x10")
        win.title("none message!")
        win.iconbitmap(r"graph\warning.ico")
        win.mainloop()
        win.quit()
        return
    lis_string = file.readlines()
    win = Tk()
    win.title(path)
    win.iconbitmap(r'graph\little.ico')
    win.geometry("500x300")
    string = ""
    for i in lis_string:
        string = string + i
    message = Label(win,text = string,justify = "left",width = 400)
    message.place(x = 0,y = 0)
    message.pack()
    win.mainloop()
    win.quit()
def button1_clicked(event):
    print(event.x,event.y)

if __name__ == "__main__":
    #首先初始化一个关于音乐的Object
    mm = music()
    #首先是对于主界面的设置
    root = Tk()
    root.bind('<Button-1>',button1_clicked)
    root.title("Meals")
    root.iconbitmap(r'graph\little.ico')
    root["height"] = 300
    root["width"] = 500
    root.geometry("500x300+0+0")
    
    #对于菜单栏的设置
    menubar = Menu()
    menu_option = Menu()
    pp = PhotoImage(file = 'graph/search.gif')
    menu_option.add_command(label = "history",command = lambda:command_history(root,pp))
    menu_option.add_command(label = "game",command = command_game)
    menu_option.add_command(label = "help",command = command_help)
    menubar.add_cascade(label = "options",menu=menu_option)
    menu_control = Menu()
    menu_control.add_command(label = "close music",command = mm.close)
    menubar.add_cascade(label = "control",menu = menu_control)
    menubar.add_command(label = "exit",command = root.quit)
    root.config(menu=menubar)
    
    #创建一个侧栏side_frame,放置时间，日期，地点，背景音乐控制
    side_frame = ttk.LabelFrame(root,height = 300,width = 150).place(x = 350,y = 0)
    #现在要添加music按钮
    button = tkinter.Button(side_frame,text = "music",command = mm.play,activebackground = "yellow",
                            activeforeground = "gray",bd = 4,
                            bg = "green",relief = RIDGE)
    button.place(x = 400,y = 225)
    #现在是side_frame里面的一些label
    str_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    ttk.Label(side_frame,text = 'Date:\n%s'%str_date).place(x = 375,y = 0+20)
    time_label=ttk.Label(text=time.strftime('Time:  \n%H:%M:%S',time.localtime(time.time())))
    time_label.place(x = 375,y = 75)
    def trickit():
        currentTime=time.strftime('Time:\n%H:%M:%S',time.localtime(time.time()))
        time_label.config(text=currentTime)
        root.update()
        time_label.after(1000, trickit)
    time_label.after(1000, trickit)
    ttk.Label(side_frame,text = 'Place:\n哈尔滨工业大学\nA09公寓').place(x = 375,y = 150 - 20)
    
    #现在是底部边栏的设计
    #关于meal的设计
    meal_label = Label(root,text = "Meal")
    meal_label.place(x = 20,y = 200)
    meal_text = Text(root,bd = 5,height = 1,width = 20)
    meal_text.place(x = 60,y = 200)
    #关于place的设计
    place_label = Label(root,text = "Place")
    place_label.place(x = 20,y = 240)
    place_text = Text(root,bd = 5,height = 1,width = 20)
    place_text.place(x = 60,y = 240)
    #关于运行按钮的设定
    run_button = Button(root,text = "Run",command=lambda:command_run(meal_text,place_text),activebackground = "yellow",
                            activeforeground = "gray",bd = 5,
                            bg = "gold",relief = GROOVE)
    run_button.place(x = 250,y = 220)
    
    root.mainloop()