from django.conf import settings
import re
def init_permission(request, user_obj):
    """
    初始化用户权限, 写入session
    :param request: 
    :param user_obj: 
    :return: 
    """
    permission_item_list = user_obj.roles.values('permissions__id',
                                                 'permissions__title',
                                                 'permissions__url',
                                                 'permissions__perm_code',
                                                 'permissions__pid_id',#组内菜id,null为二级菜单
                                                 'permissions__perm_group_id',
                                                 'permissions__perm_group__menu_id',
                                                 'permissions__perm_group__menu__title',
                                                 ).distinct()
    #print(permission_item_list)
    permission_url_list = {} # 以权限组per_group_id为分组标准，取得用户权限中url,code，--> 用于中间件验证用户权限
    permission_menu_list = []  # 取用户权限的内容，[{"title":xxx, "url":xxx, "menu_id": xxx},{},]

#取出用户的权限
    for item in permission_item_list:
        perm_group_id=item['permissions__perm_group_id']
        url=item['permissions__url']
        # 针对django 2.0 path中URL表达式，修改成常规正则表达式
        url = re.sub('<int:\w+>', '[0-9]+', url)
        url = re.sub('<str:\w+>', '[^/]+', url)
        url = re.sub('<slug:\w+>', '[-a-zA-Z0-9_]+', url)
        url = re.sub('<uuid:\w+>', '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', url)
        url = re.sub('<path:\w+>', '.+', url)
        perm_code=item['permissions__perm_code']
        if perm_group_id in permission_url_list:
            permission_url_list[perm_group_id]['codes'].append(perm_code)
            permission_url_list[perm_group_id]['urls'].append(url)
        else:
            permission_url_list[perm_group_id]={'codes':[perm_code,],
                                               'urls':[url,]}
    request.session[settings.PERMISSION_URL_KEY]=permission_url_list
    #print(permission_url_list)


#取权限表记录(用于生成页面菜单)
    for item in permission_item_list:
        # 针对django 2.0 path中URL表达式，修改成常规正则表达式
        url = item['permissions__url']
        url = re.sub('<int:\w+>', '[0-9]+', url)
        url = re.sub('<str:\w+>', '[^/]+', url)
        url = re.sub('<slug:\w+>', '[-a-zA-Z0-9_]+', url)
        url = re.sub('<uuid:\w+>', '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', url)
        url = re.sub('<path:\w+>', '.+', url)
        tpl={
            'id':item['permissions__id'],
            'title':item['permissions__title'],
            'url':url,
            'pid_id':item['permissions__pid_id'],
            'menu_id':item['permissions__perm_group__menu_id'],
            'menu_title':item['permissions__perm_group__menu__title']
        }
        permission_menu_list.append(tpl)
    #print("取权限表记录",permission_menu_list)
    request.session[settings.PERMISSION_MENU_KEY]=permission_menu_list
