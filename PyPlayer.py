
from pygame import mixer
import tkinter as tk
import customtkinter
import my_functions
import shutil
from tkinter import filedialog,messagebox
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")
mixer.init()

app = customtkinter.CTk()
app.geometry("500x300")
app.title("Py Player")


empty="--"

#add playlist function 
def select_file():
    files = filedialog.askopenfilename(initialdir ="", multiple=True,title = 'Dosya Seç',filetypes = (("Mp3 Files", "*.mp3"),))
    
   
    for path in files:
        try:
            shutil.copy(path,"C:/Users/Muhammed/.spyder-py3")
        except:
            messagebox.showerror('Copying Error', 'Error: Error Occured!')
    textbox.configure(state="normal")
    textbox.delete("0.0", "end")  # clear textbox for refresh
    my_functions.listing(textbox)



label_1 =customtkinter.CTkLabel(master=app,text=empty,width=10,height=25,corner_radius=8,font =("Arial Bold",15))
label_1.place(relx=0.74, rely=0.82,anchor=tk.CENTER)

#time slider
slider = customtkinter.CTkSlider(master=app, from_=0, to=100, command=my_functions.slider,progress_color='green')
slider.place(relx=0.5, rely=0.82, anchor=tk.CENTER)
slider.set(0,0)

label_2 =customtkinter.CTkLabel(master=app,text=empty,width=10,height=25,corner_radius=8,font =("Arial Bold",15))
label_2.place(relx=0.27, rely=0.82, anchor=tk.CENTER)

#Logo frame
frame = customtkinter.CTkFrame(master=app, width=120, height=257,fg_color='#191B26',border_color='#545458',border_width=0,corner_radius=0)
frame.place(relx=0, rely=0)

#Butoons background frame
frame2 = customtkinter.CTkFrame(master=app, width=500, height=46,fg_color='#191B26',border_color='#545458',border_width=0,corner_radius=0)
frame2.place(relx=0, rely=0.85)

#volume slider
slider2 = customtkinter.CTkSlider(master=app, from_=0, to=1, command=my_functions.volume_slider,height=100,orientation = "vertical")
slider2.place(relx=0.95, rely=0.5)

img = ImageTk.PhotoImage(Image.open("image18.png"))
imglabel =customtkinter.CTkLabel(app,image =img,text='')
imglabel.pack(padx=0, pady=0,side ="left",anchor ="n")

#textbox
textbox = customtkinter.CTkTextbox(master=app,border_width=0.6,border_color='black')
textbox.place(relx =0.265,rely=0.06,relwidth=0.67,relheight=0.73)

#current song number
label_3=customtkinter.CTkLabel(master=app,text='empty',width=10,height=25,corner_radius=8,font =("Arial Bold",20))
label_3.place(relx=0.97, rely=0.10, anchor=tk.CENTER)

#github label
label_4=customtkinter.CTkLabel(master=app,text='github/eyumurta',width=7,height=16,corner_radius=40,font =("Arial Bold",13),text_color="yellow",bg_color='#191B26')
label_4.place(relx=0.12, rely=0.30, anchor=tk.CENTER)

#Forward Button
Forward_Button = customtkinter.CTkButton(master =app,text="►‖",width=10,height=25,bg_color='#191B26',command =my_functions.forward_button,font=("Arial",13))
Forward_Button.place(relx=0.58,rely=0.93,anchor=tk.CENTER)

#Previous Button
Previous_Button = customtkinter.CTkButton(master =app,text="‖◄", width=10,height=25,bg_color='#191B26',command =my_functions.previous_button,font=("Arial",13))
Previous_Button.place(relx=0.42,rely=0.93,anchor=tk.CENTER)

#Play Button
Play_Button = customtkinter.CTkButton(master =app,text="Play", width=30,height=30,bg_color='#191B26',command =my_functions.play_button)
Play_Button.place(relx=0.5,rely=0.93,anchor="center")

add_files_button= customtkinter.CTkButton(master=app, text ='+',width=10,height=10,bg_color='white',command =select_file)
add_files_button.place(relx=0.90,rely=0.11,anchor=tk.CENTER)


my_functions.listing(textbox)
textbox.configure(state="disabled")
my_functions.scan700(app)
my_functions.scan1000(app,slider,label_1,label_2,label_3)
app.mainloop()

