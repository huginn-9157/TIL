# データ構造と配列

## Pythonのリスト型

`[0, 1, 2, ..., 10]`はJavaではただの配列だが、  
PythonではJavaのコレクションのように扱える。
- `append()`と`pop()`でスタックとして使える

キューとして使うには、`collections.deque`を使うと良い

```py
from collections import deque
queue = deque([1, 2, 3, 4, 5])
queue = append(9)
queue.popleft()
```

結果
```
1
>>> queue
deque([2, 3, 4, 5, 9])
```

## リストの内包表記

Javaと違い、for文で宣言した変数は残ってしまう

```py
squares = []
for x in range(10):
    squares.append(x**2)
```

```
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> x
9
```

残らないようにするには、以下の方法がある

```py
squares = list(map(lambda x: x**2, range(10)))
```

もしくは

```py
squares = [x**2 for x in range(10)]
```

となる。
２つめの方の書式は

```
[（式） （for句） （0個以上の for か if 句）]
```

ひとつの例じゃわかりにくいのでもう一つ

```py
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
```

は以下と同義である

```py
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
```

## del

del()でリスト内の任意の要素を削除できる
```py
a = [1, 2, 4, 8]
del a[2:]
```

```
>>> a
[1, 2]
```

## set

集合

順番を持たず、重複しない配列、という意味ではJavaと同じ。  
しかし、Pythonでは集合どうしの計算ができる！

```py
a = set('abcdefghijk')
b = set('hijklmnopqr')
```

```
>>> a
{'d', 'k', 'g', 'b', 'h', 'a', 'f', 'i', 'j', 'c', 'e'}
>>> a - b
{'d', 'g', 'b', 'a', 'f', 'c', 'e'}
>>> a | b
{'p', 'b', 'a', 'o', 'i', 'j', 'n', 'e', 'l', 'd', 'k', 'g', 'h', 'q', 'm', 'f', 'c', 'r'}
>>> a & b
{'h', 'i', 'k', 'j'}
>>> a ^ b
{'d', 'g', 'p', 'b', 'a', 'q', 'o', 'r', 'm', 'f', 'e', 'c', 'n', 'l'}
```

## dict

JavaのMapに該当。連想配列

- コンストラクタ
  - `dict([('key1', 'value1'), ('key2', 'value2')])`
- 辞書内包表現も使える
    ```
    >>> {x: x**2 for x in (2, 4, 6)}
    {2: 4, 4: 16, 6: 36}
    ```

## 配列のループ

- `item()`で辞書内の要素（キーと値）を取り出せる

```py
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)
```

```
gallahad the pure
robin the brave
```

- `enumerate()`で要素のインデックスと要素自体を出す
  
```py
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)
```

```
0 tic
1 tac
2 toe
```