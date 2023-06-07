import json


diff_list = ['services', 'staff', 'datetime']
with open('json_new.json', 'r') as file_json_new:
    roster_new = json.load(file_json_new)

with open('json_old.json', 'r') as file_json_old:
    roster_old = json.load(file_json_old)

result = {key: roster_new['data'][key] for key in diff_list if roster_new['data'][key] != roster_old['data'][key]}

print(result)
with open('result.json.', 'w') as file_result:
    json.dump(result, file_result, indent=4)
