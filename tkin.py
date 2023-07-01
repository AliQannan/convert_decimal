###    IMPORT LIBRYS
import tkinter as tk
import customtkinter as cs



### System settings
cs.set_appearance_mode("System")
cs.set_default_color_theme("blue")
### Function for convert decimal to hexa decimal
def decimal_to_hexadecimal():
    def convert(num):
        hexa_map={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
        if num < 10 :
            return str(num)
        else:
            return hexa_map[num]
    dec=int(decimal.get())

    hexa_num=""
    while dec >0:
        mode=dec%16
        hexa_num=hexa_num+convert(mode)
        dec=dec//16
    last.configure(text="hexadecimal :  "+hexa_num[::-1])
#### function for convert binary to decimal
def binary_to_decmial():
    binary1=binary.get()
    power=len(binary1)-1
    decimal_num=0
    for digit in binary1:
        decimal_num=decimal_num+int(digit)*(2**power)
        power=power-1
    finishlable.configure(text="decimal_num :  "+str(decimal_num))


###WINDOW FOR PROGRAMM
window=tk.Tk()
window.geometry("720x400")

window.title("for object")
### small window for input binary number
lable1=cs.CTkLabel(window,text="insert your binary number")
lable1.pack(padx=10,pady=5)
text_var=tk.StringVar()
binary=cs.CTkEntry(window,width=400,height=32,textvariable=text_var)
binary.pack(padx=10,pady=10)


btn1=cs.CTkButton(window,text="Convert To Decimal",command=binary_to_decmial)
btn1.pack(padx=10,pady=10)


finishlable=cs.CTkLabel(window,text="")
finishlable.pack(padx=10,pady=10)


#### input for decimal number to convert to hexa number
lable2=cs.CTkLabel(window,text="insert your decimal number")
lable2.pack(padx=10,pady=10)
var2=tk.StringVar()
decimal=cs.CTkEntry(window,width=400,height=32,textvariable=var2)
decimal.pack(padx=10,pady=10)
btn2=cs.CTkButton(window,text="Convert To HexaD",command=decimal_to_hexadecimal)
btn2.pack(padx=10,pady=10)
last=cs.CTkLabel(window,text="")

last.pack(padx=10,pady=10)


## Run App
window.mainloop()
