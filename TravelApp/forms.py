from django import forms
from .models import Users, Destinations, TodoLists
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.utils.safestring import mark_safe

###ログイン機能、ユーザー情報編集、パスワード変更###
class RegistForm(forms.ModelForm):
    username = forms.CharField(label='名前', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
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
    username = forms.CharField(label='名前', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='メールアドレス', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Users
        fields = ('username', 'email')

class PasswordChangeForm(forms.ModelForm):

    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
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
class DatePickerWidget(widgets.DateInput):
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.css',)
        }
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
            'https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js',
            'datepicker_script.js',  # カスタムJavaScriptファイル
        )

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)
        return rendered + mark_safe('<script>$(function() { $("#id_%s").datepicker({ maxDate: 0 }); });</script>' % name)

class TravelRecordInsertForm(forms.ModelForm):
    #user_id = forms.IntegerField(widget=forms.HiddenInput)
    destination_name = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label='旅行した日',widget=DatePickerWidget(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    TravelRecord = forms.CharField(label='記録', widget=forms.Textarea(attrs={'class': 'form-control'}))
    picture = forms.ImageField(label='画像アップロード', required=False)
    #latitude = forms.FloatField()
    #longitude = forms.FloatField()
    latitude = forms.FloatField(label='緯度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.FloatField(label='経度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Destinations
        fields = ['destination_id', 'destination_name', 'date', 'TravelRecord', 'latitude', 'longitude', 'picture']
 

class DestinationUpdateForm(forms.Form):
    #destination_id = forms.IntegerField(label='No.')
    destination_name = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label='旅行した日',widget=DatePickerWidget(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    TravelRecord = forms.CharField(label='記録', widget=forms.Textarea(attrs={'class': 'form-control'}))
    latitude = forms.FloatField(label='緯度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.FloatField(label='経度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    picture = forms.ImageField(label='画像アップロード', required=False)

    class Meta:
        model = Destinations
        fields = ['destination_id', 'destination_name', 'date', 'TravelRecord', 'picture', 'latitude', 'longitude']    

class DestinationDeleteForm(forms.Form):
    destination_id = forms.IntegerField(widget=forms.HiddenInput)


###Todoリスト登録、編集、削除###
class TodoListInsertForm(forms.ModelForm):
    destination = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control'}))
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    #complete_flg = forms.BooleanField(blank=True, null=True)

    class Meta:
        model = TodoLists
        fields = ['destination', 'todo_list']


class TodoListUpdateForm(forms.Form):
    #destination_id = forms.IntegerField(label='No.')
    destination = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control'}))
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    complete_flg = forms.BooleanField(label='完了', required=False)

    class Meta:
        model = TodoLists
        fields = ['destination', 'todo_list', 'complete_flg']    

class TodoListDeleteForm(forms.Form):
    TodoList_id = forms.IntegerField(widget=forms.HiddenInput)

