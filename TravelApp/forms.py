from django import forms
from .models import Users, Destinations, TodoLists
from django.contrib.auth.password_validation import validate_password
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.contrib.auth.forms import AuthenticationForm

###ログイン機能、ユーザー情報編集、パスワード変更###
class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    #confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    
    class Meta:
        model = Users
        fields = ['username', 'email', 'password']
    
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

#class UserLoginForm(forms.Form):
#    email = forms.EmailField(label='メールアドレス')
#    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='メールアドレス')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

class UserEditForm(forms.ModelForm):
    username = forms.CharField(label='名前')
    email = forms.EmailField(label='メールアドレス')

    class Meta:
        model = Users
        fields = ('username', 'email')

class PasswordChangeForm(forms.ModelForm):

    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())
    
    class Meta():
        model = Users
        fields = ('password', )
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError('パスワードが異なります')

    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data['password'], user)
        user.set_password(self.cleaned_data['password'])
        user.save()

###旅行記録登録、編集、削除###
class TravelRecordInsertForm(forms.ModelForm):
    destination_name = forms.CharField(label='旅行先')
    date = forms.DateField(label='旅行した日', widget=DatePickerInput(format='%Y-%m-%d'))
    TravelRecord = forms.CharField(label='記録', widget=forms.Textarea)
    picture = forms.FileField(label='画像アップロード', required=False)
    #latitude = forms.FloatField()
    #longitude = forms.FloatField()

    class Meta:
        model = Destinations
        fields = ['destination_id', 'destination_name', 'date', 'TravelRecord', 'picture', 'latitude', 'longitude']
 

class DestinationUpdateForm(forms.Form):
    #destination_id = forms.IntegerField(label='No.')
    destination_name = forms.CharField(label='旅行先')
    date = forms.DateField(label='旅行した日', widget=DatePickerInput(format='%Y-%m-%d'))
    TravelRecord = forms.CharField(label='記録', widget=forms.Textarea)
    picture = forms.FileField(label='画像アップロード', required=False)
    latitude = forms.FloatField()
    longitude = forms.FloatField()

    class Meta:
        model = Destinations
        fields = ['destination_id', 'destination_name', 'date', 'TravelRecord', 'picture', 'latitude', 'longitude']    

class DestinationDeleteForm(forms.Form):
    destination_id = forms.IntegerField(widget=forms.HiddenInput)


###Todoリスト登録、編集、削除###
class TodoListInsertForm(forms.ModelForm):
    destination = forms.CharField(label='旅行先')
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea)
    #complete_flg = forms.BooleanField(blank=True, null=True)

    class Meta:
        model = TodoLists
        fields = ['destination', 'todo_list']


class TodoListUpdateForm(forms.Form):
    #destination_id = forms.IntegerField(label='No.')
    destination = forms.CharField(label='旅行先')
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea)
    complete_flg = forms.BooleanField(label='完了')

    class Meta:
        model = TodoLists
        fields = ['destination', 'todo_list', 'complete_flg']    

class TodoListDeleteForm(forms.Form):
    TodoList_id = forms.IntegerField(widget=forms.HiddenInput)
