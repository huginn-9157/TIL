# 組み込み関数

[Python 3.7.2 組み込み関数](https://docs.python.org/ja/3/library/functions.html)

いつでも利用できる関数  
名前が被ると混乱のもとなので、最低限は覚えておく

|||組み込み関数|||
|-|-|-|-|-|
abs()|delattr()|hash()|memoryview()|set()
all()|dict()|help()|min()|setattr()
any()|dir()|hex()|next()|slice()
ascii()|divmod()|id()|object()|sorted()
bin()|enumerate()|input()|oct()|staticmethod()
bool()|eval()|int()|open()|str()
breakpoint()|exec()|isinstance()|ord()|sum()
bytearray()|filter()|issubclass()|pow()|super()
bytes()|float()|iter()|print()|tuple()
callable()|format()|len()|property()|type()
chr()|frozenset()|list()|range()|vars()
classmethod()|getattr()|locals()|repr()|zip()
compile()|globals()|map()|reversed()|\_\_import\_\_()
complex()|hasattr()|max()|round()|

## all(iterable)

iterableが全て真か、もしくは空なら  
`True`を返す

## any(iterable)

iterableのどれかが真なら  
`True`  
空なら  
`False`

## chr(i)

ユニコードコード`i`の文字を返す

逆は`ord(c)`

## dir()

名前一覧を出す

## divmod(a, b)

`a` / `b` の商と余りを表示する

```py
divmod(10,3)
# (3, 1)
```

## enumerate(iterable)

iterableに順番を付けて返す

```py
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
```
