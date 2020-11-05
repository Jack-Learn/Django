#建立資料夾
#\date_classification\month\date\
import os

def creat_folder(filePath):
    month=1
    while month<10:
        foder1 = '0'+str(month)
        write_filePath = os.path.join(filePath,foder1)
        if os.path.isdir(write_filePath)==False:
            os.makedirs(write_filePath)
        date=1
        while date<10:
            foder2 = '0'+str(date)
            write_filePath = os.path.join(filePath,foder1,foder2)
            if os.path.isdir(write_filePath)==False:
                os.makedirs(write_filePath)
            date+=1    
        while date<=31:
            write_filePath = os.path.join(filePath,foder1,str(date))
            if os.path.isdir(write_filePath)==False:
                os.makedirs(write_filePath)            
            date+=1
        month+=1
    while month<=12:
        write_filePath = os.path.join(filePath,str(month))
        if os.path.isdir(write_filePath)==False:
            os.makedirs(write_filePath)
        date=1
        while date<10:
            foder2 = '0'+str(date)
            write_filePath = os.path.join(filePath,str(month),foder2)
            if os.path.isdir(write_filePath)==False:
                os.makedirs(write_filePath)
            date+=1    
        while date<=31:
            write_filePath = os.path.join(filePath,str(month),str(date))
            if os.path.isdir(write_filePath)==False:
                os.makedirs(write_filePath)            
            date+=1
        month+=1
        
    #print("資料夾建立完成") 
    
