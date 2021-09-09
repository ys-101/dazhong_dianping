import requests
from fontTools.ttLib import TTFont

"""
随手测试写的 如有需求定制爬虫联系QQ1224128144
"""


# woff_name 网站更换频繁 需要重新下载导入文件名
woff_name = "2c3b5651.woff"
# b0f80c5f .woff
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


header = {
    # "user-agent": UserAgent().random,
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    # 需要登录成功后的Cookie
    'Cookie': '_lxsdk_cuid=178d4e6693fc8-04b1734b424df9-57442618-144000-178d4e6693fc8; _lxsdk=178d4e6693fc8-04b1734b424df9-57442618-144000-178d4e6693fc8; _hc.v=cbf2b1e6-fb19-bafa-9254-5be11ca56500.1618479574; s_ViewType=10; ua=dpuser_0686755957; ctu=9c9d59f71aa2439aad21026dff834bafdaa81435af80748037c508dc556b6931; cy=2; cye=beijing; cityid=2; Appshare2021_ab=shop:A:1; dper=0e73574b41d147b13fe90d0aad99dc52f42990074746085253b3a6348de353900dae2ac9129da467b113afccc93267b81b568d703e7b2b2a1c828a048f37379a57c66018f541db0314afc4a73e0dd106e00118a24ff4064a6b9397a4e000d486; ll=7fd06e815b796be3df069dec7836c3df; uamo=17669320265; fspop=test; _lx_utm=utm_source=Baidu&utm_medium=organic; dplet=ae0400a4e3dfcece69bbcd88f47705c9; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1628843319,1631168153,1631169774; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1631169850; _lxsdk_s=17bc932c24b-0e5-60c-21d||194',
    #'Referer': 'http://www.dianping.com/search/keyword/2/0_%E9%85%92%E5%BA%97/p2',
}

# 抓取异步加载的评论包进行测试
url = 'http://www.dianping.com/ajax/json/shopDynamic/allReview?shopId=Enk0gTkqu0Cyj7Ch&cityId=2&shopType=10&tcv=d7kvcg4vkp&_token=eJxVj0tvgkAUhf%2FLrCcwLxBIXBA0RoQSGTDWxgUiBURQYXxg0%2F%2FeIbWLrs6537k3OfcLtPM9sDBCiGEIblkLLIAVpOgAAtHJRKcY66ZJDTZCEKT%2FmUEpBLt2NQHWB9aoDomGtwMJJfglhs628GWJtITBQcBuLldAIcTZUtX7%2Fa7sy6Q5l02upKda7YrTWZ02Fcqj6nJFTn8YOYWsBORlHQ2XmJmQakQyLJtTioaoGiKpyUvF3%2BzLt%2BRqV%2BaNdJn7iHjHustn6HfRive9ueCc9F6KPR5T7zkVbzG%2FBb1j2Lw91JvwWhVkuT4WJ7YiySYgmf2I%2FYuDXTFZ0risxDN9BN7ihniKg3DvvldHs67rWbZ2k2x3nMXrhT21TdM%2FaPl4DL5%2FAIRta0s%3D&uuid=cbf2b1e6-fb19-bafa-9254-5be11ca56500.1618479574&platform=1&partner=150&optimusCode=10&originUrl=http%3A%2F%2Fwww.dianping.com%2Fshop%2FEnk0gTkqu0Cyj7Ch'
html = requests.get(url=url, headers=header).json()
# print(html)
list_data = html['reviewAllDOList']
for dat in list_data:
    list_text = []
    name = dat['user']['userNickName']
    list_text.append(name)
    title = dat['reviewDataVO']['reviewData']['reviewBody']
    # print(title)
    data = title.split('<svgmtsi class="review">')
    data1 = ''.join(data)
    data = data1.split('</svgmtsi>')
    data1 = ''.join(data)
    data = data1.split('&')
    print('data',data)

    list1 = []
    for i in data:
        # print(type(i),i)
        if not i:
            pass
        elif i[0] == '#':
            str1 = i.split(';')[0]
            # print('str1',str1)
            unicode = 'uni' + str1[2:6]
            # print('unicode',unicode)
            num = word_dict.get(unicode)
            list1.append(num)
            # print(i.split(';')[1])
            str2 = i.split(';')[1]
            list1.append(str2)

        else:
            list1.append(i)
    # print('list1',list1)
    # print(''.join(list1))
    T = ''.join(list1)
    list_text.append(T)
    print(list_text)
