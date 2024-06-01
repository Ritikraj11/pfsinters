from tkinter import *
from tkinter import ttk
import requests



def city_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=48faa58fb102c009daefa87c695e18c1").json()
    weather_climate1.config(text=data['weather'][0]['main'])
    weather_description1.config(text=data['weather'][0]['description'])
    temp1.config(text=str(int(data['main']['temp']-273.15)))
    pressure1.config(text=data['main']['pressure'])
    
    









Font= ('Time New Roman', 35, "bold")
win= Tk()
win.title("Weather Forecasting")
win.geometry("500x500")

win.config(bg= "light blue")

name_label = Label(win, text="GECM Weather App", font= Font,  bg= "light blue")
name_label.place(x=25, y=40, height=50, width=450)

creator_label= Label(win,text="This is a mini Project by Ritik ", font="Arial", bg="light blue")
creator_label.pack(pady=5)
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

city_name=StringVar()
box_label=ttk.Combobox(win, text="GECM Weather App",values=list_name, font= ("calibre", 15, "bold"),textvariable=city_name)
box_label.place(x=35, y=120, height=40, width=400)

weather_climate= Label(win, text="Weather climate ", font= ("calibre", 18,),  bg= "light blue")
weather_climate.place(x=25, y=260, height=50, width=200)

weather_climate1= Label(win, text=" ", font= ("calibre", 18,))
weather_climate1.place(x=250, y=260, height=50, width=240)


weather_description= Label(win, text="Weather Description ", font= ("calibre", 18,),  bg= "light blue")
weather_description.place(x=25, y=320, height=50, width=240)

weather_description1= Label(win, text=" ", font= ("calibre", 18,))
weather_description1.place(x=250, y=320, height=50, width=240)

temp= Label(win, text="Temperature ", font= ("calibre", 18,),  bg= "light blue")
temp.place(x=25, y=380, height=50, width=165)

temp1= Label(win, text=" ", font= ("calibre", 18,))
temp1.place(x=250, y=380, height=50, width=240)

pressure = Label(win, text="pressure ", font= ("calibre", 18,),  bg= "light blue")
pressure.place(x=25, y=440, height=50, width=130)

pressure1 = Label(win, text=" ", font= ("calibre", 18,))
pressure1.place(x=250, y=440, height=50, width=240)

done_button=Button(win, text="Done", font= ("calibre", 15, "bold"),command=city_get )
done_button.place(y=190, x=200, height=40, width=100)
 

win.mainloop()