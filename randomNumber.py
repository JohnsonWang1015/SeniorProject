import pandas as pd
import tkinter as tk
from datetime import datetime
import time, random
from tkinter import filedialog, messagebox
#from pydub import AudioSegment
#from pydub.playback import play
#import os

#---------------------------------------------------------------------------------
#url = r'C:\Users\USER\Desktop\抽籤\201_data.xlsx'
#---------------------------------------------------------------------------------
#data = pd.read_excel(url, sheet_name = 0)
#print(data.head(35))
#Data = data.iloc[:, 1]
#data.drop()
#print(data.iloc[:, 1])

'''
ListName = tuple(data.iloc[:, 1])
ListNumber = tuple(data.iloc[:, 0])
'''
Data_List = []

Data_Set = set()
Number_Set = set()

Name = []


#print(ListName)
#print(ListNumber)
#print(data.iloc[:, 1])
#activeData = data.head(35)
#print(activeData)
'''
for i in range(len(data)):
     print(data.head(i))
'''

#print(len(data))
#---------------------------------------------------------------------------------

class Application(tk.Tk):
     def __init__(self):
          Number_List = []
          
          self.ListName = ()
          self.ListNumber = ()

          self.MIN = 0
          self.MAX = 0
          
          #版面設定
          tk.Tk.__init__(self)
          self.title('亂數抽籤')
          self.geometry('1800x1800')
          
          self.num = tk.IntVar()

          #按鈕
          #btn = tk.Button(self, text='開始抽籤', command=self.randomNumber, padx=10, pady=5)
          btn_browse = tk.Button(self, text='瀏覽檔案')
          self.btn = tk.Button(self, text='開始抽籤', state=tk.DISABLED)
          #btn_list = tk.Button(self, text='不重複模式')
               

          #滾動軸
          scrollbar = tk.Scrollbar(self)

          #清單方塊
          self.listbox = tk.Listbox(self, yscrollcommand = scrollbar.set)

          #標籤
          self.label = tk.Label(self, text='中獎人:', font=('標楷體', 60))
          self.label_1 = tk.Label(self, text='', font=('標楷體', 100))
          self.label_2 = tk.Label(self, text='========================\n請先製作一份Excel檔\n並將欄位只設定座號和姓名兩欄\n再輸入資料進行操作\n========================', font=('標楷體', 30))
          self.label_3 = tk.Label(self, text='請輸入欲取人數', font=('標楷體', 20))

          #文字方塊
          textbox = tk.Entry(self, text='', width=20, textvariable=self.num)
          
          #位置設定
          scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
          
          self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

          textbox.place(x=1150, y=80)

          self.label_2.pack(side='top')
          self.label_3.place(x=1150, y=50)
          
          #self.label_2.place(x=50, y=30)
          #self.label_2.grid(row=0, column=1)
          #btn_browse.pack(side=tk.TOP)
          
          btn_browse.place(x=200, y=50)
          #btn_browse.grid(row=1, column=3)
          
          self.btn.pack(side='top')
          
          #btn_list.place(x=400, y=230)
          #btn.grid(row=1, column=2)
          #btn.pack()
          
          self.label.pack(side='left')
          
          #self.label.grid(row=1, column=0)
          #self.label_1.pack(side='right')
          
          self.label_1.place(x=500, y=500)
          #self.label_1.grid(row=1, column=1)

          #屬性設定
          scrollbar.config(command=self.listbox.yview)
          
          self.listbox.config(font=('標楷體', 13))

          btn_browse.config(bd=20, font=('標楷體', 20), command = self.browse_file)

          self.btn.config(bd=35, font=('標楷體', 30), command = self.multipleRandom)

          '''
          if not(self.ListNumber is None):
               #btn['state'] = tk.NORMAL
               btn.config(bd=35, font=('標楷體', 30), command = self.multipleRandom)
          else:
               btn['state'] = tk.DISABLED
          '''
          
          #btn_list.config(bd=25, font=('標楷體', 20))

          #btn.bind("NoList", self.randomNumber)
          #btn.bind('haveList', self.ListRandomNumber)



     def browse_file(self):
          fileName = tk.filedialog.askopenfilename(filetypes=(('Template files', '*.xlsx'), ('All files', '*.*')))
          #print(fileName)

          #用pandas讀取excel檔
          data = pd.read_excel(fileName, sheet_name = 0)
          #print(data.head(35))
          
          self.ListName = tuple(data.iloc[:, 1])
          self.ListNumber = tuple(data.iloc[:, 0])
          
          #print(self.ListName)
          #print(self.ListNumber)
          
          #判斷是否有資料
          for i in range(len(self.ListName)):
               if not(self.listbox.size() == len(self.ListName)):
                    self.listbox.delete(0, i)
          #放入資料       
          for i in range(len(self.ListName)):
             self.listbox.insert(i, self.ListName[i])
                    
          self.listbox.config(font=('標楷體', 13))
          
          '''
          print(self.listbox.size())
          print(len(self.ListName))
          '''
          #print(self.listbox.get(0))

          if not(self.ListNumber is None):
               self.btn['state'] = tk.NORMAL
          else:
               self.btn['state'] = tk.DISABLED


     def randomNumber(self):
          number = random.randint(1, self.ListNumber[-1])
          #print(number)
          for i in range(len(self.ListNumber)):
               if self.ListNumber[i] == number:
                    self.label_1.config(text=self.ListName[i])
                    #print(self.ListName[i])
                    #self.after(1200, self.randomNumber)
                    '''
                    self.after(400, self.randomNumber)
                    if i > 5:
                         self.after_cancel(self.after(300, self.randomNumber))
                    '''
               else:
                    continue

     def ListRandomNumber(self):
          temp = 0
          #print(self.ListNumber)
          #print(len(self.ListNumber))
          Number_List = random.sample(range(self.ListNumber[0], self.ListNumber[-1]),len(self.ListNumber))
          #Number_List = random.sample(range(self.ListNumber[0], self.ListNumber[-1]), 10)
          #Number_List = tuple(Number_List)
          #print(Number_List)
          #print('-' * 30)
          #print(self.ListNumber)
          for i in range(len(Number_List)):
               #print(Number_List[i])
               if Number_List[i] not in self.ListNumber:
                    temp = Number_List[i]
                    
               if Number_List[i] >= temp:
                    Number_List[i] += 1
               else:
                    Number_List[i] = Number_List[i]

               if Number_List[i] == self.ListNumber[i]:
                    #print(Number_List[i])
                    #print(i)
                    #print(self.ListName[i])
                    self.label_1.config(text=self.ListName[i])
                    
                    #print(Number_List[i] + 1)
               #print(self.ListName[Number_List[i]])
               #self.label_1.config(text=self.ListName[Number_List[i]])
          #print(Number_List)

               
          '''
          for i in range(len(self.ListNumber)):
               if self.ListNumber[i] == Number_List[i]:
                    self.label_1.config(text=self.ListName[i])
          '''
          '''
          number = random.randint(1, self.ListNumber[-1])
          #print(number)
          #List.append(number)
          #tmp = random.sample(List, len(List))
          #List.sort()
          #random.shuffle(List)
          #print(List)
          #print(random.sample(List, len(List)))
               
          for i in range(len(self.ListNumber)):
               if self.ListNumber[i] == number:
                    self.label_1.config(text=self.ListName[i])
                    Data_List.append(number)
                    #Name_List.append(self.ListName[i])
          for j in range(len(Data_List)):
               if number == Data_List[j]:
                    if self.ListNumber[j] == number:
                         self.label_1.config(text=self.ListName[i])                         
          '''                   
          #print(Data_List)   
          #print(Data_List)
          #print(Name_List)
          #Data_Set = set(Data_List)
          #print(Data_Set)
          '''
               if number in Data_Set:
                    #print(Data_Set)
                    number = random.randint(1, self.ListNumber[-1])
          '''
               
     def multipleRandom(self):
          #playsound('start.mp3')
          
          #btn.config(state=tk.NORMAL)
          
          #number = random.randint(1, self.ListNumber[-1])
          temp = 0
          #Name = []
          if Name is not None:
               Name.clear()

          #對話方塊
          if self.num.get() > len(self.ListNumber):
               msg = messagebox.showwarning('警告', '抽取人數輸入錯誤')
          elif self.num.get() <= 0:
               msg = messagebox.showwarning('警告', '抽取人數小於或等於0')
          else:
               Number_List = random.sample(range(self.ListNumber[0], len(self.ListNumber)+1), self.num.get())
               
          #Number_List=random.sample(self.ListNumber,self.num.get())
          #print(Number_List)
          for i in range(len(Number_List)):
               if Number_List[i] not in self.ListNumber:
                    temp = Number_List[i]
                    
               if Number_List[i] >= temp:
                    Number_List[i] += 1
               else:
                    Number_List[i] = Number_List[i]

          for i in range(len(Number_List)):
               for j in range(len(self.ListNumber)):
                    if Number_List[i] == self.ListNumber[j]:
                         #print(self.ListName[j])
                         Name.append(self.ListName[j])

          if self.num.get() > 5:
               self.label_1.config(text=Name, font=('標楷體', 15))
          else:
               self.label_1.config(text=Name, font=('標楷體', 25))

          if self.num.get() >= 30:
               self.label_1.config(text=Number_List, font=('標楷體', 13))
          elif self.num.get() >= 20:
               self.label_1.config(text=Number_List, font=('標楷體', 18))
          elif self.num.get() >= 12:
               self.label_1.config(text=Number_List, font=('標楷體', 20))
               #print(Number_List[i])
          #print(Name)
               #print(i)
               #print(self.ListName[i])
               #self.label_1.config(text=self.ListName[i], font=('標楷體', 25))
               
          '''
          if Number_List is not None:
               Number_List.clear()
          '''
          
          '''
          for i in range(len(Number_List)):
               if Number_List[i] not in self.ListNumber:
                    number = random.randint(1, self.ListNumber[1])
          '''

          #print(self.num.get())
          '''
          for i in range(self.num.get()):
               Number_Set.add(random.randint(1, self.ListNumber[-1]))
          '''

          '''
          while len(Number_List) < int(self.num.get()):
               #Number_Set.add(random.randint(1, self.ListNumber[-1]))
               number = random.randint(1, self.ListNumber[-1])
               Number_List.append(number)
               self.num.get() += 1
          '''
          '''
          if not(self.Number_Set is None):
               self.Number_Set.remove(i)
          '''

          '''
          for i in range(len(Number_List)):
               for j in range(len(Number_List)):
                    if Number_List[i] == Number_List[j]:
                         Number_List=random.sample(self.ListNumber,self.num.get())
          '''
          
          #print(Number_List)
               
          '''
          for k in range(len(Number_List)):
               print(Number_List[k] + 1)
               print(self.ListName[Number_List[k]])
                         
                         #self.label_1.config(text=self.ListName[m], font=('標楷體', 25))
               #print(self.ListNumber[m])
          '''
          #print(Name)
          '''
          for i in range(len(self.Number_List)):
               print(self.Number_List)
               #self.label_1.config(text=self.ListName[i], font=('標楷體', 25))
          '''
        

if __name__ == "__main__":
    app = Application()
    app.mainloop()
