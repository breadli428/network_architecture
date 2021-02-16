from application import lecu_list_operation
import json

LECU_NUM = 32
# initiate lecu_list when value changes


def data_operation(request_data_hex):
    frame_id, frame_data = id_data_identifier(request_data_hex)

    # read lecu_list from json file
    file = open('./html/saveddata/lecu_list.json', 'r')
    lecu_list = json.load(file)
    file.close()
    print(lecu_list)

    # save lecu_list into json file
    lecu_list = lecu_list_operation.list_updater(frame_id, frame_data, LECU_NUM, lecu_list)
    file = open('./html/saveddata/lecu_list.json', 'w')
    json.dump(lecu_list, file)
    file.close()
    print(lecu_list)

    lecu_list_operation.web_index_generator(LECU_NUM, lecu_list)


def id_data_identifier(request_data_hex):
    if len(request_data_hex) == 20:
        frame_id = int(request_data_hex[0:4], 16)
        frame_data = request_data_hex[4:]
    elif len(request_data_hex) == 24:
        frame_id = int(request_data_hex[0:8], 16)
        frame_data = request_data_hex[8:]
    return frame_id, frame_data
