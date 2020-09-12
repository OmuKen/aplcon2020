<div align="center">
<img src="./icon.png" title="ICON">
</div>

## Member
* OmuKen
* ShonClimb
* Takudon3

## Env
asgiref    3.2.10
Django     3.1.1
pip        20.1.1
pytz       2020.1
setuptools 47.1.0
sqlparse   0.3.1

## 設定
1.プロジェクトパス 
    */aplcon2020/aplcon
2.htmlで使用したい画像ファイルの置き場所
    */apln2020/aplcon/static/images

## Django HTML記述ノウハウ
1. 画像を表示させたい場合
>*/apln2020/aplcon/static/imagesに表示させたい画像をおく
>htmlに下記の記述で画像を埋め込む
    {% load static%}
    <img src="{% static "images/表示させたい画像名"%}">

## 操作方法
・サーバーの軌道
外側の「aplcon」にcdして「python manage.py runserver」を実行

## 参照資料
・Django チュートリアル 
URL:https://docs.djangoproject.com/ja/3.1/intro/tutorial01/
・Qiita
URL:https://qiita.com/gragragrao/items/373057783ba8856124f3

## 進捗
1. Djangopプロジェクト作成 (プロジェクト名 = aplcon)
2. アプリケーション作成(sアプリケーション名 = aplcon_app)

## VIew概要
1. homeのviewについて
・apl_con直下の「templete」内のhome.html を表示する
・apl_con直下の「vews.py」のhomeView関数が対応するビュー
