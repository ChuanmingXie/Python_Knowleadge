# -*- coding:utf-8 -*-
"""
DateTime    :2022/4/4 21:45:00
Author      :chuanming
File        :db_orm_peewee
Description :
*Copyright @ chuanming 2022. All rights reserved
"""
# 引入Peewee包的所有内容
from peewee import *

# 建立一个SQLite数据库引擎对象,该引擎代开数据库文件sampleDB.db
db=SqliteDatabase("sampleDB.db")

# 定义一个ORM基类, 在基类中指定本ORM所使用的数据库
# 这样在之后的子类中就不用重复声明数据库了
class BaseModel(Model):
    class Meta:
        database=db

# 定义Course表,继承自BaseModel
class Course(BaseModel):
    """定义课程表"""
    id=PrimaryKeyField()
    title=CharField(null=false)
    period=IntegerField()
    description=CharField()
    
    class Meta:
        order_by=('title')
        db_table='course'       # 定义数据库中的表名

class Teacher(BaseModel):
    """定义老师表"""
    id=PrimaryKeyField()
    name=CharField(null=false)
    gender=BooleanFiled()
    adderss=CharField()
    course_id=ForeignKeyField(Course,to_field='id',related_name="course")
    
    class Meta:
        order_by=('name')
        db_table='teacher'

def OperationORM():
    Course.create_table()
    Teacher.create_table()

    Course.create(id=1,title='经济学',period=320,description='文理科学生均可选修')
    Course.create(id=2,title='大学英语',period=300,description='大一学生必修课')
    Course.create(id=3,title='哲学',period=100,description='必修课')
    Course.create(id=104,title='编译原理',period=100,description='计算机选修')

    Teacher.create(name='柏乡里',gender=True,adderss='......',course_id=1)
    Teacher.create(name='李想僧',gender=True,adderss='......',course_id=3)
    Teacher.create(name='张乾文',gender=False,adderss='......',course_id=2)

    # 查询一行
    record=Course.get(title='大学英语')
    print(f"课程{record.title}-学时{record.period}")

    # 更新
    record.period=200
    record.save()

    # 删除
    record.delete_instacne()

    # 查询所有记录
    courses=Course.select()

    # 待条件查询,并将结果按period字段倒叙排序
    courses=Course.select().where(Course.id<10).order_by(Course.period.desc())

    # 统计所有课程的平均学时
    courses=Course.select(fn.Avg(Course.period).alias('avg_period'))

    # 更新多个记录
    Course.Update(period=300).where(Course.id>100).execute()

    # 多表连接操作，Peewee会自动根据ForeignKeyField的外键进行连接
    Record = Course.select().join(Teacher).Where(gender=True)


OperationORM()