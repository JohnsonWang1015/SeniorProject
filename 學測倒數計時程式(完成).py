import tkinter as tk
from datetime import datetime, date, timedelta
import time
import pandas as pd

currentTime = datetime.now() #取得現在時間
finalTime = datetime(2021, 1, 22, 0, 0, 0) #設定最後時間
#finalTime = datetime(2020, 6, 13, 23, 28, 0)
#currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#finalTime = time.strftime("%Y-%m-%d %H:%M:%S")

'''
currentTime = pd.to_datetime(datetime.now())
finalTime = pd.to_datetime(datetime(2021, 1, 22, 0, 0, 0))
diff = finalTime - currentTime
print(diff)
'''

#---------------------------------------------------------------------------------

dayCount = (finalTime - currentTime).days #計算剩餘天數

secondCount = (finalTime - currentTime).seconds #計算剩餘秒數

#print(finalTime - currentTime)

#---------------------------------------------------------------------------------

timestring = tuple(str(finalTime - currentTime).split(',')) #將剩餘天數用逗點隔開並轉成tuple儲存
#print(len(timestring))
'''
if len(timestring) == 1:
    print(timestring[0])
else:
    print(timestring[1])
'''

#---------------------------------------------------------------------------------
if len(timestring) == 1:
    dayString = 0
else:
    dayString = timestring[0]

#print(dayString)

if 'days' in timestring[0]:
    day = timestring[0].strip().replace('days', ' ')
else:
    day = timestring[0].strip().replace('day', ' ')
#print(day)

if len(timestring) == 1:
    day = 0
else:
    day = day

#IntDay = int(day)

'''
if IntDay < 0:
    IntDay = 0
''' 
#print(IntDay)


#---------------------------------------------------------------------------------

if len(timestring) == 1:
    tempString = timestring[0]
else:
    tempString = timestring[1] #取出tuple內的 index 1 儲存

#print(tempString)

if len(timestring) == 1:
    time_1 = timestring[0].strip().replace(':', ' ')
else:
    time_1 = timestring[1].strip().replace(':', ' ') #將 index 1 去除頭尾空白並將冒號取代成空白

#print(timestring[1].replace(':', ' '))

#---------------------------------------------------------------------------------

Date_time = tuple(time_1) #將結果儲存再將其轉成tuple
#Date_time = ('2','8', ' ', '5', '6', ' ', '3', '6', '.', '5', '2', '7', '6', '5', '6')
#print(Date_time)

#---------------------------------------------------------------------------------

length = len(Date_time) #計算tuple長度以便之後判斷
#print(length)

#---------------------------------------------------------------------------------

#('2','8', ' ', '5', '6', ' ', '3', '6', '.', '5', '2', '7', '6', '5', '6')
#('8', ' ', '4', '9', ' ', '3', '4', '.', '8', '9', '2', '2', '4', '9')
for i in range(0,2): #取出小時
    if length == 14:
        hour = Date_time[i-1] + Date_time[i]
    if length == 15:
        hour = Date_time[i-1] + Date_time[i]
print(hour)

for i in range(2,5): #取出分鐘
    if length == 14:
        minute = Date_time[i-2] + Date_time[i-1]
    if length == 15:
        minute = Date_time[i-1] + Date_time[i]
print(minute)

for i in range(6,8): #取出秒
    if length == 14:
        second = Date_time[i-2] + Date_time[i-1]
    if length == 15:
        second = Date_time[i-1] + Date_time[i]
print(second)

'''
for i in range(2,4):
    if i >= 0:
        minute = str(tmp_date[i-1]) + str(tmp_date[i])
#print(minute)
for i in range(5,7):
    if i >= 0:
        second = str(tmp_date[i-1]) + str(tmp_date[i])
#print(second)
'''

#different = timedelta(days=int(IntDay), hours=int(hour), minutes=int(minute), seconds=int(second))
#print(different)

#---------------------------------------------------------------------------------

class Application(tk.Tk): #版面設定
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('學測倒數計時器')
        self.geometry('1800x1800')

        self.label_1 = tk.Label(self, text='學測剩餘天數', font=('標楷體', 80))
        self.label_2 = tk.Label(self, text='', font=('標楷體', 80), fg='red')
        self.label_3 = tk.Label(self, text='現在時間', font=('標楷體', 80))
        self.label_4 = tk.Label(self, text='', font=('標楷體', 80))
        self.label_5 = tk.Label(self, text='剩下時間', font=('標楷體', 80))
        self.label_6 = tk.Label(self, text='', font=('標楷體', 80))
        self.label_7 = tk.Label(self, text='', font=('標楷體', 200), fg='red')
        #self.label_8 = tk.Label(self, text='', font=('標楷體', 80))
        self.label = tk.Label(self, text='', font=('標楷體', 150))
        '''
        self.label_1.grid(row=0, column=5)
        self.label_2.grid(row=1, column=5)
        self.label_3.grid(row=2, column=5)
        self.label_4.grid(row=3, column=5)
        '''
        self.label_1.pack(side='top')
        self.label_2.pack(side='top')
        self.label_5.pack(side='top')
        self.label_6.pack(side='top')
        self.label_7.place(x=900, y=900)
        #self.label_8.pack(side='left')
        self.label_3.pack(side='top')
        self.label_4.pack(side='top')
        self.label.pack(side='top')

        # 主程式內容設定
        self.remaining = 0
        self.countdown(int(day))
        self.timedown(int(hour), int(minute), int(second))
        #self.showTime(int(hour), int(minute), int(second))
        self.update_clock()

#---------------------------------------------------------------------------------

    #倒數天數
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = int(day)

        # 剩下天數
        if self.remaining == 0:
            self.label_2.configure(text="0") #學測就是今天
        else:
            self.label_2.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            #self.after(secondCount * 1000, self.countdown)
            self.after(86400 * 1000, self.countdown)

#---------------------------------------------------------------------------------
    
    #倒數時間      
    def timedown(self, hour=None, minute=None, remaining=None):
        if hour is not None:
            self.hour = int(hour)
        if minute is not None:
            self.minute = int(minute)
        if remaining is not None:
            self.remaining = int(second)

            
        # 剩下時間
        if int(day) == 0:
            self.label_2.configure(text="0") #學測就是今天
                
        else:
            if int(day) == 0:
                time = str.format("%02d:%02d:%02d") % (0, self.minute, self.remaining)
            else:
                time = str.format("%02d:%02d:%02d") % (self.hour, self.minute, self.remaining)
            '''
            Hourtime = str.format("%02d:") % self.hour
            Minutetime = str.format("%02d:") % self.minute
            Secondtime = str.format("%02d") % self.second
            '''
            #countTime = time.strptime(time, '%H:%M:%S')
            self.label_6.configure(text=time)

            #轉換時分秒(注意畫面更新)
            self.remaining = self.remaining - 1
            
            if self.remaining == 0:
                self.remaining = 60
                self.label_6.configure(text=time)
                self.minute = self.minute - 1
                self.label_6.configure(text=time)
                
            if self.minute == 0:
                self.minute = 60
                self.label_6.configure(text=time)
                self.hour = self.hour - 1
                self.label_6.configure(text=time)
                 
            if int(day) == 0 and self.hour == 0 and self.minute == 0 and self.remaining == 10:
                self.label_1.configure(self.label_1.pack_forget())
                self.label_2.configure(self.label_2.pack_forget())
                self.label_3.configure(self.label_3.pack_forget())
                self.label_4.configure(self.label_4.pack_forget())
                self.label_5.configure(self.label_5.pack_forget())
                self.label_6.configure(self.label_6.pack_forget())
            
                self.label_7.configure(text="%d" % self.remaining)

        self.after(1000, self.timedown) 
            
#---------------------------------------------------------------------------------

    #現在時間    
    def update_clock(self):
        now = time.strftime('%H:%M:%S')
        self.label_4.configure(text=now)
        self.after(1000, self.update_clock)
        
#---------------------------------------------------------------------------------
    def showTime(self, hour=None, minute=None, remaining=None):
        if hour is not None:
            self.hour = int(hour)
        if minute is not None:
            self.minute = int(minute)
        if remaining is not None:
            self.remaining = int(second)

        if int(day) == 0 and self.hour ==0 and self.minute==0 and self.remaining == 10:
            
            self.label_1.configure(self.label_1.pack_forget())
            self.label_2.configure(self.label_2.pack_forget())
            self.label_3.configure(self.label_3.pack_forget())
            self.label_4.configure(self.label_4.pack_forget())
            self.label_5.configure(self.label_5.pack_forget())
            self.label_6.configure(self.label_6.pack_forget())
            
            self.label_7.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
        self.after(1000, self.showTime)
#判斷是否為主程式
if __name__ == "__main__":
    app = Application()
    app.mainloop()
        
