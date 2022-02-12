from tkinter import*
from tkinter import ttk
def data():
    window=Tk()
    window.geometry('500x540+300+100')
    window.title('your ticket')
    window.configure(bg='#ECE5B6')
    window.resizable(0,0)
    photo=PhotoImage(file= 't.png')
      
    lb=Label(window,image=photo,width=500)
    lb.grid(columnspan=5)


    lb1=Label(window,text='Passenger Name'
             ,font=('arial',10,'bold'),
             justify='right',pady=10,
             bg='#A0CFEC',width=20 )
    lb1.grid(row=1,column=0)
    v1=StringVar()
    en1=Entry(window,textvariable=v1,
         
             bg='#FFFFFF',width=40)
               
    en1.grid(row=1,column=2)


    lb2=Label(window,text='From'
             ,font=('arial',10,'bold'),
             justify='right',pady=10,
             bg='#A0CFEC',width=20 )
    lb2.grid(row=2,column=0)
    city= ['Cairo','Alexandria','Tanta','Benha','Matrouh','Zagazig','Qwesna','Damnhour','Luxor','Aswan','Sohag','Assuit','Beni souef','Ismailia','Kafr El-sheikh']
    v2=StringVar()
    en2=ttk.Combobox(window,width=37,textvariable=v2)
               
    en2.grid(row=2,column=2)

    en2.config(value = city)
               




    lb3=Label(window,text='To',pady=10,
              font=('arial',10,'bold'),
         
             bg='#A0CFEC',width=20 )
    lb3.grid(row=3,column=0)
    v3=StringVar()
    en3=ttk.Combobox(window,width=37,textvariable=v3)
               
    en3.grid(row=2,column=2)

    en3.config(value = city)
               
    en3.grid(row=3,column=2)





    lb4=Label(window,text='date of Travel',pady=10,
              font=('arial',10,'bold'),
         
             bg='#A0CFEC',width=20 )
    lb4.grid(row=4,column=0)
    v4=StringVar()
    en4=Entry(window,textvariable=v4,
         
             bg='#FFFFFF',width=40)
               
    en4.grid(row=4,column=2)


    lb5=Label(window,text='Type of goods',pady=10,
         font=('arial',10,'bold'),
             bg='#A0CFEC',width=20 )
    lb5.grid(row=5,column=0)
    
    en5=Entry(window,text='',
         
             width=40)
               
    en5.grid(row=5,column=2)


    lb6=Label(window,text='Class',pady=10,
         font=('arial',10,'bold'),
             bg='#A0CFEC',width=20 )
    lb6.grid(row=6,column=0)

    en6=Entry(window,text='',
         
             width=40)
               
    en6.grid(row=6,column=2)

    calsstype = ['VIP class','first class','bussiness class','Economy class','Second class','third class']
    en6=ttk.Combobox(window,width=37)
               
    en6.grid(row=6,column=2)

    en6.config(value = calsstype)
               



    lb7=Label(window,text='Chair.No',pady=10,
         font=('arial',10,'bold'),
             bg='#A0CFEC',width=20 )
    lb7.grid(row=7,column=0)
    v6=StringVar()
    en7=Spinbox(window,from_=1,to=100,textvariable=v6,width=40)
               
    en7.grid(row=7,column=2)

    
    lb8=Label(window,text='Passengers.No',pady=10,
         font=('arial',10,'bold'),
             bg='#A0CFEC',width=20 )
    lb8.grid(row=8,column=0)
    v5=StringVar()
    en8=Spinbox(window, from_=1, to=10,width=40,textvariable=v5)
    en8.grid(row=8,column=2)
    #--------------------------------------
    def tkt_maker():
        window.destroy()
        show=Tk()
        show.title('Ticket')
        show.configure(bg='#3b68a3')
        show.resizable(0,0)
        show.geometry('750x470+200+100')
        h_lbl=Label(show,bg='#3b68a3',text='Here is Your ticket !',fg='#dbd0c8',font=('times 25 bold'))
        h_lbl.place(x=230,y=20)
        big_lbl=Label(show,bg='#dadbd7',width=80,height=19,borderwidth=6, relief="solid")
        big_lbl.place(x=100,y=80)
        lgs=PhotoImage(file= 't.png')
        logo=Label(show,image=lgs,width=500,height=100)
        logo.image = lgs
        logo.place(x=130,y=90)
        id_tkt=Label(big_lbl,text='Ticket I D :',bg='#dadbd7',fg='#132757',font=('times 15 bold'))
        id_tkt.place(x=30,y=110)
        id2_tkt=Label(big_lbl,text="E5hd47d899/5/20",bg='#dadbd7',fg='#632c34',font=('times 15 bold'))
        id2_tkt.place(x=160,y=110)
        
        name_tkt=Label(big_lbl,text='Name :',bg='#dadbd7',fg='#132757',font=('times 15 bold'))
        name_tkt.place(x=30,y=135)
        name2_tkt=Label(big_lbl,text=v1.get(),bg='#dadbd7',fg='blue',font=('times 15 bold'))
        name2_tkt.place(x=110,y=135)
        
        from_tkt=Label(big_lbl,text='From :',bg='#dadbd7',fg='#132757',font=('times 15 bold'))
        from_tkt.place(x=30,y=160)
        from2_tkt=Label(big_lbl,text=v2.get(),bg='#dadbd7',fg='blue',font=('times 15 bold'))
        from2_tkt.place(x=110,y=160)
        
        to_tkt=Label(big_lbl,text='To :',bg='#dadbd7',fg='#132757',font=('times 15 bold'))
        to_tkt.place(x=320,y=160)
        to2_tkt=Label(big_lbl,text=v3.get(),bg='#dadbd7',fg='blue',font=('times 15 bold'))
        to2_tkt.place(x=380,y=160)
        
        dt_tkt=Label(big_lbl,text=v4.get(),bg='#dadbd7',fg='blue',font=('times 15 bold'))
        dt_tkt.place(x=350,y=245)

        
        
        pass_tkt=Label(big_lbl,text='passengers.no :',bg='#dadbd7',fg='#132757',font=('times 15 bold'))
        pass_tkt.place(x=30,y=185)
        pass2_tkt=Label(big_lbl,text=v5.get(),bg='#dadbd7',fg='blue',font=('times 15 bold'))
        pass2_tkt.place(x=180,y=185)
        
        chair_tkt=Label(big_lbl,text="chair.no :",bg='#dadbd7',fg='#132757',font=('times 15 bold'))
        chair_tkt.place(x=320,y=185)
        chair2_tkt=Label(big_lbl,text=v6.get(),bg='#dadbd7',fg='blue',font=('times 15 bold'))
        chair2_tkt.place(x=425,y=185)
        
        signature_tkt=Label(big_lbl,text="Siganture",bg='#dadbd7',fg='#1e4094',font=('times 15 bold'))
        signature_tkt.place(x=48,y=220)
        
        sign_tkt=Label(big_lbl,text="Transport Truck",bg='#dadbd7',fg='#965212',font=('Comic 12 bold italic'))
        sign_tkt.place(x=25,y=245)
        
        
        def other():
            show.destroy()
            data()
        
        def download():
            import pyautogui
            screenshot = pyautogui.screenshot()
            screenshot.save("your ticket {}.png")
            

        another = Button(show,command=other,text='<<=== Home',bg='#00af00',fg='#3d1614',activeforeground='blue',activebackground='gray',font=("times 15 bold"))
        another.place(x=100,y=390)
        download = Button(show,command=download,text='download',bg='#00af00',fg='#3d1614',activeforeground='blue',activebackground='gray',font=("times 15 bold"))
        download.place(x=570,y=390)
        

    #---------------------------------------------------------------
    find = Button(window,command=tkt_maker,text='Find a ticket',bg='#00af00',fg='navy',activeforeground='blue',activebackground='gray',font=("times 15 bold"))
    find.place(x=185,y=460)
    #-----------------------------------------------------------------
    window.mainloop()
data()



