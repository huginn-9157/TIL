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

rules = []
with open('plural4-rules.txt', encoding='utf-8') as pattern_file:
    for line in pattern_file:
        pattern, search, replace = line.split(None, 3)
        rules.append(build_match_and_apply_functions(
                pattern, search, replace))

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)
```

クロージャについてあさっても、いまいちしっくりこない  
何が分からなかったのかは、ここでようやくわかった

[Python 関数に関数を渡す（高階関数） _ 鎖プログラム](https://pg-chain.com/python-function-2)

`高階関数` = 関数の引数に関数を使うこと  
を理解してなかった

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

クロージャと呼ばれるものについて、大分して２つある
- 関数の中で（動的に）作られる関数のこと
  - ＝高階関数
- グローバルな変数に頼らずに、関数の中に環境を閉じ込めておくこと

今回詰まったのは高階関数の仕組みであった

上の[コード](#クロージャ)で読めなかった部分
- for文で回しているのは何なのか
  - →rules[]に入っている関数のリスト
    - matches_rules()とapply_rule()
- 引数の`word`はどうやって渡されているのか
  - plural(noun)が呼ばれたときに、for文の中で引数が定義されている

詰まった理由として、「関数もオブジェクト」を理解していなかったことが一番

- リストには関数も入れられ、その中の変数は呼ばれたときに初めて実態として現れる
- 関数内の何だかわからない関数のようなものはクロージャであった

----

## ジェネレーター

`yield` は関数を一旦止める。  
値を吐き出したら再開する。

`yield`が入っている関数はジェネレーターとなり、  
ジェネレーターは名前のイメージ通り、実行されて初めて中身が生成される。

これはモジュールの起動時間を少なくするが、  
逆に言えば呼ばれるたんびに処理をはじめから行うということになる。

```py
def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

for i, n in enumerate(fib(5000)):
	print(f'{n:04d}', end=' ')
	if (i > 0):
		if ((i + 1) % 4 == 0):
			print('')

# 0000 0001 0001 0002 
# 0003 0005 0008 0013 
# 0021 0034 0055 0089 
# 0144 0233 0377 0610 
# 0987 1597 2584 4181 
```
