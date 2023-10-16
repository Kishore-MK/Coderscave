import tkinter
from tkinter import *
import random
import time

root=Tk()
root.title("Password generator")
root.geometry("1200x450")
color=("#D9EDF8")
second_color=("#ffffff")
text_color=("#000000")
button_color=("#FFD6A5")
root.configure(bg=color)
root.resizable(0,0)
default_font=("serif,sans",20)

list=""
given_char=[]
font_style=("bold serif,sans bold",30)
stop=False
start_time = 0

sentences=["Please take your dog, Cali, out for a walk – he really needs some exercise!",
"What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.",
"Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.",
"Do you know why all those chemicals are so hazardous to the environment?",
"You never did tell me how many copper pennies where in that jar; how come?",
"Max Joykner sneakily drove his car around every corner looking for his dog.",
"The two boys collected twigs outside, for over an hour, in the freezing cold!",
"When do you think they will get back from their adventure in Cairo, Egypt?",
"Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.",
"We climbed to the top of the mountain in just under two hours; isn’t that great?",
"Hector quizzed Mr. Vexife for two hours, but he was unable to get any information.",
"I have three things to do today: wash my car, call my mother, and feed my dog.",
"Xavier Puvre counted eighty large boxes and sixteen small boxes stacked outside.",
"The Reckson family decided to go to an amusement park on Wednesday.",
"That herd of bison seems to be moving quickly; does that seem normal to you?",
"All the grandfather clocks in that store were set at exactly 3 o’clock.",
"There are so many places to go in Europe for a vacation--Paris, Rome, Prague, etc.",
"Those diamonds and rubies will make a beautiful piece of jewelry.",
"The steamboats seemed to float down the Mississippi River at a snail’s pace.",
"In order to keep up at that pace, Zack Squeve would have to work all night."]

def paste(event):
    return "break"

def start():
  global list,end,start_time
  end = False
  list=random.choice(sentences)
  printable_text = '\n'.join([list[i:i+90] for i in range(0, len(list),90)])
  show_text.config(text=printable_text)
  input.focus()
  input.config(width=84)
  input.delete(0,END)
  result.config(text="")
  starting.config(state=DISABLED)
  stoping.config(state=NORMAL)
  start_time=time.time()

def speedcalculation():
    correctwords=0
    global end,start_time
    if not end:
      end= True
      given_char=input.get()
      length=min(len(list) , len(given_char))
      for i in range(length):
        if i >= len(list):
            break
        if list[i] == given_char[i]:
            correctwords += 1
      end_time=time.time()
      time_total=(end_time - start_time)
      accuracy=(correctwords/len(list))*100
      wpa=(len(given_char.split())/time_total)*60
      print(f"Time taken: {time_total:.2f} seconds")
      print(f"Accuracy: {accuracy:.2f}%")
      print(f"Words per minute :{wpa:.2f}")
      starting.config(state=NORMAL)
      stoping.config(state=DISABLED)
      result.config(text= f"Time : {time_total:.2f} seconds || Accuracy : {accuracy:.2f}% || WPA : {wpa:.2f}")


show_title=Label(root,text="TYPING SPEED TEST",font=(font_style),pady=50,bg=color,fg=second_color)
show_title.place(relx=0.5,rely=0.1,anchor="center")

starting=Button(root,text="Start",width=10,pady=2,command=start,font=("Arial",12),bg=button_color,borderwidth=0)
starting.place(relx=0.46,rely=0.2,anchor="w")
  

  
show_text=Label(root,text="",font=("Inconsolata, monospace",20),anchor="center",fg=text_color,bg=color)
show_text.place(relx=0.5,rely=0.35,anchor="center")

input = Entry(root, font=("Arial", 19))
input.place(relx=0.5,rely=0.52,anchor="center")
input.bind("<Tab>", lambda e: start())
input.bind("<Return>",lambda e:speedcalculation())
input.bind("<Control-v>",paste)
input.config(width=84)

stoping=Button(root,text="Stop",width=10,pady=2,font=("Arial",12),state=DISABLED,command=speedcalculation,bg=button_color,borderwidth=0)
stoping.place(relx=0.5,rely=0.65,anchor="center")
result = Label(root, text="", font=("Arial", 14),bg=color,fg=text_color)
result.place(relx=0.5,rely=0.80,anchor="center")


root.mainloop()