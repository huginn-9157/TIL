# 会計BIの基礎

- [会計BIの基礎](#%E4%BC%9A%E8%A8%88bi%E3%81%AE%E5%9F%BA%E7%A4%8E)
  - [会計システムの基礎](#%E4%BC%9A%E8%A8%88%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0%E3%81%AE%E5%9F%BA%E7%A4%8E)
    - [勘定項目](#%E5%8B%98%E5%AE%9A%E9%A0%85%E7%9B%AE)
    - [利益](#%E5%88%A9%E7%9B%8A)
    - [締め](#%E7%B7%A0%E3%82%81)
  - [分析手法](#%E5%88%86%E6%9E%90%E6%89%8B%E6%B3%95)
    - [BS/PL推移分析](#bspl%E6%8E%A8%E7%A7%BB%E5%88%86%E6%9E%90)
    - [セグメント分析](#%E3%82%BB%E3%82%B0%E3%83%A1%E3%83%B3%E3%83%88%E5%88%86%E6%9E%90)
    - [財務指標分析](#%E8%B2%A1%E5%8B%99%E6%8C%87%E6%A8%99%E5%88%86%E6%9E%90)

財務会計システムのデータを使う  
企業の家計簿を理解しなければならない

## 会計システムの基礎

### 勘定項目

簿記のおさらい

- 資産
- 負債
- 資本
- 収益
- 費用

貸借対照表 (BS)

|借方|貸方|
|-|-|
|資産|負債<br>資本|

----

損益計算書 (PL)

|借方|貸方|
|-|-|
|収益|費用|

全ての項目の増減は、対応する項目の増減と合わせてプラマイゼロになるよう記載される

例
|借方|貸方
|-|-|
|商品仕入れで資産+|買掛金で負債+
|事務用品購入で費用+|預金減で資産-

----

### 利益

```
収益 - 費用
```

通常４つに分類される

- 営業利益
  - 一般的な営業活動
  - ものを仕入れて売る
- 経常利益
  - 営業外利益を計算に入れたもの
    - 銀行からの利息や借入金利息の支払いもここ
  - `経常利益 = 営業利益 + 営業外収益 - 営業外費用`
- 税引前純利益
  - 経常利益に特別利益・損失を加味したもの
    - 土地を売ったとき等
  - `税引前純利益 = 経常利益 + 特別利益 - 特別損失`
- 純利益
  - `税引前純利益 - 税金`

### 締め

お金の出入りの度にシステムのデータは更新されるが、  
システムは一定の区切りごとに貸借対照表と損益計算書を吐き出す。

このタイミングを**締め**と呼び、レポート作成はバッチ処理で行われる

----

## 分析手法

### BS/PL推移分析

- 時間を軸して貸借対照表や損益計算書の数字を並べる
  - その企業の決算月を元に年度を設定
  - 半期決算か四半期か
- 集計項目は実績だけでは不十分
  - 通常、前年度との対比
  - もしくは予測・目標との対比

※予算や目標データはExcelソースにしか無い、という場合も多いので注意。  
その場合はETL処理やBIツールの機能で追加する

### セグメント分析

会社の規模が大きいと、全体を見ただけでは原因はわからない

ので  
勘定科目とは別の次元で仕訳して分析する

- 事業ごと
  - 事業部ごとにわけて表示
- 地域ごと
- 機能ごと
  - 部門を横断して役割毎にセグメントを定義する
  - 販売／生産 といった具合

### 財務指標分析

複数のBS・PL科目に対して[KPI](./Analysis.md#kpi%E3%81%A8%E3%81%AF)を設定し、特定の次元ごとに並べる