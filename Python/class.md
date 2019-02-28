# クラス

## スコープ

Python のスコープの指定

|スコープ|宣言|
|-|-|
|同じ階層|無し(local)
|グローバル|global
|それ以外|nonlocal

> global 文を使うと、特定の変数がグローバルスコープに存在し、そこで再束縛されることを指示できます。   
> nonlocal 文は、特定の変数が外側のスコープに存在し、そこで再束縛されることを指示します。

例

```py
def scope_test():
    def do_local():
        spam = "ローカルスコープ"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal スコープ"

    def do_global():
        global spam
        spam = "global スコープ"

    spam = "test spam"
    do_local()
    print("関数からローカル指定でvar変更:", spam)
    do_nonlocal()
    print("関数からnonlocal指定でvar変更:", spam)
    do_global()
    print("関数からglobal指定でvar変更:", spam)

scope_test()
print("In global scope:", spam)
```

```
関数からローカル指定でvar変更: test spam
関数からnonlocal指定でvar変更: nonlocal スコープ
関数からglobal指定でvar変更: nonlocal スコープ
In global scope: global スコープ
```

関数から既存の変数に再代入する際は、nonlocal、ないしはglobalが必要

----

## クラス

クラスオブジェクトの作成

```py
class MyClass:
    f = 12345
    i = []

    def __init__(self, name):
        self.name = name

    def add_i(self, i):
        self.i.append(i)

    def set_f(self, num):
        self.f = num

x = MyClass('A')
y = MyClass('B')

x.set_f(9999)
y.set_f(0000)
x.add_i(1)
x.add_i(2)
y.add_i(4)
```

```py
>>> x.f
9999
>>> y.f
0000
>>> x.i
[1, 2, 4]
>>> y.f
[1, 2, 4]
```

- `self`
    - 指定しないと、インスタンス化したときに取り出せなくなる
    - 単語自体に意味があるわけでは無く、単なる慣習
- クラス変数とインスタンス変数
  - クラス変数(上の例では`f`)がMutableの場合、クラス間で共通となってしまう点に注意
  - Mutableな変数を扱う場合、init内で宣言するなどして、インスタンス変数に格納する
- インスタンス作成
  - ただ代入するだけ

### クラスの例２

```py
lass Greeter(object):
	# コンストラクタ
	def __init__(self, name):
		self.name = name # インスタンス変数を作成
	# インスタンスメソッド
	def greet(self, loud=False):
		if loud:
			print('H E L L O, %s!' % self.name.upper())
		else:
			print('Hello, %s' % self.name)
```

呼び出し

```py
g = Greeter('Andrew')
g.greet()
# Hello, Andrew
g.greet(loud=True)
# H E L L O, ANDREW!
```

### クラスの継承

```py
class ClassName(Base1, Base2, ...)
```

クラスは多重継承もできる

### プライベート変数

`private`修飾子はPythonには存在しない

かわりに、頭にアンダースコアを付けている変数 `_name` は  非publicとしてあつかう**慣習**がある
