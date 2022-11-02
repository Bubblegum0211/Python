'''8-9
def show_messages(txts):
    for txt in txts:
        print(txt)
txts=['a','b','c','d']
show_messages(txts)
'''

'''8-10
def show_messages(txts):
    for txt in txts:
        print(txt)
def send_messages(sent_messages):
    for txt in txts:
        sent_messages.append(txt)
    print(sent_messages)
txts=['a','b','c','d']
sent_messages=[]
show_messages(txts)
send_messages(sent_messages)
'''

#8-11
def show_messages(txts):
    for txt in txts:
        print(txt)
def send_messages(sent_messages):
    sent_messages1 = sent_messages[:]
    for txt in txts:
        sent_messages1.append(txt)
    print(sent_messages)
    print(sent_messages1)
txts=['a','b','c','d']
sent_messages=[]
show_messages(txts)
send_messages(sent_messages)