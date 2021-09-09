# -*- coding: utf-8 -*-
import requests
from fontTools.ttLib import TTFont
from lxml import etree
from urllib import parse
from fake_useragent import UserAgent
import time
import random
import csv


def get_word_dict(name):
    """读取指定的woff得到字体，变化比较频繁，下载后需要更换woff_name"""
    if name == "reviewTag" or name == "shopNum":
        woff_name = "2c3b5651.woff"
    elif name == "tagName":
        woff_name = "f80b7f21.woff"
    elif name == "address":
        woff_name = '502a528d.woff'

    # 读取文件的编码，和自己的字符串并 一一对应组成字典
    word_dict = {}
    tag_name_list = TTFont(woff_name).getGlyphOrder()
    word_string = ' .1234567890店中美家馆小车大市公酒行国品发电金心业商司超生装园场食有新限天面工服海华水房饰城乐汽香部利子老艺花专东肉菜学福饭' \
                  '人百餐茶务通味所山区门药银农龙停尚安广鑫一容动南具源兴鲜记时机烤文康信果阳理锅宝达地儿衣特产西批坊州牛佳化五米修爱北养卖建材三会鸡' \
                  '室红站德王光名丽油院堂烧江社合星货型村自科快便日民营和活童明器烟育宾精屋经居庄石顺林尔县手厅销用好客火雅盛体旅之鞋辣作粉包楼校鱼平彩上' \
                  '吧保永万物教吃设医正造丰健点汤网庆技斯洗料配汇木缘加麻联卫川泰色世方寓风幼羊烫来高厂兰阿贝皮全女拉成云维贸道术运都口博河瑞宏京际路祥青' \
                  '镇厨培力惠连马鸿钢训影甲助窗布富牌头四多妆吉苑沙恒隆春干饼氏里二管诚制售嘉长轩杂副清计黄讯太鸭号街交与叉附近层旁对巷栋环省桥湖段乡厦府' \
                  '铺内侧元购前幢滨处向座下臬凤港开关景泉塘放昌线湾政步宁解白田町溪十八古双胜本单同九迎第台玉锦底后七斜期武岭松角纪朝峰六振珠局岗洲横边济' \
                  '井办汉代临弄团外塔杨铁浦字年岛陵原梅进荣友虹央桂沿事津凯莲丁秀柳集紫旗张谷的是不了很还个也这我就在以可到错没去过感次要比觉看得说常真' \
                  '们但最喜哈么别位能较境非为欢然他挺着价那意种想出员两推做排实分间甜度起满给热完格荐喝等其再几只现朋候样直而买于般豆量选奶打每评少算又' \
                  '因情找些份置适什蛋师气你姐棒试总定啊足级整带虾如态且尝主话强当更板知己无酸让入啦式笑赞片酱差像提队走嫩才刚午接重串回晚微周值费性桌拍跟块调糕'
    for index, value in enumerate(word_string):
        word_dict[tag_name_list[index]] = value

    return word_dict


def get_response(url):
    # 登录成功后的cookie值，可以进行翻页
    headers = {
        # "user-agent": UserAgent().random,
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        'Cookie': 'cy=2; cye=beijing; _lxsdk_cuid=178d4e6693fc8-04b1734b424df9-57442618-144000-178d4e6693fc8; _lxsdk=178d4e6693fc8-04b1734b424df9-57442618-144000-178d4e6693fc8; _hc.v=cbf2b1e6-fb19-bafa-9254-5be11ca56500.1618479574; s_ViewType=10; fspop=test; _lx_utm=utm_source=Baidu&utm_medium=organic; thirdtoken=ccbf9349-b863-4b74-b47b-853a3a28a8bb; _thirdu.c=cfcd75b665c3a1ff147876c8eeca152c; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1618539903,1620719527,1620782343,1620791513; dplet=9352bb3fe28711a227153c0617d4a479; dper=297bb9dd84eb426fff02262549da3f48036d94322e7f452592b36e07afa9de953749200a8496d68210f0e2bcad491fed32f1c77814a6a6136d83db5c4b0a64649211243fc83c5d20faad6fd3b5e712130bd81294b80c3d44663b94865ddfcfa4; ll=7fd06e815b796be3df069dec7836c3df; ua=dpuser_0686755957; ctu=9c9d59f71aa2439aad21026dff834bafdaa81435af80748037c508dc556b6931; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1620791575; _lxsdk_s=1795eb20d0b-b37-3de-8da||49',
        'Referer': 'http://www.dianping.com/search/keyword/2/0_%E9%85%92%E5%BA%97/p2',
    }
    response = requests.get(url=url, headers=headers)
    return response


if __name__ == '__main__':
    sum = 0
    # 解析页面
    #url = 'http://www.dianping.com/search/keyword/2/0_酒店'
    url = 'http://www.dianping.com/search/keyword/2/0_{}'

    keyword = input("搜索>>>>")
    f = open(keyword + '.csv', 'w', encoding='utf-8')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['店铺名称', '店铺评分','评论数','人均消费'])

    keyword = parse.quote(keyword)
    url = url.format(keyword)
    print(url)
    content = get_response(url).content.decode("utf-8")
    # print(content)
    xpath_obj = etree.HTML(content)
    # 获取该页的数据,十五条
    li_list = xpath_obj.xpath('//div[@id="shop-all-list"]//ul//li')
    for li in li_list:
        list_data = []
        item = dict()
        # item["shop_url"] = li.xpath("./div[1]/a/@href")[0]  # 店铺的url
        # item["shop_img_url"] = li.xpath("./div[1]/a/img/@src")[0]  # 店铺图片的url
        # //div[@class="comment"]/a[1]/text() 评论数量
        item["shop_name"] = li.xpath("./div[1]/a/img/@title")[0]  # 店铺名称
        list_data.append(item["shop_name"])
        # 店铺的星级一般通过类名展现出来了，那个数字就代表星数，因此切割出来
        star_class = li.xpath('.//*[@class="star_icon"]/span[1]/@class')[0]
        item["shop_star"] = star_class.split(" ")[1].split("_")[-1]  # 店铺评分
        list_data.append(item["shop_star"])
        # 评论数
        item["shop_comment_num"] = ''
        class_name = li.xpath('./div[2]/div[2]/a[1]/b/svgmtsi/@class')
        if class_name:  # 有加密
            class_name = class_name[0]
            word_dict = get_word_dict(class_name)
            for unicode in li.xpath('./div[2]/div[2]/a[1]/b//text()'):
                # 1字体可能不加密
                if unicode == '1':
                    num = '1'
                elif unicode == '11':
                    num = '11'
                elif unicode == '11':
                    num = '11'
                else:
                    # print(unicode,"****************************")
                    # 0和匹配的不一样，可能更新
                    unicode = 'uni' + ''.join(list(map(lambda b: hex(b)[2:], ord(unicode).to_bytes(2, 'big'))))
                    num = word_dict.get(unicode, '0')
                item["shop_comment_num"] += num
        else:  # 没有加密
            item["shop_comment_num"] = "".join(li.xpath('./div[2]/div[2]/a[1]/b//text()'))  # 评论数
        list_data.append(item["shop_comment_num"])
        # 人均消费
        item["shop_avg_money"] = ''
        class_name = li.xpath('./div[2]/div[2]/a[2]/b/svgmtsi/@class')
        if class_name:  # 有加密
            class_name = class_name[0]
            word_dict = get_word_dict(class_name)
            for unicode in li.xpath('./div[2]/div[2]/a[2]/b//text()'):
                if unicode == '￥':
                    num = ''
                elif unicode == '￥1':
                    num = '1'
                elif unicode == '11':
                    num = '11'
                elif unicode == '￥11':
                    num = '11'
                else:
                    # 0和匹配的不一样，可能更新
                    unicode = 'uni' + ''.join(list(map(lambda b: hex(b)[2:], ord(unicode).to_bytes(2, 'big'))))
                    num = word_dict.get(unicode, '0')

                item["shop_avg_money"] += num

        else:  # 没有加密
            item["shop_avg_money"] = "".join(li.xpath('./div[2]/div[2]/a[2]/b//text()'))  # 人均消费
        list_data.append(item["shop_avg_money"])
        print(item)
        print(list_data)
        csv_writer.writerow(list_data)
        sum += 1
        print("*****************第", sum, "条数据*****************")
    time.sleep(random.randint(19, 21))
    for i in range(2,51):
        two_url = 'http://www.dianping.com/search/keyword/2/0_{}/p{}'
        url = two_url.format(keyword,i)

        content = get_response(url).content.decode("utf-8")

        xpath_obj = etree.HTML(content)
        # 获取该页的数据,十五条
        li_list = xpath_obj.xpath('//div[@id="shop-all-list"]//ul//li')
        for li in li_list:
            list_data = []
            item = dict()
            # item["shop_url"] = li.xpath("./div[1]/a/@href")[0]  # 店铺的url
            # item["shop_img_url"] = li.xpath("./div[1]/a/img/@src")[0]  # 店铺图片的url
            # //div[@class="comment"]/a[1]/text() 评论数量
            item["shop_name"] = li.xpath("./div[1]/a/img/@title")[0]  # 店铺名称
            list_data.append(item["shop_name"])
            # 店铺的星级一般通过类名展现出来了，那个数字就代表星数，因此切割出来
            star_class = li.xpath('.//*[@class="star_icon"]/span[1]/@class')[0]
            item["shop_star"] = star_class.split(" ")[1].split("_")[-1]  # 店铺评分
            list_data.append(item["shop_star"])
            # 评论数
            item["shop_comment_num"] = ''
            class_name = li.xpath('./div[2]/div[2]/a[1]/b/svgmtsi/@class')
            if class_name:  # 有加密
                class_name = class_name[0]
                word_dict = get_word_dict(class_name)
                for unicode in li.xpath('./div[2]/div[2]/a[1]/b//text()'):
                    # 1字体可能不加密
                    if unicode == '1':
                        num = '1'
                    elif unicode == '11':
                        num = '11'
                    elif unicode == '111':
                        num = '111'
                    else:
                        # 0和匹配的不一样，可能更新
                        unicode = 'uni' + ''.join(list(map(lambda b: hex(b)[2:], ord(unicode).to_bytes(2, 'big'))))
                        num = word_dict.get(unicode, '0')
                    item["shop_comment_num"] += num
            else:  # 没有加密
                item["shop_comment_num"] = "".join(li.xpath('./div[2]/div[2]/a[1]/b//text()'))  # 评论数
            list_data.append(item["shop_comment_num"])
            # 人均消费
            item["shop_avg_money"] = ''
            class_name = li.xpath('./div[2]/div[2]/a[2]/b/svgmtsi/@class')
            if class_name:  # 有加密
                class_name = class_name[0]
                word_dict = get_word_dict(class_name)
                for unicode in li.xpath('./div[2]/div[2]/a[2]/b//text()'):
                    if unicode == '￥':
                        num = ''
                    elif unicode == '￥1':
                        num = '1'
                    elif unicode == '11':
                        num = '11'
                    elif unicode == '￥11':
                        num = '11'
                    else:
                        # 0和匹配的不一样，可能更新
                        unicode = 'uni' + ''.join(list(map(lambda b: hex(b)[2:], ord(unicode).to_bytes(2, 'big'))))
                        num = word_dict.get(unicode, '0')

                    item["shop_avg_money"] += num

            else:  # 没有加密
                item["shop_avg_money"] = "".join(li.xpath('./div[2]/div[2]/a[2]/b//text()'))  # 人均消费
            list_data.append(item["shop_avg_money"])
            print(item)
            print(list_data)
            csv_writer.writerow(list_data)
            sum += 1
            print("*****************第", sum, "条数据*****************")
        time.sleep(random.randint(19, 21))
print("读取完成！")
"""
{'shop_name': '万爱情侣主题酒店(北京国贸双井地铁站店)', 'shop_star': '50', 'shop_comment_num': '1051', 'shop_avg_money': '299'}
['万爱情侣主题酒店(北京国贸双井地铁站店)', '50', '1051', '299']
*****************第 1 条数据*****************
{'shop_name': '北京JW万豪酒店', 'shop_star': '50', 'shop_comment_num': '2481', 'shop_avg_money': '1399'}
['北京JW万豪酒店', '50', '2481', '1399']
*****************第 2 条数据*****************
"""