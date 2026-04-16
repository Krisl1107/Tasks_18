import json

json_str = input("Enter a list of [string, number] pairs in JSON format: ")
json_form = json.loads(json_str)

sorted_lst = sorted(json_form, key=lambda x: x[1], reverse=True)

print(sorted_lst)
