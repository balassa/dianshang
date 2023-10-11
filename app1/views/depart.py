from django.shortcuts import render,redirect
from app1 import models

def depart_list(request):
    """部门列表"""
    queryset = models.Department.objects.all()

    return render(request,'depart_list.html',{'queryset':queryset})

def depart_add(request):
    """新建部门"""
    if request.method == 'GET':
        return render(request, 'depart_add.html')

    #获取用户POST提交过来的数据(title输入为空)
    title = request.POST.get("title")

    #保存到数据库
    models.Department.objects.create(title=title)

    #重定向回首页
    return redirect("/depart/list/")

def depart_delete(request):
    """删除部门"""

    #获取ID
    nid = request.GET.get('nid')

    #删除
    models.Department.objects.filter(id=nid).delete()

    # 重定向回首页
    return redirect("/depart/list/")

def depart_edit(request,nid):
    """修改部门"""
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()

        print(row_object.id,row_object.title)

        return render(request,'depart_edit.html', {"row_object":row_object})


    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)

    return redirect("/depart/list/")