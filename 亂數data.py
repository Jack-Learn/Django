import os
import random

path = './原html_data備份/random'

month_seq = ['01','02','03','04','05','06','07','08','09','10','11','12']
date_seq = ['01','02','03','04','05','06','07','08','09','10', 
            '11','12','13','14','15','16','17','18','19','20', 
            '21','22','23','24','25','26','27','28','29','30','31']

for month in month_seq:
    for date in date_seq:
        fish = '白蝦'
        file = open(os.path.join(path,fish+month+date+'.txt'),'w',encoding="utf-8")
        i =  round(random.uniform(80, 100),1)
        price_mid =  round(random.uniform(180, 210),1)
        j =  round(random.uniform(80, 130),1)
        price_high =  str(price_mid + i)
        price_low =  str(price_mid - j)
        price_mid = str(price_mid)
        
        string = '109/'+ month + '/' + date + '\n' + \
                '市場：台北\n' + fish + '\n上價：' + price_high + \
                '\n中價：' +price_mid+ \
                '\n下價：'+price_low
                
        file.write(string)
        file.close() 

path = './原count備份/random'
for month in range(12):
    for date in range(31):
        filename = 'Counting_result_2020年' + str(month+1) +'月'+ str(date+1) +'號'
        file = open(os.path.join(path,filename+'.txt'),'w',encoding="utf-8")
        string = 'Count:' + str(random.randint(0,30))
        file.write(string)
        file.close() 