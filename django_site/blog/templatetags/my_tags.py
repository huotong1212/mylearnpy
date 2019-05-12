from django import template
from django.utils.safestring import mark_safe

register = template.Library() # register名字固定，不可改变

@register.filter   # 过滤器，{{ var|filter_name:参数 }} 参数只能是两个，一个参数是变量var ，一个是参数是后面的那个参数
def multi(x,y):
    return x*y  # 自定义过滤器函数的参数只能两个，可以进行逻辑判断

@register.simple_tag # 标签  {% simple_tag 参数1 参数2 ... %}
def addtags(x,y,z):
    return x+y+z   # 自定义标签无参数限制，不能进行逻辑判断

@register.simple_tag # 标签
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" % (id, arg,)
    return mark_safe(result)