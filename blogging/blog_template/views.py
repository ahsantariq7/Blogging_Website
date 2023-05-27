from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, UpdateView
from .models import Blog,Category,Section
from django.contrib.auth.models import User
from .forms import ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

class Index_View(TemplateView):
    template_name='index.html'
  
    
class Contact_Us_View(TemplateView):
    template_name='contactus.html'
    

class Blog_View(TemplateView):
    template_name='blogs.html'

#class ProfileView(UpdateView):
#    model = User
#    form_class = ProfileForm
#    success_url = reverse_lazy('home')
#    template_name = 'commons/profile.html'


#@login_required(login_url='/login/')
def Blog_detail(request,slug):
    blogs=Blog.objects.filter(slug=slug)
    if blogs.exists():
        blogs=Blog.objects.filter(slug=slug)
    else:
        return redirect('404')


    context={
        'blogs':blogs,
    }

    return render(request, 'product_detail.html',context)


def product(request):
    categories=Category.objects.all()
    blogs=Blog.objects.all()
    sections=Section.objects.all()
    
    #if 'q' in request.GET:
    #    q=request.GET['q']
    #    products=Product.objects.filter(name__icontains=q)
    #else:
    #    products=Product.objects.all()
    #''''

    context={
        'categories':categories,
        'blogs':blogs,
        'sections':sections,
    }
    return render(request, 'product.html',context)

