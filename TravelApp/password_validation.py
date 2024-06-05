# validators.py
from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def validate(self, password, user=None):
        '''
        if len(password) < 8:
            raise ValidationError(
                'パスワードは8文字以上である必要があります。',
                code='password_too_short',
            )'''
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                'パスワードには少なくとも1つの大文字を含める必要があります。',
                code='password_no_upper',
            )
        if not re.search(r'[a-z]', password):
            raise ValidationError(
                'パスワードには少なくとも1つの小文字を含める必要があります。',
                code='password_no_lower',
            )
        if not re.search(r'\d', password):
            raise ValidationError(
                'パスワードには少なくとも1つの数字を含める必要があります。',
                code='password_no_number',
            )

    def get_help_text(self):
        return (
            'パスワードは8文字以上であり、'
            '大文字、小文字、数字を含める必要があります。'
        )
