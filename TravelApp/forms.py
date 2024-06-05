from django import forms
from .models import Users, Destinations, TodoLists
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import widgets, ClearableFileInput
from django.utils.safestring import mark_safe
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth import authenticate

###ログイン機能、ユーザー情報編集、パスワード変更###

class RegistForm(UserCreationForm):
    #username = forms.CharField(label='名前', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #email = forms.EmailField(label='メールアドレス', widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Users
        fields = ('username', 'email', 'password1', 'password2')

'''
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
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("パスワードが一致しません")
        return password2
'''
'''
    def clean_name(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        if username == password:
            raise forms.ValidationError("登録者名とパスワードを同じにしないで下さい")
        return self.cleaned_data
'''

    
#class UserLoginForm(forms.Form):
#    email = forms.EmailField(label='メールアドレス')
#    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

'''
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label='メールアドレス', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
'''

class UserLoginForm(forms.Form):
    email = forms.EmailField(label='メールアドレス', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            try:
                user = Users.objects.get(email=email)
            except Users.DoesNotExist:
                raise forms.ValidationError("ユーザーが存在しません")

            user = authenticate(username=email, password=password)
            if user is None:
                raise forms.ValidationError("メールアドレスまたはパスワードが間違えています")
        
        return cleaned_data


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
'''
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
'''
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

    def __init__(self, attrs=None, format=None):
        super().__init__(attrs={'type': 'text', 'readonly': 'readonly'}, format=format)
        if attrs:
            self.attrs.update(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        rendered = super().render(name, value, attrs=attrs, renderer=renderer)
        return rendered + mark_safe('<script>$(function() { $("#id_%s").datepicker({ maxDate: 0 }); });</script>' % name)

'''
class TravelRecordInsertForm(forms.ModelForm):
    #user_id = forms.IntegerField(widget=forms.HiddenInput)
    destination_name = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(label='旅行した日',widget=DatePickerWidget(attrs={'class': 'form-control', 'readonly': 'readonly'}))
    TravelRecord = forms.CharField(label='記録', widget=forms.Textarea(attrs={'class': 'form-control'}))
    picture = forms.ImageField(label='画像アップロード', required=False)
    latitude = forms.FloatField(label='緯度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.FloatField(label='経度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Destinations
        fields = ['destination_id', 'destination_name', 'date', 'TravelRecord', 'latitude', 'longitude', 'picture']
''' 
class TravelRecordInsertForm(forms.Form):
    #user_id = forms.IntegerField(widget=forms.HiddenInput)
    destination_name = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    date = forms.DateField(label='旅行した日',widget=DatePickerWidget(attrs={'class': 'form-control', 'required': 'required'}), error_messages={'required': '日付を選択してください'})
    TravelRecord = forms.CharField(label='記録', widget=forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}))
    picture = forms.ImageField(label='画像アップロード', required=False)
    latitude = forms.FloatField(label='緯度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    longitude = forms.FloatField(label='経度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))

    def clean_destination_name(self):
        destination_name = self.cleaned_data.get('destination_name')
        if not destination_name.strip():
            raise ValidationError('適切な入力をしてください。')
        return destination_name

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise ValidationError('日付を選択してください。')
        return date

    def clean_TravelRecord(self):
        TravelRecord = self.cleaned_data.get('TravelRecord')
        if not TravelRecord.strip():
            raise ValidationError('適切な入力をしてください。')
        return TravelRecord
    
    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        if not latitude:
            raise ValidationError('地図上で場所を選択してください。')
        return latitude
    
    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        if not longitude:
            raise ValidationError('地図上で場所を選択してください。')
        return longitude

'''
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
'''

class CustomClearableImageInput(ClearableFileInput):
    template_name = 'update_destination.html'


class DestinationUpdateForm(forms.Form):
    #destination_id = forms.IntegerField(label='No.')
    destination_name = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    date = forms.DateField(label='旅行した日',widget=DatePickerWidget(attrs={'class': 'form-control', 'required': 'required'}), error_messages={'required': '日付を選択してください'})
    TravelRecord = forms.CharField(label='記録', widget=forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}))
    latitude = forms.FloatField(label='緯度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    longitude = forms.FloatField(label='経度(地図上で場所を選択すると自動入力されます)', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    picture = forms.ImageField(label='画像アップロード', required=False)

    def clean_destination_name(self):
        destination_name = self.cleaned_data.get('destination_name')
        if not destination_name.strip():
            raise ValidationError('適切な入力をしてください。')
        return destination_name

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if not date:
            raise ValidationError('日付を選択してください。')
        return date

    def clean_TravelRecord(self):
        TravelRecord = self.cleaned_data.get('TravelRecord')
        if not TravelRecord.strip():
            raise ValidationError('適切な入力をしてください。')
        return TravelRecord
        
    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')
        if not latitude:
            raise ValidationError('地図上で場所を選択してください。')
        return latitude
    
    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')
        if not longitude:
            raise ValidationError('地図上で場所を選択してください。')
        return longitude
    
class DestinationDeleteForm(forms.Form):
    destination_id = forms.IntegerField(widget=forms.HiddenInput)


###Todoリスト登録、編集、削除###
'''
class TodoListInsertForm(forms.ModelForm):
    destination = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}))
    #complete_flg = forms.BooleanField(blank=True, null=True)

    class Meta:
        model = TodoLists
        fields = ['destination', 'todo_list']
'''
class TodoListInsertForm(forms.Form):
    destination = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}))
    #complete_flg = forms.BooleanField(blank=True, null=True)

    def clean_destination(self):
        destination = self.cleaned_data.get('destination')
        if not destination.strip():
            raise ValidationError('適切な入力をしてください。')
        return destination

    def clean_todo_list(self):
        todo_list = self.cleaned_data.get('todo_list')
        if not todo_list.strip():
            raise ValidationError('適切な入力をしてください。')
        return todo_list

'''
class TodoListUpdateForm(forms.Form):
    #destination_id = forms.IntegerField(label='No.')
    destination = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control'}))
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    complete_flg = forms.BooleanField(label='完了', required=False)

    class Meta:
        model = TodoLists
        fields = ['destination', 'todo_list', 'complete_flg']    
'''
class TodoListUpdateForm(forms.Form):
    #destination_id = forms.IntegerField(label='No.')
    destination = forms.CharField(label='旅行先', widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'required'}))
    todo_list = forms.CharField(label='やりたいこと', max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'required': 'required'}))
    complete_flg = forms.BooleanField(label='完了', required=False)

    def clean_destination(self):
        destination = self.cleaned_data.get('destination')
        if not destination.strip():
            raise ValidationError('適切な入力をしてください。')
        return destination

    def clean_todo_list(self):
        todo_list = self.cleaned_data.get('todo_list')
        if not todo_list.strip():
            raise ValidationError('適切な入力をしてください。')
        return todo_list

class TodoListDeleteForm(forms.Form):
    TodoList_id = forms.IntegerField(widget=forms.HiddenInput)