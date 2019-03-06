# データベース接続

PythonのDB接続には２通りの方法がある

1. psycopg2を使う
2. sqlalchemyを使う

sqlalchemyはORMであり、システムで扱うならばこちらが推奨されている  
...が、日本語の資料は少ない

## psycopg2

```py
import psycopg2
```

- connect()
  - コネクションを作成
  - [The psycopg2 module content — Psycopg 2.8b1 documentation](http://initd.org/psycopg/docs/module.html?highlight=connect#psycopg2.connect)
  ```py
  conn = psycopg2.connect("dbname=test user=postgres password=pass")
  ```

  または

  ```py
  pgconfig = {
    'host': 'localhost',
    'port': '5432',
    'database': 'test',
    'user': 'postgres',
    'password': 'pass'
  }

  conn = pg.connect(**pgconfig)
  ```

## sqlalchemy

```py
import sqlalchemy
```

- create_engine()
  - コネクションを作成
  ```py
  engine = sqlalchemy.create_engine('postgresql://postgres:pass@localhost:5432/test)
  ```

## データフレームの作成

pandas を使うと手軽にデータフレーム（セル状の形式）に格納できる

```py
import pandas as pd

sql = """
    SELECT * FROM hoge
"""
pd.read_sql(sql, [SQLSlchemyのEngine or psycopg2のconnection])
```