import requests
import time
from bs4 import BeautifulSoup as BS
from homework_modify import Homework_modify

def down_load(url_base:str,save_path:str):
    resp = requests.get(url_base)

    soup = BS(resp.text, "lxml")


    down_list = soup.find_all(lambda tag: tag.name== "a" and tag.get("download")=="")
    if len(down_list) == 0 :
        return False
    down_list_final = {}
    for i in range(len(down_list)):
        name = down_list[i]["href"].split("/")[3]
        name_modified = name[33:]
        down_list_final[name_modified] = "https://ocw.mit.edu"+down_list[i]["href"]



    for name in down_list_final.keys():
        r = requests.get(down_list_final[name])
        with open(save_path+"/"+name,'wb') as f:  # pdf的保存路径
            f.write(r.content)
        r.close()
        print("Downloading file " + name)
        
        time.sleep(0.5)
        
    if "assignments" in url_base:
        Homework_modify(save_path)
    if "recitations" in url_base:
        Homework_modify(save_path)
        
    return True