import requests
import json
import time
import pandas as pd

def get_html(url):
	headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
	r=requests.get(url,headers=headers)
	return r.text

def get_code(stock_list):
	codes = json.loads(stock_list)
	ls=[]
	for i in codes['data']['list']:
		ls.append(i['symbol'])
	return ls

def get_infos(codes):
	gsmc_ls=[]
	ywmc_ls=[]
	agdm_ls=[]
	sszjhhy_ls=[]
	frdb_ls=[]
	zcdz_ls=[]
	gswz_ls=[]
	zczb_ls=[]
	gyrs_ls=[]
	jyfw_ls=[]
	all_ls=[]
	for code in codes:
		url = ['http://f10.eastmoney.com/CompanySurvey/CompanySurveyAjax?code={}'.format(code)]
		for u in url:
			# print(u)
			stock_infos = get_html(u)
			infos = json.loads(stock_infos)
			
			# 公司名称
			gsmc = infos['jbzl']['gsmc']
			gsmc_ls.append(gsmc)

			# 英文名称
			ywmc = infos['jbzl']['ywmc']
			ywmc_ls.append(ywmc)

			# A股代码
			agdm = infos['jbzl']['agdm']
			agdm_ls.append(agdm)

			# 所属证监会行业
			sszjhhy = infos['jbzl']['sszjhhy']
			sszjhhy_ls.append(sszjhhy)

			# 法人代表
			frdb = infos['jbzl']['frdb']
			frdb_ls.append(frdb)

			# 注册地址
			zcdz = infos['jbzl']['zcdz']
			zcdz_ls.append(zcdz)

			# 公司网址
			gswz = infos['jbzl']['gswz']
			gswz_ls.append(gswz)

			# 注册资本(元)
			zczb = infos['jbzl']['zczb']
			zczb_ls.append(zczb)

			# 雇员人数
			gyrs = infos['jbzl']['gyrs']
			gyrs_ls.append(gyrs)

			# 经营范围
			jyfw = infos['jbzl']['jyfw']
			jyfw_ls.append(jyfw)

	all_ls.append(gsmc_ls)
	all_ls.append(ywmc_ls)
	all_ls.append(agdm_ls)
	all_ls.append(sszjhhy_ls)
	all_ls.append(frdb_ls)
	all_ls.append(zcdz_ls)
	all_ls.append(gswz_ls)
	all_ls.append(zczb_ls)
	all_ls.append(gyrs_ls)
	all_ls.append(jyfw_ls)
	return all_ls

def save_infos(info):
	data = {}
	data['公司名称'] = info[0]
	data['英文名称'] = info[1]
	data['A股代码'] = info[2]
	data['所属行业'] = info[3]
	data['法人代表'] = info[4]
	data['注册地址'] = info[5]
	data['公司网址'] = info[6]
	data['注册资本'] = info[7]
	data['雇员人数'] = info[8]
	data['经营范围'] = info[9]
	data_frame = pd.DataFrame(data,columns=['公司名称','英文名称','A股代码','所属行业','法人代表','注册地址','公司网址','注册资本','雇员人数','经营范围'])
	data_frame.to_csv('company0.csv',header=False,index=False,mode='a',encoding='ANSI')
	print("sucessful")

def main():
	urls=["https://xueqiu.com/service/v5/stock/screener/quote/list?page={}&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz&_=1599114{}"
	.format(str(i),r'\d{6}') for i in range(1,5)]
	stock_codes=[]
	for u in urls:
		stock_list = get_html(u)
		code = get_code(stock_list)
		for c in code:
			stock_codes.append(c)
		time.sleep(1)
	infos = get_infos(stock_codes)
	print(infos)
	# save_infos(infos)

main()