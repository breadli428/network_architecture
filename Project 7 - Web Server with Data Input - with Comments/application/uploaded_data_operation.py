from application import lecu_list_operation
import json

LECU_NUM = 32
# 设置LECU总数
# 当LECU总数改变时，使用lecu_list_initiation()更新LECU状态列表


def data_operation(request_data_hex):
    """分离帧ID与数据信息并进行解析"""
    frame_id, frame_data = id_data_identifier(request_data_hex)
    # 获得分离后的帧ID与数据信息

    file = open('./html/saveddata/lecu_list.json', 'r')
    # 打开保存LECU状态列表的lecu_list.json文件
    lecu_list = json.load(file)
    # 加载lecu_list.json文件内容至LECU状态列表
    file.close()
    # 关闭文件
    print(lecu_list)
    # 打印LECU状态列表

    lecu_list = lecu_list_operation.list_updater(frame_id, frame_data, LECU_NUM, lecu_list)
    # 将分离后的帧ID与数据信息、LECU总数与读取的LECU状态列表送入list_updater()进行LECU状态列表更新
    file = open('./html/saveddata/lecu_list.json', 'w')
    # 打开保存LECU状态列表的lecu_list.json文件
    json.dump(lecu_list, file)
    # 将更新后的LECU状态列表写入lecu_list.json文件
    file.close()
    # 关闭文件
    print(lecu_list)
    # 打印LECU状态列表

    lecu_list_operation.web_index_generator(LECU_NUM, lecu_list)
    # 将LECU总数与更新后的LECU状态列表送入web_index_generator生成LECU状态监控Web静态网页


def id_data_identifier(request_data_hex):
    """分离帧ID与数据信息"""
    if len(request_data_hex) == 20:
        # 报文长度为20位（标准帧）时
        frame_id = int(request_data_hex[0:4], 16)
        # 帧ID为前4位，并进行16进制转换
        frame_data = request_data_hex[4:]
        # 帧数据信息为后16位
    elif len(request_data_hex) == 24:
        # 报文长度为24位（扩展帧）时
        frame_id = int(request_data_hex[0:8], 16)
        # 帧ID为前8位，并进行16进制转换
        frame_data = request_data_hex[8:]
        # 帧数据信息为后16位
    return frame_id, frame_data
    # 返回分离后的帧ID和数据信息
