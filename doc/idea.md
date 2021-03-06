# 岩の状況を共有するアプリケーション

## 概要
* エリア、岩の状況情報の共有サービス
* エリアに行く前に他ユーザの投稿により岩の状況把握可能
* 無駄足を防ぐ
* 閲覧は登録不要
* 投稿は登録制

## ユーザ登録
* ユーザ名
    * ユーザ入力情報の信憑性把握のため
* メアド
    * ユーザ特定のため
* ユーザ登録削除

## エリア状態登録時入力情報
* 時間
    * 今の時間(デフォルト)
    * 過去3日分入力可能
* 岩の状況
    * 濡れてる
    * 乾いてる
    * 湿ってる
        * 乾きそう
        * 乾かなそう
* エリア状況(川エリア限定)
    * 水量
        * 登れる
        * 登れない
    * 渡渉
        * 可能
        * 不可能
* 場所
    * 地域
        * 北海道
        * 東北
        * 関東
        * 中部
        * 東海
        * 関西
    * エリア名(有名エリアなら選択、自由入力も可能)
        * ユーザ自由選択のエリアも追加に伴い選択肢に自動追加される
    * 岩(任意)
    * 課題(任意)

## 検索方法
* ストーリー
  * 地域選択
  * エリア選択
  * 状態選択
    * 地域選択で乾いてるエリア一覧表示

## 展望
* データ収集による渇き具合の予想
    * 過去データから雨天日からの渇き時間
    * 地域の天気状況
    * 時期
    * パーセント表示(◯◯エリア乾いてる確率x%)
* 事前にエリア設定による岩状況の通知
* 増水状況の追加(普通に入れる？)
* bleau.infoの日本版の一機能
    * https://bleau.info