#!/usr/bin/env python
# _*_ coding: utf-8 _*_

import urllib2
import time
import json

'''
转转发条熊活动-自动刷金币脚本
只需在main()里添加自己的unionID即可，可配合crontab实现每天自动刷币
功能描述:
    自动签到
    自动抚摸
    自动喂食
    自动分享微信
    自动领取金币

DATE:2016-11-02
Author:guoshijie
'''

def printLog(obj,flag=1):
    print  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\t" + str(obj) + "\t" + "flag=" + str(flag)
def getUrl(taskType,unionID,flag):
    prefix = "http://59.110.43.122/interface/public/index.php?s=/index/action/doTask&taskType=" + str(taskType) + "&unionID=" + str(unionID)
    prefix2 = "http://59.110.43.122/interface/public/index.php?s=/index/action/getCoin&taskType=" + str(taskType) + "&unionID=" + str(unionID)
    now = int(time.time())
    old = now - 135911
    url = prefix + "&_=" + str(now) + "&_callback=Zepto" + str(old)
    url2 = prefix2 + "&_=" + str(now) + "&_callback=Zepto" + str(old)
    if flag == 1:
        return url
    else:
        return url2

def getJson(result):
    begin = result.find('(') + 1
    end = result.find(')')
    obj = json.loads(result[begin:end])
    return obj

def send(taskType,unionID,flag):
    req = urllib2.Request(getUrl(taskType,unionID,flag))
    res_data = urllib2.urlopen(req)
    res = res_data.read()
    obj = getJson(res)
    printLog(obj,flag)
    return obj

def addCoin(times,taskType,unionID,flag):
    printLog("leftTimes=" + str(times),flag)
    for x in range(times):
        obj = send(taskType,unionID,flag)
        if isSuccess(obj):
            continue
        else:
            break
        time.sleep(1)

def isSuccess(obj):
    code = obj["code"]
    msg = obj["msg"]

    if code == 0 and msg == "success":
        return True
    else:
        return False

def execute(taskType,unionID,flag):
    obj = send(taskType,unionID,flag)
    if isSuccess(obj):
        if flag == 1:
            leftTimes = obj["data"]["leftTimes"]
            addCoin(leftTimes,taskType,unionID,flag)
        else:
            printLog("getCoin success!",flag)
    else:
        printLog("Please wait a minute...",flag)

def main():
    userList = ['of-R3jqYibckWS2YeDkWEW5s6rkM', 'of-R3jtHeVuENCM4ehqsB4UurnMs']
    for unionID in userList:
        execute(0,unionID,1)
        execute(1,unionID,1)
        execute(2,unionID,1)
        execute(4,unionID,1)
        execute(4,unionID,2)

if __name__=='__main__':
    main()
