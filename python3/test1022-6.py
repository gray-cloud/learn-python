#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

height = 1.75
weight = 60

bmi = weight // (height * height)

if bmi < 18.5:
    print('bmi指数为：', bmi, '过轻')
elif bmi >= 18.5 and bmi < 25:
    print('bmi指数为：', bmi, '正常')
elif bmi >= 25 and bmi < 28:
    print('bmi指数为：', bmi, '过重')
elif bmi >= 28 and bmi < 32:
    print('bmi指数为：', bmi, '肥胖')
else:
    print('bmi指数为：', bmi, '严重肥胖')
