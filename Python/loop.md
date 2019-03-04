# Python の制御フロー文

- [Python の制御フロー文](#python-%E3%81%AE%E5%88%B6%E5%BE%A1%E3%83%95%E3%83%AD%E3%83%BC%E6%96%87)
	- [for()](#for)
		- [enumerate](#enumerate)
	- [pass](#pass)
	- [def()](#def)
		- [引数のデフォルト値](#%E5%BC%95%E6%95%B0%E3%81%AE%E3%83%87%E3%83%95%E3%82%A9%E3%83%AB%E3%83%88%E5%80%A4)
		- [キーワード引数](#%E3%82%AD%E3%83%BC%E3%83%AF%E3%83%BC%E3%83%89%E5%BC%95%E6%95%B0)
		- [可変長引数](#%E5%8F%AF%E5%A4%89%E9%95%B7%E5%BC%95%E6%95%B0)
			- [*args](#args)
			- [**kwargs](#kwargs)

## for()

あらかじめ配列を作っておかなくとも、`range()`で指定した数だけ反復を行える

```python
for i in range(10):
    print(i)
```

for文やwhile文に`else`を付けられる  
これはリストを使い切ったときに実行される  
`break`との組み合わせを想定している

```python
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', x//x)
			break
		else:
			print(n, 'is a prime number')
```

### enumerate

`enumerate()`を指定すると、配列のインデックスがとれる  
カウンターいらず

```py
for i, n in enumerate(fib(5000)):
	print('{0:02d}: {1:04d}'.format(i + 1, n), end=' ')
	if (i != 0):
		if ((i + 1) % 4 == 0):
			print('')
```

## pass

何もしない！

```python
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)
```

最小のクラス

```python
class MyEmptyClass
    pass
```

## def()

関数を定義する。

例によって返す型の宣言はいらない  
メソッド内にreturnが無くともよい  
その場合、内部では`None`が返っている

フィボナッチ数列の例（引数で上限を定める）

```python
def fib(n):
	a, b = 0, 1
	while a < n:
		print(a, end=', ')
		a, b = b, a + b
	print()
```

実行結果

```
>>> fib(2000)
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 
```

ちゃんと数列を返すようにすると

```py
def fib2(n):
	result =  []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result
```

結果

```
>>> fib2(2000)
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
```

### 引数のデフォルト値

引数にはデフォルト値を指定できる

```py
def hoge(must_param, arg1='省略された際の', arg2='デフォルト値'):
    print(arg1 + arg2)
```

結果

```
>>> hoge(1)
省略された際のデフォルト値
```

### キーワード引数

デフォルト引数を持つ関数の呼び出しについて

呼び出す関数内で、hoge(must_param = 1)というように  
キーワードで引数を指定できる

上の[hoge()](#引数のデフォルト値)の例で試す

〇 `hoge(must_param = 'foo', arg1 = 'bar')`  
〇 `hoge('foo', arg1 = 'bar')`  

✖ `hoge(arg1 = 'foo', arg2 = 'bar')`  
✖ `hoge(arg1 = 'foo', 'bar')`  

キーワード引数は、必須の引数（デフォルト値が指定されていないもの）の後に書かなければならない！

### 可変長引数

ってなんぞ  
[Pythonの可変長引数（_args, __kwargs）の使い方 _ note.nkmk.me](https://note.nkmk.me/python-args-kwargs-usage/)

```py
def hoge(*arg, **kwargs)
```

- `*args`: 複数の引数をタプルとして受け取る
- `**kwargs`: 複数のキーワード引数を辞書として受け取る

この名前で使われる慣習がある

#### *args

`*args` に該当する位置以降がタプルとして渡され、  
関数内で`*`を外すと展開して呼び出される

```py
def my_sum2(*args):
	print('args: ', args)
	print('type: ', type(args))
	print('sum: ', sum(args))

	
my_sum2(1, 2, 3, 4)
# args:  (1, 2, 3, 4)
# type:  <class 'tuple'>
# sum:  10
```

#### **kwargs

要素数が不定の辞書を処理できる

```py
def get_list(**kwargs):
	for pg_key, pg_val in kwargs.items():
		print(pg_key, pg_val)

		
get_list(A01 = 'python', A02 = 'java', A03 = 'C#')
# A01 python
# A02 java
# A03 C#
```