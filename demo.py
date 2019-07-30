import jing.api
import json
import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.3.58", "jd", "jd", "jd")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了fa
'''
jing.setDefaultAppInfo("110bc5b99cfab32454dcaa8022dd8c4", "612f41079b0241fd8be42576a845084")

'''
使用自定义的域名和端口（京东没有测试沙箱环境使用）
a = jing.api.UserGetRequest("https://router.jd.com/api",443)
使用默认的配置（调用线上环境）
a = jing.api.UserGetRequest()
'''

a = jing.api.jdUnionOpenGoodsJingfenQuery()
'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(jing.appinfo("appkey","*******"))
'''

a.param_json = json.dumps({
    "goodsReq": {
        "sort": "desc",
        "pageSize": 5,
        "eliteId": 1,
        "sortName": "commission",
        "pageIndex": 1
    }
})


try:
    f = a.getResponse()
    result = json.loads(f['jd_union_open_goods_jingfen_query_response']['result'])['data']
    print(result)
    for r in result:
        print("**********************商品开始*****************")
        print("一级类目ID:{}".format(r['categoryInfo']['cid1']))
        print("一级类目名称:{}".format(r['categoryInfo']['cid1Name']))
        print("二级类目ID:{}".format(r['categoryInfo']['cid2']))
        print("二级类目名称:{}".format(r['categoryInfo']['cid2Name']))
        print("三级类目ID:{}".format(r['categoryInfo']['cid3']))
        print("三级类目名称:{}".format(r['categoryInfo']['cid3Name']))
        print("评论数:{}".format(r['comments']))
        print("佣金信息")
        print("==佣金:{}".format(r['commissionInfo']['commission']))  # 佣金
        print("==佣金比例：{}".format(r['commissionInfo']['commissionShare']))  # 佣金比例
        # 优惠券信息，返回内容为空说明该SKU无可用优惠券
        # print("优惠券合集".format(r['couponInfo']['couponList']))
        print("优惠券合集")
        if len(r['couponInfo']['couponList'])>0:
            for coupon in r['couponInfo']['couponList']:
                # coupon['bindType']券种类 (优惠券种类：0 - 全品类，1 - 限品类（自营商品），2 - 限店铺，3 - 店铺限商品券)
                print("券种类 (优惠券种类：0 - 全品类，1 - 限品类（自营商品），2 - 限店铺，3 - 店铺限商品券)")
                if coupon['bindType'] == 0:
                    print("==券种类:全品类")
                elif coupon['bindType'] == 1:
                    print("==券种类:限品类（自营商品）")
                elif coupon['bindType'] == 2:
                    print("==券种类:限店铺")
                elif coupon['bindType'] == 3:
                    print("==券种类:店铺限商品券")
                print("==券面额:{}".format(coupon['discount']))
                print("==券领取结束时间:{}".format(coupon['getEndTime']))
                print("==领取开始时间:{}".format(coupon['getStartTime']))
                print("==券链接:{}".format(coupon['link']))
                # print("一级类目ID".format(coupon['platformType']))
                print("==券使用平台 (平台类型：0 - 全平台券，1 - 限平台券)")
                if coupon['platformType'] == 0:
                    print("==券使用平:全平台券")
                elif coupon['platformType'] == 1:
                    print("==券使用平:限平台券")

                print("==券消费限额:{}".format(coupon['quota']))
                print("==券有效使用结束时间:{}".format(coupon['useEndTime']))
                print("==券有效使用开始时间:{}".format(coupon['useStartTime']))

        print("商品好评率:{}".format(r['goodCommentsShare']))
        # print(r['imageInfo']['imageList'])
        print("图片链接地址，第一个图片链接为主图链接")
        for image in r['imageInfo']['imageList']:
            print("图片链接:{}".format(image['url']))
        print("30天引单数量:{}".format(r['inOrderCount30Days']))
        print("30天引单数量(sku维度):{}".format(r['inOrderCount30DaysSku']))
        print("是否爆款，1：是，0：否:{}".format(r['isHot']))
        print("商品落地页:{}".format(r['materialUrl']))
        print("g=自营，p=pop:{}".format(r['owner']))
        print("拼购信息:{}".format(r['pinGouInfo']))
        print("拼购价格:{}".format(r['priceInfo']['price']))
        print("频道id:{}".format(r['resourceInfo']['eliteId']))
        print("频道名称:{}".format(r['resourceInfo']['eliteName']))
        print("店铺Id:{}".format(r['shopInfo']['shopId']))
        print("店铺名称（或供应商名称）:{}".format(r['shopInfo']['shopName']))
        print("商品ID:{}".format(r['skuId']))
        print("商品名称:{}".format(r['skuName']))
        print("spuid，其值为同款商品的主skuid:{}".format(r['spuid']))
        print("**********************商品结束*****************")


except Exception as e:
    print(e)
