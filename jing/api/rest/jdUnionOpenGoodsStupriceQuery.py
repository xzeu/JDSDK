from jing.api.base import RestApi


class jdUnionOpenGoodsStupriceQuery(RestApi):
    '''
    学生价商品查询接口
    根据SKUID、类目等信息查询学生价商品信息，通常用于校园推广
    '''
    def __init__(self, domain='https://router.jd.com/api', port=443):
        RestApi.__init__(self, domain, port)
        self.param_json = None

    def getapiname(self):
        return 'jd.union.open.goods.stuprice.query'
