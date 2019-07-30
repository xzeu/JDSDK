from jing.api.base import RestApi


class jdUnionOpenUserPidGet(RestApi):
    '''
    获取PID
    工具商媒体帮助子站长创建PID，该参数可在媒体和子站长之间建立关联，并通过获取推广链接、订单查询来跟踪。需向cps-qxsq@jd.com申请权限。
    '''
    def __init__(self, domain='https://router.jd.com/api', port=443):
        RestApi.__init__(self, domain, port)
        self.param_json = None

    def getapiname(self):
        return 'jd.union.open.user.pid.get'
