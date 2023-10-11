from django.shortcuts import render,redirect
from app1 import models
from app1.utils.form import UserModelForm


def user_list(request):
    """用户管理"""


    queryset = models.UserInfo.objects.all()

    return render(request, 'user_list.html', {"queryset": queryset})

def user_add(request):
    """添加用户"""

    if request.method == "GET":
        context = {
            'gender_choices':models.UserInfo.gender_choices,
            'depart_list':models.Department.objects.all()
        }
        return render(request,'user_add.html', context)

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender_id = request.POST.get('gd')
    depart_id = request.POST.get('dp')
    models.UserInfo.objects.create(name=user,password=pwd,age=age,account=account,
                                   create_time=ctime,gender=gender_id,depart_id=depart_id)

    return redirect("/user/list/")

def user_model_form_add(request):
    """添加用户（ModelForm版本）"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request,'user_model_form_add.html',{"form":form})

    form = UserModelForm(data=request.POST)
    if form.is_valid():

       form.save()
       return redirect('/user/list/')

    #校验失败（在页面上显示错误信息）
    return render(request, 'user_model_form_add.html', {"form": form})

def user_edit(request, nid):
    """编辑用户"""
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == "GET":

        form = UserModelForm(instance=row_object)
        return render(request,'user_edit.html',{'form':form})

    form = UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        #默认保存的是用户输入的所有数据
        form.save()
        return  redirect('/user/list/')
    return render(request,'user_edit.html',{"form":form})

def user_delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')