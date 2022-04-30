from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import User, Posting, Comment
from django.utils import timezone
from datetime import datetime

# Create your views here.
def index(request):
    user=request.user
    postings=Posting.objects.all()
    mypostings=Posting.objects.filter(p_User=user).all()
    return render(request,'index.html',{postings:postings , mypostings:mypostings})

def showPosting(request):
    no=request.GET['p']
    posting=Posting.objects.get(id=posting.id)
    comments=Comment.objects.filter(c_Posting=posting).all()
    return render(request,'posting.html',{posting:posting,comments:comments})

def like(request):
    no=request.GET['p']
    likes=Posting.objects.filter(id=posting.id).values('p_Likes')
    posting=Posting.objects.filter(id=posting.id).update(p_Likes=likes+1)

def addComment(request):
    no=request.GET['p']
    content=request.GET['content']
    user=request.user
    date=timezone.localdate()
    comment=Comment(c_User_id=user,c_Content=content,c_Date=date)
    comment.save()
    return True



#获取所有帖子
def adminshowwall(request):
    datalist = []
    with open("msgdata.txt", "r") as f:
        for line in f:
            linedata = line.split('--')
            if linedata[0] != None:
                d = {"user": linedata[0], "msg": linedata[1], "time": linedata[2]}
                datalist.append(d)
    return render(request, "postwall.html", {"data": datalist})

def admin_all_Posting(request):
    data_book = Posting.objects.filter(is_active=True)
    return render(request, 'postwall.html', locals())

#写帖子
def postPosting(request):
    user = request.POST.get("user", None)
    msg = request.POST.get("msg", None)
    time = datetime.now()
    with open('msgdata.txt', 'a+') as f:
        f.write("{}--{}--{}--\n".format(user, msg, time.strftime("%Y-%m-%d %H:%M:%S")))
    return render(request, "usersend.html")

#删除帖子
def deletePosting(request):
    Posting_id = request.GET.get('post_id')
    if not Posting_id:
        return HttpResponse('--请求异常')
    try:
        post = Posting.objects.get(id=Posting_id, is_active=True)
    except Exception as e:
        print('--delect post get error &s' % (e))
        return HttpResponse('---The post id is error')
    post.is_active = False
    post.save()
    return HttpResponseRedirect('postwall')

