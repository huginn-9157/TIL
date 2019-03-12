#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), 'Python'))
	print(os.getcwd())
except:
	pass
#%% [markdown]
# # pandas 学習
# 
# 既存のデータを利用してpandasを学習するQiitaの記事より
# あとjupyterの練習もかねて
# 
# ## 使うもの
# 
# [データ分析で頻出のPandas基本操作 - Qiita](https://qiita.com/ysdyt/items/9ccca82fc5b504e7913a)
# 
# 使用データ
# [コンペティション詳細／SIGNATE／データ _ SIGNATE - Data Science Competition](https://signate.jp/competitions/24/data)
#%% [markdown]
# ### 基本操作

#%%
import numpy as np
import pandas as pd


#%%
df = pd.read_csv('C:\\Users\\user\\Downloads\\train.csv')


#%%
df.head(5)


#%%
print('dataframeの行数・列数の確認==>\n', df.shape)
print('\nindexの確認==>\n', df.index)
print('\ncolumnの確認==>\n', df.columns)
print('\ndataframeの各列のデータ型を確認==>\n', df.dtypes)


#%%
# 任意の列だけ取り出したい場合
df[['name', 'kcal']].head()


#%%
# index指定
df.loc[100]


#%%
# 1,2,4 行目と 0~1 列目を取得
df.iloc[[1,2,4],[0,2]]


#%%
# 条件指定もできる
df[df['kcal'] > 450]


#%%
# queryメソッドを使うと、複数条件の指定で、特定カラムだけ出力もできる
df[['name', 'kcal']].query('name.str.contains("豚肉")')


#%%
# 上の絞り込み
df[['name', 'kcal']].query('kcal > 450 and name.str.contains("豚肉")')

#%% [markdown]
# #### クエリ指定 query()
# 
# [pandas.DataFrameの行を条件で抽出するquery _ note.nkmk.me](https://note.nkmk.me/python-pandas-query/)
# 
# ----
# 

#%%
# 列のデータ確認
df['remarks'].unique()


#%%
# datatime列内で重複確認
print(len(df), len(df['datetime'].unique()))


#%%
# 行方向で重複行を削除
df.drop_duplicates()
print(df.shape)


#%%
# 要約統計量の表示
df.describe()

#%% [markdown]
# ----
# 
# ### データの整形

#%%
# datetime列をindexにする
df.set_index('datetime', inplace=True)
df.head()


#%%
df.index


#%%
# カラム名を変更する (y を sales に変換)
df.rename(columns={'y': 'sales'}, inplace=True)
df.head()


#%%
# 'sales'列を降順で並び変え
df.sort_values(by="sales", ascending=True).head()


#%%
# sort_values は複数の列に対しても実行できる
df.sort_values(['sales', 'temperature'], ascending=False)[5:10]


#%%
# indexのデータ型を確認する
df.index


#%%
# indexのtype変更 object -> datetime64[ns]
df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
df.index

#%% [markdown]
# #### date文字列はdate型にしておく
# 
# Tableauは文字列のままでも自動で日付として取り込んでくれるが、MBでは明示しておく必要がある
# 
# これはPythonにおいても同じであり、object型のままだと正しくソートされなかったり、集計できないので困ることになる。

#%%
df.sort_index().head()


#%%
# resample()で 日付をもとに集計
df.resample('M').mean() # 月単位の平均値


