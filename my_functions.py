import os
from pygame import mixer



song_num = 0
click = False
slider_val =0
slider_state =False

files = os.listdir(".")
lisT = []
song_duration = []

# Çalma yapılırken çalma biterse parça değiştir.

def listing(textbox):
    
    files = os.listdir(".")
    global song_duration
    i=0
    for file in files:
        if file.endswith(".mp3"):
            i=i+1
            lisT.append(file)
            textbox.insert("end",str(i)+ '- ' + file + '\n')
            sound = mixer.Sound(file)
            song_duration.append(round(sound.get_length()/60, 2))

    textbox.configure(state="disabled")        
  

def forward_button():

    global song_num, click
    if click == True and (len(lisT) - 1) == song_num:
        mixer.music.stop()
        song_num = 0
        mixer.music.load(lisT[song_num])
        mixer.music.play()
    elif click == True:
        mixer.music.stop()
        song_num = song_num + 1
        mixer.music.load(lisT[song_num])
        mixer.music.play()
        
def previous_button():
    global song_num, click

    if song_num != 0 and click == True:
        mixer.music.stop()
        song_num = song_num - 1
        mixer.music.load(lisT[song_num])
        mixer.music.play()

def play_button():
    global song_num, click, parca

    if not click:
        click = True 
        if mixer.music.get_pos() == -1:
            mixer.music.load(lisT[song_num])
            mixer.music.play()
        else:
            mixer.music.unpause()
    else:
        click = False
        mixer.music.pause()
        print(click)


def scan700(app):
    global song_num, click

    if mixer.music.get_busy() == 0 and click == 1:
        if (len(lisT) - 1) == song_num:
            song_num = 0
            mixer.music.load(lisT[song_num])
            mixer.music.play()
        else:
            song_num = song_num + 1
            mixer.music.load(lisT[song_num])
            mixer.music.play()

    app.after(700, scan700,app)

def scan1000(app,slider,label_1,label_2,label_3):
    global click, song_num,slider_state
    if click and not slider_state:
        
        #timeline slider
        slider.set(maP(mixer.music.get_pos()/1000,0,(song_duration[song_num]*60),0,100))
        label_1.configure(text=str(song_duration[song_num]).replace('.',':'))
        
        #current time
        pos_in_sec = mixer.music.get_pos() // 1000
        time_str = f"0:{pos_in_sec}" if pos_in_sec < 60 else f"{pos_in_sec // 60}:{pos_in_sec % 60}"
        label_2.configure(text=time_str)
    if slider_state ==True:
        slider_state =False
    
    label_3.configure(text=song_num+1)
    
    #every 1000 ms refresh the function
    app.after(1000, scan1000,app,slider,label_1,label_2,label_3)
    
    
def  maP(x,in_min,in_max,out_min,out_max) :
    return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
    
def volume_slider(value):
    
    mixer.music.set_volume(float(value))

        
def slider(value):
    pass
   
   
    
    
    
    
