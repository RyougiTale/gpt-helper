# %%
from revChatGPT.V1 import Chatbot
from Util import *

# read config from file
myconfig = read_from_file('config.json')
print(myconfig)

# %%
# create chatbot
chatbot = Chatbot(config=myconfig)

# %%
# read history
conversations = chatbot.get_conversations(offset=0, limit=20)
# print("get_conversations: ", conversations)

# %%
import sys
print(sys.getdefaultencoding())
print(len(conversations))
for conversation in conversations:
    print(conversation['title'].encode(
        'raw_unicode_escape').decode() + '      ['+conversation['id']+']')


# %%
conversation_id = "6f771f73-2f55-43fd-851d-ba389d6ea1e2"

# %%
# read msg history
history = chatbot.get_msg_history(
    conversation_id)

# %%
import datetime
print(history["title"])
print(history["create_time"])
dt = datetime.datetime.fromtimestamp(history["create_time"])
print(dt)
print(history["moderation_results"])
print(history["current_node"])

# %%
chat_messages_array = []
# print(history)
for i, msg in enumerate(history["mapping"]):
    print(str(i+1) + " / " + str(len(history["mapping"])) + " :")
    print(history["mapping"][msg]["id"])
    print(history["mapping"][msg]["parent"])
    print(history["mapping"][msg]["children"])
    chat_messages = {}
    try:
        role = history["mapping"][msg]["message"]["author"]["role"]
        chat_messages[history["mapping"][msg]["id"]] = history["mapping"][msg]["message"]["content"]["parts"][0].encode('raw_unicode_escape').decode()
        chat_messages_array.append(chat_messages)
        print(chat_messages_array)
    except KeyError:
        print("Role does not exist for this message.")
    except TypeError:
        print("There is no message")


# %%
print(chat_messages_array)
for i, chat_messages in enumerate(chat_messages_array):
    print(str(i+1) + " / " + str(len(history["mapping"])) + " :")
    print(chat_messages)

# %%
# for idkey in history["mapping"]:
#     for keys, values in history["mapping"][idkey]:
#         print(keys, values)
#         for k, v in values:
#             if k == "role":
#                 print(v)
#             if k == "id":
#                 print(v)
#             if k == "content":
#                 print(v)

# %%
# last_message 
for key, value in chat_messages_array[-1].items():
    parent_id = key
print(parent_id)

# %%
def ask(prompt, conversation_id, parent_id):
    prev_text = ""
    for data in chatbot.ask(
        prompt,
        conversation_id=conversation_id,  # "6f771f73-2f55-43fd-851d-ba389d6ea1e2"
        parent_id=parent_id  # "1cf849ce-3376-4539-ae8d-993751ca65e2"
    ):
        print(data)
        message = data["message"][len(prev_text):]
        print(message, end="", flush=True)
        print("end?")
        prev_text = data["message"]
    print()


# %%
def ask_sync(prompt, conversation_id, parent_id):
    response = ""
    for data in chatbot.ask(
        prompt,
        conversation_id=conversation_id,  # "6f771f73-2f55-43fd-851d-ba389d6ea1e2"
        parent_id=parent_id  # "1cf849ce-3376-4539-ae8d-993751ca65e2"
    ):
        response = data["message"]
    print("response:")
    print(response)

# %%
ask_sync("write a python hello world", conversation_id, None)

# %%
def rollback(num):
    chatbot.rollback_conversation(num)


def MultilineInput(prompt):
    chatbot.get_intput(prompt)


# %%
len(messages)

# %%
for message in messages:
    ask_sync(message, conversation_id, None)

# %%



