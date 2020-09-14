# Djangoデプロイ

## package Verisinon
nginx==1.18.0


## 手順
1.EC2作成  
2.SSM設定⇒コンソール上から接続  
3.sudo  

```sh
sudo su -
```

4.python環境作成

```sh
# python (EC2独自コマンド)
sudo amazon-linux-extras install python3.8 //Version3.8.5がインストールされる

# virtualenv
pip3 install virtualenv

# 仮想環境作成
virtualenv -p python3.8 env-django

# Activate
cd env-django
source ./bin/activate
```

5.gitインストール/クローン

```sh
yum install git  
git clone https://github.com/OmuKen/aplcon2020.git
```

6.pythonパッケージを取得

```sh
pip install -r requirements.txt
```

7.nginxインストール

```sh
sudo amazon-linux-extras install nginx1
```

8.Web公開用にdjangoプロジェクトを編集

* settings.py

'''python
ALLOWED_HOSTS = []  
→ ALLOWED_HOSTS = ['13.231.109.224'] # インスタンスのグローバルIPを挿入
'''

9.sqlite3を無理やりバージョンアップ

```sh
# ビルド用パッケージ
bash-4.2# yum install -y wget tar gzip gcc make

## ソースを取得・展開
wget https://www.sqlite.org/2019/sqlite-autoconf-3270100.tar.gz
tar xvfz sqlite-autoconf-3270100.tar.gz

＃ビルド
cd sqlite-autoconf-3270100
./configure --prefix=/usr/local
make # ちょっと時間かかる
make install

# インストールしたsqliteにシンボリックリンクを貼る
mv /usr/bin/sqlite3 /usr/bin/sqlite3_old
ln -s /usr/local/bin/sqlite3 /usr/bin/sqlite3

# path追加

```




