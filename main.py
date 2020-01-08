#실행전 pip3 install pillow 를 설치해주세요

from tkinter import *
from PIL import ImageTk, Image
from PIL import Image
import os

 
class App:
   def __init__(self,r):
      frame=Frame(r)
      frame.pack()
      frame.config(bg="#ffedb5")

      image = Image.open("logo2.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=0, column=0, rowspan = 10, columnspan=10)
      label.config(bg="#ffedb5")
      
      self.kimchi=IntVar()
      button1=Checkbutton(frame,text='kimchi', variable=self.kimchi, width=10, height=5, command=self.convert)
      button1.grid(row=20, column=0)
      button1.config(bg="#ffedb5")
      image = Image.open("kimchi.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=19, column =0)
      label.config(bg="#ffedb5")
      
 
      self.ham=IntVar()
      button2=Checkbutton(frame,text='ham', variable=self.ham,  width=10, height=5,command = self.convert)
      button2.grid(row=20, column=1)
      button2.config(bg="#ffedb5")
      image = Image.open("ham.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=19, column =1)
      label.config(bg="#ffedb5")
      
 
      self.leek=IntVar()
      button3=Checkbutton(frame,text='leek', variable=self.leek, width=10, height=5,command = self.convert)
      button3.grid(row=20, column=2)
      button3.config(bg="#ffedb5")
      image = Image.open("leek.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=19, column =2)
      label.config(bg="#ffedb5")

      self.egg=IntVar()
      button4=Checkbutton(frame,text='egg', variable=self.egg,width=10, height=5, command = self.convert)
      button4.grid(row=20, column=3)
      button4.config(bg="#ffedb5")
      image = Image.open("egg.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=19, column =3)
      label.config(bg="#ffedb5")


      self.cheese=IntVar()
      button5=Checkbutton(frame,text='cheese', variable=self.cheese, width=10, height=5,command = self.convert)
      button5.grid(row=20, column=4)
      button5.config(bg="#ffedb5")
      image = Image.open("cheese.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=19, column =4)
      label.config(bg="#ffedb5")


      self.carrot=IntVar()
      button6=Checkbutton(frame,text='carrot', variable=self.carrot, width=10, height=5,command = self.convert)
      button6.grid(row=20, column=5)
      button6.config(bg="#ffedb5")
      image = Image.open("carrot.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=19, column =5)
      label.config(bg="#ffedb5")


      self.tuna=IntVar()
      button7=Checkbutton(frame,text='tuna', variable=self.tuna,width=10, height=5, command = self.convert)
      button7.grid(row=22, column=0)
      button7.config(bg="#ffedb5")
      image = Image.open("tuna.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=21, column =0)
      label.config(bg="#ffedb5")


      self.tofu=IntVar()
      button8=Checkbutton(frame,text='tofu', variable=self.tofu,width=10, height=5, command = self.convert)
      button8.grid(row=22, column=1)
      button8.config(bg="#ffedb5")
      image = Image.open("tofu.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=21, column =1)
      label.config(bg="#ffedb5")


      self.onion=IntVar()
      button9=Checkbutton(frame,text='onion', variable=self.onion,width=10, height=5, command = self.convert)
      button9.grid(row=22, column=2)
      button9.config(bg="#ffedb5")
      image = Image.open("onion.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=21, column =2)
      label.config(bg="#ffedb5")


      self.potato=IntVar()
      button10=Checkbutton(frame,text='potato', variable=self.potato, width=10, height=5,command = self.convert)
      button10.grid(row=22, column=3)
      button10.config(bg="#ffedb5")
      image = Image.open("potato.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=21, column =3)
      label.config(bg="#ffedb5")


      self.cabbage=IntVar()
      button11=Checkbutton(frame,text='cabbage', variable=self.cabbage, width=10, height=5,command = self.convert)
      button11.grid(row=22, column=4)
      button11.config(bg="#ffedb5")
      image = Image.open("cabbage.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=21, column =4)
      label.config(bg="#ffedb5")

      self.mayo=IntVar()
      button11=Checkbutton(frame,text='mayo', variable=self.mayo, width=10, height=5,command = self.convert)
      button11.grid(row=22, column=5)
      button11.config(bg="#ffedb5")
      image = Image.open("mayo.png")
      photo = ImageTk.PhotoImage(image)
      label = Label(frame,image=photo)
      label.image = photo
      label.grid(row=21, column =5)
      label.config(bg="#ffedb5")
      
 
      startbutton = Button(r, text = "START", command  = self.decision,
                           width=15, height=2, highlightbackground='#ea9154' ,activeforeground='blue')
      startbutton.pack(pady=10)


 
   def convert(self):
       ss=[]
       if (self.kimchi.get() == 1):
            ss.append('kimchi')
       if (self.ham.get() == 1):
            ss.append('ham')
       if (self.leek.get() == 1):
            ss.append('leek')
       if (self.egg.get() == 1):
            ss.append('egg')
       if (self.cheese.get() == 1):
            ss.append('cheese')
       if (self.carrot.get() == 1):
            ss.append('carrot')
       if (self.tuna.get() == 1):
            ss.append('tuna')
       if (self.tofu.get() == 1):
            ss.append('tofu') 
       if (self.onion.get() == 1):
            ss.append('onion')
       if (self.cabbage.get() == 1):
            ss.append('cabbage')
       if (self.potato.get() == 1):
            ss.append('potato')
       if (self.mayo.get() == 1):
            ss.append('mayo')
       return ss
 
 
   def decision(self):
       kimchiBokkembop = ['kimchi','ham','leek', 'egg', 'cheese']
       cheeseEggmari = ['egg', 'leek', 'carrot', 'cheese']
       kimchiStew = ['kimch', 'tuna', 'tofu', 'onion', 'leek']
       soybeanpasteStew = ['tofu', 'potato', 'onion', 'leek']
       chickenBokkeumtang = ['potato', 'onion', 'leek', 'carrot', 'cabbage']
       tteokbokki = ['onion', 'egg', 'leek', 'cabbage', 'cheese']
       toast = ['cheese', 'egg', 'cabbage', 'ham', 'onion']
       budaeJjigae = ['ham', 'kimch', 'tofu', 'onion', 'leek', 'cabbage']
       tunamayorice = ['egg', 'tuna', 'onion']
       softtofuStew = ['tofu', 'onion', 'leek', 'egg', 'kimchi']
       
       total_list = [kimchiBokkembop, cheeseEggmari, kimchiStew, soybeanpasteStew, chickenBokkeumtang,
                     tteokbokki, toast, budaeJjigae, tunamayorice, softtofuStew]
       
       selected_list=[]
       newlist = self.convert()
       
       for k in range(10):
           count=0
           for i in total_list[k]:
               for j in newlist:
                   if(i==j):
                       count=count+1
           if(count>=2):
               selected_list.append(total_list[k])
       
 
       if ['kimchi','ham','leek', 'egg', 'cheese'] in selected_list:
          c = Button(text ='김치볶음밥', command = self.kimchirice_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['egg', 'leek', 'carrot', 'cheese'] in selected_list:
          c = Button(text ='치즈계란말이', command = self.eggmari_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['kimch', 'tuna', 'tofu', 'onion', 'leek'] in selected_list:
          c = Button(text ='김치찌개', command = self.kimchisoup_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['tofu', 'potato', 'onion', 'leek'] in selected_list:
          c = Button(text ='된장찌개', command = self.soysoup_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['potato', 'onion', 'leek', 'carrot', 'cabbage'] in selected_list:
          c = Button(text ='닭볶음탕', command = self.chickensoup_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['onion', 'egg', 'leek', 'cabbage', 'cheese'] in selected_list:
          c = Button(text ='떡볶이', command = self.tteok_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['cheese', 'egg', 'cabbage', 'ham', 'onion'] in selected_list:
          c = Button(text ='토스트', command = self.toast_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['ham', 'kimch', 'tofu', 'onion', 'leek', 'cabbage'] in selected_list:
          c = Button(text ='부대찌개', command = self.budae_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['egg', 'tuna', 'onion'] in selected_list:
          c = Button(text ='참치마요덮밥', command = self.tunarice_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)
       if ['tofu', 'onion', 'leek', 'egg', 'kimchi'] in selected_list:
          c = Button(text ='순두부찌개', command = self.softtofu_R, width=8, height=4, highlightbackground='#6E7C3A')
          c.pack(side=LEFT, padx=12)

       if selected_list == []:
          self.no_recipe()
         
          
   def no_recipe(self):
       win = Toplevel()
       win.wm_title("no_recipe")
       win.config(bg="#ffedb5")

       b = Label(win, text="Sorry! There's no recipe.", font=('Times', 30))
       b.config(bg="#ffedb5")
       b.pack(padx= 100, pady=70)

       a = Button(win, text="Close",width=10, height=2,command=win.destroy)
       a.pack(pady=10)
       
  
 
   def kimchirice_R(self):
       win = Toplevel()
       win.wm_title("김치볶음밥 레시피")
       win.configure(bg='#ffedb5')
       
       image = Image.open("kimchiBokkembop.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()


   def eggmari_R(self):
       win = Toplevel()
       win.wm_title("계란말이 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("cheeseEggmari.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()

   def kimchisoup_R(self):
       win = Toplevel()
       win.wm_title("김치찌개 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("kimchiStew.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()

   def soysoup_R(self):
       win = Toplevel()
       win.wm_title("된장찌개 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("soybeanpasteStew.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()
 
   def chickensoup_R(self):
       win = Toplevel()
       win.wm_title("닭볶음탕 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("chickenBokkeumtang.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()

   def tteok_R(self):
       win = Toplevel()
       win.wm_title("떡볶이 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("tteokbokki.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()

   def toast_R(self):
       win = Toplevel()
       win.wm_title("토스트 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("toast.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE",width=20, height=4, highlightbackground='#ea9154', command=win.destroy)
       b.pack()
       
       win.mainloop() 

   def budae_R(self):
       win = Toplevel()
       win.wm_title("부대찌개 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("budaeJjigae.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()

   def tunarice_R(self):
       win = Toplevel()
       win.wm_title("참치마요 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("tunamayorice.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop()

   def softtofu_R(self):
       win = Toplevel()
       win.wm_title("순두부찌개 레시피")
       win.configure(bg='#ffedb5')

       image = Image.open("softtofuStew.JPG")
       photo = ImageTk.PhotoImage(image)

       label = Label(win,image=photo)
       label.image = photo
       label.pack()
       
       b = Button(win, text="CLOSE", width=20, height=4, highlightbackground='#ea9154',command=win.destroy)
       b.pack()
       
       win.mainloop() 



                  
root=Tk()
root.wm_title('냉장고를 부탁해')
root.geometry("1020x800")
root.config(bg="#ffedb5")

 
 
app=App(root)      
root.mainloop()
