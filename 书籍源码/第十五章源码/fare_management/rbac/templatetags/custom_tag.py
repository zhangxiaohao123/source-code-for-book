from django import template
from django.conf import settings
import re,os
from django.utils.safestring import mark_safe

register = template.Library()


def get_structure_data(request):
    """处理菜单结构"""
    current_url= request.path_info

    perm_menu = request.session[settings.PERMISSION_MENU_KEY]
    #print('custom_tag',perm_menu)

    # 取出是权限菜单（二级菜单），判断依据，pid_id为空即为二级菜单
    menu_dict = {}

    for item in perm_menu:
        if not item["pid_id"]: #pid_id为null
            menu_dict[item["id"]]=item.copy()
    #print('menu_dict1', menu_dict)

    for item in perm_menu:
        regex="^{0}$".format(item["url"])
        if  re.match(regex,current_url):#如果是url匹配，就设置权限菜单active为True
            #print(current_url)
            if not item["pid_id"]:
                menu_dict[item["id"]]["active"]=True
            else:
                menu_dict[item["pid_id"]]["active"]=True #非权限菜单记录，把本记录所在组的权限菜单设置active

    #print('menu_dict1', menu_dict)

    #print('for2_per_menu', perm_menu)
    #形成一级二级菜单数据
    menu_result={}
    for item in menu_dict.values():
        active=item.get("active")
        menu_id=item.get("menu_id")
        if menu_id in menu_result:
            menu_result[menu_id]["children"].append({'title':item['title'],'url':item['url'],'active':active})
            if active:
                menu_result[menu_id]["active"]=True #设置一级菜单active为True
        else:
            menu_result[menu_id]={
                'menu_id':menu_id,
                'menu_title':item['menu_title'],
                'active':active,
                'children':[
                    {'title': item['title'], 'url': item['url'], 'active': active}
                ]
            }

    #print(menu_result)

    #print('2_per_menu', request.session[settings.PERMISSION_MENU_KEY])
    return menu_result




@register.inclusion_tag("rbac_menu.html")
def rbac_menu(request):
    menu_data = get_structure_data(request)

    return {'menu_result':menu_data}



# @register.simple_tag
# def rbac_css():
#     """
#     rabc要用到的css文件路径，并读取返回；注意返回字符串用mark_safe，否则传到模板会转义
#     :return:
#     """
#     css_path = os.path.join('rbac', 'style_script','rbac.css')
#     css = open(css_path,'r',encoding='utf-8').read()
#     return mark_safe(css)
#
#
# @register.simple_tag
# def rbac_js():
#     """
#     rabc要用到的js文件路径，并读取返回
#     :return:
#     """
#     js_path = os.path.join('rbac', 'style_script', 'rbac.js')
#     js = open(js_path, 'r', encoding='utf-8').read()
#     return mark_safe(js)



