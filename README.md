# Visualization of the number of Covid19 infected people by Python
 
PythonによるCovid19 / 新型コロナ感染者数関連データの分析および可視化の試み

「新型コロナ関連の情報提供:NHK等」

本コンテンツでは、一般に入手可能なCovid-19関連のオープンデータを、筆者の興味・関心を満たすためにPythonのデータサイエンスの知識を使って分析・可視化を試みたものである。試行錯誤しながら学習を進めているため、内容については正確でなかったり、間違いも含まれる可能性がある。参考にするのは読者の自由であるが、その点については、理解されたい。またデータの出典は、本コンテンツで明記している通りである。データを自由に利用させていただけることに感謝したい。

### 0. 主な利用データ

タイトル|Link|説明
-----|--------|--------|
NHK 特設サイト 新型コロナ データ一覧 |<a href="https://www3.nhk.or.jp/news/special/coronavirus/data-widget/">https://www3.nhk.or.jp/news/special/coronavirus/data-widget/</a>| NHKによるまとめ　新型コロナウイルス関連データ・ダウンロードサービス|

### 1. 日本国内の感染状況：1日ごとの感染者数・死者数