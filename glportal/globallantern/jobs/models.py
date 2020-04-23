from django.db import models
from seeker import models as m1
from company import models as m2
from django.urls import reverse

# Create your models here.
class job_post_activity(models.Model):
    user_account_id=models.IntegerField(unique=True)
    job_post_id=models.IntegerField(unique=True)
    apply_date=models.DateField()
    class Mate:
        verbose_name_plural='Job Post Table'

class job_location(models.Model):
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    zip=models.CharField(max_length=50)
    
class job_type(models.Model):
    job_type=models.CharField(max_length=100)

class job_post(models.Model):
    posted_by_id=models.ForeignKey(job_post_activity,on_delete=models.CASCADE)
    job_type_id=models.ForeignKey(job_type,on_delete=models.CASCADE)
    company_id=models.ForeignKey(m2.company,on_delete=models.CASCADE)
    is_company_name_hidden=models.CharField(max_length=1)
    create_date=models.DateTimeField(auto_now_add=True)
    job_description=models.TextField()
    job_location_id=models.ForeignKey(job_location,on_delete=models.CASCADE)
    is_active=models.CharField(max_length=1)
    job_title=models.CharField(max_length=50)
    closing_date=models.DateField()
    minimum_pay=models.CharField(max_length=100)
    maximum_pay=models.CharField(max_length=100)
    slug=models.SlugField(max_length=150,unique=True)

    def __str__(self):
        return 'JOB POST {}'.format(self.job_title)
    def get_absolute_url(self):
        return reverse('addpost', kwargs={'pk': self.pk})
    class Mate:
        verbose_name_plural='jobsposts'

class job_post_skill_set(models.Model):
    skill_set_id=models.ForeignKey(m1.skill_set,on_delete=models.CASCADE)
    job_post_id=models.ForeignKey(job_post,on_delete=models.CASCADE)
    skill_level=models.IntegerField()

