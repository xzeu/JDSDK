import jing.api
import json
import pymysql

# 打开数据库连接
db = pymysql.connect("192.168.3.58", "jd", "jd", "jd")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

jing.setDefaultAppInfo("110bc5b99cfab32454dcaa8022dd8c4", "612f41079b0241fd8be42576a845084")

b = jing.api.jdUnionOpenCategoryGoodsGet()


sql = "select id from category"

try:
    # 执行sql语句
    print(sql)
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()

data = cursor.fetchall()

for d in data:
    print(d[0])
    b.param_json = json.dumps({
        "req": {
            "parentId": d[0],
            "grade": 2
        }
    })

    try:
        result = b.getResponse()
        category = json.loads(result['jd_union_open_category_goods_get_response']['result'])['data']
        # SQL 插入语句
        sql_temp = "INSERT INTO category(id, name, grade, parentId) VALUES ('%s', '%s', '%s', '%s')"
        for i in range(len(category)):

            print("类目Id:{}".format(category[i]['id']))
            print("类目名称:{}".format(category[i]['name']))
            print("类目级别(类目级别 0，1，2 代表一、二、三级类目):{}".format(category[i]['grade']))
            print("父类目Id:{}".format(category[i]['parentId']))
            sql = sql_temp % (category[i]['id'], category[i]['name'], category[i]['grade'], category[i]['parentId'])
            try:
                # 执行sql语句
                print(sql)
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

            # 关闭数据库连接


        # result = json.loads(f['jd_union_open_goods_jingfen_query_response']['result'])['data']

    except Exception as e:
        print(e)
db.close()