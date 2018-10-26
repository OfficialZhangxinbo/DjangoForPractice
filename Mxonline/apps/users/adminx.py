# -*- coding:utf-8 -*-

import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "昕课堂后台管理系统"
    site_footer = "昕课堂"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time'] # 后台显示列表
    search_fields = ['code', 'email', 'send_type'] # 后台查询选项，时间不作为查询项
    list_filter = ['code', 'email', 'send_type', 'send_time'] # 后台搜索选项


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']  # 后台显示列表
    search_fields = ['title', 'image', 'url', 'index']  # 后台查询选项，时间不作为查询项
    list_filter = ['title', 'image', 'url', 'index', 'add_time']  # 后台搜索选项


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
