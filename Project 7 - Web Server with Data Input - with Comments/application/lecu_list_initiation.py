import json
LECU_NUM = 32
# 设置LECU总数


def lecu_list_initiation(lecu_num):
    """初始化LECU状态列表,将初始化后的LECU状态列表写入lecu_list.json文件"""
    lecu_list = [{'Voltage': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Temperature': [0, 0, 0, 0, 0, 0]} for i in
                 range(lecu_num)]
    # 初始化LECU状态列表
    file = open('../html/saveddata/lecu_list.json', 'w')
    # 打开保存LECU状态列表的lecu_list.json文件
    json.dump(lecu_list, file)
    # 将初始化后的LECU状态列表写入lecu_list.json文件
    file.close()
    # 关闭文件
    print(lecu_list)
    # 打印LECU状态列表


def main():
    lecu_list_initiation(LECU_NUM)
    # 执行LECU状态列表初始化程序


if __name__ == '__main__':
    main()
    # 执行主函数
