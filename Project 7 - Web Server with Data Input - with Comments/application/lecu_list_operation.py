from application import frame_operation


def list_updater(frame_id, frame_data, lecu_num, lecu_list):
    """LECU状态列表更新"""
    func, lecu_order, lecu_parsed_data = frame_operation.frame_handler(frame_id, frame_data, lecu_num)
    # 将分离后的帧ID与数据信息、LECU总数送入frame_handler()获取报文功能代码、操作的LECU对象编号及解析后的数据信息

    if func == 0 or func == 1 or func == 2:
        lecu_list[lecu_order]['Voltage'][func * 4:func * 4 + 4] = lecu_parsed_data
        # 根据LECU协议，当功能代码为0、1、2，即功能基址为0x104、0x105、0x106时
        # 将解析后的数据信息写入LECU状态列表的对应LECU对象的电压状态数据中，完成对该LECU电压的更新
    elif func == 3:
        lecu_list[lecu_order]['Temperature'][0:4] = [i / 10 - 40 for i in lecu_parsed_data]
    elif func == 4:
        lecu_list[lecu_order]['Temperature'][4:6] = [i / 10 - 40 for i in lecu_parsed_data[0:2]]
        # 根据LECU协议，当功能代码为3、4，即功能基址为0x107、0x108时
        # 将解析后的数据信息写入LECU状态列表的对应LECU对象的温度状态数据中，完成对该LECU温度的更新

    return lecu_list
    # 返回更新后的LECU状态列表


def web_index_generator(lecu_num, lecu_list):
    """生成LECU状态监控Web静态网页"""
    index_headers = '''<!DOCTYPE html>
<html lang="en" >
<head>
<meta charset="UTF-8" http-equiv="refresh" content="30">
<title>LECU Status Monitor</title>

<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.10.2/css/all.min.css'>
<link rel="stylesheet" href="css/style.css">

</head>
'''

    index_body = '''<body>
<div class="headers">
<h2>LECU Status Monitor</h2>
<div>Powered by breadli428</div>
</div>
    '''

    for i in range(lecu_num):
        index_body_sub = '''
<div class="reviews-container">
    <h2>LECU lecu_num_replace</h2>
    <div class="review">
        <span class="icon-container">Vol 01 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 1 data_done"></div>
        </div>
        <span class="percent">Voltage 1 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 02 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 2 data_done"></div>
        </div>
        <span class="percent">Voltage 2 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 03 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 3 data_done"></div>
        </div>
        <span class="percent">Voltage 3 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 04 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 4 data_done"></div>
        </div>
        <span class="percent">Voltage 4 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 05 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 5 data_done"></div>
        </div>
        <span class="percent">Voltage 5 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 06 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 6 data_done"></div>
        </div>
        <span class="percent">Voltage 6 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 07 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 7 data_done"></div>
        </div>
        <span class="percent">Voltage 7 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 08 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 8 data_done"></div>
        </div>
        <span class="percent">Voltage 8 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 09 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 9 data_done"></div>
        </div>
        <span class="percent">Voltage 9 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 10 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 10 data_done"></div>
        </div>
        <span class="percent">Voltage 10 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 11 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 11 data_done"></div>
        </div>
        <span class="percent">Voltage 11 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Vol 12 <i class="fas fa-bolt"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Voltage 12 data_done"></div>
        </div>
        <span class="percent">Voltage 12 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Tmp 1 <i class="fas fa-thermometer-half"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Temperature 1 data_done"></div>
        </div>
        <span class="percent">Temperature 1 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Tmp 2 <i class="fas fa-thermometer-half"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Temperature 2 data_done"></div>
        </div>
        <span class="percent">Temperature 2 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Tmp 3 <i class="fas fa-thermometer-half"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Temperature 3 data_done"></div>
        </div>
        <span class="percent">Temperature 3 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Tmp 4 <i class="fas fa-thermometer-half"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Temperature 4 data_done"></div>
        </div>
        <span class="percent">Temperature 4 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Tmp 5 <i class="fas fa-thermometer-half"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Temperature 5 data_done"></div>
        </div>
        <span class="percent">Temperature 5 data</span>
    </div>
    <div class="review">
        <span class="icon-container">Tmp 6 <i class="fas fa-thermometer-half"></i></span>
        <div class="progress">
            <div class="progress-done" data-done="Temperature 6 data_done"></div>
        </div>
        <span class="percent">Temperature 6 data</span>
    </div>
</div>
'''
        index_body_sub = index_body_sub.replace("lecu_num_replace", '%d' % i)
        for j in range(12):
            index_body_sub = index_body_sub.replace("Voltage %d data_done" % (j + 1),
                                                    '%d' % (lecu_list[i]['Voltage'][j] / 32767 * 100))
            index_body_sub = index_body_sub.replace("Voltage %d data" % (j + 1), '%d mV' % lecu_list[i]['Voltage'][j])
        for k in range(6):
            index_body_sub = index_body_sub.replace("Temperature %d data_done" % (k + 1),
                                                    '%d' % (lecu_list[i]['Temperature'][k] / 190 * 100))
            index_body_sub = index_body_sub.replace("Temperature %d data" % (k + 1),
                                                    '%d &#8451' % lecu_list[i]['Temperature'][k])
        index_body = index_body + index_body_sub

    index_end = '''<script  src="js/script.js"></script>

<div style="text-align:center;clear:both;">
<script src="/gg_bd_ad_720x90.js" type="text/javascript"></script>
<script src="/follow.js" type="text/javascript"></script>
</div>

</body>
</html>'''

    index_content = index_headers + index_body + index_end
    file = open('./html/webpage/index.html', 'w')
    file.write(index_content)
    file.close()
