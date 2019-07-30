from jing.api.base import RestApi


class jdUnionOpenCouponQuery(RestApi):
    '''
    优惠券领取情况查询接口

    '''

    def __init__(self, domain='https://router.jd.com/api', port=443):
        '''
        优惠券领取情况查询接口
        :param domain: 域名
        :param port: 端口
        :param param_json {
            eliteId 1-好券商品,2-京粉APP-jingdong.超级大卖场,3-小程序-jingdong.好券商品,4-京粉APP-jingdong.主题聚惠1-jingdong.服装运动,5-京粉APP-jingdong.主题聚惠2-jingdong.精选家电,6-京粉APP-jingdong.主题聚惠3-jingdong.超市,7-京粉APP-jingdong.主题聚惠4-jingdong.居家生活,10-9.9专区,11-品牌好货-jingdong.潮流范儿,12-品牌好货-jingdong.精致生活,13-品牌好货-jingdong.数码先锋,14-品牌好货-jingdong.品质家电,15-京仓配送,16-公众号-jingdong.好券商品,17-公众号-jingdong.9.9,18-公众号-jingdong.京东配送
            pageIndex
            pageSize
            sortName
            sort
        }
        '''
        RestApi.__init__(self, domain, port)
        self.couponUrls = None

    def getapiname(self):
        return 'jd.union.open.coupon.query'
