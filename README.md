# Visualization of the number of Covid19 infected people by Python

## PythonによるCovid19 / 新型コロナ感染者数関連データの分析および可視化の試み

データ出典：「新型コロナ関連の情報提供:NHK等」

本コンテンツでは、一般に入手可能なCovid-19関連のオープンデータを、筆者の興味・関心を満たすためにPythonのデータサイエンスの知識を使って分析・可視化を試みたものである。試行錯誤しながら学習を進めているため、内容については正確でなかったり、間違いも含まれる可能性がある。参考にするのは読者の自由であるが、その点については、理解されたい。またデータの出典は、本コンテンツで明記している通りである。データを自由に利用させていただけることに感謝したい。

### 0. 主な利用データ

タイトル|Link|説明
-----|--------|--------|
NHK 特設サイト 新型コロナ データ一覧 |<a href="https://www3.nhk.or.jp/news/special/coronavirus/data-widget/">https://www3.nhk.or.jp/news/special/coronavirus/data-widget/</a>| NHKによるまとめ　新型コロナウイルス関連データ・ダウンロードサービス|

### 01. 日本国内の感染状況

#### 01. 1日ごとの感染者数・死者数
No.|タイトル|nbviewer|Open in Colab
-----|--------|--------|-------------
01-01|都道府県別の1日ごとの感染者数・死者数|[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/01_Number_of_infected_persons_per_day_by_pref.ipynb)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/01_Number_of_infected_persons_per_day_by_pref.ipynb)

![Number of infected persons per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20210622/01_Number_of_infected_persons_per_day_by_pref_20210622.png?raw=true "Number of infected persons per day by prefecture")

![Number of deaths per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20210622/02_Number_of_deaths_per_day_by_pref_20210622.png?raw=true "Number of deaths per day by prefecture")

上記グラフで注意が必要なのは、ひとつ突出している例外的なデータの存在である。調べてみると、2021年5月18日の兵庫県のデータであり、詳細は下記ニュースを参考にするとよい。

https://www3.nhk.or.jp/news/html/20210518/k10013037951000.html

```
兵庫県は18日、新型コロナウイルスに感染していた129人の死亡が確認されたと発表しました。

このうち121人は、神戸市がことし3月26日から5月17日までの1か月半余りの期間に亡くなり、これまで計上していなかった人を、18日、まとめて発表したものです。

以上、NHKニュースより引用
```

とのことなので、この兵庫県のデータについては実態を反映していないと思われるが、ひとまずデータ通りに出力している。1日の死者数としては適切でないため、外れ値としての処理が必要であろう。

![Cumulative number of infected persons per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20210622/03_Cumulative_number_of_infected_persons_per_day_by_pref_20210622.png?raw=true "Cumulative number of infected persons per day by prefecture")

![Cumulative number of deaths per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20210622/04_Cumulative_number_of_deaths_per_day_by_pref_20210622.png?raw=true "Cumulative number of deaths per day by prefecture")