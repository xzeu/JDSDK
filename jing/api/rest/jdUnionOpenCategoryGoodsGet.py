from jing.api.base import RestApi


class jdUnionOpenCategoryGoodsGet(RestApi):
    '''
    商品类目查询
    '''

    def __init__(self, domain='https://router.jd.com/api', port=443):
        RestApi.__init__(self, domain, port)
        self.param_json = None

    def getapiname(self):
        return 'jd.union.open.category.goods.get'
