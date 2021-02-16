from application import lecu_list_operation
import json

LECU_NUM = 5

frame_id = 0x138
frame_data = 'A1 00 B2 00 91 00 81 00'

# read lecu_list from json file
file = open('./html/saveddata/lecu_list.json', 'r')
lecu_list = json.load(file)
file.close()
print(lecu_list)

# initiate lecu_list
# lecu_list = [{'Voltage': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 'Temperature': [0, 0, 0, 0, 0, 0]} for i in range(LECU_NUM)]

# save lecu_list into json file
lecu_list = lecu_list_operation.list_generator(frame_id, frame_data, LECU_NUM, lecu_list)
file = open('./html/saveddata/lecu_list.json', 'w')
json.dump(lecu_list, file)
file.close()
print(lecu_list)

lecu_list_operation.web_index_generator(LECU_NUM, lecu_list)
