#!/usr/bin/env python3

import json
import requests

def request(method,url,rData):
    headers = {
        'headerMap': '{"appId":"com.pingan.zhiniao","nonce":"4735a4998fb218a4761ac15caec9b102","sign":"3548b209acaaf30abbf616341d60a373","timestamp":1593572889912,"appDevicePlatform":"99"}',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'nonGzip': '1',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'http://www.zhi-niao.com',
        'Connection': 'close',
        'Cookie' : rData['Cookie']
    }

    if method == 'get':
        r = requests.get(url,headers=headers)
    elif method == 'post':
        r = requests.post(url,headers=headers,data=rData['postdata'])

    return r.text

def getCoursesList(rData):
    # 必修required=1 选修required=0
    url = 'http://www.zhi-niao.com/learn/app/clientapi/course/myCoursesList.do?required=1&sortType=1&curPage=1&numPerPage=30&strOs=99&cateId=SY0002148&sid='+ rData['sid'] +'&os=99'
    cl = json.loads(request('get',url,rData))
    print (cl)
    courseData = cl['body']['courseArr']
    print(courseData)
    courseIdList = dict()
    for item in courseData:
        if item['learningProgress'] == 0:
            courseIdList[item['courseId']] = item['courseName']

    print(courseIdList)
    return courseIdList

def queryCourseDetail(rData,courseId):
    url = 'http://www.zhi-niao.com/learn/app/clientapi/course/queryCourseDetail.do?os=99'
    rData['postdata'] = 'courseId='+courseId+'&ver=3.8.2&sid='+rData['sid']

    cd = json.loads(request('post',url,rData))
    courseDetailData = cd['body']['courseFileArr']
    coursewareIdList = dict()
    for item in courseDetailData:
        coursewareIdList[item['coursewareId']] = item['fileName']
    return coursewareIdList

def uploadLearnFlag(rData,coursewareId):
    url = 'http://www.zhi-niao.com/learn/app/clientapi/course/uploadLearnFlag.do?os=99'
    rData['postdata'] = 'courseId='+coursewareId+'&sid='+rData['sid']

    checkInfo = json.loads(request('post',url,rData))
    if checkInfo['code'] == 0:
        print('[-] secuess!!!')

def main():
    rData = {
        'sid': '5F8762A079FB4BCFA9A18977E2EA8981',
        "Cookie": "Hm_lvt_80e714466be8b29412a73567cc4dee53=1611833682,1614161611; BIGipServerhrmsv3-mlearning_DMZ_CLOUD_PrdPool_HIPPO=1462704556.8073.0000"

    }
    coursesList = getCoursesList(rData)
    for item in coursesList.keys():
        print('====start {coursesList[item]} collange====')
        courseDetailData = queryCourseDetail(rData,item)
        for item in courseDetailData.keys():
            print('[+] running {courseDetailData[item]}')
            uploadLearnFlag(rData,item)
            pass


if __name__ == '__main__':

    main()