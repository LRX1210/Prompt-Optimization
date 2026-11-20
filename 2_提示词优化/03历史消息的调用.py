from openai import OpenAI
#1,  获取client对象，openai类对象
client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key="{密钥}",
    #！！！保护安全，在环境变量设置后，api_key可有可无。
    base_url="{ai接口的地址}"
    #平台地址
)

# 2.  调用模型
e=[
    {"role":"system","content":"你是一个AI助理，回答很简洁"},
    {"role":"user","content":"小明有5条宠物狗"},
    {"role":"assistant","content":"好的"},
    {"role":"user","content":"小红有4条宠物狗"},
    {"role":"assistant","content":"好的"},
    {"role":"user","content":"总共有多少只宠物"}
]
response=client.chat.completions.create(
    model="qwen3.7-max",
    messages=e,
    stream=True      #开启流式输出的功能
)
# 3. 处理结束
for chuck in response:
    if not chuck.choices:
        continue
    shuc=chuck.choices[0].delta.content
    if not shuc:
        continue
    print(
        shuc,
        end=" ",  # 分隔
        flush=True  # 立刻刷新缓冲区
    )