from revChatGPT.V1 import Chatbot
from Util import *

# read config from file
myconfig = read_from_file('config.json')
print(myconfig)

# create chatbot
chatbot = Chatbot(config=myconfig)


# read history
conversations = chatbot.get_conversations(offset=0, limit=20)
# print("get_conversations: ", conversations)
for conversation in conversations:
    print(conversation)

history = chatbot.get_msg_history(
    "6f771f73-2f55-43fd-851d-ba389d6ea1e2")  # json.loads
print("get_msg_history: ", history)
msgs = history["mapping"]
for keys, values in msgs:
    print(keys, values)
    for k, v in values:
        if k == "role":
            print(v)
        if k == "id":
            print(v)
        if k == "content":
            print(v)


def traverse_json_loads(data):
    if isinstance(data, list):
        for item in data:
            traverse_json_loads(item)
    elif isinstance(data, dict):
        for key, value in data.items():
            if key == "content":
                print(value)
            traverse_json_loads(value)
    else:
        pass

# json.loads


def rooback(num):
    chatbot.rollback_conversation(num)


def MultilineInput(prompt):
    chatbot.get_intput(prompt)


def ask(prompt, conversation_id, parent_id):
    prev_text = ""
    for data in chatbot.ask(
        prompt,
        conversation_id=conversation_id,  # "6f771f73-2f55-43fd-851d-ba389d6ea1e2"
        parent_id=parent_id  # "1cf849ce-3376-4539-ae8d-993751ca65e2"
    ):
        pritn(data)
        message = data["message"][len(prev_text):]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print()
