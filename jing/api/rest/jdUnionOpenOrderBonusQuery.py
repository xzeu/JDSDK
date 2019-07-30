from jing.api.base import RestApi


class jdUnionOpenOrderBonusQuery(RestApi):
    '''
    奖励订单查询接口【申请】

    '''

    def __init__(self, domain='https://router.jd.com/api', port=443):
        '''
        京粉精选商品查询接口
        :param domain: 域名
        :param port: 端口
        :param param_json {
            orderReq{
                optType 时间类型 (1：下单时间，sortValue和pageSize组合使用； 2：更新时间，pageNo和pageSize组合使用)
                startTime 订单开始时间，时间戳（毫秒），起止时间限制10min内
                endTime 订单结束时间，时间戳（毫秒），起止时间限制10min内
                pageNo 页码，默认值为1
                pageSize 每页数量，上限100
                sortValue 时间类型按'下单'查询时，和pageSize组合使用。获取最后一条记录的sortValue，指定拉取条数（pageSize），以此方式查询数据。
            }
        }
        '''
        RestApi.__init__(self, domain, port)
        self.couponUrls = None

    def getapiname(self):
        return 'jd.union.open.order.bonus.query'
