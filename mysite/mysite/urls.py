"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# url网页目录
from django.urls import path,re_path
from . import view

urlpatterns = [
    # 两个必选参数：route、view 和两个可选参数：kwargs、name
    # route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
    # view: 用于执行与正则表达式匹配的 URL 请求。
    # kwargs: 视图使用的字典类型的参数。
    # name: 用来反向获取 URL。
    # path('', view.hello),

    # Django >= 2.0 的版本，urls.py的django.conf.urls已经被django.urls取代
    # Django >= 2.0 的版本，path() 函数无法匹配正则表达式，需要使用 re_path() 即可匹配正则表达式
    # 首页
    re_path(r'^$',view.dengLu),

    # 登录后接受表单跳转页面
    path('tiao_zhuan',view.getDengLu,name="dengLu"),

    # 选择其他按钮后跳转页面
    path('denglu',view.dengLu,name="deng_lu"),
    path('index',view.index,name='index'),
    path('che_liang',view.che_liang,name='che_liang'), # 这里设置name，为了在模板文件中，写name，就能找到这个路由
    path('zhan_dian',view.zhan_dian,name='zhan_dian'),
    path('xian_lu',view.xian_lu,name='xian_lu'),
    path('graph_flot',view.graph_flot,name='graph_flot'),
    path('form_basic',view.form_basic,name='form_basic'),
    path('table_basic',view.table_basic,name='table_basic'),
    # 员工
    path('my_index',view.save_user,name="form"),
    path('my_delete',view.delete_user,name="form2"),
    path('my_modify',view.modify_user,name="form3"),
    path('index_find',view.chaXun_user,name="form4"),
    # 车辆
    path('che_liang_index',view.che_save,name="che_liang_form"),
    path('che_liang_delete',view.che_delete,name="che_liang_form2"),
    path('che_liang_modify',view.che_modify,name="che_liang_form3"),
    path('che_liang_find',view.chaXun_che,name="che_liang_form4"),
    # 站点
    path('zhan_dian_index',view.zhan_dian_save,name="zhan_dian_form"),
    path('zhan_dian_delete',view.zhan_dian_delete,name="zhan_dian_form2"),
    path('zhan_dian_modify',view.zhan_dian_modify,name="zhan_dian_form3"),
    path('zhan_dian_find',view.chaXun_zhan_dian,name="zhan_dian_form4"),
    # 线路
    path('xian_lu_index',view.xian_lu_save,name="xian_lu_form"),
    path('xian_lu_delete',view.xian_lu_delete,name="xian_lu_form2"),
    path('xian_lu_modify',view.xian_lu_modify,name="xian_lu_form3"),
    path('xian_lu_find',view.chaXun_xian_lu,name="xian_lu_form4"),
    # 排班
    path("pai_ban_index",view.pai_ban_save,name="pai_ban_form"),
    path("pai_ban_delete",view.pai_ban_delete,name="pai_ban_form2"),
    path("pai_ban_modify",view.pai_ban_modify,name="pai_ban_form3"),
    path("form_basic_find",view.chaXun_pai_ban,name="pai_ban_form4"),
]
