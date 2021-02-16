from application import lecu_list_operation, lecu_list_initiation
import json

LECU_NUM = 10
# initiate lecu_list when value changes
# lecu_list_initiation.lecu_list_initiation(LECU_NUM)

frame_id = 0x138
frame_data = 'A1 00 B2 00 91 00 81 00'

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
