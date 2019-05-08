# SQL構文

達人に学ぶSQL徹底指南書

著者：ミック

出版社：翔泳社

## 読書メモ

### 一章

#### CASE文
- ELSEを省略すると、`ELSE NULL` の扱いになる
    - 明示的にELSE文を書くこと
- CASEでグループ化
    ```sql
    SELECT CASE pref
        WHEN '宮城' THEN '東北'
        WHEN '山形' THEN '東北'
        ELSE 'その他'
        END AS district,
    SUM(population)
    FROM tb1
    GROUP BY district
    ```
    - **上の句は、OracleやSQL Serverだとエラーになる**
    - 同じCASE文を２度書かなければならない

