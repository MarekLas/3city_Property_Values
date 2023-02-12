![GitHub last commit](https://img.shields.io/github/last-commit/MarekLas/3city_Property_Values)

<img align="center" width ="30%" src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/work_in_progress.webp" />

<img align="center" width ="100%" src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/smart-city.gif" />

# 3City - Property values

## Context

### Sales transactions of premises in 2021-2022 in the cities of Gdańsk, Sopot and Gdynia. Price for 1 square meter is our label data.


'Gdynia is a relatively young city transformed from a village to an important industrial and maritime city between 1920 and 1930, with a population today of approximately 250 thousand. Numerous businesses are based here, in particular those which deal with international trade, shipping and fishing.

Places of interest are plentiful in Gdynia. Three of them are located around Kościuszko Square: the Oceanographic Museum, the Marine Aquarium and the Naval Museum. Marine enthusiasts can visit the ship museums moored in the southern dockyard to see the ORP Błyskawica ("Lightning") destroyer and the Dar Pomorza sailing ship. Those who prefer relaxing promenades will appreciate the seashore boulevards lined with cafés and taverns where shanties play and sailors recount tales to anyone willing to listen.
It is worth looking at the repertoire of the Music Theatre and the Drama Theatre in Gdynia. They are known for holding premieres by authors and artists from all parts of the world. Every summer the city becomes a venue for acclaimed international jazz musicians who participate in the Gdynia Summer Jazz Festival.

Some important sporting events are organised here regularly, conditions are very good for practicing water sports in the region; Gdynia Sailing Days or The Cutty Sark Tall Ships Race - a spectacular parade of tall ships from distant seas and countries. These events are always accompanied by artistic presentations and performances in which every one in the city is involved, especially during the partying and revelry.

Sopot, called the summer capital of Poland, is a busy place especially in the holiday season and welcomes tourists from around the world. The city centre is located along Bohaterów Monte Cassino Street, on the shore, along a beautiful promenade, closed to traffic, with plenty of restaurants and clubs. Straying a little from this promenade into one of the small streets of the town is all it takes to discover a different face of Sopot.

The famous Sopot pier juts out of Bohaterów Monte Cassino Street and is the longest wooden construction of this kind in Europe. From it there is a wonderful view of the Gulf of Gdańsk and a marvellous panorama of the city. Near the pier, there is a lighthouse open to the public. Plays and performances by the Atelier Theatre located nearby are an interesting option for summer evenings.

The city offers accommodation in hotels and private guest houses, some or which are in historical villas just by the sea.

With over 1000 years of history and tradition Gdańsk offers visitors many interesting monuments located mostly along Długa Street and its direct surroundings. 16th and 17th century renovated residences line the street on an itinerary leading to the Old Town. Each building has its unique form and character mirroring that of its original owner.
The Gothic Main Town Hall houses the historical museum of the city. The Neptune Fountain, the symbol of the city, stands in Długa Street. The High Gate (Brama Wyżynna), together with the Executioner's House and the Prison Tower (Katownia), the Golden Gate (Złota Brama) and The Amber Museum should be visited. On the quayside of the Mołtawa River stands the Crane, the biggest Medieval port crane in Europe. The Old Town is rich in ecclesiastical monuments, among which, the largest brick built church in Europe, the St. Mary Basilica (Kościół Mariacki), deserves special attention.

Gdańsk is not only the history of the past millennium. Modern Gdańsk is also the home of Lech Wałęsa, one of the founders of "Solidarność", Nobel Peace laureate and former President of Poland. Many places in Gdańsk are closely linked to the "Solidarność" movement. One of them, The Pomnik Poległych Stoczniowców, also known as the Monument of Three Crosses, was erected to commemorate those who gave their lives in the streets of Gdańsk in the fight for democracy.'

 ###### source: https://www.poland.travel/en/news/welcome-to-the-tricity

## Data Dictionary

* Data transakcji/Date - day, month and year of the transaction.

* Miasto/City - one of the three cities: Gdańsk, Sopot and Gdynia.

* Obręb/Precinct - part of the city where the premises is located.

* Zbyte prawo/Sold right - the legal status of the premises.

* Pu lokalu [m2]/Usable area - area of the property.

* Pow. przynależna [m2]/Assigned area - area of the belonging room.

* Pom. przynależne/Belonging room - the room outside the premises that belongs to it.

* Cena 1m2 bez VAT [zł]/Price 1m2 - the label column. Price for the one squared meter without VAT.

* Zakt.cena bez VAT [zł]/Updated price - secondary data. The product of the area of the premises and the price for the 1 squared meter.

* Program użytkowy/Rooms - number and types of rooms.

* Kondygnacja/Storey - floor number.

* Sprzedał/Seller - information who sold the property.

* Kupił/Buyer - information who bought the property.

## <b>Link to the script</b>

### <b></b>

## Modules used in the script

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/01_pv_modules_v3.png" align="center" width ="65%"/> 

## Data sample

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/02_pv_data.JPG" align="center" width ="100%"/> 

## Change the columns names
After the first review of the data, I decided to change the columns names to English.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/06_pv_data_rename.JPG" align="center" width ="100%"/>

## Data information
There is a lot of text data and some missing values.There is also 7.5 MB memory usage :/.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/03_pv_info_v2.JPG" align="center" width ="35%"/>

## Data describe
We can see that the are some disturbing values.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/04_pv_describe_v2.JPG" align="center" width ="50%"/>

## Duplicated rows
Thera are 40 duplicated rows that I have to delete.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/04a_pv_duplicated.JPG" align="center" width ="30%"/>

## Missing values
There are missing values in two columns, but only in 3 rows. i decidet to drop this rows.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/05_pv_isnull_v2.JPG" align="center" width ="100%"/>

## Price for 1 squared meter
This is the label column. Let's see what the data looks like after removing some outliers.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/07_pv_price_for_1m2_hist.jpg" align="center" width ="50%"/>

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/08_pv_price_for_1m2_boxplot.jpg" align="center" width ="35%"/>

## Date
I decided to divide Date column to the columns: Year, Month and Day.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/09_date_to_year_month_day_v2.JPG" align="center" width ="100%"/>

## City
The study area covers three cities: Gdańsk, Gdynia, Sopot. We can see that most of the transactions was made in Gdańsk.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/10_pv_cities_v2.jpg" align="center" width ="80%"/>

## Precinct
There are 80 precints in the data. I decided to group them into larger urban areas and change the column name to 'Urban area'.
The new areas:
* Gdańsk Oliwa
* Gdańsk Port
* Gdańsk Południe
* Gdańsk Przymorze
* Gdańsk Wrzeszcz
* Gdańsk Zachód
* Gdynia Centrum
* Gdynia Port
* Gdynia Północ
* Gdynia Przymorze
* Gdynia Zachód
* Sopot

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/11_pv_urban_areas_v2.jpg" align="center" width ="60%"/>

## Sold right
Type of rights assigned to the property. There are only two rows without sold right value, so I decided to drop them.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/12_pv_sold_right_v2.jpg" align="center" width ="80%"/>

## Usable area
There was some outliers in the data so I decided to use 'remove_outlier' function to delete them.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/13_pv_usable_area_hist.jpg" align="center" width ="50%"/>

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/14a_pv_usable_area_boxplot.jpg" align="center" width ="35%"/>

## Assign area
Area of the room belonging to the premises. I decided to remove some outliers and assign areas with value 1 (obious mistake) to value 0.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/14_pv_assign_area_hist_v2.jpg" align="center" width ="60%"/>

## Belonging room
After final data cleaning, 12 categories remained from 30.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/16_pv_belonging_room_countplot_v2.jpg" align="center" width ="70%"/>

## Updated prices
It was created by multiplying price for 1 square meter and usable area. I decided to use it for some data cleaning, but it was no sens to use it in predictions.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/17a_pv_updted_prices_hist.jpg" align="center" width ="60%"/>

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/17b_pv_updted_prices_boxplot.jpg" align="center" width ="35%"/>

## Rooms
Number of rooms in the property. Problematic and dirty column. Number of rooms placed in sentences. Lots of wrong data. I sumed up the numbers of rooms to evaluate the quality of the data. The quality turned out to be rather poor.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/17_pv_numbers_of_rooms_countplot_v2.jpg" align="center" width ="70%"/>

## Storey
Floor on which the premises is located. I decided to divide them to the three main categories: very_good, good, bad.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/19_pv_storey_countplot_v2.jpg" align="center" width ="60%"/>

## Seller
There are 12 different categories of sellers. Most of the sellers were indyvidual persons.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/20_pv_sellers_countplot_v2.jpg" align="center" width ="70%"/>

## Buyer
There are 8 different categories of buyers. Most of the buyers were also indyvidual persons.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/21_pv_buyers_countplot_v2.jpg" align="center" width ="70%"/>

## Final dataframe
For the first analysis I decided to use almost every column from the data, except the obious ones: 'Updated_price', 'Rooms', 'Storey', 'Rooms_sum'. There were 10168 observations at the begining with a memory usage 7.5 MB. Now we have 9156 entries and 565.6 KB memory usage.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/21a_pv_final_data_v2.jpg" align="center" width ="100%"/>

## Correlation matrix

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/22_pv_correlation_matrix_v2.jpg" align="center" width ="50%"/>

## Models

### Linear Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/26_pv_linear_regression_v3.jpg" align="center" width ="40%"/>

### Lasso Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/27_pv_lasso_regression_v3.jpg" align="center" width ="40%"/>

### Adaboost Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/28_pv_adaboost_regressor_v3.jpg" align="center" width ="40%"/>

### Ridge Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/29_pv_ridge_regressor_v3.jpg" align="center" width ="40%"/>

### Random Forest Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/28b_pv_random_forest_v4.jpg" align="center" width ="40%"/>

### KNeighbors Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/30_pv_kneighbors_v3.jpg" align="center" width ="40%"/>

### SVR Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/31_pv_svr_v3.jpg" align="center" width ="40%"/>

### ElasticNet Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/31a_pv_elasticnet_v1.jpg" align="center" width ="40%"/>

### Decision Tree Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/31b_pv_decision_tree_v1.jpg" align="center" width ="40%"/>

### Ranking table

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/32_pv_scores_mae_ranking_table.JP" width ="40%"/>

### Barplot charts

* Coefficient of determination - R2-score

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/33_pv_r2_barplot.jp" width ="40%"/>

* Mean Absolute Error - MAE

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/34_pv_mae_barplot.jp" width ="40%"/>

## Summary

<img align="center" width ="30%" src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/work_in_progress.webp" />


![GitHub last commit](https://img.shields.io/github/last-commit/MarekLas/3city_Property_Values)









