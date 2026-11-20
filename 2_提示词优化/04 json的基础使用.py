import json
q={
    "name":"小明",
    "age":18,
    "like":"basketboll"
}
s=json.dumps(q,ensure_ascii=False)          #转化为json字符串,json字符串强制识别双引号,可以把字典转化为字符串
print(s)


q1=json.loads(s)                            #把python字符串通过json.loads转化为字典或列表
print(q1)
q2=json.loads(s)
print(q2)