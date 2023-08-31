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
                "Cookies": "" #put your cookies in it
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

