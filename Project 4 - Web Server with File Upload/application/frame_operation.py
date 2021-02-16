import re


def id_handler(frame_id, lecu_num):
    base_address = [0x104, 0x105, 0x106, 0x107, 0x108]
    id_address = [[0 for i in range(lecu_num)] for j in range(len(base_address))]
    for i in range(len(base_address)):
        for j in range(lecu_num):
            id_address[i][j] = base_address[i] + 16 * j

    func = -1
    lecu_order = -1
    for i in range(len(base_address)):
        for j in range(lecu_num):
            if frame_id == id_address[i][j]:
                func = i
                lecu_order = j
                break
    return func, lecu_order


def data_handler(frame_data):
    pattern = re.compile(r'\w{2}')
    frame_data_hex = pattern.findall(frame_data)
    frame_data_hex_combined = [0 for i in range(4)]
    lecu_parsed_data = [0 for i in range(4)]
    for i in range(4):
        frame_data_hex_combined[i] = frame_data_hex[2 * i + 1] + frame_data_hex[2 * i]
        lecu_parsed_data[i] = int(frame_data_hex_combined[i], 16)
        if lecu_parsed_data[i] > 32767:
            print("Warning!!!")
    return lecu_parsed_data


def frame_handler(frame_id, frame_data, lecu_num):
    func, lecu_order = id_handler(frame_id, lecu_num)
    parsed_data = data_handler(frame_data)
    return func, lecu_order, parsed_data
