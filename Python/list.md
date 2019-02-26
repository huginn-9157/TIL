# リスト内包表記

新しいリストを作成するときに、短縮して書ける書式

参考
- [Pythonリスト内包表記の使い方 _ note.nkmk.me](https://note.nkmk.me/python-list-comprehension/)
- [5. データ構造 リストの内包表記 — Python 3.7.2](https://docs.python.org/ja/3/tutorial/datastructures.html#list-comprehensions)


例えば以下の文は

```py
squares = []
for i in range(5):
    squares.append(i**2)

print(squares)
# [0, 1, 4, 9, 16]
```

こう書ける

```py
squares = [i**2 for i in range(5)]
print(squares)
# [0, 1, 4, 9, 16]
```

## 条件分岐

ifで条件分岐もできる

```
[式 for 任意の変数名 in イテラブルオブジェクト if 条件式]
```

例

```py
odds = []
for i in range(10):
    if i % 2 == 1:
        odds.append(i)

print(odds)
# [1, 3, 5, 7, 9]
```

```py
odds = [i for i in range(10) if i % 2 == 1]
print(odds)
# [1, 3, 5, 7, 9]
```

この例では条件式に合致するもののみしかリストに格納できないが、  
当然elseも使える

```
[真のときの値 if 条件式 else 偽のときの値 for 任意の変数名 in イテラブルオブジェクト]
```

例

```py
odd_even = []
for i in range(10):
	if i % 2 == 1:
		odd_even.append(11)
	else:
		odd_even.append(44)

print(odd_even)
# [44, 11, 44, 11, 44, 11, 44, 11, 44, 11]
```

```py
odd_even = [11 if i % 2 == 1 else 44 for i in range(10)]
print(odd_even)
# [44, 11, 44, 11, 44, 11, 44, 11, 44, 11]
```

## ネスト

```py
cells = [(row, col) for row in range(3) for col in range(2)]
print(cells)
# [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

### 集合内包表記

角カッコ`[`を波カッコ`{`に変えると、集合(`set型obj`)が生成される

<!-- TODO  set型について -->

### ジェネレータ

角カッコ`[`を丸カッコ`(`に変えると、ジェネレーターが生成される

```py
g = (i**2 for i in range(5))

print(g)
# <generator object <genexpr> at 0x10af944f8>

print(type(g))
# <class 'generator'>

for i in g:
    print(i)
# 0
# 1
# 4
# 9
# 16
```

ジェネレーターオブジェクトはprint()しても表示されない

これはfor文で回して初めて値がメモリに入れられるので、配列のサイズが極端に大きい場合には環境にやさしくて良いらしい

丸カッコで括られているため、引数がジェネレーター式のみの場合はカッコを省略しても良い


