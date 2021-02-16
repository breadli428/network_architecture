import re


def id_handler(frame_id, lecu_num):
    """获取报文功能代码及操作的LECU对象编号"""
    base_address = [0x104, 0x105, 0x106, 0x107, 0x108]
    # LECU电压、温度CAN ID功能基址
    id_address = [[0 for i in range(lecu_num)] for j in range(len(base_address))]
    # 初始化“功能—LECU矩阵”
    for i in range(len(base_address)):
        for j in range(lecu_num):
            id_address[i][j] = base_address[i] + 16 * j
    # 针对任一LECU的任一功能，其ID号均是唯一的
    # 对“功能—LECU矩阵”所有元素赋对应ID值
    func = -1
    # 初始化功能代码
    lecu_order = -1
    # 初始化LECU编号
    for i in range(len(base_address)):
        for j in range(lecu_num):
            if frame_id == id_address[i][j]:
                func = i
                lecu_order = j
                break
    # 在“功能—LECU矩阵”中进行寻址操作，确定CAN报文ID号所要执行的功能代码和指定的操作对象编号
    return func, lecu_order
    # 返回报文功能代码及操作的LECU对象编号


def data_handler(frame_data):
    """获取报文解析后的数据信息"""
    pattern = re.compile(r'\w{2}')
    # 利用正则表达式编译匹配对象规则
    frame_data_hex = pattern.findall(frame_data)
    # 在分离后的帧数据信息中找到16进制字符，共8个元素，生成列表
    frame_data_hex_combined = [0 for i in range(4)]
    # 初始化16进制组合列表，共4个元素
    lecu_parsed_data = [0 for i in range(4)]
    # 初始化解析后的10进制组合列表，共4个元素
    for i in range(4):
        frame_data_hex_combined[i] = frame_data_hex[2 * i + 1] + frame_data_hex[2 * i]
        # 根据LECU协议，将帧数据信息的bit15-bit0、bit31-bit16、bit47-bit32、bit63-bit48组合
        lecu_parsed_data[i] = int(frame_data_hex_combined[i], 16)
        # 将组合后的数据转换为10进制
        if lecu_parsed_data[i] > 32767:
            print("Warning!!!")
        # 判断数据范围，做出报警提示
    return lecu_parsed_data
    # 返回解析后的数据信息


def frame_handler(frame_id, frame_data, lecu_num):
    """获取报文功能代码、操作的LECU对象编号及解析后的数据信息"""
    func, lecu_order = id_handler(frame_id, lecu_num)
    # 获取报文功能代码及操作的LECU对象编号
    parsed_data = data_handler(frame_data)
    # 获取解析后的数据信息
    return func, lecu_order, parsed_data
    # 返回报文功能代码、操作的LECU对象编号及解析后的数据信息
