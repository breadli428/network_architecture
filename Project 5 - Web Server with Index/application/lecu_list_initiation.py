import json


def lecu_list_initiation(lecu_num):
    lecu_list = [{'Voltage': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Temperature': [0, 0, 0, 0, 0, 0]} for i in
                 range(lecu_num)]

    file = open('./html/saveddata/lecu_list.json', 'w')
    json.dump(lecu_list, file)
    file.close()
    print(lecu_list)
