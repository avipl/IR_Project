from . import bert_search, lucene_search
import requests
from bs4 import BeautifulSoup
import ast

class Search():
    def __init__(self, search_query, search_type, top_k):
        self.query = search_query
        self.type =  search_type
        self.top_k = top_k

#     def add_images(self,res_json):
#         movie_urls=[]
#         res_json_li=ast.literal_eval(res_json)
        
#         for i in res_json_li:
#             movie_urls.append("https://imdb.com/title/"+i["movie_id"])
        
#         headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        
#         ct=0
#         for i in movie_urls:
#             response=requests.get(i,headers=headers)
#             soup = BeautifulSoup(response.text, 'html.parser')
#             ilink=soup.find("a", {"class": "ipc-lockup-overlay ipc-focusable"})
#             n_url="https://www.imdb.com/"+ilink['href']
#             n_response=requests.get(n_url,headers=headers)
#             n_soup=BeautifulSoup(n_response.text, 'html.parser')
#             iid=n_url.split("/")[-2]+"-curr"
#             img=n_soup.find("img",{"data-image-id":iid})
#             try:
#                 res_json_li[ct]["image_url"]=img["src"]
#             except:
#                 img=n_soup.find("img",{"class":"ipc-image"})
#                 res_json_li[ct]["image_url"]=img["src"]
#             ct+=1
        
#         return res_json_li        

    def res_return(self):
        if self.type=="bert":
            res_json=ast.literal_eval(bert_search.bert_query(self.query, self.top_k))
            #final_json=self.add_images(res_json)
            return res_json
        else:
            res_json=ast.literal_eval(lucene_search.lucene_query(self.query, self.top_k))
            #final_json=self.add_images(res_json)
            return res_json