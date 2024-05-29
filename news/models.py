# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from ckeditor.fields import RichTextField

# class Post(models.Model):
#     title = models.CharField(max_length=255)
#     title_tag = models.CharField(max_length=255, default="Interesting News")
#     #body = RichTextField(blank=True, null=True)
#     # author = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateField(auto_now_add=True)
    
#     def __str__(self) -> str:
#         return self.title + " | " #self.author.username
    
#     def get_absolute_url(self):
#         # return reverse("news-detail", kwargs={"pk": self.pk})
#         return reverse("home")
    
# class Paragraph(models.Model):
#     post = models.ForeignKey(Post, related_name='paragraphs', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200, blank=True)
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     text = models.TextField()

#     def __str__(self):
#         return f'{self.title} (Paragraph of {self.post.title})' if self.title else f'Paragraph of {self.post.title}'


from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='post_photos/')
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title

class Paragraph(models.Model):
    post = models.ForeignKey(Post, related_name='paragraphs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='paragraph_photos/', blank=True, null=True)

    def __str__(self):
        return f'Paragraph of {self.post.title}'
