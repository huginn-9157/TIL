# ファイルシステムとパーミッション

## Linuxのパーミッション

- 所有者
- グループ
- その他

３つの分類で

- **R**ead : 読み込み
- **W**rite : 書き込み
- e**X**cute : 実行

３種類のアクセス権を設定する

ファイルにread権限があっても、ファイルが存在する  
ディレクトリにexcute権限がなければ読み込めないので注意

![chmod](./img/chmod.png)

|記号表記|2進数|8進数
|-|-|-|
|---|000|0
|--x|001|1
|-w-|010|2
|-wx|011|3
|r--|100|4
|r-x|101|5
|rw-|110|6
|rwx|111|7

アクセス権の設定は`chmod`で行う

```
chmod [-R (Dir再帰指定)] 755 filename
```

### SUID

UID = ユーザを管理するID

一時的に別のUIDに変更できる機能のことを`SUID` (Set User ID)と呼ぶ

SUIDが設定されている場合、所有者パーミッションの`x`にあたる部分が`s`と表記される。

```
# ls -la | grep passwd
-rwsr-xr-x   1 root root     78272 10月 31 01:33 gpasswd
-rwsr-xr-x   1 root root     27832  6月 10  2014 passwd
```
