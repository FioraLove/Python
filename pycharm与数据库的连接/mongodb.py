"""
pycharm与mongodb的连接：
  1.打开cmd ，依次进入D:\mongodb\bin\mongod
  2.cmd下，进入数据库存储data位置：mongod --dbpath D:\mongodb\data
  3.打开服务，启动mongodb
"""
# mongodb测试代码一：
from pymongo import MongoClient

class MongoTest:
    def __init__(self):
        self.client=MongoClient('localhost',27017)
        self.mongodb=self.client['Test1']
        self.user=self.mongodb['user']
        print(self.user)
    def insertdata(self):
        try:
            # self.user.insert_one({'name':'咋还','age':18,'sex':'男'})
              self.user.insert_many([
                  {'name':'咋还2','age':19,'sex':'男'},
                  {'name':'咋还3','age':20,'sex':'男'},
                  {'name':'咋还4','age':21,'sex':'男'}
              ])
        except:
              raise
        finally:
              self.client.close()

    def deletedata(self):
        try:
            # self.user.delete_one({'name': '咋还'})
            self.user.delete_many({'name':'咋还'})
        except:
            raise
        finally:
            self.client.close()

    def updatedata(self):
        try:
            #self.user.update({'name':'咋还2'},{'name':'咋还3'})#修改一条
            self.user.update_many({'name':'咋还3'},{'$set':{'name':'咋还4'}})#修改多条
        except:
            raise
        finally:
            self.client.close()
    def selectdata(self):
        try:

            resuleSet=self.user.find({'age':20})
            for item in resuleSet:
                print(item['name'])

        except:
            raise
        finally:
            self.client.close()
if __name__=='__main__':
        t=MongoTest()
        t.insertdata()
        t.deletedata()
        t.updatedata()
        t.selectdata()
        
        

# mongodb测试代码二：
"""
1.准备工作：
  启动mongodb服务
2.连接mongodb：
  import pymongo
  client = pymongo.MongoClient(host='localhost',port=27017)
  
3.指定数据库：
  db = client.test  # 调用test数据库

4.指定集合（类似于表）：
  collection = db.student # 指定student表

"""
