# ファイルとテキストのコマンド

- [ファイルとテキストのコマンド](#%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%A8%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E3%81%AE%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89)
  - [テキスト処理系](#%E3%83%86%E3%82%AD%E3%82%B9%E3%83%88%E5%87%A6%E7%90%86%E7%B3%BB)
    - [tr](#tr)
    - [expand](#expand)
    - [ソート](#%E3%82%BD%E3%83%BC%E3%83%88)
  - [ファイル処理系](#%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E5%87%A6%E7%90%86%E7%B3%BB)
  - [リダイレクトとパイプ](#%E3%83%AA%E3%83%80%E3%82%A4%E3%83%AC%E3%82%AF%E3%83%88%E3%81%A8%E3%83%91%E3%82%A4%E3%83%97)

## テキスト処理系

### tr

```
tr [ オプション ] 文字列1 [ 文字列2 ]
```

| オプション| 説明|
|-|-|
|-d|「文字列1」で合致した文字列の削除
|-s|連続するパターン文字列を1文字として処理

|文字列の指定方法|説明|
|-|-|
|[ :alpha:]	|英字
|[ :lower:]	|英小文字
|[ :upper:]	|英大文字
|[ :digit:]	|数字
|[ :alnum:]	|英数字
|[ :space:]	|スペース


data.txtの全ての小文字を大文字に変換

```
cat data.txt | tr [:lower:] [:uppder:]
```

もしくは

```
cat data.txt | tr 'a-z' 'A-Z'
```

### expand

テキストファイルのタブをスペースに変換する

デフォルトでは8桁なので、`-t 桁数`で指定してやる

`unexpand`で逆の動きができる

### ソート

- `sort`
  - テキストを並べ替え
- `uniq`
  - 並べ替えテキストをもとに、重複行を削除。
  - `sort data.txt | uniq`
- `wc`
  - ファイルの行数、単語数、文字数を表示する
  ```
  $ wc data.txt
  5 10 300
  ```

## ファイル処理系

- `touch`
  - タイムスタンプ操作のコマンドだが、空ファイル作成にも使われる
- ディレクトリ削除は`rmdir`だが、これは空でなければならない
- ディレクトリごと削除するには、`rm -r dirname`
- アーカイブ
  - 解凍は、
    - `tar xvzf hoge.gz`
    - `tar xvjf hoge.bz2`
    - `unzip hoge.zip`
  - 作成は、
    - `tar vzcf hoge.gz directory` 
  - 中身確認は、
    - `tar tvzf hoge.gz`
  - cpio
    - アーカイブ形式の一つ

## リダイレクトとパイプ

- `>` : リダイレクト
  - コマンドの実行結果をファイルに渡す
  - `<` : ファイルから読み込む
- `|` : パイプ
  - コマンドの出力結果を別のコマンドの標準入力に渡す

ファイルに書き込む

```
ls -la > ../hoge.txt
```

ファイルに追記

```
pwd >> ../hoge.txt
```

- tee
  - `コマンド |tee [-a] ファイル名`
  - コマンドの内容をファイルに書き込んだうえで、標準出力する。