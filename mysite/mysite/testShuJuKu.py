# encoding: utf-8
'''
@author: 李昂
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: testShuJuKu.py
@time: 2019/6/22 23:22
@desc:
'''

# -*- coding: utf-8 -*-

from django.shortcuts import render

from shuJuKu.models import Bus

def shuJuKu(request):
    #车辆表管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = Bus.objects.all()
    return render(request, 'test.html', {"people_list":my_list})
