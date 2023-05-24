

from tkinter import *
import requests
from tkinter import messagebox








url="https://api.openweathermap.org/data/2.5/weather?q={}&appid=7287fc84c0d69ea2c54ab2c4df210874"




def get_weather(city):
    result = requests.get(url.format(city)) #,api_key
    if result:
        json=result.json()
        city=json['name']
        country=json['sys']['country']
        temp_kelvin=json['main']['temp']
        temp_celsius=temp_kelvin-273
        weather=json['weather'][0]['main']
        final=(city,country,temp_celsius,weather) 
        return final
    else:
        return None



def search():
    city=city_name.get()  
    weather=get_weather(city)

    if weather:
        location_label['text'] = '{},{}'.format(weather[0],weather[1])
        temperature_lbl['text']='{:.2f}°C'.format(weather[2])
        weather_lbl['text']=weather[3]
    else:
        messagebox.showerror('error',"cannot find the city {} ".format(city))

app = Tk()
app.title("Weather App")
app.geometry('600x600')
app.config(padx=20,pady=20)
city_name = StringVar()
city_label = Entry(app,textvariable=city_name)
city_label.pack(pady=10)

search_btn = Button(app,text = "Search Weather",width=12,command=search)
search_btn.pack()
# search_btn.place(x=150,y=70)


location_label = Label(app,text='',font=('bold,20'))
location_label.pack()



temperature_lbl = Label(app,text = "")
temperature_lbl.pack()

weather_lbl = Label(app, text = '')
weather_lbl.pack()




app.mainloop()