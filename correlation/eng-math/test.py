import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pip install matplotlib
from datetime import datetime, timedelta

# データ取得先
# https://www.data.jma.go.jp/risk/obsdl/index.php

# データの読み込み
data1 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\eng-math\\test1.csv')
data2 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\eng-math\\test2.csv')

# 最新の11人分のデータを抽出
latest_data1 = data1.tail(11)
latest_data2 = data2.tail(11)

# 日付をキーにしてデータをマージ
merged_data = pd.merge(latest_data1, latest_data2, on='student')

# 試験結果の相関係数を計算
correlation = np.corrcoef(merged_data['math'], merged_data['english'])[0, 1]

# 結果の表示
print("相関係数:" , correlation)
# 相関係数: 0.6268027245323116

# プロット
plt.scatter(merged_data['math'], merged_data['english'], c='blue', label='math')
plt.scatter(merged_data['math'], merged_data['english'], c='red', label='english')

# グラフのタイトルと軸ラベルの設定

plt.title('English-Math')
plt.xlabel('math')
plt.ylabel('english')

# グラフの表示
plt.show()