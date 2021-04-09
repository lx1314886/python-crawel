import contents
import re
import time
from parsel import Selector
import requests
import emoji

from mysql.pymysql_comm1 import UsingMysql1

class QbhjSpider():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
    }
    def __init__(self):
        self.parse()

    def parse(self):
        response = requests.get('https://faxian.smzdm.com/', headers=self.headers).text
        sel = Selector(text=response)
        qbhj_list = sel.xpath(contents.XPATH_QB_BOOT)
        qbhj_result = []
        for qbhj in qbhj_list:
            item = {}
            item['lTitle'] = qbhj.xpath(contents.XPATH_QB_L_TITLE).extract_first().replace("'",'')
            item['lImageUrl'] = qbhj.xpath(contents.XPATH_QB_L_IMAGE_URL).extract_first()
            item['vouchers'] = qbhj.xpath(contents.XPATH_QB_QUAN).extract_first()
            item['descr'] = qbhj.xpath(contents.XPATH_QB_CONTENTS).extract_first().replace("'",'')
            titleUrl = qbhj.xpath(contents.XPATH_QB_TITLE_URL).extract_first()
            if titleUrl is None:
                continue
            # 正则匹配商品编码
            shopNum = re.search(r'-?\d+', titleUrl, re.M|re.I).group()
            print("qbhj" + shopNum)
            item['titleUrl'] = titleUrl
            item['shopNum'] = shopNum
            item['goShoppingUrl'] = qbhj.xpath(contents.XPATH_QB_GO_SHOPPING_URL).extract_first()
            if item['goShoppingUrl'] is None:
                continue
            if 'www.smzdm.com/p' in item['goShoppingUrl']:
                item['goShoppingUrl'] = self.parse_link(item['goShoppingUrl'])
            item['sType'] = 1
            curDate = time.strftime(contents.Y_m_d_H_M_S, time.localtime(time.time()))
            item['createDate'] = curDate
            item['grabTime'] = curDate
            item['time1'] = qbhj.xpath(contents.XPATH_QB_TIME).extract_first()
            item['jxuan'] = qbhj.xpath(contents.XPATH_QB_JX).extract_first()
            item['pageUrl'] = titleUrl
            self.parse_detail(item)
            qbhj_result.append(item)
        if len(qbhj_result) > 0:
            with UsingMysql1(log_time=True) as um:
                # 删除数据
                del_data = [(qbhj_result[i]['shopNum']) for i in range(len(qbhj_result))]
                um.update_batch_by_pk(contents.SMZDM_DATA_DEL_SQL, del_data)
                um.update_batch_by_pk(contents.SMZDM_DETAIL_DATA_DEL_SQL, del_data)
                smzdm_data = [(qbhj_result[i]['lTitle'],qbhj_result[i]['titleUrl'],qbhj_result[i]['descr']
                                                                                ,qbhj_result[i]['goShoppingUrl'],qbhj_result[i]['time1'],qbhj_result[i]['lImageUrl']
                                                                                ,qbhj_result[i]['vouchers'],qbhj_result[i]['sType'],qbhj_result[i]['jxuan'],qbhj_result[i]['createDate']
                                                                                ,qbhj_result[i]['grabTime'],qbhj_result[i]['shopNum']) for i in range(len(qbhj_result))]
                um.update_batch_by_pk(contents.SMZDM_DATA_SQL, smzdm_data)
                smzdm_data_detail = [(qbhj_result[i]['dTitle'], qbhj_result[i]['contents'], qbhj_result[i]['quan'], qbhj_result[i]['dImageUrl'], qbhj_result[i]['pageUrl'], qbhj_result[i]['createDate'], qbhj_result[i]['createDate'], qbhj_result[i]['shopNum']) for i in range(len(qbhj_result))]
                um.update_batch_by_pk(contents.SMZDM_DATA_DETAIL_SQL, smzdm_data_detail)
                coupons = []
                coupons_shop_nums = []
                tags = []
                tags_shop_nums = []
                links = []
                links_shop_nums = []
                for crawl in qbhj_result:
                    if len(crawl.get('couponContent', '')) !=0 and len(crawl.get('couponUrl', '')) !=0:
                        coupons.append((crawl['shopNum'], crawl['couponContent'], crawl['couponUrl'], crawl['createDate']))
                        coupons_shop_nums.append((crawl['shopNum']))
                    if len(crawl.get('tags', '')) != 0 and len(crawl.get('tags', '')) != 0:
                        tags.append((crawl['shopNum'], crawl['tags']))
                        tags_shop_nums.append((crawl['shopNum']))
                    if len(crawl['links']) > 0:
                        links_shop_nums.append((crawl['shopNum']))
                        for link in crawl['links']:
                            if len(link) == 0:
                                crawl['text_links'].pop()
                                continue
                            links.append((crawl['shopNum'], link, crawl['text_links'].pop()))
                if len(coupons) > 0:
                    um.update_batch_by_pk(contents.SMZDM_COUPON_DEL_SQL, coupons_shop_nums)
                    um.update_batch_by_pk(contents.SMZDM_COUPON_SQL, coupons)
                if len(tags) > 0:
                    um.update_batch_by_pk(contents.SMZDM_TAG_DEL_SQL, tags_shop_nums)
                    um.update_batch_by_pk(contents.SMZDM_TAG_SQL, tags)
                if len(links) > 0:
                    um.update_batch_by_pk(contents.SMZDM_LINK_DEL_SQL, links_shop_nums)
                    um.update_batch_by_pk(contents.SMZDM_LINK_SQL, links)

    def parse_detail(self, item):
        response1 = requests.get(item['titleUrl'], headers=self.headers).text
        sel = Selector(text=response1)
        item['dTitle'] = sel.xpath(contents.XPATH_D_TITLE).extract_first().replace("'", '')
        item['dImageUrl'] = sel.xpath(contents.XPATH_D_IMAGE_URL).extract_first()
        content_a = sel.xpath(contents.XPATH_D_CONTENTS)
        dd = ''
        for content in content_a:
            content_temp = content.xpath('normalize-space(.)').extract_first().replace("'", '')
            if contents.JSF in content_temp or contents.CKDP in content_temp or contents.ZLDXF in content_temp or contents.XZJQR in content_temp:
                continue
            emoji_str = emoji.demojize(content_temp)
            content_temp = re.sub(r':(.*?):', '', emoji_str).strip()  # 清洗后的数据
            dd += content_temp + '\n'
        item['contents'] = dd
        item['quan'] = sel.xpath(contents.XPATH_D_QUAN).extract_first()
        if item['quan'] is None:
            item['quan'] = sel.xpath(contents.XPATH_D_QUAN_).extract_first()
        coupons = sel.xpath(contents.XPATH_COUPON)
        couponContent = []
        couponUrl = []
        for coupon in coupons:
            couponContent.append(coupon.xpath(contents.XPATH_COUPON_CONTENT).extract_first())
            couponUrl.append(coupon.xpath(contents.XPATH_COUPON_URL).extract_first())
        if len(couponContent) != 0:
            item['couponContent'] = contents.BLTX.join(couponContent)
            item['couponUrl'] = contents.BLTX.join(couponUrl)
        tags = sel.xpath(contents.XPATH_D_TAG)
        tag_txt = []
        for tag in tags:
            tag_txt.append(tag.xpath(contents.XPATH_D_TAG_TXT).extract_first().replace("'",''))
        if len(tag_txt) != 0:
            item["tags"] = contents.COMMA.join(tag_txt)
        links = sel.xpath(contents.XPATH_D_CONTENTS_LINK).getall()
        text_links = sel.xpath(contents.XPATH_D_CONTENTS_TEXT_LINK).getall()
        temp_links = []
        temp_text_links = []
        if links and text_links:
            for link in links:
                if len(text_links) > 0:
                    text_link = text_links.pop()
                    if text_link in dd:
                        if 'www.smzdm.com/p' in link:
                          temp_links.append(self.parse_link(link))
                        if 'go.smzdm.com' in link:
                          temp_links.append(link)
                        temp_text_links.append(text_link)
        item['links'] = temp_links
        item['text_links'] = temp_text_links

    def parse_link(self, url):
        response = requests.get(url, headers=self.headers).text
        sel = Selector(text=response)
        urls = sel.xpath(contents.XPATH_D_GO_SHOPPING_URL).extract()
        go_url = ''
        if len(urls) > 0:
            go_url = urls[0]
        return go_url


