from django import forms

#スキル検索用のフォーム
class SkillSerchForm(forms.Form):
   skill_name = forms.CharField(label='スキル検索', max_length=30, required=True, widget=forms.TextInput())

#スキル登録用のフォーム
class SkillRegForm(forms.Form):
   code = forms.CharField(label='スキルコード', required=True,max_length = 1000)
   name = forms.CharField(label='スキル名', max_length=30, required=True, widget=forms.TextInput())

#社員登録用フォーム
class WorkerRegForm(forms.Form):
   code = forms.CharField(label='社員コード', required=True,max_length = 9)
   name = forms.CharField(label='名前', max_length=30, required=True, widget=forms.TextInput())
   dep = forms.CharField(label='所属', required=True)
   mail = forms.EmailField(label='メールアドレス', max_length=128, required=True, widget=forms.TextInput())

#社員保有スキル登録フォーム
class WorkerSkillRegForm(forms.Form):
   worker_code = forms.CharField(label='社員コード', required=True,max_length = 9)
   skill_name = forms.CharField(label='スキル名', max_length=30, required=True, widget=forms.TextInput())