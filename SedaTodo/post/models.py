from django.db import models

# Create your models here.
from django.db import models
from django.template.defaultfilters import slugify



class Post(models.Model):
    #user = models.ForeignKey("auth.User", on_delete=models.CASCADE)  # user
    title = models.CharField(max_length=150, verbose_name='Post Başlık')
    content = models.TextField(verbose_name='Post İçeriği')
    email = models.EmailField(null=True,blank=True)
    econtact = models.CharField(max_length=15, null=True, blank=True)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)