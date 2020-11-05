from creat_folder import creat_folder
from classify import Price_classify ,Count_classify
from write_HTML import write_html
from IP_to_menu import IP_to_menu
import os
import time
import subprocess

#IP = input('請輸入IP:')
IP = 'jackproject01.df.r.appspot.com'
#IP = '140.124.44.92:8000'
print("程式開始運作")
print('按下ctrl+C停止')
creat_folder('./data_classification/Price')
creat_folder('./data_classification/Count')
write_html('./locallibrary/chart/templates',IP)
IP_to_menu('./locallibrary/menu/templates/menu.html',IP)
while True :
    while os.listdir('./data/Price' ) or os.listdir('./data/Count' ):
        time.sleep(3)
        Price_classify('./data/Price' ,'./data_classification/Price')
        Count_classify('./data/Count', 'data_classification/Count')
        write_html('./locallibrary/chart/templates',IP)
        IP_to_menu('./locallibrary/menu/templates/menu.html',IP)
        #subprocess.Popen("C:/Users/Jack/Desktop/update_website.bat")
    time.sleep(5)
