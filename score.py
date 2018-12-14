import tkinter as tk
import time
import requests
import bs4

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.label = tk.Label(text="vikas")
        self.label.pack()
        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        res = requests.get('https://www.cricbuzz.com/live-cricket-scores/20302/aus-vs-ind-2nd-test-india-tour-of-australia-2018-19')
        soup = bs4.BeautifulSoup(res.text, 'lxml')
        content = soup.select('.cb-font-20')
        # score=content[0].getText()
        now = time.strftime("%H:%M:%S")
        self.label.configure(text= "Time : "+now + "  " + content[0].getText())
        self.root.after(5000, self.update_clock)

app=App()
