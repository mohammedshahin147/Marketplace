from django.db import models
from django.contrib.auth.models import User

# here the models to store all the user details including the documents..
# adding documents at the time of signup will help to ease the agreement process..

#username , password and email stores in user (by using inbuilt User)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE , primary_key=True)
    fullname = models.CharField(max_length=255)
    contactno = models.BigIntegerField()
    address = models.TextField()
    documents = models.ImageField(upload_to='uploads/')
    def __str__(self):
        return self.user.username

    