# 入出力とフォーマット

- [入出力とフォーマット](#%E5%85%A5%E5%87%BA%E5%8A%9B%E3%81%A8%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88)
  - [フォーマット済み文字列リテラル](#%E3%83%95%E3%82%A9%E3%83%BC%E3%83%9E%E3%83%83%E3%83%88%E6%B8%88%E3%81%BF%E6%96%87%E5%AD%97%E5%88%97%E3%83%AA%E3%83%86%E3%83%A9%E3%83%AB)
  - [ファイルの読み書き](#%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E8%AA%AD%E3%81%BF%E6%9B%B8%E3%81%8D)
    - [ファイルオブジェクトのメソッド](#%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%AA%E3%83%96%E3%82%B8%E3%82%A7%E3%82%AF%E3%83%88%E3%81%AE%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89)

## フォーマット済み文字列リテラル

- 文字列頭に`f/F`を付ける

    ```py
    year = 2019
    month = 2
    date = 22
    f'now : {year}/{month}/{date}
    ```

    ```
    'now : 2019/2/22'
    ```

    `:02d`とつけると0埋め2桁位取り

    ```
    >>> f'now {year}/{month:02d}/{date}'
    'now 2019/02/22'
    ``` 

    `:.3f`で小数点３桁位取り

    ```py
    import math
    print (f'円周率は {math.pi:.3f}')
    ```

    ```
    円周率は 3.142
    ```

    >書式については、[書式指定文字列の文法](https://docs.python.org/ja/3/library/string.html#formatstrings)
    を参照

    - format()

    Javaのstring.format()に相当
    ```
    >>> 'hogehoge {}, {}'.format('foo', 'bar')
    'hogehoge foo, bar'
    ```

    `{}`内にはキーワードを入れてもよいし、順序引数(0, 1, 2...)を入れてもよい

    ```py
    for(i in range(1, 11)):
        print('{0:2d} {1:3d} {2:4d}.format(x, x*x, x*x*x)
    ```

    ```
    1   1    1
    2   4    8
    3   9   27
    4  16   64
    5  25  125
    6  36  216
    7  49  343
    8  64  512
    9  81  729
    10 100 1000
    ```

## ファイルの読み書き

open()でファイルを指定して、read()したりclose()したりする

>open() は file object を返します。  
大抵、 open(filename, mode) のように二つの引数を伴って呼び出されます。

```py
 with open("hoge.txt", 'r', encoding="utf-8") as f:
	read = f.read()
	print(read)
```

```
（hoge.txtの中身）
```

- 留意点
  - Windows環境の場合、デフォルトのエンコーディングがSJISになっている。（参考：[WindowsでCP932(Shift-JIS)エンコード以外のファイルを開くのに苦労した話 - Qiita](https://qiita.com/Yuu94/items/9ffdfcb2c26d6b33792e)
  - `with open(file) as name:`
    - withを指定してやると、自動でclose()してくれる
    - Javaのtry with resource
    - ファイルを閉じてしまうと、read()はできない。もう一度open()する必要がある

### ファイルオブジェクトのメソッド

一行ずつ読み込む

```py
with open("Dockerfile", 'r', encoding="utf-8") as f:
	for line in f:
        print(line, end='')
```

全ての行を一行にする

```py
with open("Dockerfile", 'r', encoding="utf-8") as f:
    print(f.readlines())
```