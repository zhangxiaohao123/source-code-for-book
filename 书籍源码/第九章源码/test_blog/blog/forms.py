from django import forms
from . import models
from django.core.exceptions import ValidationError

class reg_form(forms.Form):
    username=forms.CharField(
        max_length=20,
        label='登录账号',
        error_messages={
            "max_length":"登录账号不能超过20位",
            "required":"登录账号不能为空"
        },
        widget=forms.widgets.TextInput(
            attrs={"class":"form-control"},
        )
    )
    password=forms.CharField(
        min_length=6,
        label='密码',
        error_messages={
            'min_length':'密码最少6位',
            "required":"密码不能为空",
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class':'form-control'},
            render_value=True,
        )
    )
    repassword = forms.CharField(
        min_length=6,
        label='确认密码',
        error_messages={
            'min_length': '密码最少6位',
            "required": "密码不能为空",
        },
        widget=forms.widgets.PasswordInput(
            attrs={'class': 'form-control'},
            render_value=True,
        )
    )
    nikename=forms.CharField(
        max_length=20,
        required=False,
        label='姓名',
        error_messages={
            'max_length':'姓名长度不能超过20位',
        },
        initial='无名氏',
        widget=forms.widgets.TextInput(
            attrs={'class':'form-control'}
        )
    )
    email=forms.EmailField(
        label='邮箱',
        error_messages={
            'invalid':'邮箱格式不对',
            'required':'邮箱不能为空',

        },
        widget=forms.widgets.EmailInput(
            attrs={'class': 'form-control',}
        )
    )
    telephone=forms.CharField(
        label='联系电话',
        required=False,
        error_messages={
            'max_length':'最大长度不超过11位',
        },
        widget=forms.widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    head_img=forms.ImageField(
        label='头像',
        widget=forms.widgets.FileInput(
            attrs={'style': "display: none"}
        )
    )

    def clean_username(self): #重写username字段校验函数
        uname=self.cleaned_data.get('username')
        vexist=models.loguser.objects.filter(username=uname)
        if vexist:
            self.add_error('username',ValidationError('登录账号已存在!'))
        else:
            return uname
    def clean_repassword(self):
        passwd=self.cleaned_data.get('password')
        repasswd=self.cleaned_data.get('repassword')
        #print(repasswd)
        if repasswd and repasswd != passwd:
            self.add_error('repassword', ValidationError('两次录入密码不一致'))
            #raise ValidationError('两次密码不一致')
        else:
            return repasswd



"""
"""
