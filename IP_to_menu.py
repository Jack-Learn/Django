

def IP_to_menu(path,IP):
    f = open(path,'w',encoding="utf-8")
    message = """
    <html>
        <head>
            <title>AIoT 魚蝦苗計數系統</title>
        </head>
        <body>
            <img src="https://i.ibb.co/pLz4k73/logo.jpg" alt="logo" border="0" style=" width:300px; position:relative; top:100px;left:500px "></a>
            <select  style=" font-size:24px; width:300px; position:relative; top:150px;left:200px " onchange="location.href=value" > 
                <option value="網址連結">選擇月份</option>
                <option value="chart/January">1月</option>
                <option value="chart/February">2月</option>
                <option value="chart/March">3月</option>
                <option value="chart/April">4月</option>
                <option value="chart/May">5月</option>
                <option value="chart/June">6月</option>
                <option value="chart/July">7月</option>
                <option value="chart/August">8月</option>
                <option value="chart/September">9月</option>
                <option value="chart/October">10月</option>
                <option value="chart/November">11月</option>
                <option value="chart/December">12月</option>
            </select>    
            <table width="400" height="80" style= "position:relative; top:95px;left:220px">
                <tr><td align="center"  style=" font-size:24px;">查詢魚市行情</td></tr>
            </table>        
        </body>
    </html>
    """
    
    f.write(message)
    f.close()
    
    # <img src="https://i.ibb.co/ys0gJNm/logo.jpg" alt="logo" border="0" style=" width:300px; position:relative; top:100px;left:500px "></a>
