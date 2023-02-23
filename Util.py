import json
# read json from file


def read_from_file(file_name):
    with open(file_name, "r") as f:
        data = json.load(f)
        return data


def make_questions(title, apis):
    target = title
    messages = list(map(
        lambda api: f"I'm a beginner of {target}, {'I already know that ' + api[1] + ', ' if api[1] != '' else ''}and I want to learn to use the api {api[0]} of {target}. Don't say extra words like conclustion, all I need is 1.the short descripsion of usage of {api[0]} and 2.an example code of {api[0]} in basic situation, and 3.is there any other api has relationships with {api[0]}, tell me the relationship.", apis))
    # print(messages)
    print(len(messages))
    return messages
