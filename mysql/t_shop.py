from mysql.pymysql_comm import UsingMysql
from mysql.pymysql_comm1 import UsingMysql1
import time
import datetime
from parsel import Selector
import requests
import re
def update_title():
    detail_links = []
    shop_nums_link = []
    with UsingMysql(log_time=True) as um:
        start_time = (datetime.datetime.now() - datetime.timedelta(hours=12)).strftime("%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sql = "select id,smzdm_url from t_shop_ where create_date between '{}' and '{}'".format(start_time, end_time)
        data_list = um.fetch_all(sql)
        if data_list and len(data_list):
            ids=[]
            titles=[]
            contents = []
            # 爬取数据
            for data in data_list:
                if 'smzdm_url' in data and data['smzdm_url'] is not None:
                    title, content, temp_links, temp_text_links, shop_num= parse_detail(data['smzdm_url'])
                    if title and len(title):
                        ids.append(data['id'])
                        titles.append(title)
                    if shop_num and len(shop_num) > 0:
                        if content and len(content):
                            contents.append((content, shop_num))
                        if len(temp_links) > 0 and len(temp_text_links) > 0:
                            shop_nums_link.append((shop_num))
                            for temp_link in temp_links:
                                detail_links.append((temp_link, temp_text_links.pop(),shop_num))
            update_data = [(titles[i], ids[i]) for i in range(len(ids))]
            if update_data and len(update_data):
                sql = "update t_shop_ set title=%s where id=%s"
                um.update_batch_by_pk(sql, update_data)
            if len(contents) > 0:
                sql = "update t_shop_detail set contents=%s where shop_num=%s"
                um.update_batch_by_pk(sql, contents)

    if (len(detail_links)) > 0 :
        with UsingMysql1(log_time=True) as um:
            del_sql = "delete from t_shop_detail_links where shop_num=%s"
            um.update_batch_by_pk(del_sql, shop_nums_link)
            ins_sql = "insert into t_shop_detail_links(url,link_text,shop_num) values (%s,%s,%s)"
            um.update_batch_by_pk(ins_sql, detail_links)



def parse_detail(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    response = requests.get(url, headers=headers).text
    sel = Selector(text=response)
    title = sel.xpath("normalize-space(//div[@class='title-box']/h1[@class='title J_title']/text())").extract()[0]
    content_a = sel.xpath("//article[@class='wrap-main']/div[@id='feed-main']/div[@class='item-name']/article[@class='txt-detail']/*[name(.)!='span']")
    dd = ''
    for content in content_a:
        content_temp = content.xpath('normalize-space(.)').extract_first().replace("'", '')
        if "极速发" in content_temp or "查看点评" in content_temp or "中立的消费门户" in content_temp or "小值机器人" in content_temp:
            continue
        dd += content_temp + '\n'
    links = sel.xpath("//article[@class='txt-detail']/p/a[@itemprop='description']/@href").getall()
    text_links = sel.xpath("//article[@class='txt-detail']/p/a[@itemprop='description']/text()").getall()
    temp_links = []
    temp_text_links = []
    shop_num = re.search(r'-?\d+', str(url), re.M|re.I).group()
    if links and text_links:
        for link in links:
            if len(text_links) > 0:
                text_link = text_links.pop()
                if text_link in dd:
                    if 'www.smzdm.com/p' in link:
                        temp_links.append(parse_link(link))
                    if 'go.smzdm.com' in link:
                        temp_links.append(link)
                    temp_text_links.append(text_link)
    return (title, dd, temp_links, temp_text_links, shop_num)

def parse_link(self, url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    response = requests.get(url, headers=headers).text
    sel = Selector(text=response)
    urls = sel.xpath("//div[@class='info-details']/div[@class='btn-group J_btn_group']/a[@class='go-buy btn']/@href").extract()
    go_url = ''
    if len(urls) > 0:
        go_url = urls[0]
    return go_url
if __name__ == '__main__':
    update_title()