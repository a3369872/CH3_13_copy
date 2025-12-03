from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from myapp.models import *
from django.forms.models import model_to_dict

# def test(request):
    # datas = Student.objects.all() #QuerySet 內為Student物件
    # # print(datas)
    # for data in datas:
    #     print(model_to_dict(data)) #物件轉字典
######################################################
    # datas = Student.objects.values('cID','cName','cPhone','cAddr')
    # # print(datas)
    # for data in datas:
    #     print(data)
######################################################
    # datas = Student.objects.values('cSex').distinct()
    # for data in datas:
    #     print(data)
######################################################
    # data = Student.objects.get(cID=8)
    # print(model_to_dict(data))
######################################################
    # datas = Student.objects.filter(cSex='F')
    # for data in datas:
    #     print(model_to_dict(data))
######################################################
    #__gte >= 大於等於 greater than or equal 
    #__lte <= 小於等於 less then or equal
    # datas = Student.objects.filter(cID__gt=5,cSex='M')
    # for data in datas:
    #     print(model_to_dict(data))
    # from django.db.models import Q
    # datas = Student.objects.filter(~Q(cID__gt=5),cSex='M')
    # # datas = Student.objects.filter(~Q(cID__gt=5) & Q(cSex='M'))
    # for data in datas:
    #     print(model_to_dict(data))
    # datas = Student.objects.filter(
    #     Q(cID=1)|Q(cID__gte=8) #顯示為cID 1、8、9、10
    # )
    # for data in datas:
    #     print(model_to_dict(data))
######################################################
    # datas = Student.objects.filter(cID__range=[4,6]) # 4到6區間，顯示cID 4、5、6
    # for data in datas:
    #     print(model_to_dict(data))
######################################################
    # datas = Student.objects.filter(cID__in=[1,5,7,9]) #篩選，顯示cID 1、5、7、9
    # for data in datas:
    #     print(model_to_dict(data))
######################################################
    # datas = Student.objects.filter(cPhone__startswith='0918') #查找開頭為 0918 資料
    # for data in datas:
    #     print(model_to_dict(data))

    # datas = Student.objects.filter(cAddr__contains='建國') #查找為 建國 資料
    # for data in datas:
    #     print(model_to_dict(data))
######################################################
    # datas = Student.objects.all().order_by("cBirthday") # 排序，依生日排序
    # for data in datas:
    #     print(model_to_dict(data))

    # datas = Student.objects.all().order_by("cSex","cBirthday") # 排序，先性別排序再生日排序
    # for data in datas:
    #     print(model_to_dict(data))
######################################################
    # datas = Student.objects.all()[0:2] #顯示1、2
    # for data in datas:
    #     print(model_to_dict(data))

    # datas = Student.objects.all()[1:3] #顯示2、3
    # for data in datas:
    #     print(model_to_dict(data))

    # datas = Student.objects.all()[3:7] #顯示4、5、6、7
    # for data in datas:
        # print(model_to_dict(data))
######################################################
    # from django.db.models import Sum,Count,Max,Min,Avg
    # data = Scorelist.objects.aggregate(Sum('score'))
    # print(data)
    # data = Scorelist.objects.filter(course="國文").aggregate(Avg('score')) 
    # print(data)
######################################################
    # datas = Scorelist.objects.values_list('cID').annotate(Sum('score')) #顯示 cID 和 score總分
    # for data in datas:
    #     print(data)
######################################################
    # datas = Scorelist.objects.filter(cID__lte=5).values_list('cID').annotate(Sum('score'))
    # for data in datas:
    #     print(data)
######################################################
    #新增
    # student_exists = Student.objects.filter(cName="San2").exists()
    # if not student_exists:
    #     add = Student(cName="San2",cSex="M",cBirthday="2025-10-28"
    #                   ,cEmail="San@gmai.com",cPhone="0987654321",cAddr="桃園"
    #                   ,cHeight=180,cWeight=70)
    #     add.save()
    #     print("資料已新增")
    # else:
    #     print("資料已存在,為新增成功")
    # if not student_exists:
    #     Student.objects.create(cName="San2",cSex="M",cBirthday="2025-10-28"
    #                   ,cEmail="San@gmai.com",cPhone="0987654321",cAddr="桃園"
    #                   ,cHeight=180,cWeight=70)
    #     print("資料已新增")
    # else:
    #     print("資料已存在,為新增成功")
######################################################
    #更新
    # try:
    #     update = Student.objects.get(cID=11)
    #     update.cHeight=190
    #     update.cWeight=100
    #     update.save()
    #     print("資料已修改")
    # except:
    #     print("資料未更新")

    # try:
    #     update = Student.objects.filter(cID__gte=11).update(cHeight=150,cWeight=40)
    #     print("資料已修改")
    # except:
    #     print("資料未更新")
######################################################
    #刪除
    # delete_exists = Student.objects.filter(cName="San2")
    # if delete_exists.exists():
    #     delete_exists.delete()
    #     print("資料已刪除")
    # else:
    #     print("資料未刪除")

######################################################
    # 一對一 (one to one)
    #新增
    # student_exists = Student.objects.filter(cName="San3").exists()
    # if not student_exists:
    #     datas = Student.objects.create(cName="San2",cSex="M",cBirthday="2025-10-28"
    #                   ,cEmail="San@gmai.com",cPhone="0987654321",cAddr="桃園"
    #                   ,cHeight=180,cWeight=70)
    #     Permissions.objects.create(cID=datas,passwd="1234",level="0")
    #     print("資料已新增")
    # else:
    #     print("資料為新增")
######################################################
    #搜尋
    # datas = Permissions.objects.values("cID__cID","cID__cName","passwd","level")
    # datas = Permissions.objects.values("cID_id","cID__cName","passwd","level")
    # for data in datas:
    #     print(data)
######################################################
    #更新
    # try:
    #     student_data = Student.objects.get(cName="San2") #一筆是get() 多筆可以改filter()
    #     permissions_data = Permissions.objects.get(cID=student_data)
    #     permissions_data.passwd ="0000"
    #     permissions_data.save()
    #     print("資料已更新")
    # except:
    #     print("資料未更新")
######################################################
    #刪除
    # try:
    #     student_data = Student.objects.get(cName="San2")
    #     student_data.delete()
    #     print("資料已刪除")
    # except:
    #     print("資料未刪除")
######################################################
    #一對多(one to many)
    # try:
    #     student_data = Student.objects.get(cName="王大明")
    #     print("此學員已存在")
    # except:
    #     student_data = Student.objects.create(cName="王大明",cSex="M",cBirthday="2025-10-28"
    #                   ,cEmail="Wang@gmai.com",cPhone="0987654321",cAddr="桃園"
    #                   ,cHeight=180,cWeight=70)
    #     print('新增學員成功')
    #     Scorelist.objects.create(cID=student_data,course="地理",score=60)
    #     Scorelist.objects.create(cID=student_data,course="音樂",score=100)
    #     print("新增成績成功")
###
    # try:
    #     student_data = Student.objects.get(cName="王大明")
    #     geography_exists = Scorelist.objects.filter(cID=student_data,course="國文").exists()
    #     if not geography_exists:
    #         Scorelist.objects.create(cID=student_data,course="國文",score=60)
    #         print("新增成績成功")
    #     else:
    #         print("新增成績失敗")
    # except:
    #     print("此學員不存在")
    ###
    #更新
    # try:
    #     student_data = Student.objects.get(cName="王大明")
    #     course_exists = Scorelist.objects.filter(cID=student_data,course="國文").exists()
    #     if course_exists:
    #         Scorelist.objects.filter(cID=student_data,course="國文").update(score=100)
    #         print("更新成功")
    #     else:
    #         print("未找到該科目,無法更新")
    # except:
    #     print("此學員不存在")
    ###
    #刪除
    # try:
    #     student_data = Student.objects.get(cName="王大明")
    #     course_exists = Scorelist.objects.filter(cID=student_data,course="國文").exists()
    #     if course_exists:
    #         Scorelist.objects.filter(cID=student_data,course="國文").delete()
    #         print("刪除成功")
    #     else:
    #         print("未找到該項目,無法刪除")
    # except:
    #     print("此學員不存在")
    ###
    #搜尋
    # datas = Student.objects.filter(scorelist__course="國文").values("cID","cName","scorelist__course","scorelist__score")
    # for data in datas:
    #     print(data)

    # datas = Student.objects.values_list("cID","cName").annotate(Sum("scorelist__score"),Avg("scorelist__score"))
    # for data in datas:
    #     print(data)
######################################################
    #多對多
    #新增
    # 新增作者與新增書名    
    # try: 
    #     # 检查作者是否已存在 
    #     author = Author.objects.get(aID='b100002') 
    #     print("作者已存在")
    # except: 
    #     # 如果不存在，则创建新的作者 
    #     author = Author.objects.create(aID='b100002', name='San')
    #     print("作者新增成功")
    # # 检查并添加第一本书籍 
    # try: #查看此書html有沒有這個作者
    #     book1 = Book.objects.get(isbn='97871') 
    #     if not book1.authors.filter(aID='b100001').exists(): 
    #         book1.authors.add(author) 
    #     else:   
    #         print("作者已存在")
    # except: 
    #     book1 = Book.objects.create(isbn='97871', name='HTML')
    #     book1.authors.add(author)
    #     print("書與書的作者新增成功")

    ###
    #搜尋
    # try: 
    #     # 查找指定ISBN的书籍 
    #     book = Book.objects.get(isbn='8004402') 
    #     # 获取书籍的所有作者 
    #     authors = book.authors.all() 
    #     # # 打印作者信息 
    #     for author in authors: 
    #         print(f'aID: {author.aID}, Name: {author.name}') 
    # except : 
    #     print(f'No book found')

    # datas = Book.objects.filter(isbn="8004402").values("name","authors__name")
    # for data in datas:
    #     print(data)

    # datas = Book.objects.filter(authors__aID="b100002").values('name','authors__name')
    # for data in datas:
    #     print(data)

    ###########
    #更新
    # old_name="San"
    # new_name="San2"
    # try:
    #     # 检查作者是否存在
    #     author = Author.objects.get(name=old_name)
    #     author.name = new_name  # 修改名字
    #     author.save()
    #     print(f"Author name updated from '{old_name}' to '{new_name}'.")
    # except Author.DoesNotExist:
    #     print(f"No author found with name '{old_name}'.")

    # old_name="C++"
    # new_name="C++2"
    # try:
    #     # 检查书籍是否存在
    #     book = Book.objects.get(name=old_name)
    #     book.name = new_name  # 修改书名
    #     book.save()
    #     print(f"Book name updated from '{old_name}' to '{new_name}'.")
    # except Book.DoesNotExist:
    #     print(f"No book found with name '{old_name}'.")

    ####
    #刪除
    # 刪除某書的作者，Author內作者仍保留
    # try: 
    #     # 查找指定ISBN的书籍 
    #     book = Book.objects.get(isbn="97871") 
    #     #获取书籍的所有作者 
    #     authors = book.authors.all() 
    #     #移除所有与书籍相关的作者 
    #     book.authors.clear() 
    #     #打印结果 
    #     print(f'作者已被移除。') 
    # except : 
    #     print(f'没有找到的書籍。')  

    # try:
    #     # 查找指定ISBN的书籍
    #     book = Book.objects.get(isbn='8004402')
    #     # 获取书籍的所有作者
    #     authors = book.authors.all()
        
    #     # 移除所有与书籍相关的作者
    #     book.authors.clear()
    #     # 刪除書籍
    #     book.delete()
    #     # 打印结果
    #     print(f'所有与ISBN相關的作者已被移除。')
    # except Book.DoesNotExist:
    #     print(f'没有找到ISBN的書籍。')

    # 刪除作者，book內書仍保留
    # try:
    #     # 查找指定作者
    #     author = Author.objects.get(aID='b100001')
    #     # 刪除所有書籍與作者的關係
    #     author.book_set.clear()
    #     # 删除作者
    #     author.delete()
    #     # 打印结果
    #     print(f'作者已被删除，但書籍保留。')
    # except Author.DoesNotExist:
    #     print(f'没有找到aID。')
    # ##############################################
    #  CH3_12

def test(request):
    return HttpResponse("Hello world")
def search_list(request):
    if 'cName' in request.GET:
        cName = request.GET['cName']
        # print(cName)
        # resultObject = student.objects .filter(cName=cName)
        resultObject =  Student.objects.filter(cName__conatains=cName)
    else:
        resultObject = Student.objects.all().order_by("cID")
    errormessage=""
    if not resultObject:
        errormessage="無此資料"

    return render(request,"search_list.html",locals())

def search_name(request):
    # return HttpResponse("hello")
    return render(request,"search_name.html")
from django.db.models import Q
from django.core.paginator import Paginator
def index(request):
    if  'site_search' in request.GET:
        site_search =  request.GET["site_search"]
        site_search = site_search.strip() #去前後空白
        keyworks = site_search.split() #切割字元
        print(keyworks)
        # resultList=[]
        q_object = Q()
        for keywork in keyworks:
            q_object.add(Q(cName__contains=keywork),Q.OR)
            q_object.add(Q(cBirthday__contains=keywork),Q.OR)
            q_object.add(Q(cEmail__contains=keywork),Q.OR)
            q_object.add(Q(cPhone__contains=keywork),Q.OR)
            q_object.add(Q(cAddr__contains=keywork),Q.OR)
        resultList = Student.objects.filter(q_object)


        # print(site_search)
        # resultList = Student.objects.filter(
        #     Q(cName__contains=site_search)|
        #     Q(cBirthday__contains=site_search)|
        #     Q(cEmail=site_search)|
        #     Q(cPhone__contains=site_search)|
        #     Q(cAddr__contains=site_search)
        # )
    else:
        resultList = Student.objects.all().order_by("cID")
    status = True
    if not resultList:
        errormessage = "無此資料"
        status =False
    data_count = len(resultList)
    # print(data_count)
    # for d in resultList:
    #     print(model_to_dict(d))
    paginator = Paginator(resultList,3)#分頁設定，每頁顯示3筆
    Page_number = request.GET.get("page")
    page_obj = paginator.get_page(Page_number)
    # print(dir(page_obj))
    
    return render(request,"index.html",locals())

from django.shortcuts import redirect
def post(request):
    if request.method == "POST":
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        print(f"cName={cName},cSex={cSex},cBirthday={cBirthday},cEmail={cEmail},cPhone={cPhone},cAddr={cAddr}")
        # return HttpResponse("資料已新增")
        add = Student(cName=cName,cSex=cSex,cBirthday=cBirthday,cEmail=cEmail,cPhone=cPhone,cAddr=cAddr)
        add.save()      
        return redirect("/index/")
    else:
        return render(request, "post.html",locals())
    
def edit(request,id):
    if request.method == "POST":
        print(id)
        cName = request.POST["cName"]
        cSex = request.POST["cSex"]
        cBirthday = request.POST["cBirthday"]
        cEmail = request.POST["cEmail"]
        cPhone = request.POST["cPhone"]
        cAddr = request.POST["cAddr"]
        print(f"cName={cName},cSex={cSex},cBirthday={cBirthday},cEmail={cEmail},cPhone={cPhone},cAddr={cAddr}")
        # return HttpResponse("資料已修改")
        update = Student.objects.get(cID=id)
        update.cName =cName
        update.cSex =cSex
        update.cBirthday =cBirthday
        update.cEmail =cEmail
        update.cPhone =cPhone
        update.cAddr =cAddr
        update.save()
        return redirect("/index/")
    else:
        obj_data = Student.objects.get(cID=id)
        print(model_to_dict(obj_data))

        # return HttpResponse("hello")
        return render(request, "edit.html",locals())    
def delete(request,id):
    if request.method == "POST":
        print(id)
        delete_data = Student.objects.get(cID=id)
        delete_data.delete()
        return redirect("/index/")
        # return HttpResponse("hello") 
    else:
        print(id)
        obj_data = Student.objects.get(cID=id)  
        print(model_to_dict(obj_data)) 
        return render(request, "delete.html",locals())  






    
    