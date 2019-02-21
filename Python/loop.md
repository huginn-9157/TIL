# Python の制御フロー文

## for

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

## def

関数を定義する。

