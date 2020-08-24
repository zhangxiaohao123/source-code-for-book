from django import forms


#------开始的
class test_form(forms.Form):
    account=forms.CharField(label="账户")
    password=forms.CharField(label='密码')



class test_widget(forms.Form):
    username = forms.CharField(
        min_length=2,
        label="用户名",
        initial="张三"  # 设置默认值
    )
    pwd = forms.CharField(
        min_length=8,
        label="密码",
        widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True)
    )

    date=forms.DateField()
    time=forms.TimeField()
    dt=forms.DateTimeField()

    inter=forms.IntegerField(max_value=100, min_value=10)
    fl=forms.FloatField(max_value=199.88, min_value=10.66)
    de=forms.DecimalField(max_value=2199.88, min_value=210.37,max_digits=7,decimal_places=2)
    sex = forms.ChoiceField(
        choices=((1, '男'), (2, '女'),),
        initial=1
    )
    gender = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )
    hobby = forms.fields.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
    hobby1 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )


class login_formold(forms.Form):
    account = forms.CharField(
        min_length=2,
        label="账号",
    )
    pwd = forms.CharField(
        min_length=6,
        label="密  码",
        widget=forms.widgets.PasswordInput(attrs={'class': 'password'}, render_value=True)
    )

class login_form(forms.Form):
    account = forms.CharField(
        min_length=2,
        label="账号",
        widget=forms.widgets.TextInput(attrs={"class":"form-control", "placeholder":"请输入账号","autofocus":True})
    )
    pwd = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(attrs={"class":"form-control", "placeholder":"请输入密码"}, render_value=True)
    )

class loguser_form(forms.Form):
    id=forms.IntegerField(label='',widget=forms.widgets.NumberInput(attrs={'hidden':'true'}), required=False)
    account=forms.CharField(
        label='账号',
        widget=forms.widgets.TextInput(attrs={'class':'form-control', "placeholder":"请输入账号","autofocus":True}))
    password=forms.CharField(
        label='密码',
        widget=forms.widgets.TextInput(attrs={'class':'form-control', "placeholder":"请输入密码"}))
    email=forms.EmailField(
        label='邮箱',
        widget=forms.widgets.EmailInput(attrs={'class':'form-control', "placeholder":"请输入邮箱"}))
    gander=forms.ChoiceField(
        choices=((1, "男"), (2, "女"),),
        label='性别',
        initial='1',
        widget=forms.widgets.RadioSelect())
    hobby = forms.ChoiceField(
        choices=((1, "游泳"), (2, "自行车"), (3, "跑酷"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
    hair=forms.ChoiceField(
        label='发量',
        choices=((1,'很多'),(2,'一般'),(3,'很少'),),
        widget=forms.widgets.RadioSelect())
    img=forms.ImageField(label='头像',required=False)

#===================ModelForm==========

from . import models
class loguser_modelform(forms.ModelForm):
    gander = forms.ChoiceField(
        choices=((1, "男"), (2, "女"),),
        label='性别',
        initial='1',
        widget=forms.widgets.RadioSelect())
    hobby = forms.ChoiceField(
        choices=((1, "游泳"), (2, "自行车"), (3, "跑酷"),),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
    hair = forms.ChoiceField(
        label='发量',
        choices=((1, '很多'), (2, '一般'), (3, '很少'),),
        widget=forms.widgets.RadioSelect())
    class Meta:
        model=models.loguser
        fields="__all__"
        labels={
            'account':'账户',
            'password': '密码',
            'email':'邮箱',
            'img':'头像'
        }
        widgets = {
            'account':forms.widgets.TextInput(attrs={'class':'form-control', "placeholder":"请输入账号","autofocus":True}),
            'password':forms.widgets.TextInput(attrs={'class':'form-control', "placeholder":"请输入密码"}),
            'email':forms.widgets.EmailInput(attrs={'class':'form-control', "placeholder":"请输入邮箱"})
        }




