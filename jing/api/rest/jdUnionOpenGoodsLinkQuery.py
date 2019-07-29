from jing.api.base import RestApi


class jdUnionOpenGoodsLinkQueryt(RestApi):
    '''
    秒杀商品查询接口
    '''
    def __init__(self, domain='https://router.jd.com/api', port=443):
        RestApi.__init__(self, domain, port)
        self.param_json = None

    def getapiname(self):
        return 'jd.union.open.goods.seckill.query'
