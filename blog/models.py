from django.db import models

SEX = (
		('male', '男性'),
		('female', '女性'),
		('other', 'その他'),
		
	)
class BlogUser(models.Model):
    """ ユーザ(適当、認証など考えるとDjangoデフォルトのモデルが良さそう) """
    name = models.CharField(max_length=30)
    email = models.EmailField()
    following = models.ManyToManyField("self",related_name="followed_by",symmetrical=False,blank=True)
    sex = models.CharField(max_length=10, choices=SEX, unique=True, default='')

    def __str__(self):
        return self.name

class BlogUserMoreData(models.Model):
    user = models.OneToOneField(BlogUser,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.user.name

class Blog(models.Model):
    author = models.ForeignKey(BlogUser,on_delete=models.CASCADE,related_name="wrote_blog")
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    liked_by = models.ManyToManyField(BlogUser,related_name="liked_blog")

    def __str__(self):
        return self.title

class Comment(models.Model):
    """ Blogに対するコメント """
    target_blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="comment")
    author = models.ForeignKey(BlogUser,on_delete=models.CASCADE,related_name="comment")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)