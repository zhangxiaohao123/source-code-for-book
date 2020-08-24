from django.test import TestCase

# Create your tests here.
import json

# person = {
#     'name': 'zhangsan',
#     'age':18,
# }
#
# # 一个Python数据结构转换为JSON 字符串
# json_str = json.dumps(person)
#
# print(json_str)
#==================
# str= '{"name":"Tom", "age":23}'
# dic =json.loads(str)
# print(type(dic))


#========================

# import json
# person = {
#     '姓名': '张三',
#     '年龄':18,
# }
# # 一个Python数据结构转换为JSON 字符串
# json_str1 = json.dumps(person)
# print(json_str1)
# json_str2 = json.dumps(person,ensure_ascii=False)
# print(json_str2)


# person = {
#     'name': 'zhangsan',
#     'age':18,
# }
#
# with open('person.txt','w') as f:
# 	json.dump(person,f)

with open('person.txt', 'r') as f:
    person = json.load(f)
print(person)
