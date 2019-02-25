# Linux 学習

なんとなくLinux Mintを使っているだけだったが、  
[LPIC Level 1程度](https://www.infraeye.com/study/studyz4.html)の知識の定着を目指す。

## LPICとLinuC

直接関係は無いらしい

LinuCは日本向けに最近出たもの
LPICは世界基準だが、LinuCは全然関係ないとのこと

どうやら[分裂](https://qiita.com/Alpha_Nine/items/15e4eb478166fcf9008d)した模様

## 環境構築

Windows でCentOSを動かすにはWSLの手もあるが、
マシン環境に依存しないに越したことはない

ということでDockerを使う
[Docker for Windows をインストールしCentOSを起動するまでの手順をまとめる - orangeitems’s diary](https://www.orangeitems.com/entry/2018/06/18/153510)

### Docker for Windows

コンテナ管理  
作成からコンテナ保存まで一通り

1. DockerImageを作成
   - リポジトリから持ってくる
   - イメージ一覧 : `docker images`
2. イメージからコンテナを作成
   - `docker run -it [--name "コンテナ名" | リポジトリ名]`
   - コンテナ一覧 : `docker ps -a`
3. コンテナに接続
   - `docker attach コンテナ[名|ID]`
4. コンテナをイメージに保存
   - `docker commit コンテナ[名|ID] リポジトリ名[:タグ名]`
   - これを`2`で起動すればよい

留意点
- コンテナは破棄(`docker rm コンテナ[ID|名]`)されるまで変更は保持される。
- コンテナは作成した分だけ増える。`docker ps`だけだと起動しているコンテナ(`docker start`)のみしか表示されないので注意。

参考
- [Dockerの作業済みコンテナからイメージを作って移植を楽にする - Qiita](https://qiita.com/tubone/items/a3bad04abf4c700cae3d)
- [Dockerのライフサイクルがよくわからなかった - Qiita](https://qiita.com/0ashina0/items/f8b960e822a40a6a2eed)
- [DockerでCentOS 7のイメージを利用してみよう _ WEB ARCH LABO](https://weblabo.oscasierra.net/docker-centos7/)

通常、コンテナイメージはDockerfileで管理する  
[Window10に日本語対応CentOS7のdockerコンテナを作ってみた - Qiita](https://qiita.com/0ashina0/items/f8b960e822a40a6a2eed)

今回は一先ず動けば良いのでここまで
