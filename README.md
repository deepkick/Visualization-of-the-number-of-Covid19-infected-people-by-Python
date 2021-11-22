# Visualization of the number of Covid19 infected people by Python

## PythonによるCovid19 / 新型コロナ感染者数関連データの分析および可視化の試み

データ出典：「新型コロナ関連の情報提供:NHK等」  
Data source: "Information on the new Corona: NHK, etc.

本コンテンツでは、一般に入手可能なCovid-19関連のオープンデータを、筆者の興味・関心を満たすためにPythonのデータサイエンスの知識を使って分析・可視化を試みたものである。試行錯誤しながら学習を進めているため、内容については正確でなかったり、独自の解釈であったり、少なからぬ間違いも含まれる可能性がある。参考にするのは読者の自由であり、またMIT Licenceとして本コンテンツ上のソースコードは公開しているため、自由に利用していただいても問題ないが（元データの利用については含まない）、その点については、理解されたい。またデータの出典は、本コンテンツで明記している通りである。データ提供者・関連諸機関に対し、自由に利用させていただけることに深く感謝したい。

This content is an attempt to analyze and visualize publicly available open data related to Covid-19, using Python data science knowledge to satisfy the author's interests. The content may contain inaccuracies, misinterpretations, and errors, as the author is learning by trial and error. It is up to the reader to refer to it, and as the source code on this content is open to the public as an MIT Licence, there is no problem in using it freely (not including the use of the original data), but please be aware of those points. The source of the data is as specified in this content. I would like to express my sincere gratitude to the data providers and related organisations for allowing me to use the data freely.

### 0. 主な利用データ / Main use data

タイトル / Title |Link|説明 / description
-----|--------|--------|
NHK 特設サイト 新型コロナ データ一覧 / NHK special site: New Corona data list |<a href="https://www3.nhk.or.jp/news/special/coronavirus/data-widget/">https://www3.nhk.or.jp/news/special/coronavirus/data-widget/</a>| NHKによるまとめ　新型コロナウイルス関連データ・ダウンロードサービス|
東京都福祉保健局 新型コロナウイルス感染症検査陽性者の状況 / Bureau of Social Welfare and Public Health, Tokyo Metropolitan Government Status of new coronavirus infection test positive patients |<a href="https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000089/resource/54996023-7255-45c5-b5b0-60458d874715">https://catalog.data.metro.tokyo.lg.jp/dataset/</a>| 東京都 新型コロナウイルス感染症検査陽性者の状況|

### 01. 日本国内の感染状況 / Infection status in Japan

#### 01. 1日ごとの感染者数・死者数 / Number of infected people and deaths per day
No.|タイトル / Title|nbviewer|Open in Colab
-----|--------|--------|-------------
01-01|都道府県別の1日ごとの感染者数・死者数 / Number of infections and deaths per day by prefecture|[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/01_Number_of_infected_persons_per_day_by_pref.ipynb)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/01_Number_of_infected_persons_per_day_by_pref.ipynb)

![Number of infected persons per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20211121/01_Number_of_infected_persons_per_day_by_pref_20211121.png?raw=true "Number of infected persons per day by prefecture")

![Number of deaths per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20211121/02_Number_of_deaths_per_day_by_pref_new_20211121.png?raw=true "Number of deaths per day by prefecture")

![Cumulative number of infected persons per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20211121/03_Cumulative_number_of_infected_persons_per_day_by_pref_20211121.png?raw=true "Cumulative number of infected persons per day by prefecture")

![Cumulative number of deaths per day by prefecture](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/20211121/04_Cumulative_number_of_deaths_per_day_by_pref_20211121.png?raw=true "Cumulative number of deaths per day by prefecture")

#### 02. 東京都の自宅療養者数・入院者数・その他人数の比較
No.|タイトル|nbviewer|Open in Colab
-----|--------|--------|-------------
01-02|東京都の自宅療養者数・入院者数・その他人数 / Number of people treated at home, hospitalised and others in Tokyo|[![nbviewer](https://camo.githubusercontent.com/bfeb5472ee3df9b7c63ea3b260dc0c679be90b97/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72656e6465722d6e627669657765722d6f72616e67652e7376673f636f6c6f72423d66333736323626636f6c6f72413d346434643464)](https://nbviewer.jupyter.org/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/02_Tokyo_Number_of_People_Convalescing_Home.ipynb)|[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/02_Tokyo_Number_of_People_Convalescing_Home.ipynb)

![Number of people receiving home treatment in Tokyo, 20211121](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/tokyo_dataset/20211121/01_Number_of_people_receiving_home_treatment_in_Tokyo_20211121.png?raw=true "Number of people receiving home treatment in Tokyo, 20211121")

![Number of Positives in Tokyo, 20211121](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/tokyo_dataset/20211121/02_Number_of_positives_in_Tokyo_20211121.png?raw=true "Number of Positives in Tokyo, 20211121")

![Number of people hospitalized in Tokyo, 20211121](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/tokyo_dataset/20211121/03_Number_of_people_hospitalized_in_Tokyo_20211121.png?raw=true "Number of people hospitalized in Tokyo, 20211121")

![Status of infected persons in Tokyo, 20211121](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/tokyo_dataset/20211121/04_Status_of_infected_persons_in_Tokyo_20211121.png?raw=true "Status of infected persons in Tokyo, 20211121")

![Status of infected persons in Tokyo, 20211121](https://github.com/deepkick/Visualization-of-the-number-of-Covid19-infected-people-by-Python/blob/main/tokyo_dataset/20211121/05_Status_of_infected_persons_in_Tokyo_20211121.png?raw=true "Status of infected persons in Tokyo, 20211121")