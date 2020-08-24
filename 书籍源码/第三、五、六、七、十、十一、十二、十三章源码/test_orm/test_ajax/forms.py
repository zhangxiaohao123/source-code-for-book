from django import forms
class person_form(forms.Form):
    id=forms.IntegerField(label='',widget=forms.widgets.NumberInput(attrs={'hidden':'true'}), required=False)
    name=forms.CharField(
        label='姓名',
        error_messages={
            "required": "字段不为为空",
            "invalid": "格式错误"
        },
        widget=forms.widgets.TextInput(attrs={'class':'form-control', "placeholder":"请输入姓名","autofocus":True}))

    email=forms.EmailField(
        label='邮箱',
        error_messages={
            "required": "字段不为为空",
            "invalid": "格式错误，请录入邮箱格式"
        },
        widget=forms.widgets.EmailInput(attrs={'class':'form-control', "placeholder":"请输入邮箱"}))

    salary=forms.DecimalField(
        label='薪金',
        error_messages={
            "required": "字段不为为空",
            "invalid": "格式错误,请录入数字"
        },
        widget=forms.widgets.NumberInput(attrs={'class':'form-control', "placeholder":"请输入薪金"}))



