# 標準ライブラリ

[Python 3.7.2 標準ライブラリ](https://docs.python.org/ja/3/library/index.html#library-index)

インポートして使う

```py
import ライブラリ名
```



- os
  - OSのAPIを使う
  - `os.getcwd()`
    - カレントDir取得
  - `os.chdir('directory')`
    - カレントDir変更
- glob
  - ワイルドカードでファイル名を取ってくる
  - `glob.glob('*.py')`
    ```
    ['open.py', 'testclass.py']
    ```
- re
  - 正規表現マッチング
  - `re.findall(r'\d+', 'Lose O\'2 We Stand!!')`
    ```
    ['2']
    ```
- random
  - JavaのMath.randomより楽な使い勝手
  - `choice(配列)`
    - リストから一つ選んで返す
  - `sample(range(n), i)`
    - nの範囲でi個選んで出す
  - `randrange(n)`
    - 0 ~ n-1 の範囲で一つ選んで出す
- statistics
  - 基本的な統計
  - `mean(配列)`
    - 平均値
  - `median(配列)`
    - 中央値
- urllib.request
  - urlからデータを取得
    ```py
    with urlopen('https://docs.python.org/ja/3/tutorial/stdlib.html') as response:
	for line in response:
		line = line.decode('utf-8')
		if 'インターネット' in line:
		       print(line)
    ```
- datetime
  - 日付と時刻
    ```py
    from datetime import date
    now = date.today()
    now
    # datetime.date(2019, 2, 27)
    ```
  - 曜日の日本語フォーマットは無いんかな？
    ```py
     day = {'Mon': '月曜日', 'Tue': '火曜日', 'Wed': '水曜日', 'Thu': '木曜日', 'Fri': '金曜日', 'Sat': '土曜日', 'Sun': '日曜日'}
     print(now.strftime("%Y年%m月%d日"), day[now.strftime("%a")])
     # 2019年02月27日 水曜日
     ```
- データ圧縮
  - 主要な圧縮形式のモジュールが揃っている
  - zlib, gzip, bz2, lzma, zipfile, tarfile
- パフォーマンス計測
  - `timeit`
    - 一行分のパフォーマンス計測
  - より大きな粒度向けとして、`profile`や`pstat`がある
- doctest
  - docstring(`"""`で囲まれた部分)に埋め込まれたテストの評価を行う
  - 例
    ```py
    def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

    import doctest
    doctest.testmod()   # automatically validate the embedded tests
    ```
    問題が無ければ、何も返さない
  - 上の例でテスト結果を誤って`30`とすると
    ```
    ******************************************************
    File "D:\Python\docstring_test.py", line 4, in __main__.average
    Failed example:
        print(average([20, 30, 70]))
    Expected:
        30.0
    Got:
        40.0
    ******************************************************
    1 items had failures:
    1 of   1 in __main__.average
    ***Test Failed*** 1 failures.
    ```
    エラー文が表示される
- unittest
  - junitのように、網羅的なテストをクラス単位に別ファイルで管理する
- 出力
  - reprlib
    - 長い配列等の省略表示
  - pprint
    - 配列を次元毎に改行して表示
    - `pprint(配列, width=n)`
  - textwrap
    - 文字数指定で折り返し
    - `fill(文字列, width=n)`
- 文字列テンプレート
    ```py
    from string import Template
    t = Template('こんにちは、$hoge。')
    d = dict(hoge='新田氏')
    t.substitute(d)
    # 'こんにちは、新田氏。'
    ```
