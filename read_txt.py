#只需要改path，不需要執行
import os

def read_price(path):
    categories = ""
    pricemid_1,pricemid_2,pricemid_3,pricemid_4 = "","","",""
    priceup_1,priceup_2,priceup_3,priceup_4 = "","","",""
    pricelow_1,pricelow_2,pricelow_3,pricelow_4 = "","","",""
    
    #自行新增魚類名稱
    fish_1 = "黃花(養殖)"
    fish_2 = "虱目魚"
    fish_3 = "吳郭魚"
    fish_4 = "白蝦"
        
    allFileList = os.listdir(path)
    for folder in allFileList:
        label = [0,0,0,0]
        folderPath = os.path.join(path,folder)
        allFileList2 = os.listdir(folderPath)
        categories = categories +"'" +folder + "',"
        for filename in allFileList2:    
            filepath = os.path.join(folderPath,filename)
            file = open(filepath,encoding="utf-8")
            text = []
            #讀取資料日期
            for line in file:
                text.append(line)  
                pos = line.find('/')
                pos2 = line.find('\n')
                pos4 = line.find('：')
                if pos != -1:   #如果那行有'/'
                    date =line[pos+1 : pos2]
                    #print('date=',date)
                    
                elif pos4 == -1:   #如果沒有'/'代表不是第一行，但沒有'：'，代表魚種那行
                    fish = line[: line.find('\n')]
                    #print('fish=',fish)     
                    
                pos3 = line.find('中價：')     
                if pos3 != -1:
                    pricemid = line[pos3+3 :-1]
                    #print('price=',pricemid)
                pos3 = line.find('上價：')     
                if pos3 != -1:
                    priceup = line[pos3+3 :-1]
                    #print('priceup=',priceup)
                pos3 = line.find('下價：')     
                if pos3 != -1:
                    pricelow = line[pos3+3 :-1]
                    #print('pricelow=',pricelow)
            file.close()   
            #魚價分類        
            if fish == fish_1:
                label[0]=1
                pricemid_1 = pricemid_1 + pricemid + ","
                priceup_1 = priceup_1 + priceup + ","
                pricelow_1 = pricelow_1 + pricelow + ","
            if fish == fish_2:
                pricemid_2 = pricemid_2 + pricemid + ","
                priceup_2 = priceup_2 + priceup + ","
                pricelow_2 = pricelow_2 + pricelow + ","
                label[1]=1
            if fish == fish_3:
                pricemid_3 = pricemid_3 + pricemid + ","
                priceup_3 = priceup_3 + priceup + ","
                pricelow_3 = pricelow_3 + pricelow + ","
                label[2]=1
            if fish == fish_4:
                pricemid_4 = pricemid_4  + pricemid + ","
                priceup_4 = priceup_4 + priceup + ","
                pricelow_4 = pricelow_4 + pricelow + ","
                label[3]=1
                
        #當天沒有那種魚的資料 設為0
        if  label[0] == 0:
            pricemid_1 = pricemid_1 + '0' + ","
            priceup_1 = priceup_1 + '0' + ","
            pricelow_1 = pricelow_1 + '0' + ","
        if  label[1] == 0:
            pricemid_2 = pricemid_2 + '0' + "," 
            priceup_2 = priceup_2 + '0' + ","
            pricelow_2 = pricelow_2 + '0' + ","
        if  label[2] == 0:
            pricemid_3 = pricemid_3 + '0' + ","
            priceup_3 = priceup_3 + '0' + ","
            pricelow_3 = pricelow_3 + '0' + ","
        if  label[3] == 0:
            pricemid_4 = pricemid_4 + '0' + ","   
            priceup_4 = priceup_4 + '0' + ","
            pricelow_4 = pricelow_4 + '0' + ","
   
    return  (categories, 
            priceup_1,priceup_2,priceup_3,priceup_4, 
            pricemid_1,pricemid_2,pricemid_3,pricemid_4, 
            pricelow_1,pricelow_2,pricelow_3,pricelow_4)

def read_count(path):
    sum_list=[]
    allFileList = os.listdir(path)
    for folder in allFileList:
        folderPath = os.path.join(path,folder)
        allFileList2 = os.listdir(folderPath)
        sum = 0
        for filename in allFileList2:                    
            filepath = os.path.join(folderPath,filename)
            file = open(filepath,encoding="utf-8")
            #print(filepath)
            text = []
            for line in file:
                text.append(line)
                count = int(line[line.find(':')+1:])
                sum += count
            file.close()
        #print('sum=',sum)
        sum_list.append(sum)
    return sum_list

#sum_list = read_count(os.path.join('./data_classification/Count',str(10)))
