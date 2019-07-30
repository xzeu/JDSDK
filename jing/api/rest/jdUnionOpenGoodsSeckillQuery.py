from jing.api.base import RestApi


class jdUnionOpenGoodsSeckillQuery(RestApi):
    '''
    秒杀商品查询接口
    根据SKUID、类目等信息查询秒杀商品信息，秒杀商品的价格通常为近期低价，有利于促成购买。需向cps-qxsq@jd.com申请权限。
    '''
    def __init__(self, domain='https://router.jd.com/api', port=443):
        RestApi.__init__(self, domain, port)
        self.param_json = None

    def getapiname(self):
        return 'jd.union.open.goods.seckill.query'