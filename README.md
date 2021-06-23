# Visualization of the number of Covid19 infected people by Python

## PythonによるCovid19 / 新型コロナ感染者数関連データの分析および可視化の試み

データ出典：「新型コロナ関連の情報提供:NHK等」

本コンテンツでは、一般に入手可能なCovid-19関連のオープンデータを、筆者の興味・関心を満たすためにPythonのデータサイエンスの知識を使って分析・可視化を試みたものである。試行錯誤しながら学習を進めているため、内容については正確でなかったり、間違いも含まれる可能性がある。参考にするのは読者の自由であるが、その点については、理解されたい。またデータの出典は、本コンテンツで明記している通りである。データを自由に利用させていただけることに感謝したい。

### 0. 主な利用データ

タイトル|Link|説明
-----|--------|--------|
NHK 特設サイト 新型コロナ データ一覧 |<a href="https://www3.nhk.or.jp/news/special/coronavirus/data-widget/">https://www3.nhk.or.jp/news/special/coronavirus/data-widget/</a>| NHKによるまとめ　新型コロナウイルス関連データ・ダウンロードサービス|

### 1. 日本国内の感染状況

### 01. 1日ごとの感染者数・死者数
No.|タイトル|nbviewer|Open in Colab
-----|--------|--------|-------------
01-01|1日ごとの感染者数・死者数|[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/01_Number_of_infected_persons_per_day_by_pref.ipynb)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/01_Number_of_infected_persons_per_day_by_pref.ipynb)