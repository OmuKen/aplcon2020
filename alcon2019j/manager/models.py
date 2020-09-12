from django.db import models

# Create your models here.
#データベースを定義する

#社員情報 社員コード/名前/所属/メアド
class TB_Worker(models.Model):
    worker_code = models.CharField(unique=True,max_length=9)#社員コード
    name = models.CharField(max_length=128)#名前
    dep = models.CharField(max_length=32)#所属
    mail = models.EmailField(unique=True)#メアド
    
#資格表 資格コード/資格名
class TB_Skill(models.Model):

    skill_code = models.CharField(unique=True,max_length = 1000)#スキルコード
    name = models.CharField(max_length=64)#スキル名

#社員コードと資格の対応 社員コード/スキルコード
class TB_VsSkill(models.Model):
    worker_code = models.ForeignKey(TB_Worker, on_delete=models.CASCADE)#社員コード
    skill_code = models.ForeignKey(TB_Skill, on_delete=models.CASCADE)#スキルコード



    
