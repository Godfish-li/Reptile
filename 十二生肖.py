import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def get_html(url):
	headers={'User-agent':UserAgent().random}
	try:
		r=requests.get(url,headers=headers)
		r.raise_for_status()
		r.encoding='utf-8'
		return r.text
	except:
		return 'missing'

def get_info(html):
	soup=BeautifulSoup(html,'html.parser')
	demo=soup.find_all('p',class_="txt")[1].text.strip()
	return demo

def main():
	shengxiao=['shu','niu','hu','tu','long','she','ma','yang','hou','ji','gou','zhu']
	for name in shengxiao:
		url="https://www.d1xz.net/sx/{}/".format(name)
		html=get_html(url)
		if html=="missing":
			print('{}{}'.format(name,url))
		else:
			print('{}:{}'.format(name,'done'))
		luck=get_info(html)
		print(luck)

main()