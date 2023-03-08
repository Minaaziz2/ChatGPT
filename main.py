from ast import literal_eval
from tkinter import *
import os
import requests

my_dir = os.getcwdb()
photo = my_dir + bytes("\\logo.png", encoding='windows-1255')


class Form:
    def __init__(self):
        self.URL = ""
        self.payload = {}
        self.headers = {}
        self.out = ""
        self.res = ""
        self.window = Tk()
        self.window.title('ChatGPT')
        self.window.config(padx=10, pady=10, bg='black', highlightthickness=0)
        self.api_frame = Frame(self.window, bg='black', highlightthickness=0)
        self.api_frame.grid(row=0, column=0)
        self.api_label = Label(self.api_frame, text="API:", fg='white', bg='black', highlightthickness=0, font=14)
        self.api_label.grid(row=1, column=0, pady=10, padx=10)
        self.api_entry = Entry(self.api_frame, width=50)
        self.api_entry.grid(row=1, column=1, pady=10, padx=10)
        self.request_frame = Frame(self.window, bg='black', highlightthickness=0)
        self.request_frame.grid(row=1, column=0)
        self.request_label = Label(self.request_frame,  text="Your inquiry:", fg='white', bg='black', highlightthickness=0, font=14)
        self.request_label.grid(row=0, column=0, pady=10, padx=10)
        self.request_entry = Entry(self.request_frame, width=40)
        self.request_entry.grid(row=0, column=1, pady=10, padx=10)
        self.canvas_frame = Frame(self.window, bg='black', highlightthickness=0)
        self.canvas_frame.grid(row=2, column=0)
        self.canvas = Canvas(self.canvas_frame, height=600, width=900)
        self.img = PhotoImage(file=photo)
        self.canvas.create_image(450, 300, image=self.img)
        self.canvas.grid(row=0, column=0)
        self.but_frame = Frame(self.window, bg='black', highlightthickness=0)
        self.but_frame.grid(row=3, column=0)
        self.but = Button(self.but_frame, text="ASK", bg='green', command=self.GPT, width=60)
        self.but.grid(row=0,column=1)
        self.window.mainloop()

    def GPT(self):
        self.URL = "https://api.openai.com/v1/chat/completions"
        self.payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": f"{self.request_entry.get()}"}],
            "temperature": 1.0,
            "top_p": 1.0,
            "n": 1,
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 0,
        }
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_entry.get()}"
        }
        response = requests.post(self.URL, headers=self.headers, json=self.payload, stream=False)
        out = response.content
        out2 = literal_eval(out.decode('utf-8'))
        self.out = out2['choices'][0]['message']['content']
        self.canvas.itemconfig(self.res, text ="")
        self.res = self.canvas.create_text(500, 200, text=self.out, width=680, fill='white')


my_form = Form()


