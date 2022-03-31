# -*- coding:utf-8 -*-
"""
DateTime    :2022/3/31 15:26:24
Author      :chuanming
File        :numbertype
Description :number类型数据的定义和使用
*Copyright @ chuanming 2022. All rights reserved
"""

def numberclac():
    '''number类型运算'''
    # 整数运算
    print(1 + 2)        # 1. 加
    print(3 - 1)        # 2. 减
    print(10 * 3)       # 3. 乘
    print(10 / 3)       # 4. 除
    print(10 // 3)      # 5. 求商/取整
    print(10 % 3)       # 6. 取余/模
    print(2 ** 10)      # 7. 幂
    
    # 8.比较
    print(True)
    print(False)
    print(1 > 2)
    print(1 == 2)
    print(5 != 3)
    print(5 + 5 > 3 - 2)

     # 整型定义
    age = 99
    number = 10

    # 整形方法
    v1 = 5
    print(bin(v1))
    result = v1.bit_length()
    print(result)

    # 查看二进制有多少个位组成
    v2 = 10
    print(bin(10))
    result2 = v2.bit_length()
    print(result2)

    # 查看共轭复数
    v3 = complex(2, 4)
    v4 = 3 - 5j
    print(v3, v4)
    print(v3.real, v3.imag)
    print(v3.conjugate(), v4.conjugate(), v3.conjugate()+v4.conjugate())

    '''浮点数数据类型'''
    v1 = 3.14
    v2 = 9.89

    # 1. 浮点数转换为int型时,会将小数部分去掉
    print(int(3.14))
    # 2.使用round函数保留N位有效小数
    print(round(3.1415926, 4))
    # 3.浮点数精度上的计算问题
    v1 = 0.1
    v2 = 0.2
    v3 = v1 + v2
    print(v3)
    # 4.使用decimal解决精度问题
    import decimal
    v1 = decimal.Decimal('0.1')
    v2 = decimal.Decimal('0.2')
    print(v1 + v2)       
    
    # 3. 提示输入两个数字,计算两数之和
    num1 = float(input('数字1:'))
    num2 = float(input('数字2:'))
    print(num1, num2, int(num1 / num2))

def numberconvert():
    """数据类型的转换"""
    # 1. 布尔转整形
    print(True, int(True))
    print(False, int(False))
    # 2. 字符串转整形
    print('123', int('123'))
    #print('hello', int('hello'))
    # 3. 整形转字符串
    print(12, str(12))
    # 4. 布尔转整形
    print(True, str(True))
    print(False, str(False))
    # 5. 整形转布尔
    print(12, bool(12))
    print(0, bool(0))
    # 6. 字符串转布尔
    print('sasasa', bool('sasasa'))
    print('莎莎', bool('莎莎'))
    print('', bool(''))
    print(bool(1))
    print(bool(10))
    print(bool(0))

    # 布尔值转整型
    n1 = int(True)      # True转换为整数 1
    n2 = int(False)     # False转换为整数 0
    print('n1:'+n1,"n2:"+n2);

    # 8 浮点型（小数）
    print(int(8.7))

