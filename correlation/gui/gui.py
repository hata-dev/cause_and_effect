import sys
# pip install PyQt5
# バージョン確認
# python -c "import PyQt5.QtCore; print(PyQt5.QtCore.PYQT_VERSION_STR)"
from PyQt5.QtWidgets import QApplication, QLabel,QFileDialog,QWidget, QPushButton,QLineEdit,QMessageBox,QVBoxLayout
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#pip install matplotlib
from datetime import datetime, timedelta

def correlation_calc(input_data1,input_data2):
# def correlation_calc():
    # データの読み込み
    data1 = pd.read_csv(input_data1)
    data3 = pd.read_csv(input_data2)

    # data1 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\test_csv\\data.csv')
    # data3 = pd.read_csv('C:\\Users\\endst\\.vscode\\repository\\cause_and_effect\\correlation\\test_csv\\data3.csv')

    # 最新の30日分のデータを抽出
    latest_data1 = data1.tail(365)
    # latest_data2 = data2.tail(56)
    latest_data3 = data3.tail(365)
    
    # 日付をキーにしてデータをマージ
    # data1がDataFrame型なので1つ目の要素である年月日を「.columns」で取得
    merged_data = pd.merge(latest_data1, latest_data3, on=data1.columns[0])
    # merged_data = pd.merge(latest_data1, latest_data2, on='年月日')
    # merged_data = pd.merge(latest_data1, latest_data3, on='年月日')

    print(merged_data)
    column_names2 = merged_data.columns

    # 降水量列の相関係数を計算
    # correlation = np.corrcoef(merged_data['東京降水量'], merged_data['博多降水量'])[0, 1]
    # correlation = np.corrcoef(merged_data['東京降水量'], merged_data['埼玉降水量'])[0, 1]
    correlation = np.corrcoef(merged_data[merged_data.columns[1]], merged_data[merged_data.columns[2]])[0, 1]

    # 結果の表示
    print("相関係数:", correlation)

    # 散布図の作成
    # plt.scatter(merged_data['東京降水量'], merged_data['埼玉降水量'])
    plt.scatter(merged_data[merged_data.columns[1]],merged_data[merged_data.columns[2]])

    # グラフのタイトルと軸ラベルの設定
    # 'pandas.core.series.Series' を文字列に変換
    plt.title('Scatter Plot')
    # plt.xlabel('tokyo')
    # # plt.ylabel('hakata')
    # plt.ylabel('saitama')
    str_series1 = str(merged_data.columns[1])
    str_series2 = str(merged_data.columns[2])

    print(type(str_series1))
    print(str_series1)
    print(str_series2)

    plt.xlabel(str_series1)
    plt.ylabel(str_series2)

    # グラフの表示
    plt.show()


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # ボタンの作成
        self.button = QPushButton('ファイルを選択', self)
        self.button.clicked.connect(self.buttonClicked)

        # レイアウトの作成とウィジェットへの追加
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        # layout.addWidget(line_edit)

        self.setLayout(layout)

        self.setWindowTitle('ボタンと入力フォーム')
        self.show()

    def buttonClicked(self):
        data1, data2 = self.openFile()
        correlation_calc(data1,data2)
    
    def openFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name1 , _ = QFileDialog.getOpenFileName(self, "ファイルを選択", "", "All Files (*);;Text Files (*.txt)", options=options)
        file_name2 , _ = QFileDialog.getOpenFileName(self, "ファイルを選択", "", "All Files (*);;Text Files (*.txt)", options=options)
        return file_name1,file_name2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
