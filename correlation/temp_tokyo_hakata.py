import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pip install matplotlib
from datetime import datetime, timedelta

# データの読み込み
data1 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\test_csv\\data.csv')
data2 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\test_csv\\data2.csv')

# 開始日付の設定
start_date = datetime(2019, 1, 1)  # 開始日を適宜変更してください


# 年月日列を日付型に変換
data1['年月日'] = pd.to_datetime(data1['年月日'])
data2['年月日'] = pd.to_datetime(data2['年月日'])


# 最新の30日分のデータを抽出
latest_data1 = data1.tail(30)
latest_data2 = data2.tail(30)

# 日付をキーにしてデータをマージ
merged_data = pd.merge(data1, data2, on='年月日')
print(merged_data)

# 降水量列の相関係数を計算

correlation = np.corrcoef(merged_data['東京降水量'], merged_data['博多降水量'])[0, 1]

# 結果の表示
print("相関係数:", correlation)

# 散布図の作成
plt.scatter(merged_data['東京降水量'], merged_data['博多降水量'])

# グラフのタイトルと軸ラベルの設定

plt.title('Scatter Plot')
plt.xlabel('data1')
plt.ylabel('data2')

# グラフの表示
plt.show()