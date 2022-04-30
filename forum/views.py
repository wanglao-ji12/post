from django.shortcuts import render
from .models import User, Posting, Comment
from django.utils import timezone
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