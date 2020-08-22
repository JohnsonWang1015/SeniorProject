import random
from datetime import datetime
from time import sleep

account = ''
password = ''

def LoginLottorySystem(account, password):
     if account == 'abc' and password == '123':
          flag = True
          print('\n登入中...\n')
          sleep(1)
          print('******歡迎登入系統!!******')
     elif (len(account) == 0) or (len(password) == 0):
          flag = False
          print('帳號密碼輸入錯誤!!\n')
     else:
          flag = False
          print('此帳密不存在\n')
     return flag 

def BigLottoryGenerator():
     lottoNumber = []
     while len(lottoNumber) < 6:
          r = random.randint(1, 49)
          for i in lottoNumber:
               if i == r:
                    break
          lottoNumber.append(r)
          lottoNumber.sort()
     specialNumber = random.randint(1, 49)
     time = datetime.today() #獲得當地時間
     timeFormat = time.strftime('%Y/%m/%d %H:%M:%S')
     print('大樂透中獎號:%s 特別號:%d' %(lottoNumber, specialNumber))
     print('建立時間:%s\n' %timeFormat)

def PowerLottoryGenerator():
     lottoNumber = []
     while len(lottoNumber) < 6:
          r = random.randint(1, 38)
          for i in lottoNumber:
               if i == r:
                    break
          lottoNumber.append(r)
          lottoNumber.sort()
     specialNumber = random.randint(1, 38)
     time = datetime.today() #獲得當地時間
     timeFormat = time.strftime('%Y/%m/%d %H:%M:%S')
     print('威力彩中獎號:%s 特別號:%d\n' %(lottoNumber, specialNumber))
     print('建立時間:%s\n' %timeFormat)

def Lottory539Generator():
     lottoNumber = []
     while len(lottoNumber) < 5:
          r = random.randint(1, 39)
          for i in lottoNumber:
               if i == r:
                    break
          lottoNumber.append(r)
          lottoNumber.sort()
     specialNumber = random.randint(1, 39)
     time = datetime.today() #獲得當地時間
     timeFormat = time.strftime('%Y/%m/%d %H:%M:%S')
     print('今彩539中獎號:%s 特別號:%d\n' %(lottoNumber, specialNumber))
     print('建立時間:%s\n' %timeFormat)



#主程式
print('==========請登入樂透系統==========')

for i in range(3):
     account = input('請輸入帳號:') #abc
     password = input('請輸入密碼:') #123
     flag = LoginLottorySystem(account, password)
     if flag:
          while True:
               keyin = input('\n請選擇 1)大樂透 2)威力彩 3)今彩539 4)結束:')
               if keyin == '1':
                    BigLottoryGenerator()
                    print('-'*30)
               elif keyin == '2':
                    PowerLottoryGenerator()
                    print('-'*30)
               elif keyin == '3':
                    Lottory539Generator()
                    print('-'*30)
               elif keyin == '4':
                    print('\n系統即將結束...\n')
                    sleep(1)
                    print('系統關閉')
                    break
               else:
                    print('輸入錯誤，請再輸入一次\n')
                    continue
     break
