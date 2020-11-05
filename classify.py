import os
import shutil


def Price_classify(read_folder,write_folder):
    i=0
    j=0
    allFileList = os.listdir(read_folder)
    for filename in allFileList:
        file = open(os.path.join(read_folder,filename),encoding="utf-8")
        text = []
        #讀取資料日期
        for line in file:
            text.append(line)  
            pos = line.find('/')
            pos2 = line.find('\n')
            pos4 = line.find('：')
            if pos != -1:   #如果那行有'/'
                month = line[pos+1 : pos+3]
                date = line[pos+4 : pos2]
                #print('month=',month)
                #print('date=',date)
            elif pos4 == -1:   #如果沒有'/'代表不是第一行，但沒有'：'，代表魚種那行
                fish = line[: line.find('\n')]
                #print('fish=',fish) 
        file.close()
       
        write_Path = os.path.join(write_folder,month,date)
        
        if os.path.isfile(os.path.join(write_Path,filename))==False:
            shutil.move(os.path.join(read_folder,filename),write_Path)            
            i=i+1           
        else:
            os.remove(os.path.join(read_folder, filename))
            j=j+1
            
    print('Price新增',i,'筆資料')   
    print('Price重複',j,'筆資料')
    
def Count_classify(read_folder,write_folder):
    i=0
    j=0
# =============================================================================
#     allFileList = os.listdir(read_folder)
#     for filename in allFileList:       
#         month = int(filename[filename.find('年')+1 : filename.find('月')])
#         date = int(filename[filename.find('月')+1 : filename.find('號')])
#         if(month < 10):
#             month = '0' +str(month)
#         if(date < 10):
#             date = '0' +str(date)
#         #print(month,'月',date,'號')       
#         write_Path = os.path.join(write_folder,str(month),str(date))
#         if os.path.isfile(os.path.join(write_Path,filename))==False:
#             shutil.move(os.path.join(read_folder,filename),write_Path)     
#             i=i+1  
#         else:
#             os.remove(os.path.join(read_folder,filename))
# =============================================================================
    
    allFileList = os.listdir(read_folder)
    for filename in allFileList:     
        month = filename[filename.find('-')+1:filename.find('-')+3]
        date = filename[filename.find('-')+4:filename.find('-')+6]
        write_Path = os.path.join(write_folder,month,date,filename)
        #print(write_Path)
        if os.path.isfile(write_Path)==False:
            shutil.move(os.path.join(read_folder,filename),write_Path)   
            i=i+1  
        else:
            os.remove(os.path.join(read_folder,filename))
            j=j+1
            
    print('Count新增',i,'筆資料')   
    print('Count重複',j,'筆資料') 
    
#Count_classify('./data/Count', 'data_classification/Count')
        
