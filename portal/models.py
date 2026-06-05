from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    hod_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.department_name


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='faculty/', blank=True, null=True)

    def __str__(self):
        return self.name


class Notice(models.Model):
    title = models.CharField(max_length=200)
    attachment = models.FileField(upload_to='notices/', blank=True, null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_posted'] 

    def __str__(self):
        return self.title


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200)

    def __str__(self):
        return self.caption