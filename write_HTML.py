import os
from read_txt import read_price,read_count


def write_html(path,IP):
    
    i = 1
    while i <= 12:
        if i < 10:
            month = '0' + str(i)
        else:
            month = str(i)
        i+=1
        categories, \
        priceup_1,priceup_2,priceup_3,priceup_4, \
        pricemid_1,pricemid_2,pricemid_3,pricemid_4, \
        pricelow_1,pricelow_2,pricelow_3,pricelow_4 = read_price(os.path.join('./data_classification/Price',month))
        
        sum_list = read_count(os.path.join('./data_classification/Count',month))
        f = open(os.path.join(path,month+'.html'),'w',encoding="utf-8")
        message = """
        <html>
        <head>
        <meta charset="UTF-8" />
        <title>AIoT市價漲跌–水產系統</title>
        <script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
        <script src="https://code.highcharts.com/highcharts.js"></script>
        </head>
        
        <body>                        
        <table width="300" border="1" style=" position:absolute; top:200px;left:0px">
            <tr>
            <td colspan="2" align="center">每日計數數量</td>
            </tr>
            <tr>
            <td align="center">日期</td>            
            <td align="center">數量</td>    
            </tr>
            <tr>
            <td align="center">01</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">02</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">03</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">04</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">05</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">06</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">07</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">08</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">09</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">10</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">11</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">12</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">13</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">14</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">15</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">16</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">17</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">18</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">19</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">20</td>
            <td align="center">%s</td>
            </tr>
            <td align="center">21</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">22</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">23</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">24</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">25</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">26</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">27</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">28</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">29</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">30</td>
            <td align="center">%s</td>
            </tr>
            <tr>
            <td align="center">31</td>
            <td align="center">%s</td>
            </tr>
        </table>
        
        <input type="button" value="返回首頁" onclick="location.href='https://%s'" style=" position:relative; top:150px;left:30px"></input>
        <select onchange="location.href=this.options[this.selectedIndex].value" style=" width:150px ;position:relative; top:150px;left:65px">
         	<option value="網址連結">選擇其他月份</option>
        	<option value="January">1月</option>
         	<option value="February">2月</option>
         	<option value="March">3月</option>
         	<option value="April">4月</option>
         	<option value="May">5月</option>
         	<option value="June">6月</option>
         	<option value="July">7月</option>
         	<option value="August">8月</option>
         	<option value="September">9月</option>
         	<option value="October">10月</option>
         	<option value="November">11月</option>
         	<option value="December">12月</option>
    	</select>
        
        <tr>
            <td>
                <div id="container1" style="width: 1100px; height: 400px; margin: 100px auto; position:absolute; top:0px;left:300px"></div>
            <td/>
            <td>
                <div id="container2" style="width: 1100px; height: 400px; margin: 100px auto; position:absolute; top:400px;left:300px"></div>
            <td/>    
            <td>
                <div id="container3" style="width: 1100px; height: 400px; margin: 100px auto; position:absolute; top:800px;left:300px"></div>
            <td/>
            <td>
                <div id="container4" style="width: 1100px; height: 400px; margin: 100px auto; position:absolute; top:1200px;left:300px"></div>
            <td/>
        <tr/>

        
        <script language="JavaScript">
        $(document).ready(function() {
           var title = {
               text: '台北魚市行情(%s月份)'
           };
           var subtitle1 = {
                text: '黃花(養殖)'
           };
        
           var subtitle2 = {
                text: '虱目魚'
           };
           
           var subtitle3 = {
                text: '吳郭魚'
           };
        
           var subtitle4 = {
                text: '白蝦'
           };
              
           var xAxis = {
               categories: [%s]
           };
           var yAxis = {
              title: {
                 text: '價格 (新台幣)'
              },
              plotLines: [{
                 value: 0,
                 width: 1,
                 color: '#808080'
              }]
           };
         
           var tooltip = {
              valueSuffix: '元'
           }
         
           var legend = {
              layout: 'vertical',
              align: 'right',
              verticalAlign: 'middle',
              borderWidth: 0
           };
         
           var series1 =  [
              {
                 name: '上價',
                 data: [%s]
              },
              {
                 name: '中價',
                 data: [%s]
              },
              {
                 name: '下價',
                 data: [%s]
              }
           ];
           var series2 =  [
              {
                 name: '上價',
                 data: [%s]
              },
              {
                 name: '中價',
                 data: [%s]
              },
              {
                 name: '下價',
                 data: [%s]
              }
           ];
           var series3 =  [
              {
                 name: '上價',
                 data: [%s]
              },
              {
                 name: '中價',
                 data: [%s]
              },
              {
                 name: '下價',
                 data: [%s]
              }
           ];
           var series4 =  [
              {
                 name: '上價',
                 data: [%s]
              },
              {
                 name: '中價',
                 data: [%s]
              },
              {
                 name: '下價',
                 data: [%s]
              }
           ];
           
           var json1 = {};
           var json2 = {};
           var json3 = {};
           var json4 = {};
         
           json1.title = title;
           json1.subtitle = subtitle1;
           json1.xAxis = xAxis;
           json1.yAxis = yAxis;
           json1.tooltip = tooltip;
           json1.legend = legend;
           json1.series = series1;
           
           json2.title = "";
           json2.subtitle = subtitle2;
           json2.xAxis = xAxis;
           json2.yAxis = yAxis;
           json2.tooltip = tooltip;
           json2.legend = legend;
           json2.series = series2;
        
           json3.title = "";
           json3.subtitle = subtitle3;
           json3.xAxis = xAxis;
           json3.yAxis = yAxis;
           json3.tooltip = tooltip;
           json3.legend = legend;
           json3.series = series3;
           
           json4.title = "";
           json4.subtitle = subtitle4;
           json4.xAxis = xAxis;
           json4.yAxis = yAxis;
           json4.tooltip = tooltip;
           json4.legend = legend;
           json4.series = series4;
         
           $('#container1').highcharts(json1);
           $('#container2').highcharts(json2);
           $('#container3').highcharts(json3);
           $('#container4').highcharts(json4);
        });
        </script>
        </body>
        """%(sum_list[0],sum_list[1],sum_list[2],sum_list[3],sum_list[4],sum_list[5],sum_list[6],sum_list[7],sum_list[8],sum_list[9],sum_list[10],
        sum_list[11],sum_list[12],sum_list[13],sum_list[14],sum_list[15],sum_list[16],sum_list[17],sum_list[18],sum_list[19],sum_list[20],
        sum_list[21],sum_list[22],sum_list[23],sum_list[24],sum_list[25],sum_list[26],sum_list[27],sum_list[28],sum_list[29],sum_list[30],
        IP,month,categories,priceup_1,pricemid_1,pricelow_1,priceup_2,pricemid_2,pricelow_2,priceup_3,pricemid_3,pricelow_3,priceup_4,pricemid_4,pricelow_4)
        
        f.write(message)
        f.close()
    print('網頁寫入完成')
    return()