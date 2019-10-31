#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:28:37 2019

@author: chy
"""
import requests
import json
import base64
import os
import logging
import speech_recognition as sr
import numpy as np
import re

def get_token():
    logging.info('开始获取token...')
    #获取token
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    client_id = "sdv8f6ZP6d2rCUjArNwU4TpY"
                 
    client_secret = "kY2Mcbl4rEQW69AEgZ5Ygucgi9CkeKMC"
                     
    #拼url
    url = f"{baidu_server}grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    print (token)
    return token


def audio_baidu(filename):
    logging.info('开始识别语音文件...')
    with open(filename, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
#        speech = base64.b64encode(f.read())
    size = os.path.getsize(filename)
    token = get_token()
    headers = {'Content-Type': 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": "wav",
        "rate": "16000",
        "dev_pid": "1737",
        "speech": speech,
        "cuid": "TEDxPY",
        "len": size,
        "channel": 1,
        "token": token,
    }

    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)

    if result["err_msg"] == "success.":
        print(result['result'])
        
        s1=result['result']
        string = s1
        num = []
        for i in string:
            r = re.findall(r"\d+\.?\d*",i)
            num.append(int(r[0]))
        #print(num)#得到字符串[123]
        list2=[str(i) for i in num]
        #print(list2)#['123']
        list3=' '.join(list2)
        #print (list3)#123
        results = list(map(int,list3))
        a = np.array(results)
        #print (a)#[1 2 3]
        s2 = tuple(a)
#        print(s2)#(1,2,3)
        
#        print (re.findall(r"\d",result['result'])
#        f = open('/home/chy/log.txt','w')
#        print(result['result'],file=f)
        
       
#        file = open('log.txt')
#        content = file.read()
#        s = [i for i in content if str.isdigit(i)]
#        s2 = ''.join(s)
#        print(s2)
        return s2
    else:
        print("内容获取失败，退出语音识别")
        return ""

#if __name__ == "__main__":
#    logging.basicConfig(level=logging.INFO)

wav_num=0
r = sr.Recognizer()
        #启用麦克风
mic = sr.Microphone()
print ('录音中...')
with mic as source:
            #降噪
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
#        with open(f"00{wav_num}.wav", "wb") as f:
with open(f"00{wav_num}.wav", "wb") as f:
            #将麦克风录到的声音保存为wav文件
    f.write(audio.get_wav_data(convert_rate=16000))
print('录音结束，识别中...')
s3 = audio_baidu(f"00{wav_num}.wav")
print(s3)

wav_num += 1       
#            with open(f"00{wav_num}.txt", "a") as f:
#            #将麦克风录到的声音保存为wav文件
#            f.write(target[0],file=f)
            
            
#    if s3[0].find("退出") !=-1:
#        break
#        if target == -1:
#            break        

        