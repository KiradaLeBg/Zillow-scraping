import requests as r
import json
import csv
from csv import DictWriter
import time


def extract_info(key,subkey):
    request = r.get(url, headers=headers_dict)
    data = request.json()
    info = [review[key][subkey] for review in data["reviews"]]
    return info

def extract_from_one_key(key):
    request = r.get(url, headers=headers_dict)
    data = request.json()
    info = [review[key] for review in data["reviews"]]
    return info


fieldnames = ["name", "comment", "agent_name", "rating", "date", "work_description"]

page = 1
with open("reviews.csv", "a", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        while page < 180:

            url = f"https://www.zillow.com/profile-page/api/public/v1/reviews?encodedZuid=X1-ZUytm150b2rcax_3s95i&profileTypeIds=1%2C2%2C15&page={page}&size=5&sortType=2&sortOrder=2"

            headers_dict = {
                "authority": "www.zillow.com",
                "method": "GET",
                "path": f"/profile-page/api/public/v1/reviews?encodedZuid=X1-ZUytm150b2rcax_3s95i&profileTypeIds=1%2C2%2C15&page={page}&size=5&sortType=2&sortOrder=2",
                "scheme": "https",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
                "Cookie": 'zguid=24|%24f1591818-52bc-4a53-94a7-9f99592e4e4e; zgsession=1|5f17edcd-5102-42ad-a554-b2d10ae49b47; _ga=GA1.2.230081960.1692742301; _gid=GA1.2.1850580423.1692742301; zjs_anonymous_id=%22f1591818-52bc-4a53-94a7-9f99592e4e4e%22; zjs_user_id=null; zg_anonymous_id=%22885a1a34-6842-449f-b6d6-7cc55d02d4d7%22; pxcts=deac6c3a-4138-11ee-99d5-725256664a6d; _pxvid=deac5f79-4138-11ee-99d5-2a951ee76d22; _gcl_au=1.1.1820630681.1692742303; DoubleClickSession=true; __pdst=e6fc5632033648f0a0c0db007955b1cf; _pin_unauth=dWlkPU1XWmtaREF4TmpndFpEVXdZeTAwTURVeExUazBNelV0T0RGaE56YzBaRFUxT0RZdw; _cs_c=0; _cs_id=ae7af619-34b9-ad38-d090-049ef2c5189d.1692743862.1.1692744962.1692743862.1.1726907862113; _hp2_id.1215457233=%7B%22userId%22%3A%224706356599956019%22%2C%22pageviewId%22%3A%223455215414593314%22%2C%22sessionId%22%3A%223383122088758164%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _clck=1qfwkbg|2|fef|0|1329; JSESSIONID=4340CC305AC63EAEFB136BA7B2E8A91C; _pxff_cc=U2FtZVNpdGU9TGF4Ow==; _pxff_cfp=1; _pxff_bsco=1; _gat=1; AWSALB=t7hIY4FRbcw+3emCK8YS2izDdiW/1PpoY1YkjzuUJVOkqINbb8F+C3NVtjdnzA4oG0T4ja9xlwoA/xAMxRdsJSQ1SHAP1Da3knJRwNuq1EGcc67Z2LgqpRbe2AtK; AWSALBCORS=t7hIY4FRbcw+3emCK8YS2izDdiW/1PpoY1YkjzuUJVOkqINbb8F+C3NVtjdnzA4oG0T4ja9xlwoA/xAMxRdsJSQ1SHAP1Da3knJRwNuq1EGcc67Z2LgqpRbe2AtK; _px3=3e22598f06aa7219621e6a9c5b777b2884576c1e2d7f89e23a2fa22a8a8be5d3:vqFWq/JU/zcJRgxsDLfO/RmeSvQUm1+tYunaPDoAoiT6OcpvtCeoovYhP2pMMDjzRYavixcrIvXCl4FbvSyEow==:1000:noWyveDwxCXPHHIYSzKODod1BqPoyy0/l4e8NzHu0ia+XdJh6Q5DOlDB8cBksyCVX3KOIMelmw9tgB/ALjKwKWTEw1YxZcCDWI5xR/WZc2XkuW+MyGrkyw018XPody2J0aYbJmETqkdQGg+fJMD3MMBJMqWws/+09Ydy1kX2i14TrYqSmZgiP+ifO1f/Bn0rU3OhPi3/94FkybWVmJcsTQ==; _uetsid=e0573a50413811eea007b5615a300d63; _uetvid=e0576fe0413811eeacb257224e078a8a; _clsk=19ymyda|1692897102187|1|0|z.clarity.ms/collect; g_state={"i_p":1692904321280,"i_l":1}',
                "Referer": "https://www.zillow.com/profile/Stephanie-Younger-CA/",
                "Sec-Ch-Ua": "\"Chromium\";v=\"116\", \"Not)A;Brand\";v=\"24\", \"Google Chrome\";v=\"116\"",
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": "\"Windows\"",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
            }

            time.sleep(2)
            name  = extract_info("reviewer","screenName")
            comment = extract_from_one_key("reviewComment")
            agent_name = extract_info("reviewee", "lastName")
            rating = extract_from_one_key("rating")
            date = extract_from_one_key("createDate")
            work_description = extract_from_one_key("workDescription")
            page += 1   
            
            for i in range(5):
                instance = i
                data = [
                        {
                            "name": name[instance], "comment": comment[instance], "agent_name": agent_name[instance],
                            "rating": rating[instance], "date": date[instance], "work_description": work_description[instance]
                        }
                    ]
                writer.writerows(data)
            instance += 1

