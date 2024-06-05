from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            user_name=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name="ユーザーネーム", max_length=150, default='')
    email = models.EmailField(verbose_name="メールアドレス", max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    create_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新日時", auto_now=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_absolute_url(self):
        return reverse_lazy('TravelApp:home')

class Destinations(models.Model):
    destination_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, db_column='user_id', on_delete=models.CASCADE, max_length=150, blank=True, null=True)
    destination_name = models.CharField(max_length=150)
    date = models.DateField(verbose_name="旅行した日", blank=False, null=False, default=timezone.now)
    TravelRecord = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='destination/')
    latitude = models.FloatField(verbose_name="緯度", default=0.0)
    longitude = models.FloatField(verbose_name="経度", default=0.0)    
    create_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新日時", auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'destinations'


class TodoLists(models.Model):
    TodoList_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, db_column='user_id', on_delete=models.CASCADE, max_length=150, blank=True, null=True)
    destination = models.CharField(max_length=150, default='')
    todo_list = models.CharField(max_length=500, blank=True, null=True)
    complete_flg = models.BooleanField(verbose_name="完了", default=False)
    create_at = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)
    update_at = models.DateTimeField(verbose_name="更新日時", auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'todolists'

