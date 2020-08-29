from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import Contact, Project, Resume
from .forms import ContactForm
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# def home(request):
#     return render(request,'pages/home.html')



def contact(request):
    projects = Project.objects.order_by('id')
    resume = Resume.objects.all()

    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Thank you for contacting.Your message has been delivered successfully.You will be responded as soon as possible')
        return redirect('/')

    context = {
        'form': form,
        'projects' : projects,
        'resume' : resume,
    }

    return render(request, 'pages/home.html', context)


