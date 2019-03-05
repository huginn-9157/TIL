# クラス

- [クラス](#%E3%82%AF%E3%83%A9%E3%82%B9)
  - [スコープ](#%E3%82%B9%E3%82%B3%E3%83%BC%E3%83%97)
  - [クラス](#%E3%82%AF%E3%83%A9%E3%82%B9-1)
    - [クラスの例２](#%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AE%E4%BE%8B%EF%BC%92)
    - [クラスの継承](#%E3%82%AF%E3%83%A9%E3%82%B9%E3%81%AE%E7%B6%99%E6%89%BF)
    - [プライベート変数](#%E3%83%97%E3%83%A9%E3%82%A4%E3%83%99%E3%83%BC%E3%83%88%E5%A4%89%E6%95%B0)
    - [イテレーターの作り方](#%E3%82%A4%E3%83%86%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC%E3%81%AE%E4%BD%9C%E3%82%8A%E6%96%B9)

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

- `__init__`
  - クラスのインスタンスが生成すると、最初に呼ばれる
  - インスタンスの作成には、これが要求する引数を渡す
  - コンストラクタに似ているが、厳密には違う
    - 何故なら、これが呼ばれる前に既にインスタンスへアクセスできるから
- `self`
  - 全てのメソッドの最初の引数は、呼び出されたインスタンスそのものを指す
  - メソッドには必ず書くが、呼ぶときに引数を渡してはならない。Python側が自動で行う
  - 単語自体に意味があるわけでは無いが、強い慣習
  - `self.xxx`とすると、インスタンス変数になり他のメソッドからアクセスできる
- クラス変数とインスタンス変数
  - クラス変数(上の例では`f`)がMutableの場合、クラス間で共通となってしまう点に注意
  - Mutableな変数を扱う場合、init内で宣言するなどして、インスタンス変数に格納する

### クラスの例２

```py
lass Greeter(object):
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

### イテレーターの作り方

> イテレータとは`__iter__()`メソッドを実装した単なるクラスだ

```py
class Fib:
	'''iterator that yields number in the Fibonacci sequence'''

	def __init__(self, max):
		self.max = max
	def __iter__(self):
		self.a = 0
		self.b = 1
		return self
	def __next__(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib
```

- `__iter__`はiter(インスタンス名)で呼び出せる。
  - ループの初期化処理
  - forループはこれを自動で呼びだす
- `__next__`
  - ループ処理
