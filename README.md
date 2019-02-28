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
- Python
  - Numpyについて
    - [【Python入門】Python Numpy チュートリアル](https://avinton.com/academy/python-numpy-tutorial-japanese/)
  - Web系は使う予定は無いが親しみやすいので、[Django](https://docs.djangoproject.com/ja/2.1/)を[触って](https://docs.djangoproject.com/ja/2.1/intro/tutorial01/)Pythonに慣れる
  - スクレイピングについて
    - Scrapy
      - [Scrapy入門 (1)](https://qiita.com/checkpoint/items/038b59b29df8e1e384a2)
- BI
  - [公式のtips](http://navi.wingarc.com/motionboard/)で使いそうなものをやる
    - [x] 主たる分析チャート表示
    - [x] ボタンによるチャート連動
    - [x] チャートクリックでのドリルダウン
    - [x] MBでピボットテーブルライクな自由集計
    - コンテナ利用
      - [x] 検索条件をポップアップ表示
      - [ ] チャートのアニメーション
  - ~~[tableauのサンプル](https://public.tableau.com/s/resources?build=20183.18.1219.1533&edition=public&lang=ja-jp&platform=windows&version=2018.3)で遊ぶ~~
- UML
  - ~~汚いので何とかしたい~~
    - なんともなりませんでした
    - 方向指示語でコントロール可能な大きさになるよう、機能ごとに分割するしかない
  - [打倒！PlantUMLのなにこれレイアウト – VELTRA Engineering – Medium](https://medium.com/veltra-engineering/how-difficult-it-is-to-adjust-the-layout-using-plantuml-997884410db5)
- Linux
  - LPICに向けて
    - とりあえず、[LinuCイージス](https://www.infraeye.com/study/studyz4.html)でざっと確認

## Categories

### BI

- BI全般
  - [BIシステムのアーキテクチャ](./BI/BI.md)
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

### DB

- [PostgreSQL](./DB/postgres.md)
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
  - [チュートリアル内のもの]((./Python/commonlib.md))

### Linux

- [dockerでCentOS](./Linux/centos01.md)
- [基本コマンド：ファイル](./Linux/centos02.md)
- [基本コマンド：プロセス](./Linux/centos03.md)
- [ファイルシステム、パーミッション](./Linux/centos04.md)
- [シェルスクリプト](./Linux/centos05.md)
- ユーザー管理