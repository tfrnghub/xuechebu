import requests
import http.cookiejar
import json
import time
import datetime
import hashlib
import sys,getopt
import argparse


def read_cookies():
    try:
        f=open("cookies","r")
    except FileNotFoundError:
        f=open("cookies","w")
        f.write("{}")
        f.close()
        return {}
    else:
        ret=json.load(f)
        f.close()
        return ret


def update_cookies(cookies):
    f=open("cookies","w")
    f.write(json.dumps(cookies))
    f.close()  


def main():
    s=requests.session()
    cookies=read_cookies()
    callback="tfrnghub"
    os="pc"
    
    params={
    "username":username,
    "passwordmd5":passwordmd5,
    "callback":callback,
    "os":os}
    while True:
        try:
            r = s.get('https://api.xuechebu.com/usercenter/userinfo/login',params=params)
            if r.status_code==200:
                print(json.loads(r.text)["message"])
                if "账号或密码错误" in json.loads(r.text)["message"]:
                    return 1
                if "账号还未注册" in json.loads(r.text)["message"]:
                    return 1
                break
            else:
                print("再次请求页面")
                continue
        except KeyboardInterrupt:
            return 1
        except:
            print("再次请求页面")
            continue
    for c in s.cookies:
        cookies.update({c.name: c.value})
    XXZH=json.loads(r.text)["data"]["XXZH"]
    XYBH=json.loads(r.text)["data"]["XYBH"]
    JGID=json.loads(r.text)["data"]["JGID"]

    s=requests.session()
    params={
    "xybh":XYBH,
    "password":password,
    "jgid":JGID,
    "callback":callback,
    "os":os}
    headers={
    'Host': 'longquanapi.xuechebu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.xuechebu.com/sign.html',
    'Connection': 'keep-alive'}
    while True:
        try:
            r = s.get('http://longquanapi.xuechebu.com/Student/setbadingstuinfo',params=params,headers=headers,cookies=cookies)
            if r.status_code==200:
                print("成功获取cookies!!")
                break
            else:
                print("再次请求页面")
                continue
        except KeyboardInterrupt:
            return 1
        except:
            print("再次请求页面")
            continue

    for c in s.cookies:
        cookies.update({c.name: c.value})
    update_cookies(cookies)
    
    s=requests.session()  
    params={
    "callback":callback,
    "os":os,
    "cnbh":CNBH,
    "xxzh":XXZH,
    "params":CNBH+"."+Yyrq+"."+Xnsd+".",
    "isJcsdYyMode":1} 
    headers={
    'Host': 'longquanapi.xuechebu.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://www.xuechebu.com/yueche.html',
    'Connection': 'keep-alive'}
    while True:
        try:
            r2 = s.get('http://longquanapi.xuechebu.com/KM2/ClYyAddByMutil',params=params,headers=headers,cookies=cookies)
            if r2.status_code==200:
                print(json.loads(r2.text)["message"].strip())
                if "身份认证失败,请重新登录" in json.loads(r2.text)["message"]:
                    return 0
                elif "该时段已被别人预约,请刷" in json.loads(r2.text)["message"]:
                    time.sleep(60)
                    continue
                elif "您不能预约该时间的车辆" in json.loads(r2.text)["message"]:
                    print("waite!")
                    time.sleep(0.7)
                    continue
                elif "该科目训练每天最多能预" in json.loads(r2.text)["message"]:
                    return 1
                elif "不可预约已过期的时段" in json.loads(r2.text)["message"]:
                    return 1
                elif "访问太过频繁,请输入验证" in json.loads(r2.text)["message"]:
                    return 0
                elif "未查到该车辆" in json.loads(r2.text)["message"]:
                    print("教练ID错误")
                    return 1
                elif "请预约对应科目的车!" in json.loads(r2.text)["message"]:
                    print("该时段不可预约")
                    return 1
                elif "您该科目的训练小时将超出学时数!请核对" in json.loads(r2.text)["message"]:
                    return 1
                elif "预约失败,您该科目训练已预约完成" in json.loads(r2.text)["message"]:
                    return 1
                else:
                    return 1
            else:
                continue
        except KeyboardInterrupt:
            return 1
        except Exception as e:
            print(e)
            continue
            
    
    
if __name__ == '__main__':
    parser=argparse.ArgumentParser(description='学车不平台科目二预约训练脚本')
    parser.add_argument("-v","--version",action="store_true",default=False,help="show version information")
    options = parser.add_argument_group('options')
    options.add_argument("-u",dest="username",help="用户名")
    options.add_argument("-p",dest="password",help="密码")
    options.add_argument("-i",dest="ID",help="教练ID")
    options.add_argument("-d",dest="day",help="预约日期, 例如 1990-1-1")
    options.add_argument("-t",dest="time",help="预约时段, 1代表8:00-12:00, 2代表13:00-17:00, 3代表17:00-20:00",type=int)
    args = parser.parse_args()
    if args.version:
        print('xuechebu version 1.1.0')
        sys.exit(0)
    if args.username:
        username=args.username
    else:
        print('error: the following arguments are required: -u')
        sys.exit(0)
    if args.password:
        password=args.password
    else:
        print('error: the following arguments are required: -p')
        sys.exit(0)
    if args.ID:
        CNBH=args.ID
    else:
        print('error: the following arguments are required: -i')
        sys.exit(0)
    if args.time:
        if args.time == 1:
            Xnsd="812"
        elif args.time == 2:
            Xnsd="15"
        elif args.time == 3:
            Xnsd="58"
        else:
            print('error: the value of TIME must be 1,2,3')
            sys.exit(0)
    else:
        print('error: the following arguments are required: -t')
        sys.exit(0)
    
    
    
    m=hashlib.md5()
    m.update(password.encode(encoding='utf-8'))
    passwordmd5=m.hexdigest()
    
    
    now=datetime.datetime.now()
    print(now.strftime("现在时间:%Y-%m-%d %H:%M:%S"))
    nsec=int(time.mktime(now.timetuple()))
    hour=int(now.strftime("%H"))

    if args.day:
        Yyrq=args.day       
    else:
        if hour<7:
            future=now+datetime.timedelta(days=6)
        else:
            future=now+datetime.timedelta(days=7)
        Yyrq=future.strftime("%Y-%m-%d")
    ftime=Yyrq+' 7:00:00'
    if args.time == 1:
        print("预约时间:"+Yyrq+" 8:00-12:00")
    elif args.time == 2:
        print("预约时间:"+Yyrq+" 13:00-17:00")
    elif args.time == 3:
        print("预约时间:"+Yyrq+" 17:00-20:00")
    fsec=int(time.mktime(time.strptime(ftime,'%Y-%m-%d %H:%M:%S')))
    wait_sec=fsec-nsec-518415
    if(wait_sec>0):
        print("预约时间未到,"+str(wait_sec)+"秒后开始预约")
        time.sleep(wait_sec)  
    while True:
        a=main()
        if a==1:
            break
