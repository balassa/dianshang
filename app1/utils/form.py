from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app1.utils.bootstrap import BootStrapModeForm
from app1 import models
from django import forms

class UserModelForm(BootStrapModeForm):
    name = forms.CharField(min_length=3,
                           label="用户名",
                           widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = models.UserInfo
        fields = ["name", "password","age","account","create_time","gender","depart"]

class PrettyModelForm(BootStrapModeForm):
    #验证方法1
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'),],
    )

    class Meta:
        model = models.PrettyNum
        #fields = ["mobile","price","level","status"]
        #exclude = ['level']
        fields = ["mobile", "price", "level", "status"]

        #验证方法2
        def clean_mobile(self):
            txt_mobile = self.cleaned_data['mobile']
            exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
            if exists:
                # 验证不通过
                raise ValidationError("手机号已存在")

            # 验证通过，用户输入的值返回
            return txt_mobile

class PrettyEditModelForm(BootStrapModeForm):
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'),],
    )

    class Meta:
        model = models.PrettyNum
        fields = ["mobile","price","level","status"]

        # 验证方法2
        def clean_mobile(self):
           # print(self.instance.pk)
            txt_mobile = self.cleaned_data["mobile"]
            exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
            if exists:
                # 验证不通过
                raise ValidationError("手机号已存在")
            # 验证通过，用户输入的值返回
            return txt_mobile
