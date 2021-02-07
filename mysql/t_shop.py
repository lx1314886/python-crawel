from mysql.pymysql_comm import UsingMysql
import time
import datetime
from parsel import Selector
import requests

def update_title():
    with UsingMysql(log_time=True) as um:
        start_time = (datetime.datetime.now() - datetime.timedelta(hours=24)).strftime("%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "select id,smzdm_url from t_shop_ where create_date between '{}' and '{}'".format(start_time, end_time)
        data_list = um.fetch_all(sql)
        if data_list and len(data_list):
            ids=[]
            titles=[]
            # 爬取数据
            for data in data_list:
                if 'smzdm_url' in data and data['smzdm_url'] is not None:
                    title = parse_detail(data['smzdm_url'])
                    if title and len(title):
                        ids.append(data['id'])
                        titles.append(title)
            update_data = [(titles[i], ids[i]) for i in range(len(ids))]
            if update_data and len(update_data):
                sql = "update t_shop_ set title=%s where id=%s"
                um.update_batch_by_pk(sql, update_data)


def parse_detail(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    response = requests.get(url, headers=headers).text
    sel = Selector(text=response)
    title = sel.xpath("normalize-space(//div[@class='title-box']/h1[@class='title J_title']/text())").extract()[0]
    return title
if __name__ == '__main__':
    update_title()