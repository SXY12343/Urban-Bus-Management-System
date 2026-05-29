# encoding: utf-8
'''
@author: 李昂
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: view.py
@time: 2019/6/19 20:10
@desc:
'''

import json
from django.shortcuts import render
from shuJuKu.models import *


def dengLu(request):
    # 登陆管理
    return render(request, "denglu.html")

def getDengLu(request):
    # 用户登录后跳转页面
    username = request.POST.get("username")
    userpassword = request.POST.get("userpassword")
    response = Sysuser.objects.filter(loginname=username,password=userpassword)
    if response:
        for i in response:
            quan_xian = i.role.rolecode
            zhuang_tai = i.status
            if quan_xian == 0:
                return render(request, "index.html")
            if quan_xian == 1 and zhuang_tai == '启动':
                schedul_list = Scheduling.objects.all()
                return render(request,"form_basic_diao_du.html",{"schedul_list":schedul_list})
            elif quan_xian == 2 and zhuang_tai == '启动':
                schedul_list = Scheduling.objects.all()
                return render(request, "form_basic_look.html",{"schedul_list":schedul_list})
    else:
        return 0


def index(request):
    # 用户表管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = Sysuser.objects.all()
    return render(request,"index.html",{"user_list": my_list})


def che_liang(request):
    # 车辆表管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = Bus.objects.all()
    return render(request, 'che_liang.html',{"cheLiang_list": my_list})


def zhan_dian(request):
    # 站点表管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = Station.objects.all()
    return render(request, 'zhan_dian.html',{"zhanDian_list":my_list})


def xian_lu(request):
    # 线路表管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = Line.objects.all()
    a = {}
    for i in my_list:
        my_linecode = i.linecode
        response = LineStationRef.objects.filter(linecode=my_linecode)
        b = []
        for j in response:
            b.append(j.stationcode.stationname)
        a[my_linecode] = b
    return render(request, 'xian_lu.html',{"xianLu_list":my_list,"a":a})


def graph_flot(request):
    # 基础数据管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = Role.objects.all()
    my_list2 = Permission.objects.all()
    return render(request, 'graph_flot.html',{"role_list":my_list,"primission":my_list2})


def form_basic(request):
    # 排班表管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = Scheduling.objects.all()
    return render(request, 'form_basic.html',{"schedul_list":my_list})


def table_basic(request):
    # 关系数据管理
    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    my_list = RolePermissionRef.objects.all()
    my_list2 = LineStationRef.objects.all()
    return render(request, 'table_basic.html',{"guanXi_list":my_list,"guanXi2_list":my_list2})


# 处理表单
# 接收POST请求数据

# 用户操作
def save_user(request):
    all_list = {}
    # 保存员工信息增加数据
    if request.method == 'POST':
        code = request.POST.get('code')
        loginName = request.POST.get('loginName')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        idCard = request.POST.get('idCard')
        role = request.POST.get('role')
        driving = request.POST.get('driving')
        status = request.POST.get('status')
        if driving=='':
            driving = 0
        my_role = Role.objects.filter(rolename=role)
        for i in my_role:
            user = Sysuser(code=code,loginname=loginName,password=password,name=name,phone=phone,idcard=idCard,
                       role=i,driving=driving,status=status)
            user.save()
        all_list = {"code":code, "loginName":loginName, "password":password, "name":name,
                       "phone":phone, "idCard":idCard, "driving":driving,"status":status,"role":role}
    return render(request,'my_index.html',{"user_list2":all_list})


def delete_user(request):
    all_list = {}
    # 删除员工信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        Sysuser.objects.filter(code=aa).delete()
    return render(request, 'index.html')


def modify_user(request):
    # 修改员工信息
    if request.method == 'POST':
        code = request.POST.get('code')
        code2 = request.POST.get('code2')
        loginName = request.POST.get('loginName')
        password = request.POST.get('password')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        idCard = request.POST.get('idCard')
        role = request.POST.get('role')
        driving = request.POST.get('driving')
        status = request.POST.get('status')
        if driving=='':
            driving = 0
        my_role = Role.objects.filter(rolename=role)
        for i in my_role:
            Sysuser.objects.filter(code=code).update(code=code2,loginname=loginName,password=password,
                             role=i,name=name,phone=phone,idcard=idCard,driving=driving,status=status)
    return render(request, 'index.html')


def chaXun_user(request):
    if request.method == 'POST':
        one = request.POST.get('one')
        two = request.POST.get('two')
        response = Sysuser.objects.filter(loginname=one,status=two)
        return render(request,'index_find.html',{'find_user_list':response})




# 车辆操作
def che_save(request):
    all_list = {}
    # 保存车辆信息增加数据
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        busLicense = request.POST.get('busLicense')
        busType = request.POST.get('busType')
        busStatus = request.POST.get('busStatus')
        startTime = request.POST.get('startTime')
        this_bus = Bus(buscode=busCode,buslicense=busLicense,bustype=busType,busstatus=busStatus,
                       starttime=startTime)
        this_bus.save()
    return render(request,'che_liang.html')


def che_delete(request):
    all_list = {}
    # 删除车辆信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        Bus.objects.filter(buscode=aa).delete()
    return render(request, 'che_liang.html')


def che_modify(request):
    all_list = {}
    # 修改车辆信息
    if request.method == 'POST':
        busCode = request.POST.get('busCode')
        busCode2 = request.POST.get('busCode2')
        busLicense = request.POST.get('busLicense')
        busType = request.POST.get('busType')
        busStatus = request.POST.get('busStatus')
        startTime = request.POST.get('startTime')
        Bus.objects.filter(buscode=busCode).update(buscode=busCode2,buslicense=busLicense,bustype=busType,busstatus=busStatus,
                       starttime=startTime)
    return render(request,'che_liang.html')

def chaXun_che(request):
    if request.method == 'POST':
        one = request.POST.get('one')
        two = request.POST.get('two')
        response = Bus.objects.filter(buslicense=one,busstatus=two)
        return render(request,'che_liang_find.html',{'find_user_list':response})




# 站点
def zhan_dian_save(request):
    all_list = {}
    # 保存站点信息增加数据
    if request.method == 'POST':
        stationCode = request.POST.get('stationCode')
        stationName = request.POST.get('stationName')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        region = request.POST.get('region')
        street = request.POST.get('street')
        this_zhan_dian = Station(stationcode=stationCode,stationname=stationName,longitude=longitude,
                                 latitude=latitude,region=region,street=street)
        this_zhan_dian.save()
    return render(request,'zhan_dian.html')

def zhan_dian_delete(request):
    all_list = {}
    # 删除站点信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        Station.objects.filter(stationcode=aa).delete()
    return render(request, 'zhan_dian.html')

def zhan_dian_modify(request):
    all_list = {}
    # 修改站点信息
    if request.method == 'POST':
        stationCode = request.POST.get('stationCode')
        stationCode2 = request.POST.get('stationCode2')
        stationName = request.POST.get('stationName')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')
        region = request.POST.get('region')
        street = request.POST.get('street')
        Station.objects.filter(stationcode=stationCode).update(stationcode=stationCode2,stationname=stationName,longitude=longitude,
                                 latitude=latitude,region=region,street=street)
    return render(request,'zhan_dian.html')

def chaXun_zhan_dian(request):
    if request.method == 'POST':
        one = request.POST.get('one')
        two = request.POST.get('two')
        three = request.POST.get('three')
        response = Station.objects.filter(stationname=one,region=two,street=three)
        return render(request,'zhan_dian_find.html',{'find_user_list':response})




# 线路
def xian_lu_save(request):
    all_list = {}
    # 保存线路信息增加数据
    if request.method == 'POST':
        lineCode = request.POST.get('lineCode')
        lineName = request.POST.get('lineName')
        status = request.POST.get('status')
        startLineTime = request.POST.get('startLineTime')
        direction = request.POST.get('direction')
        xian_lu_dian = Line(linecode=lineCode,linename=lineName,status=status,
                                 startlinetime=startLineTime,direction=direction)
        xian_lu_dian.save()
    return render(request,'xian_lu.html')

def xian_lu_delete(request):
    all_list = {}
    # 删除线路信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        Line.objects.filter(linecode=aa).delete()
    return render(request, 'xian_lu.html')

def xian_lu_modify(request):
    all_list = {}
    # 修改线路信息
    if request.method == 'POST':
        lineCode = request.POST.get('lineCode')
        lineCode2 = request.POST.get('lineCode2')
        lineName = request.POST.get('lineName')
        status = request.POST.get('status')
        startLineTime = request.POST.get('startLineTime')
        direction = request.POST.get('direction')
        xian_lu_dian = Line.objects.filter(linecode=lineCode).update(linecode2=lineCode2,linename=lineName,status=status,
                                 startlinetime=startLineTime,direction=direction)
        xian_lu_dian.save()
    return render(request,'xian_lu.html')

def chaXun_xian_lu(request):
    if request.method == 'POST':
        one = request.POST.get('one')
        two = request.POST.get('two')
        three = request.POST.get('three')
        response = Line.objects.filter(linename=one,direction=two,status=three)
        print(response)
        return render(request,'xian_lu_find.html',{'find_user_list':response})




# 排班
def pai_ban_save(request):
    # 保存排班信息增加数据
    all_list1 = {}  # 存储线路编号
    all_list2 = {}  # 存储车牌号
    all_list3 = {}  # 存储司机编号
    all_list4 = {}  # 存储始发站
    all_list5 = {}  # 存储终点站

    for i in Line.objects.all():
        all_list1[i] = i.linecode

    for i in Bus.objects.all():
        # 判断汽车是否启运
        if i.busstatus == '启运':
            all_list2[i] = i.buslicense
        else:
            continue


    for i in Sysuser.objects.all():
        # 判断是否为司机
        k = i.role.rolecode
        if k == 2:
            all_list3[i] = i.code
        else:
            continue


    for i in Station.objects.all():
        all_list4[i] = i.stationname

    for i in Station.objects.all():
        all_list5[i] = i.stationname

    if request.method == 'POST':
        code = request.POST.get('code')
        lineCode = request.POST.get('lineCode')
        busLicense = request.POST.get('busLicense')
        tcNumber = request.POST.get('tcNumber')
        tcTime = request.POST.get('tcTime')
        userCode = request.POST.get('userCode')
        startStation = request.POST.get('startStation')
        endStation = request.POST.get('endStation')

        user = Scheduling(code=code)
        # 线路编号
        lineCode = Line.objects.filter(linecode=lineCode)
        for i in lineCode:
            user.linecode = i

        # 车牌号
        busLicense = Bus.objects.filter(buslicense=busLicense)
        for i in busLicense:
            user.buslicense = i

        # 趟次
        user.tcnumber = tcNumber
        # 每趟时间
        user.tctime = tcTime

        # 司机编号
        userCode = Sysuser.objects.filter(code=userCode)
        for i in userCode:
            user.usercode = i

        # 始发站
        startStation = Station.objects.filter(stationname=startStation)
        for i in startStation:
            user.startstation = i

        # 终点站
        endStation = Station.objects.filter(stationname=endStation)
        for i in endStation:
            user.endstation = i

        user.save()

    return render(request,'form_basic.html',{"lineCode":all_list1,"busLicense":all_list2,"userCode":all_list3,
                    "startStation":all_list4,"endStation":all_list5})


def pai_ban_delete(request):
    all_list = {}
    # 删除排班信息
    if request.method == 'POST':
        aa = request.POST.get("my_delete")
        Scheduling.objects.filter(code=aa).delete()
    return render(request, 'form_basic.html')


def pai_ban_modify(request):
    # 修改排班信息
    all_list1 = {}  # 存储线路编号
    all_list2 = {}  # 存储车牌号
    all_list3 = {}  # 存储司机编号
    all_list4 = {}  # 存储始发站
    all_list5 = {}  # 存储终点站

    for i in Line.objects.all():
        all_list1[i] = i.linecode

    for i in Bus.objects.all():
        # 判断汽车是否启运
        if i.busstatus == '启运':
            all_list2[i] = i.buslicense
        else:
            continue


    for i in Sysuser.objects.all():
        # 判断是否为司机
        k = i.role.rolecode
        if k == 2:
            all_list3[i] = i.code
        else:
            continue


    for i in Station.objects.all():
        all_list4[i] = i.stationname

    for i in Station.objects.all():
        all_list5[i] = i.stationname

    if request.method == 'POST':
        code = request.POST.get('code')
        code2 = request.POST.get('code2')
        lineCode = request.POST.get('lineCode')
        busLicense = request.POST.get('busLicense')
        tcNumber = request.POST.get('tcNumber')
        tcTime = request.POST.get('tcTime')
        userCode = request.POST.get('userCode')
        startStation = request.POST.get('startStation')
        endStation = request.POST.get('endStation')

        user = Scheduling.objects.filter(code=code).update(code=code2)


        # 线路编号
        lineCode = Line.objects.filter(linecode=lineCode)
        for i in lineCode:
            user.linecode = i

        # 车牌号
        busLicense = Bus.objects.filter(buslicense=busLicense)
        for i in busLicense:
            user.buslicense = i

        # 趟次
        user.tcnumber = tcNumber
        # 每趟时间
        user.tctime = tcTime

        # 司机编号
        userCode = Sysuser.objects.filter(code=userCode)
        for i in userCode:
            user.usercode = i

        # 始发站
        startStation = Station.objects.filter(stationname=startStation)
        for i in startStation:
            user.startstation = i

        # 终点站
        endStation = Station.objects.filter(stationname=endStation)
        for i in endStation:
            user.endstation = i

        user.save()
    return render(request,'form_basic.html',{"lineCode":all_list1,"busLicense":all_list2,"userCode":all_list3,
                    "startStation":all_list4,"endStation":all_list5})


def chaXun_pai_ban(request):
    if request.method == 'POST':
        one = request.POST.get('one')
        two = request.POST.get('two')
        three = request.POST.get('three')
        response = Scheduling.objects.filter(code=one,tcnumber=two,tctime=three)
        return render(request,'form_basic_find.html',{'schedul_list2':response})
