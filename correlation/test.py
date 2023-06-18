import pandas as pd

# データの読み込み
data1 = pd.read_csv('データ1.csv')
data2 = pd.read_csv('データ2.csv')

# 相関係数の計算
correlation = data1.corrwith(data2)

# 結果の表示
print("相関係数:", correlation)