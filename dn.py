import requests
import os
def download_image(content,number):
 try:
     
     os.mkdir(f"./{content}_images")
     url=f'https://pixabay.com/api/?key=37154513-ad4763ca10d238126989d13e1&q={content}&image_type=photo&pretty=true'
     response=requests.get(url)
     for i in range(number):
         r=response.json()['hits'][i]['webformatURL']
         resp=requests.get(r)
     
         open(f'./{content}_images/{content}{i+1}.jpg','wb').write(resp.content)
 except:
    print("Error")
