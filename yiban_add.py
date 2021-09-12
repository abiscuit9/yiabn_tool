import requests, json
import time
url_org = "http://mp.yiban.cn/admin/org/org/index"
url_add= "http://mp.yiban.cn/admin/org/org/add"
data_org="{\"orgId\":\"2006178\"}"
headers = {
  'Cookie': '',
  'Content-Type': 'text/plain'
}
res_org = requests.request("POST", url_org, headers = headers, data = data_org)
list_org = json.loads(res_org.text).get('data')
time.sleep(2)
for org in list_org:
    id_org = org.get('id')
    name_org = org.get('name')
    data_2015 = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"2015级\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "2015级学生" + "\"}"
    data_2016 = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"2016级\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "2016级学生" + "\"}"
    data_2017 = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"2017级\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "2017级学生" + "\"}"
    data_2018 = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"2018级\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "2018级学生" + "\"}"
    data_2019 = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"2019级\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "2019级学生" + "\"}"
    data_2020 = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"2020级\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "2020级学生" + "\"}"
    data_2021 = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"2021级\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "2021级学生" + "\"}"
    data_tec = "{\"fOrgId\":\"" + id_org + "\",\"name\":\"易班发展中心\",\"kind\":\"5\",\"description\":\"" + "中国矿业大学" + name_org + "易班发展中心" + "\"}"
    if name_org == "xxxx学院":
        res_add = requests.request("POST", url_add, headers = headers, data = data_2015.encode("utf-8").decode("latin1"))
        print(name_org + "2015" + "\n" + res_add.text)
        time.sleep(2)
        res_add = requests.request("POST", url_add, headers = headers, data = data_2016.encode("utf-8").decode("latin1"))
        print(name_org + "2016" + "\n" + res_add.text)
        time.sleep(2)
        res_add = requests.request("POST", url_add, headers = headers, data = data_2017.encode("utf-8").decode("latin1"))
        print(name_org + "2017" + "\n" + res_add.text)
        time.sleep(2)
        res_add = requests.request("POST", url_add, headers = headers, data = data_2018.encode("utf-8").decode("latin1"))
        print(name_org + "2018" + "\n" + res_add.text)
        time.sleep(2)
        res_add = requests.request("POST", url_add, headers = headers, data = data_2019.encode("utf-8").decode("latin1"))
        print(name_org + "2019" + "\n" + res_add.text)
        time.sleep(2)
        res_add = requests.request("POST", url_add, headers = headers, data = data_2020.encode("utf-8").decode("latin1"))
        print(name_org + "2020" + "\n" + res_add.text)
        time.sleep(2)
        res_add = requests.request("POST", url_add, headers = headers, data = data_2021.encode("utf-8").decode("latin1"))
        print(name_org + "2021" + "\n" + res_add.text)
        time.sleep(2)
        res_add = requests.request("POST", url_add, headers = headers, data = data_tec.encode("utf-8").decode("latin1"))
        print(name_org + "易班" + "\n" + res_add.text)
        time.sleep(2)