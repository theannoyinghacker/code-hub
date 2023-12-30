import tkinter
from tkintermapview import TkinterMapView
import phonenumbers
root=tkinter.Tk()
root.title("Drone map")

root.geometry("800x800")
root.resizable(False,False)

label_num=tkinter.Entry(root)
label_num.place(x=200,y=600)
new_label=tkinter.Label(root)
new_label.place(x=200,y=625)
new_label1=tkinter.Label(root)
new_label1.place(x=200,y=645)

def get_num()
    number=int(label_num.get())
    key=''

    from phonenumbers import geocoder
    x=phonenumbers.parse(number, "CH")
    print(geocoder.description_for_number(number,"en")


    from opencage.geocoder import OpenCageGeocode
    geocoder=OpenCageGeocode(key)
    query=str(yourLocation) 
    results=geocoder.geocode(query)
    lat=results[0]['geometry']['lat']
    lng=results[0]['geometry']['lng']
    print(lat,lng)
    label = " "
    global label
    label += lat
    lab=eval(label)
    new_label.config(text=lab)
    reg = " "
    global reg
    reg += lng
    lag=eval(reg)
    new_label1.config(text=lab)
    
button_ph=tkinter.Button(root,command=get_num)
button_ph.place(x=200,y=665)
gmap_widget = TkinterMapView(root,width=600,height=800)
gmap_widget.pack()

gmap_widget.set_title_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}-&y={y-&z={z}-&s=Ga",max_zoom=22)
mrkr=gmap_widget.set_address("Motor Plaza 695017 Sreekariyam",marker=True)
mrkr.set_text("default location")

text=tkinter.Label(root,text="enter location:")
text.place(x=100,y=600)

f=tkinter.Entry(root)
f.place(x=100,y=620)

text1=tkinter.Label(root,text="enter latitude:")
text1.place(x=300,y=600)
la=tkinter.Entry(root)
la.place(x=300,y=620)
text2=tkinter.Label(root,text="enter longntude:")
text2.place(x=300,y=635)
lo=tkinter.Entry(root)
lo.place(x=300,y=655)
def move_UP():
    latitude=la.get()
    longnitude=lo.get()
    gmap_widget.set_position(latitude,longnitude,marker=True)
    print("longnitude pressed")
def position():
    latitude = f.get()
    gmap_widget.set_address(latitude, marker=False)

location_navigx=tkinter.Button(root,text="locate",command=position)
location_navigx.place(x=100,y=642)

location_navigx2=tkinter.Button(root,text="confirm",command=move_UP)
location_navigx2.place(x=300,y=682)

def color_black():
    root['background'] = 'black'
def color_white():
    root['background'] = 'white'


x=tkinter.Button(root,text="black", command=color_black)
x.place(x=430,y=600)
y=tkinter.Button(root,text="white", command=color_white)
y.place(x=430,y=636)
root.mainloop()

