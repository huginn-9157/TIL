# MotionBoard インストール

- [MotionBoard インストール](#motionboard-%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  - [使うもの](#%E4%BD%BF%E3%81%86%E3%82%82%E3%81%AE)
  - [インストール](#%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB)
  - [ポート](#%E3%83%9D%E3%83%BC%E3%83%88)
  - [ログインの確認](#%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%AE%E7%A2%BA%E8%AA%8D)
  - [ドライバーZIPファイルの作成](#%E3%83%89%E3%83%A9%E3%82%A4%E3%83%90%E3%83%BCzip%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E4%BD%9C%E6%88%90)

## 使うもの

- マニュアル
  - [一覧](https://manual.wingarc-support.com/manual/mb/)

----

## インストール

- 設定の履歴は`必ず`残す
  - エビデンス提出を求められたりする。

## ポート

- 本体とRC Serviceは別々
- ポート一覧

>|ポート|解説|
>|-|-|
>|8787|MotionBoardクライアントからMotionBoardサーバーにアクセスするためのポート
>|9797|コマンドラインツールからの接続に使用します。リモートからコマンドラインツールを使用する場合に必要
>|19797|クラスタリング環境で、MotionBoardサーバー間での通信に使用するポート。クラスタリングを有効にした場合に、必要に応じて開放する。
>|49797|拡張プログラムの開発（デバッグ）時に使用する。

- 旧verからのドライバは自動で移行しない
- デフォルトのメモリ割当量は、物理メモリの1/4

## ログインの確認

>MotionBoardのサービスが起動したら、MotionBoardにログインできるかどうかを確認します。ログイン後、初期パスワードを変更します。

ログインURL

```
http://<Webサーバーの名前またはIPアドレス>:8787/motionboard/
```

初回ログイン

```
    テナントID「system」（マルチテナントのライセンスを保有している場合のみ必要）
    ユーザーID「admin@local」
    パスワード「admin」
```


## ドライバーZIPファイルの作成

- driver createコマンドを使ってドライバーZIPファイルを作成
  - 管理者権限で

    ```
    java -jar mbcmd.jar -user MBユーザー名 -pass MBパスワード
    ```

- driver createコマンドを実行して、指定したJDBCドライバーのドライバーZIPファイルを作成。

    ```
    driver create "ZIPファイルパス" "JARファイルパス" "出力先フォルダーパス"
    ```

  - ZIPファイルパス  
  MotionBoardの製品メディアの「EXTRAS」フォルダーに含まれているZIPファイル（ドライバーZIPファイル）のパスを指定。

  - JARファイルパス  
  データベースごとのJDBCドライバーファイルのパス、またはドライバーファイルの存在するフォルダーのパスを指定。

  - 出力先フォルダーパス  
  「<InstallDir>\system\resources\communicator\drivers\extra」を指定します。<InstallDir>は、MotionBoardをインストールしたフォルダーです。

- 自分の環境時メモ

    ```
    driver create D:\TEMP\MotionBoard_5.7_win_warp\EXTRAS\mariadb.zip "C:\Users\user\lib\mariadb-java-client-2.2.6.jar" "C:\MotionBoard57\system\resources\communicator\drivers\extra"
    ```
