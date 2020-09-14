# Djangoデプロイ

## 手順
1.EC2作成  
2.SSM設定⇒コンソール上から接続  
3.sudo  

'''sh
sudo su -
'''

4.python環境作成

'''sh
# python (EC2独自コマンド)
sudo amazon-linux-extras install python3.8 //Version3.8.5がインストールされる

# virtualenv
pip3 install virtualenv

# 仮想環境作成
virtualenv -p python3.8 env-django

# Activate
cd env-django
source ./bin/activate
'''

5.gitインストール/クローン

```sh
yum install git  
git clone https://github.com/OmuKen/aplcon2020.git
```

6.pythonパッケージを取得

```sh
pip install -r requirements.txt
```

