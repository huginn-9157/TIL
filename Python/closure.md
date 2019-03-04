# クロージャ

[クロージャとジェネレータ - Dive Into Python 3 日本語版](http://diveintopython3-ja.rdy.jp/generators.html)

ここのコードがさっぱりわからない

```py

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)
```

クロージャについてあさっても、いまいちしっくりこない

そもそも、`高階関数` = 関数の引数に関数を使うこと  の意味がわかってなかった！

----

## 高階関数

```py
def convert_type(num, type):
    if type == 16:
        # 16進数に変換する
        return hex(num)
    elif type == 2:
        # 2進数に変換する
        return bin(num)

# 高階関数
# funcにあたる部分は関数であるが、
# この部分に他の関数を呼べるということ
# 関数内のfuncはただの名前なので、参照して考える
def convert_hex(func, num):
    return func(num, 16)

# funcの部分に'convert_type()'を当てはめる
convert_hex(convert_type, 100)
# 0x64

```

引数２つに対して、動的なものが３つできるというのが  
最初どうにも解せなかったが、残りの一つは呼び出された方の関数を見に行けばいいと納得

半日かかった。

## クロージャとは

>『定義が評価された時の環境を閉じ込めて一緒に包んでしまうこと』  
[Java - 恥ずかしながらクロージャが分かりません。｜teratail](https://teratail.com/questions/41031)

関数の中で（動的に）作られる関数のことをクロージャと呼ぶ  
呼ばれたときの**環境**を保持しておく

オブジェクトが持つ環境

|オブジェクト|環境|
|-|-|
|クラス|フィールド、プロパティ|
|関数|クロージャ|

執筆中...