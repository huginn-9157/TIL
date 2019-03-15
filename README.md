# TIL

>Today I Learned

- [TIL](#til)
  - [Plans](#plans)
  - [Categories](#categories)
    - [BI](#bi)
    - [DB](#db)
    - [Python](#python)
    - [Linux](#linux)

## Plans

- DB
  - 実践的なSQL文について
    - SELECT句での条件分岐とか
- Python
  - SIGNATE[練習問題](https://signate.jp/competitions/practice)で分析結果を出せるようにする。
  - djangoのTODO管理サンプルがあったので読む
  - スクレイピングについて
    - [Scrapy入門 (1)](https://qiita.com/checkpoint/items/038b59b29df8e1e384a2)
- BI
  - ~~[tableauのサンプル](https://public.tableau.com/s/resources?build=20183.18.1219.1533&edition=public&lang=ja-jp&platform=windows&version=2018.3)で遊ぶ~~
- Linux
  - LPICに向けて
    - とりあえず、[LinuCイージス](https://www.infraeye.com/study/studyz4.html)でざっと確認
  - Windows上でDockerコンテナ(CentOS)を走らせるよりは、  
    WSL上でUbuntu動かした方が圧倒的に早くて軽い。  
    今後はそちらでやる

## Categories

### BI

- BI全般
  - [BIシステムのアーキテクチャ](./BI/BI.md)
    - [BIツール以外の選択肢](./BI/option.md)
    - [分散処理](./BI/spark.md)
    - [データマート](./BI/dm.md)
    - [NoSQL](./BI/nosql.md)
    - [ワークフロー管理](./BI/workflow.md)
  - [販売管理の設計](./BI/products.md)
  - [会計BIの基礎](./BI/accounting.md)
- MotionBoard
  - [概要とインストール](./BI/MotionBoard/Install.md)
  - [guiflowで画面遷移図](./BI/MotionBoard/guiflow.md)
  - [ボタンアクション](./BI/MotionBoard/buttonAction.md)
  - [ユーザと認証](./BI/MotionBoard/auth.md)
  - [忘備録](./BI/MotionBoard/tips.md)
- Dr.Sum
  - [概要とインストール](./BI/Dr.Sum/Install.md)
  - [Dr.Sumで業務分析](./BI/Dr.Sum/Analysis.md)
  - [忘備録](./BI/Dr.Sum/tips.md)
- Tableau
- re:dash
  - [ハンズオン](./BI/redash/handson.md)

### DB

- [PostgreSQL](./DB/postgres.md)
- [RedShift](./DB/redshift.md)
- DB設計
  - [販売管理](./DB/販売管理.md)
    - [マスタ設計](./DB/販売管理_マスタ.md)

### Python

- [制御文](./Python/loop.md)
- [配列](./Python/array.md)
  - [リスト内包表記](./Python/list.md)
- [モジュール](./Python/module.md)
- [入出力](./Python/stdinout.md)
- [クラス](./Python/class.md)
- 標準ライブラリ
  - [組み込み関数](./Python/commoncommand.md)
  - [チュートリアル内のもの](./Python/commonlib.md)
- [クロージャ、高階関数](./Python/closure.md)
- [DB接続](./Python/connectDB.md)
- [シリアライズ、JSON](./Python/json.md)
- [Numpy](./Python/numpy.md)
- Jupyterノート
  - pandasで前処理（モデリング前）
    - [Githubで表示](./Python/pandas_sample.ipynb)
    - [Colaboratoryで表示](https://colab.research.google.com/github/huginn-9157/TIL/blob/master/Python/pandas_sample.ipynb)
  - SIGNATE 練習問題 - 自動車の走行距離予測
    - [Github](./Python/Signate_practice1.ipynb)
    - [Colaboratory](https://colab.research.google.com/github/huginn-9157/TIL/blob/master/Python/Signate_practice1.ipynb)
  - 走行距離予測 答えのコピペ
    - [Github](./Python/Signate_practice1a.ipynb)
    - [Colaboratory](https://colab.research.google.com/github/huginn-9157/TIL/blob/master/Python/Signate_practice1a.ipynb)
- [リンク集](./Python/link.md)

### Linux

- [dockerでCentOS](./Linux/centos01.md)
- [基本コマンド：ファイル](./Linux/centos02.md)
- [基本コマンド：プロセス](./Linux/centos03.md)
- [ファイルシステム、パーミッション](./Linux/centos04.md)
- [シェルスクリプト](./Linux/centos05.md)
- ユーザー管理
<!-- - [ユーザー管理](./Linux/centos06.md) -->

----

- [読書リスト](./Books/list.md)