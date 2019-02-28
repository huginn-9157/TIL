# シェルスクリプト

## 実行方法

```sh
source script.sh
# または
bash script.sh
# もしくは
. script.sh
```

実行権限がある場合

```sh
./script.sh
```

でも可

## 書式

１行目に実行するシェルを指定する

```sh
#!/bin/bash
```

### コマンド

#### read

入力待ち

```sh
$ cat hello.sh 

#!/bin/bash
echo -n "What your name: "
read yourname
echo "Hello, $yourname"

$ source hello.sh

What your name: hoge
Hello, hoge
```

#### test

条件分岐の際に使われるboolean

ファイル存在や権限の可否、更新日付比較や数値・文字列比較等、多岐にわたる

#### seq

シーケンス。Python のrange()

```sh
seq [OPTION]... LAST
seq [OPTION]... FIRST LAST
seq [OPTION]... FIRST INCREMENT LAST
```

例
```sh
seq 0 3 20
# 0
# 3
# 6
# 9
# 12
# 15
# 18
```

### 条件分岐

#### if

```sh
if test式
    then
        (Trueの場合)
    else
        (Falseの場合)
    fi
```

```sh
if test式1
    then
        (1=True)
    elif test式2
    then
        (1=False, 2=True)
    else
        (1=False, 2=False)
    fi
```

#### for

```sh
for 変数名 in リスト
    do
        実行分
    done
```

例
```sh
$ cat fortest2.sh

#!/bin/bash
for NUM in `seq 1 3`
do
    echo LinuC Level $NUM
done

$ source fortest2.sh

LinuC Level1
LinuC Level2
LinuC Level3
```

#### while

`while read line`  
はシェルスクリプトでもよく使う

```sh
$ cat whiletest.sh

#!/bin/bash
while read LINE
do
echo LinuC Level $LINE
done < test.txt
```

```sh
$ cat test.txt

1
2
3
```

```sh
$ source whiletest.sh

LinuC Level1
LinuC Level2
LinuC Level3
```
