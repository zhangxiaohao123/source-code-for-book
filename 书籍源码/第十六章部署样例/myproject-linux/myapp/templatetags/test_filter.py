from django import template #导入模板模块
register=template.Library() #取出注册库，固定写法
@register.filter(name='coderstatus')#注册过滤器的名字为coderstatus
def coder_status(value,arg):
    if value=='morehair':
        return "{}是菜鸟程序员".format(arg)
    if value=="middlehair":
        return "{}是工程师级程序员".format(arg)
    if value=='fewhair':
        return "{}是资深程序员".format(arg)
