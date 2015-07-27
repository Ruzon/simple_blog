from django.shortcuts import render
from django.http import HttpResponse
from models import BlogArticle
# Create your views here.
from django.contrib.auth import authenticate, login
def index(request):
    blogs = BlogArticle.objects.all()
    if request.method == 'POST':
        usname = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(username=usname, password=pwd)
        if user is not None:
            login(request, user)
            return render(request, "main.html", {'testvar':"Test String 2!",'blogs':blogs, 'user':user} )
    return render(request, "main.html", {'testvar':"Test String 2!",'blogs':blogs, 'user':None})
    # return render_to_response('main.html', {'object': varobject},context_instance=RequestContext(request))
    
def createBlog(request):
    blogs = BlogArticle.objects.all()
    newBlog = BlogArticle()
    newBlog.title = request.POST['title']
    newBlog.author = request.user
    newBlog.blog_content = request.POST['blog_content']
    newBlog.save()
    return render(request, "main.html", {'testvar':"Test String 2!",'blogs':blogs, 'user':request.user} )

# def java_script(request):
#     filename = request.path.strip("/")
#     data = open(filename, "rb").read()
#     return HttpResponse(data, mimetype="application/x-javascript")