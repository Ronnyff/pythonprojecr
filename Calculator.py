from tkinter import*

app = Tk()
app.geometry('660x1350')
app.title('calculator by Rawnak')
app.config(bg='light blue')
lab_title = Label(app,text='Welcome to Rawnak\'s calculator',font = ('Days',10),fg='red',bg ='light blue')
lab_title.place(x='100',y='135')
#function
def click(event):

    text = event.widget.cget('text')
    if text == '=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                value = 'Error'

        scvalue.set(value)
        
    elif text == 'C':
        scvalue.set('')
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()
    
#enter
scvalue = StringVar()
scvalue.set('')
screen = Entry(app,text=scvalue,font=('Lucida',15,'bold'))
screen.place(x='40',y='200')

#button 1
button_1 = Button(text='1',font=('mystyle',20))
button_1.pack(side='left',padx=58,pady=180)
button_1.place(x='80',y='665')
button_1.bind('<Button-1>',click)
#button 2
button_2 = Button(text='2',font=('mystyle',20))
button_2.pack(side='left',padx=18,pady=180)
button_2.place(x='250',y='665')
button_2.bind('<Button-1>',click)
#button 3
button_3 = Button(text='3',font=('mystyle',20))
button_3.pack(side='left',padx=18,pady=180)
button_3.place(x='400',y='665')
button_3.bind('<Button-1>',click)
#button 4
button_4 = Button(text='4',font=('mystyle',20))
button_4.pack(side='left',padx=18,pady=180)
button_4.place(x='80',y='865')
button_4.bind('<Button-1>',click)
#button 5
button_5 = Button(text='5',font=('mystyle',20))
button_5.pack(side='left',padx=18,pady=180)
button_5.place(x='250',y='865')
button_5.bind('<Button-1>',click)
#button 6
button_6 = Button(text='6',font=('mystyle',20))
button_6.pack(side='left',padx=18,pady=180)
button_6.place(x='400',y='865')
button_6.bind('<Button-1>',click)
#button 7
button_7 = Button(text='7',font=('mystyle',20))
button_7.pack(side='left',padx=58,pady=180)
button_7.place(x='80',y='1065')
button_7.bind('<Button-1>',click)
#button 8
button_8 = Button(text='8',font=('mystyle',20))
button_8.pack(side='left',padx=18,pady=180)
button_8.place(x='250',y='1065')
button_8.bind('<Button-1>',click)
#button 9
button_9 = Button(text='9',font=('mystyle',20))
button_9.pack(side='left',padx=18,pady=180)
button_9.place(x='400',y='1065')
button_9.bind('<Button-1>',click)
#button 0
button_0 = Button(text='0',font=('mystyle',20))
button_0.pack(side='left',padx=18,pady=180)
button_0.place(x='250',y='1265')
button_0.bind('<Button-1>',click)
#button c
button_C = Button(text='C',font=('mystyle',20))
button_C.pack(side='left',padx=58,pady=180)
button_C.place(x='80',y='1265')
button_C.bind('<Button-1>',click)
#button =
button_e = Button(text='=',font=('mystyle',20))
button_e.pack(side='left',padx=18,pady=180)
button_e.place(x='400',y='1265')
button_e.bind('<Button-1>',click)
#button +
button_add = Button(text='+',font=('mystyle',20))
button_add.pack(side='left',padx=18,pady=180)
button_add.place(x='550',y='665')
button_add.bind('<Button-1>',click)
#button -
button_sub = Button(text='-',font=('mystyle',20))
button_sub.pack(side='left',padx=980,pady=580)
button_sub.place(x='550',y='865')
button_sub.bind('<Button-1>',click)
#button x
button_mul = Button(text='*',font=('mystyle',20))
button_mul.pack(side='left',padx=18,pady=180)
button_mul.place(x='550',y='1065')
button_mul.bind('<Button-1>',click)
#button /
button_d = Button(text='/',font=('mystyle',20))
button_d.pack(side='left',padx=18,pady=180)
button_d.place(x='550',y='1265')
button_d.bind('<Button-1>',click)

app.mainloop()
