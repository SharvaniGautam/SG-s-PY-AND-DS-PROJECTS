import requests
from tkinter import *
from urllib.request import urlopen
import io
import webbrowser
from PIL import ImageTk,Image

class NewsApp:

    def __init__(self):
        self.data=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=81dda274fb7b4a678871efa6dafd03d0").json()
        #print(data)

        self.load_gui()
        

        self.load_news_item(0)




    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_gui(self):
        self.root=Tk()
        self.root.geometry("360x600")
        self.root.resizable(0,0)
        self.root.title("News App")
        self.root.configure(background="black")


    def load_news_item(self,index):

        #clear the screen for the new news item
        self.clear()
        #image
        try:
            img_url=self.data["articles"][index]["urlToImage"]
            raw_data=urlopen(img_url).read()
            im=Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo=ImageTk.PhotoImage(im)
        except:
             img_url="data:image/jpeg;base64,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"
             raw_data=urlopen(img_url).read()
             im=Image.open(io.BytesIO(raw_data)).resize((350,250))
             photo=ImageTk.PhotoImage(im)

        label=Label(self.root,image=photo)
        label.pack()

#heading
        heading=Label(self.root,text=self.data["articles"][index]["title"],bg="black",fg="white",wraplength=350,justify="center")
        heading.pack(pady=(10,20))
        heading.configure(font=("verdana",15))
#details
        details=Label(self.root,text=self.data["articles"][index]["description"],bg="black",fg="white",wraplength=350,justify="center")
        details.pack(pady=(2,20))
        details.configure(font=("verdana",12))


        frame=Frame(self.root,bg="black")
        frame.pack(expand=True,fill=BOTH)

        if index !=0:
             prev=Button(frame,text="Prev",width=16,height=3,command=lambda :self.load_news_item(index-1))
             prev.pack(side=LEFT)

        read=Button(frame,text="Read",width=16,height=3,command=lambda :self.open_link(self.data["articles"][index]["url"]))
        read.pack(side=LEFT)

        if index !=len(self.data["articles"])-1:
            next=Button(frame,text="Next",width=16,height=3,command=lambda :self.load_news_item(index+1))
            next.pack(side=LEFT)



        self.root.mainloop()

    def open_link(self,url):
        webbrowser.open(url)




obj=NewsApp()