import requests
import json
import time
import ast
num_1=1
#try:
while(1):
  #url="http://api.springernature.com/meta/v2/json?q=(year:2000+subject:%22Material%20Science%22)&p=100&s={}&api_key=4c5cbdedd45766d18a9d1dd5acdd73f0".format(str(num_1))
  url="http://api.springernature.com/meta/v2/json?api_key=4917bbb04b36227a16216f32621e4f07&q=type:Journal+year:2000+subject:%22Materials%20Science%22+keyword:perovskite&p=100&s={}".format(str(num_1))
  response=requests.get(url)
  response=json.loads(response.text)
  Abstract=response.get('records')
  for i in Abstract:
   f = open(r'1.txt', 'a', encoding='UTF8')
   a=i.get('abstract')
   print(a,file=f)

   num_1=num_1+100
   print(num_1)

   time.sleep(1.0)
#except:print('错误')
# print(response.text)