
from django import forms
from django.forms import fields


class ClassForm(forms.Form):
    title = fields.CharField(max_length=32,required=True
                             ,error_messages={'required':'班级名称不能为空'})


class TeacherForm(forms.Form):
    name = fields.CharField(max_length=32,required=True
                            ,error_messages={'required':'教师名称不能为空'})