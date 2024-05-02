# Generated by Django 4.1 on 2024-05-01 17:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoLists',
            fields=[
                ('TodoList_id', models.AutoField(primary_key=True, serialize=False)),
                ('destination', models.CharField(default='', max_length=150)),
                ('todo_list', models.CharField(blank=True, max_length=500, null=True)),
                ('complete_flg', models.BooleanField(null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
            ],
            options={
                'db_table': 'todolists',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('destination_id', models.AutoField(primary_key=True, serialize=False)),
                ('destination_name', models.CharField(max_length=150)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='旅行した日')),
                ('GoogleMapURL', models.URLField()),
                ('TravelRecord', models.CharField(max_length=500)),
                ('picture', models.FileField(upload_to='destination/')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='更新日時')),
                ('username', models.ForeignKey(blank=True, max_length=150, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'destinations',
            },
        ),
    ]
