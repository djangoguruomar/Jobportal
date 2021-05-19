from django.shortcuts import render
from .models import *
from django.views import generic
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from .forms import UserRegisterForm

# Create your views here.
def context(request):
    jobs=Job.objects.all()
    recruiters=Recruiter.objects.all()
    category=Category.objects.all()

    context={'jobs': jobs, 'recruiters': recruiters, 'category': category}
    return context 

def home(request):

    contexts=context(request)
    return render(request, 'home.html', contexts)

    

class JobListView(generic.ListView):
    model=Job
class JobDetailView(generic.DetailView):
    model=Job
    def job_detail_view(request, primary_key):
        try:
            job = Job.objects.get(pk=primary_key)
        except Job.DoesNotExist:
            raise Http404('Job does not exist')

class JobSeekerListView(generic.ListView):
    model=JobSeeker
class JobSeekerDetailView(generic.DetailView):
    model=JobSeeker
class CategoryListView(generic.ListView):
    model=Category
class CategoryDetailView(generic.DetailView):
    model=Category
class JobCreate(generic.edit.CreateView):
    model=Job
    fields='__all__'
    
    def form_valid(self, form):
        post = form.save(commit=False)
        post.recruiter=Job.get_default_recruiter(self)
        post.save()
        return super(JobCreate, self).form_valid(form)





class JobUpdate(generic.edit.UpdateView):
    model=Job
    fields='__all__'


class JobDelete(generic.edit.DeleteView):
    model=Job
    fields='__all__'



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            username=username.capitalize()
            password= form.cleaned_data.get('password')
            #email=form.cleaned_data.get('email')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'register.html', {'form': form})