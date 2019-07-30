from jing.api.base import RestApi


class jdUnionOpenOrderQuery(RestApi):
    '''
    查询推广订单及佣金信息，会随着订单状态变化更新数据，支持按下单时间、完成时间或状态更新时间查询，
    通常可按更新时间每分钟调用一次来获取订单的最新状态。支持subunionid、推广位、PID、工具商角色订单查询。
    功能相当于原宙斯接口的订单查询、 查询引入订单、查询业绩订单、工具商订单查询、工具商引入数据查询接口、
    工具商业绩数据查询接口、PID订单查询、PID引入订单查询、PID业绩订单查询。

    '''

    def __init__(self, domain='https://router.jd.com/api', port=443):
        '''
        京粉精选商品查询接口
        :param domain: 域名
        :param port: 端口
        :param param_json {
            orderReq{
                pageNo 页码，返回第几页结果
                pageSize 每页包含条数，上限为500
                type 订单时间查询类型(1：下单时间，2：完成时间，3：更新时间)
                time 查询时间，建议使用分钟级查询，格式：yyyyMMddHH、yyyyMMddHHmm或yyyyMMddHHmmss，如201811031212 的查询范围从12:12:00--12:12:59
            }
        }
        '''
        RestApi.__init__(self, domain, port)
        self.couponUrls = None

    def getapiname(self):
        return 'jd.union.open.order.query'
