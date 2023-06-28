import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pip install matplotlib
from datetime import datetime, timedelta

# データ取得先
# https://www.data.jma.go.jp/risk/obsdl/index.php

# データの読み込み
data1 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\test_csv\\data.csv')
# 欠損値あり
data2 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\test_csv\\data2.csv')
data3 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\test_csv\\data3.csv')

# 年月日列を日付型に変換
data1['年月日'] = pd.to_datetime(data1['年月日'])
data2['年月日'] = pd.to_datetime(data2['年月日'])
data3['年月日'] = pd.to_datetime(data3['年月日'])


# 最新の30日分のデータを抽出
latest_data1 = data1.tail(365)
# latest_data2 = data2.tail(56)
latest_data3 = data3.tail(365)

# 日付をキーにしてデータをマージ
# 日付をキーにしなくてよさそう。もしやるならデータを整形してある期間だけを抽出する
# https://sci-pursuit.com/math/statistics/correlation-coefficient.html
# merged_data = pd.merge(latest_data1, latest_data2, on='年月日')
merged_data = pd.merge(latest_data1, latest_data3, on='年月日')

# 降水量列の相関係数を計算

# correlation = np.corrcoef(merged_data['東京降水量'], merged_data['博多降水量'])[0, 1]
correlation = np.corrcoef(merged_data['東京降水量'], merged_data['埼玉降水量'])[0, 1]

# 結果の表示
print("相関係数:", correlation)

# 散布図の作成
# plt.scatter(merged_data['東京降水量'], merged_data['博多降水量'])
plt.scatter(merged_data['東京降水量'], merged_data['埼玉降水量'])

# x,y軸のデータをグラフ化
# plt.scatter(merged_data['年月日'], merged_data['東京降水量'], c='blue', label='東京降水量')
# plt.scatter(merged_data['年月日'], merged_data['埼玉降水量'], c='red', label='埼玉降水量')
# # 
# plt.scatter(merged_data['年月日'], merged_data['東京降水量'], c='green', label='東京降水量')
# plt.scatter(merged_data['年月日'], merged_data['博多降水量'], c='yellow', label='博多降水量')


# グラフのタイトルと軸ラベルの設定
plt.title('Scatter Plot')
plt.xlabel('tokyo')
# plt.ylabel('hakata')
plt.ylabel('saitama')

#DataFrameのすべての値をループで出力
# for index, row in merged_data.iterrows():
#     for column in merged_data.columns:
#         value = row[column]
#         # print(f"({index}, {column}): {value}")


# グラフの表示
plt.show()