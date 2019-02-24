'''
Created on 2016年2月22日

@author: 15051125
'''
import threading
from suning.messagePush import messagePush
from suning.messagePush import message

    
if __name__ == "__main__":
    mess = message.Message()
    p=messagePush.WebSocketClient("ws://10.24.56.70:9527/websocket","6bac0d5a14c90c802a6640b54ed6a93d","7b7a3da90ddf5cbeff35df33ecd2957a","default1")
    p.connect()
    mess = p.onMessage()
    while mess != None:
        print(mess.getMessageId())
        mess = p.onMessage()
