from django import template

register=template.Library()
@register.simple_tag(name="test_simpletag")
def test_simpletag(arg1,arg2,arg3):
    return "这是一个simpletag样例，它接受参数分别是:{}、{}、{}".format(arg1,arg2,arg3)

@register.inclusion_tag('inclusion_tag_html.html')
def test_inclusiontag(name):
    name1 = "{}的经历如下：".format(name)
    data=["初级程序员，头发浓密","中级程序员，头发不多不少","高级程序员，发量日渐稀少"]
    return {"name":name1,"data": data}

