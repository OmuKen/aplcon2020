from django.db import models

# Create your models here.
#データベースを定義する

#社員情報 名前/所属/メアド
#モデルナームはworker
class worker(models.Model):
    #所属部署の定数
    FA = 0
    MS = 1
    BI = 2
    SS = 3
    EF = 4
    IST = 5
    name = models.CharField(max_length=128)#名前
    department = models.IntegerField()#所属
    mail = models.CharField(max_length=128)#メアド
    
