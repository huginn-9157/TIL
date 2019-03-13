# メモ帳

AS400
- IBMのオフィスコンピューター
  - ハードとか中身のOSとか全部ひっくるめた商品名
  - 企業の基幹システムに使われる
- 現在は`Power Systems`という名称だが、みんなAS400と呼ぶ

HULFT
- ファイル転送システム
- 企業のデータ連携に使われる
  - 形式（ftpかsftpか...）をユーザーが気にする必要が無い

XML
- 持てるルートは１つ
- 要素（タグ）は属性 `name='hoge'`を持てる
- 要素はテキストを持てる `<el>hoge</el>`
- 要素は異なる名前空間 (namespace)に定義できる
  - `<feed xmlns='http://www.w3.org/2005/Atom'>`

Docker
- ホストからコピー
    ```
    $ sudo docker cp my.cnf <コンテナID>:/etc/my.cnf
    ```

hadoop
- インストールで詰まる
  - JavaはOracleのでなければならない
  - SSH接続
    - `/etc/ssh/sshd_config`の編集必須
    - 鍵は正しいパーミッションで無いと弾かれる
      - `chmod 600`
      - ホスト秘密鍵が無ければ、`ssh-keygen -A`で作成
- docker (CentOS) からHiveの起動手順
  ```
  # /usr/sbin/sshd
  # ssh -i ~/.ssh/id_rsa root@localhost
  # start-dfs.sh
  # hive
  ```
