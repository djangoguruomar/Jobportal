from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse
import  datetime


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200, help_text='job category')
    def __str__(self):
        
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this jobseeker."""
        return reverse('category-detail', args=[str(self.id)])


class JobSeeker(models.Model):
    user= models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=20)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    highest_education= models.CharField(max_length=20, help_text='Enter your highest degree')
    institution= models.CharField(max_length=20, help_text='Your last educational institution')
    date_of_birth=models.DateField(null=True, blank=True)

    def get_age(self):
        age=datetime.date.today().year-self.date_of_birth.year
        return age
    
    def __str__(self):
        
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this jobseeker."""
        return reverse('jobseeker-detail', args=[str(self.id)])
    def default_group():
        return Group.objects.get(name="jobseeker").id

    group=models.ForeignKey(Group, default=default_group, on_delete=models.SET_NULL, null=True)
    


class Recruiter(models.Model):
    user= models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=20)
    company=models.CharField(max_length=20, help_text='Your Company Name')
    designation=models.CharField(max_length=20)

    def __str__(self):

        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this jobseeker."""
        return reverse('recruiter-detail', args=[str(self.id)])
    def default_group():
        return Group.objects.get(name="recruiter").id

    group=models.ForeignKey(Group, default=default_group, on_delete=models.SET_NULL, null=True)






class Job(models.Model):
    
    title = models.CharField(max_length=200, help_text='job title')
    education_rqr= models.CharField(max_length=200, help_text='minimum degree')
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    location= models.CharField(max_length=200, help_text='job location')
    max_age=models.IntegerField(help_text='maximum age limit of the candidates')
    experience=models.IntegerField(help_text='minimum work experience required')
    deadline=models.DateField(null=True, blank=True)
    recruiter = models.ForeignKey(Recruiter,on_delete=models.SET_NULL, null=True, blank=True, editable=False)

    def get_default_recruiter(self):
        user=self.request.user
        print(user)
        recruiter=Recruiter.objects.filter(user=user).get()
        print(recruiter)
        return recruiter

 






    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this jobseeker."""
        return reverse('job-detail', args=[str(self.id)])

 
    def get_job_update_url(self):
        """Returns the url to access a detail record for this jobseeker."""
        return reverse('update-jobs', args=[str(self.id)])

    def get_job_delete_url(self):
        """Returns the url to access a detail record for this jobseeker."""
        return reverse('delete-jobs', args=[str(self.id)])
