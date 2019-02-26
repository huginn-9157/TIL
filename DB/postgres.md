# PostgreSQL

[公式リファレンス v10.5](https://www.postgresql.jp/document/10/html/index.html)

- [PostgreSQL](#postgresql)
  - [コマンドの相違点](#%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%AE%E7%9B%B8%E9%81%95%E7%82%B9)
  - [データ型](#%E3%83%87%E3%83%BC%E3%82%BF%E5%9E%8B)
    - [シーケンス](#%E3%82%B7%E3%83%BC%E3%82%B1%E3%83%B3%E3%82%B9)
  - [INSERT時のカラム名省略について](#insert%E6%99%82%E3%81%AE%E3%82%AB%E3%83%A9%E3%83%A0%E5%90%8D%E7%9C%81%E7%95%A5%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6)
    - [データのインポート](#%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E3%82%A4%E3%83%B3%E3%83%9D%E3%83%BC%E3%83%88)
  - [SELECT句](#select%E5%8F%A5)
  - [テーブル結合](#%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB%E7%B5%90%E5%90%88)
  - [トランザクション](#%E3%83%88%E3%83%A9%E3%83%B3%E3%82%B6%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3)
  - [ウインドウ関数](#%E3%82%A6%E3%82%A4%E3%83%B3%E3%83%89%E3%82%A6%E9%96%A2%E6%95%B0)

----

MariaDBとの違いに重点を置いて書く

コマンドツール回りで最も違う点として、
DB内のCRUDコマンド以外は別のバイナリから実行することが多い

- createdb
- createuser

等

## コマンドの相違点

[PostgreSQLとMySQLの基本的なコマンドを比較 - Qiita](https://qiita.com/pugiemonn/items/75870ece3c8476bcb1c8)

|コマンド|PostgreSQL|MySQL
|-|-|-|
データーベースを作成|createdb database_name | CREATE DATABASE database_name;
データベース一覧を表示|psql -l<br>\l | SHOW DATABASES;
データーベースへ接続 | psql database_name | USE database_name;
テーブル一覧を表示 | \d | SHOW TABLES;
テーブルカラムの一覧表示 | \d table_name | DESC table_name;
ユーザーを作成 | createuser user_name | CREATE USER user_name;
ユーザー一覧を表示 | \du | SELECT User, Host FROM mysql.user;
ログアウト | exit <br>\q | exit;

## データ型

real型
- 浮動小数点、６桁まで

point型
- Postgre 独自の型の一つ
- 幾何データ型の一種
  - >幾何データ型は2次元空間オブジェクトを表現します  
     一番の基本となる型はpointで、すべての他の型の基礎を形成します
  - point型は平面における座標点を格納するためのもの

serial型
- 自動増分4バイト整数
  - `int AUTO INCREMENT`
- これが含まれるテーブルを作成すると、同スキーマに[シーケンス](#シーケンス)が作成される。

### シーケンス

DBのキーカラムに設定する自動連番のこと

MySQLでいう`AUTO INCREMENT`  
PostgreSQLでは物理的にテーブルと分けられている

```
test=# \d students_id_seq
             シーケンス "pg_temp_5.students_id_seq"
   型    | 開始 | 最小 |    最大    | 増分 | 循環？ | キャッシュ
---------+------+------+------------+------+--------+------------
 integer |    1 |    1 | 2147483647 |    1 | no     |          1
```

備考：  
[DBの自動連番がロールバックしても戻らない理由 - C Sharpens you up](http://cs.hatenablog.jp/entry/2014/03/14/103358)

----

## INSERT時のカラム名省略について

>多くの開発者は、暗黙的な順番に依存するよりも、列のリストを明示的に指定する方が良いやり方だと考えています。

ちゃんと書きます

### データのインポート

ファイルシステムから読み込む専用のコマンドとして、  
[COPYコマンド](https://www.postgresql.jp/document/10/html/sql-copy.html)がある

```sql
COPY テーブル名 FROM '/home/user/datatable.txt';
```

<!-- TODO COPYコマンドについてkwsk -->

## SELECT句

基本的に同じ

## テーブル結合

以下のINNER JOIN文は

```sql
SELECT *
    FROM weather w INNER JOIN cities c ON (w.city = c.name);
```

次のようにも書ける

```sql
SELECT *
    FROM weather w, cities c
    WHERE w.city = c.name;
```

- `AS`は省略してもよい
- JOIN構文も同じと考えてよい

----

他、集約関数、DELETE、UPDATEやビューも同じ

## トランザクション

>一連の操作の過程で可視性ということにおいてもトランザクションは「すべて」か「なし」かでなければなりません。

通常、全てのSQL文は、BEGINを指定しないと暗黙のうちに  
BEGIE ~ COMMITで囲まれる。

途中でセーブポイントを作ることもできる

```sql
BEGIN;
UPDATE accounts SET balance = balance - 100.00
    WHERE name = 'Alice';
SAVEPOINT my_savepoint;
UPDATE accounts SET balance = balance + 100.00
    WHERE name = 'Bob';
-- おっと、忘れるところだった。ウィリーの口座を使わなければ。
ROLLBACK TO my_savepoint;
UPDATE accounts SET balance = balance + 100.00
    WHERE name = 'Wally';
COMMIT;
```

## ウインドウ関数

全ての行を集計した上でなんらかの計算結果を`一行毎に`返す関数

計算結果を一行でだす集約関数とは別

```
SELECT 式 OVER(ウインドウ関数);
```

として指定する

ウインドウ関数には、