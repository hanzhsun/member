import requests
from requests.exceptions import RequestException
import re
import math
import pandas as pd
import random
import time


headers = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
]

proxies = [
	'71.19.144.122:80',
]

def get_page(url):
	try:
		header = {
			'Cookie': '', # fill
			'Host': 'www.douban.com',
			'User-Agent': random.choice(headers)
		}
		#proxy = {'http': 'http://'+random.choice(proxies)}
		#response = requests.get(url, headers=header, proxies=proxy)
		response = requests.get(url, headers=header)
		if response.status_code == 200:
			return response.text
		print(response.status_code)
		return response.status_code
	except RequestException:
		return None

def get_parse(html):
	parse = re.compile('member-item.*?people/(.*?)/', re.S)
	result = re.findall(parse, html)
	for i in result:
		yield i

if __name__ == '__main__':
	#a = [720354,'zhangjiayuan',716591,711839,680361,725966,724388,723598,720930,667924,698919,721144,721034,720977,'rikimaru',720688,'boyuan']
	#name = ['yzl','zjy','lz','zky','lm','fjyl','rdyl','lzmq','yhy','cdd','naver','gqc','ly','zd','lw','mk','by']
	#n = [3992,5828,2853,5993,4340,3169,1124,3325,3738,3749,1494,1245,7322,4832,11483,8236,15977]
	#for j in range(0,17):
	a = ['boyuan']
	name = ['by']
	n = [15977]	
	for j in range(0,1):	
		res = []
		for i in range(math.ceil(n[j]/36)):
		#for i in range(241,math.ceil(n[j]/36)):
			url = 'https://www.douban.com/group/'+str(a[j])+'/members?start='+str(i*36)
			html = get_page(url)
			l = get_parse(html)
			for item in l:
				res.append(item)
			time.sleep(random.randint(3,5))
		df = pd.DataFrame(res, columns=[name[j]])
		df.to_excel(name[j]+'.xlsx', index=False)

		
