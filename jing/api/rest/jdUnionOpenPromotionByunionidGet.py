from jing.api.base import RestApi


class jdUnionOpenPromotionByunionidGet(RestApi):
    '''
    通过unionId获取推广链接
    工具商媒体帮助子站长获取普通推广链接和优惠券二合一推广链接，可传入PID参数以区分子站长的推广位，该参数可在订单查询接口返回。需向cps-qxsq@jd.com申请权限。
    '''
    def __init__(self, domain='https://router.jd.com/api', port=443):
        RestApi.__init__(self, domain, port)
        self.param_json = None

    def getapiname(self):
        return 'jd.union.open.promotion.byunionid.get'
