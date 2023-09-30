from tkinter import *

main_color = "#FFFFFF"
button_color = "#FFFFFF"
button_fg="#0F2C59"
operators_color ="#FFFFFF"
operators_fg ="#E55604"
clear_color ="#FFFFFF"
Text_color ="#0F2C59"

button_font = ("Sans serif",20)
given_font = ("Sans serif",24)
ans_font = ("Sans serif",40,"bold")

root =Tk()

calculation=""
given_exp = ""


root.geometry("400x550")
root.resizable(0,0)

buttons = {
    7: (1, 1), 8: (1, 2), 9: (1, 3),
	4: (2, 1), 5: (2, 2), 6: (2, 3),
	1: (3, 1), 2: (3, 2), 3: (3, 3),
	0: (4, 1), '.': (4, 2)
}
operators_list={
	"%":(0,3),"/":(0,4),"*":(1,4),"-":(2,4),"+":(3,4)
}



frame1 = Frame(root , bg=main_color)
frame1.pack(side=TOP, fill="x")

frame2=Frame(root)
frame2.pack(expand=True, fill="both")


calculation_label = Label(frame1, text=calculation, anchor=E, bg=main_color,
							fg=Text_color, padx=24, font=given_font)
calculation_label.pack(expand=True, fill='both')

given_label = Label(frame1, text=given_exp, anchor=E, bg=main_color,
						fg=Text_color, padx=24, font=ans_font)
given_label.pack(expand=True, fill='both')




def create_button():
	for digit, coordinates in buttons.items():
		button = Button(frame2, text=str(digit),bg=button_color,fg=button_fg,font=button_font,borderwidth=0,command= lambda x=digit: digits(x))
		button.grid(row=coordinates[0], column=coordinates[1], sticky=NSEW)
	
def create_operators():
	for symbol, coordinates in operators_list.items():
		operator = Button(frame2, text=symbol,fg=operators_fg,bg=operators_color,font=button_font,borderwidth=0,command= lambda x=symbol: operators(x))
		operator.grid(row=coordinates[0], column=coordinates[1], sticky=NSEW)



def equal_button():
	equal_button = Button(frame2, text="=",fg=operators_fg,bg=operators_color,font=button_font,borderwidth=0,command= lambda : evaluate())
	equal_button.grid(row=4, column=3,columnspan=2, sticky=NSEW)


def clear_button():
	clear_button = Button(frame2, text="AC",fg=operators_fg,bg=button_color,font=button_font,borderwidth=0,command=clear)
	clear_button.grid(row=0, column=1,columnspan=2, sticky=NSEW)


def all_buttons():
	create_button()
	create_operators()
	equal_button()
	clear_button()


def evaluate():
	global calculation
	global given_exp
	global evaluated
	calculation +=given_exp
	calculation_label.config(text=calculation)
	try:
		given_exp =str(eval(str(calculation)))
		calculation=""
	except Exception as e:
		given_exp ="Error"
	finally:
		given_label.config(text=given_exp)
	evaluated = 1


def digits(x):
	global given_exp
	given_exp += str(x)
	given_label.config(text=given_exp)

def operators(x):
	global given_exp
	given_exp += str(x)
	given_label.config(text=given_exp)


def clear():
	global given_exp
	global calculation
	given_exp=""
	calculation=""
	calculation_label.config(text="")
	given_label.config(text="")


frame2.rowconfigure(0, weight=1)
for x in range(1, 5):
	frame2.rowconfigure(x, weight=1)
	frame2.columnconfigure(x, weight=1)



all_buttons()



root.mainloop()
