import requests, json
import time
url_org = "http://mp.yiban.cn/admin/org/org/index"
url_member= "http://mp.yiban.cn/admin/org/member/index"
url_delete = "http://mp.yiban.cn/admin/org/member/kill"
url_orgdel = "http://mp.yiban.cn/admin/org/org/delete"
data_org="{\"orgId\":\"2006178\"}"
headers = {
  'Cookie': '',
  'Content-Type': 'text/plain'
}
res_org = requests.request("POST", url_org, headers = headers, data = data_org)
list_org = json.loads(res_org.text).get('data')
for org in list_org:
    id_org = org.get('id')
    name_org = org.get('name')
    type_org = org.get("typeDesc")
    if type_org == '行政类':
        data_neworg = "{\"orgId\":\"" +  id_org + "\"}"
        time.sleep(1)
        res_neworg = requests.request("POST", url_org, headers = headers, data = data_neworg)
        print(res_neworg.text)
        list_neworg = json.loads(res_neworg.text).get('data')
        for org in list_neworg:
            id_org = org.get('id')
            name_neworg = org.get('name')
            data_member = "{\"page\":1,\"size\":20,\"orgId\":\"" + id_org + "\"}"
            time.sleep(1)
            print(data_member)
            res_member = requests.request("POST", url_member, headers = headers, data = data_member)
            print(res_member)
            num = json.loads(res_member.text).get("data").get("page").get("total")  
            print(num)    
            while num != 0:
                list_member = json.loads(res_member.text).get('data').get('list')
                id_member = None
                for member in list_member:
                    if id_member != None:
                        id_member = id_member + "\",\"" + member.get('userId')
                    else:
                        id_member = member.get('userId')
                data_delete = "{\"orgId\":\"" + id_org + "\",\"userId\":[\"" + id_member + "\"]}"
                time.sleep(1)
                res_delete = requests.request("POST", url_delete, headers = headers, data = data_delete)
                print(name_org + res_delete.text)
                time.sleep(1)
                res_member = requests.request("POST", url_member, headers = headers, data = data_member)
                num = json.loads(res_member.text).get("data").get("page").get("total")
            data_orgdel = "{\"orgId\":\"" + id_org + "\"}"
            time.sleep(1)
            res_orgdel = requests.request("POST", url_orgdel, headers = headers, data = data_orgdel)
            print(name_org+name_neworg+res_orgdel.text)
    else:
        print(0)
        data_member = "{\"page\":1,\"size\":20,\"orgId\":\"" + id_org + "\"}"
        time.sleep(1)
        res_member = requests.request("POST", url_member, headers = headers, data = data_member)
        num = json.loads(res_member.text).get("data").get("page").get("total")       
        while num != 0:
            list_member = json.loads(res_member.text).get('data').get('list')
            id_member = None
            for member in list_member:
                if id_member != None:
                    id_member = id_member + "\",\"" + member.get('userId')
                else:
                    id_member = member.get('userId')
            data_delete = "{\"orgId\":\"" + id_org + "\",\"userId\":[\"" + id_member + "\"]}"
            time.sleep(1)
            res_delete = requests.request("POST", url_delete, headers = headers, data = data_delete)
            print(name_org + res_delete.text)
            time.sleep(1)
            res_member = requests.request("POST", url_member, headers = headers, data = data_member)
            num = json.loads(res_member.text).get("data").get("page").get("total")
        data_orgdel = "{\"orgId\":\"" + id_org + "\"}"
        time.sleep(1)
        res_orgdel = requests.request("POST", url_orgdel, headers = headers, data = data_orgdel)
        print(name_org + res_orgdel.text)
