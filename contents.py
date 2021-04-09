# 变量

REG_NUM = '-?\d+'
# 精选好价
XPATH_BOOT = "//div[@id='feed-main']/div[@class='feed-main-con']/ul[@id='feed-main-list']/li[@class='J_feed_za feed-row-wide']"
XPATH_L_TITLE = "normalize-space(./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/h5/a/text())"
XPATH_L_IMAGE_URL = "./div[@class='feed-block z-hor-feed']/div[@class='z-feed-img']/a/img/@src"
XPATH_QUAN = "normalize-space(string(./div[@class='feed-block z-hor-feed']/*/*[@class='z-highlight']))"
XPATH_CONTENTS = "normalize-space(./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/div[@class='feed-block-descripe'])"
XPATH_CONTENTS_ = "normalize-space(./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/div[@class='feed-block-descripe haitao-descripe'])"
XPATH_GO_URL = "./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/h5/a/@href"
XPATH_GO_SHOPPING_URL = "./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/div[@class='z-feed-foot']/div[@class='z-feed-foot-r']/div/div/a/@href"
XPATH_GO_SHOPPING_URL_ = "./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/div[@class='z-feed-foot']/div[@class='z-feed-foot-r']/div[@class='feed-link-btn']/div[@class='feed-link-btn-inner']/a[@class='z-btn z-btn-red']/@href"
XPATH_GO_SHOPPING_URL_1 = "./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/div[@class='z-feed-foot']/div[@class='z-feed-foot-r']/div[@class='feed-link-btn multi-links']/div[@class='feed-link-btn-inner']/a[@class='z-btn z-btn-red']/@href"
XPATH_TIME = "normalize-space(./div[@class='feed-block z-hor-feed']/div[@class='z-feed-content']/div[@class='z-feed-foot']/div[@class='z-feed-foot-r']/span[@class='feed-block-extras'])"
XPATH_D_TITLE = "normalize-space(//div[@class='title-box']/h1[@class='title J_title']/text())"
XPATH_D_IMAGE_URL = "//div[@class='info J_info']/a[@class='img-box']/img[@class='main-img']/@src"
XPATH_D_CONTENTS = "//article[@class='wrap-main']/div[@id='feed-main']/div[@class='item-name']/article[@class='txt-detail']/*[name(.)!='span']"
XPATH_D_QUAN = "//div[@class='info-right ']/div[@class='title-box']/div[@class='price']/span/text()"
XPATH_D_QUAN_ = "//div[@class='title-box']/div[@class='old-price-box']/p[@class='old-price']/span[2]/text()"
XPATH_D_TAG = "//div[@id='feed-main']/div/div/div/ul[@class='z-clearfix']/li"
XPATH_D_TAG_TXT = "normalize-space(./div[@class='meta-tags']/a)"
XPATH_D_CONTENTS_LINK = "//article[@class='txt-detail']/p/a[@itemprop='description']/@href"
XPATH_D_CONTENTS_TEXT_LINK = "//article[@class='txt-detail']/p/a[@itemprop='description']/text()"
XPATH_D_GO_SHOPPING_URL = "//div[@class='info-details']/div[@class='btn-group J_btn_group']/a[@class='go-buy btn']/@href"
XPATH_PAGENATION = "//div[@class='feed-pagenation']/ul[@id='J_feed_pagenation']/li[@class='page-turn next-page']/i[@class='icon-angle-right-o-thin']"
XPATH_COUPON = "//div[@class='coupon-box']/a[@class='coupon-item J_pop_quan1']"
XPATH_COUPON_CONTENT = "normalize-space(./span[@class='coupon-info']/text())"
XPATH_COUPON_URL = "./@href"
# 全部好价
XPATH_QB_BOOT = "//div[@class='content-inner']/ul[@id='feed-main-list']/li"
XPATH_QB_L_TITLE = "normalize-space(./div/h5[@class='feed-ver-title']/a/text())"
XPATH_QB_L_IMAGE_URL = "./div/div[@class='feed-ver-pic']/a[1]/img/@src"
XPATH_QB_QUAN = "normalize-space(./div/div[@class='z-highlight z-ellipsis']/text())"
XPATH_QB_CONTENTS = "normalize-space(./div/div[@class='feed-ver-descripe'])"
XPATH_QB_TITLE_URL = "./div/h5[@class='feed-ver-title']/a/@href"
XPATH_QB_GO_SHOPPING_URL = "./div/div[@class='feed-ver-row'][2]/div[@class='feed-ver-row-r']/div/div[@class='feed-link-btn-inner']/a[@class='z-btn z-btn-red']/@href"
XPATH_QB_TIME = "./div/div[@class='feed-ver-row'][1]/div[@class='feed-ver-row-r feed-ver-date']/text()"
XPATH_QB_JX = "./div/div[@class='feed-ver-pic']/a[@class='tag-bottom-right']/text()"
# 白菜价
XPATH_BC_BOOT = "//div[@class='content-inner']/ul[@id='feed-main-list']/li/div"
XPATH_BC_L_TITLE = "normalize-space(./h5/a/text())"
XPATH_BC_L_IMAGE_URL = "./div/a[1]/img/@src"
XPATH_BC_QUAN = "./div[@class='z-highlight z-ellipsis']/text()"
XPATH_BC_CONTENTS = "normalize-space(./div[@class='feed-ver-descripe'])"
XPATH_BC_TITLE_URL = "./h5/a/@href"
XPATH_BC_GO_SHOPPING_URL = "./div/div/div/div/a[@class='z-btn z-btn-red']/@href"
XPATH_BC_TIME = "./div/div[@class='feed-ver-row-r feed-ver-date']/text()"
XPATH_BC_JX = "./div/a[@class='tag-bottom-right']/text()"
Y_m_d_H_M_S = "%Y-%m-%d %H:%M:%S"
BLTX = '@bltx'
COMMA = ','
CKDP = '查看点评'
JSF = '极速发'
ZLDXF = '中立的消费门户'
XZJQR = '小值机器人'
SMZDM_DATA_SQL = "INSERT INTO smzdm_data (title,title_url,descr,go_shopping_url,time1,image_url,vouchers,s_type,jxuan,create_date,grab_time,shop_num) VALUES (%s" \
                                 ",%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
SMZDM_DATA_DETAIL_SQL = "INSERT INTO smzdm_data_detail (title,contents,quan,image_url, page_url, create_date, grab_time, shop_num) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
SMZDM_DATA_DEL_SQL = "delete from smzdm_data where shop_num=%s"
SMZDM_DETAIL_DATA_DEL_SQL = "delete from smzdm_data_detail where shop_num=%s"
SMZDM_COUPON_SQL = "INSERT INTO smzdm_coupon (shop_num, coupon_content, coupon_url, create_time) VALUES(%s, %s, %s, %s)"
SMZDM_COUPON_DEL_SQL = "delete from smzdm_coupon where shop_num=%s"
SMZDM_TAG_SQL = "INSERT INTO t_shop_tag(shop_num, tag_name) VALUES(%s, %s)"
SMZDM_TAG_DEL_SQL = "delete from t_shop_tag where shop_num=%s"
SMZDM_LINK_SQL = "INSERT INTO t_shop_detail_links(shop_num,url,link_text) VALUES(%s, %s, %s)"
SMZDM_LINK_DEL_SQL = "delete from t_shop_detail_links where shop_num=%s"

