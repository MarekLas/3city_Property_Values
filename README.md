![GitHub last commit](https://img.shields.io/github/last-commit/MarekLas/3city_Property_Values)

<img align="center" width ="30%" src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/work_in_progress.webp" />

<img align="center" width ="100%" src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/smart-city.gif" />

# 3City - Property values

## Context

Sales transactions of premises in 2021-2022 in the cities of Gdańsk, Sopot and Gdynia. Price for 1 square meter is our label data.

## Data Dictionary

* Data transakcji/Date - day, month and year of the transaction.

* Miasto/City - one of the three cities: Gdańsk, Sopot and Gdynia.

* Obręb/Precinct - part of the city where the premises is located.

* Zbyte prawo/Sold right - the legal status of the premises.

* Pu lokalu [m2]/Usable area - area of the property.

* Pow. przynależna [m2]/Assigned area - area ofthe belonging room.

* Pom. przynależne/Belonging room - the room outside the premises that belongs to it.

* Cena 1m2 bez VAT [zł]/Price 1m2 - the labael column. Price for one squared meter without VAT.

* Zakt.cena bez VAT [zł]/Updated price - secondary data. The product of the area of the premises and the price fo 1 squared meter.

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
There is a lot of text data and some missing values.There is also 7.5 MB usage :/.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/03_pv_info_v2.JPG" align="center" width ="30%"/>

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
There are 80 percints in the data. I decided to group them into larger urban areas and change the column name to 'Urban area'.
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

## Belongin room
After final data cleaning, 12 categories remained from 30.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/16_pv_belonging_room_countplot.jp" align="center" width ="60%"/>

## Rooms
Number of rooms in the property. Problematic and dirty column. Number of rooms placed in sentences. Lots of wrong data. I sumed the numbers of room to evaluate the quality of the data. The quality was rather poor.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/17_pv_numbers_of_rooms_countplot.jp" align="center" width ="60%"/>

## Updated prices
It was created by multiplying price for 1 square meter and usable area. I decided to use for some data cleaning, but it was no sens to use it in predictions.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/17a_pv_updted_prices_hist.jpg" align="center" width ="60%"/>

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/17b_pv_updted_prices_boxplot.jpg" align="center" width ="35%"/>

## Storey
Floor on which the premises is located. I decided to divide the to three main categories: very_good, good, bad.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/18_pv_storey_cat.pn" align="center" width ="60%"/>

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/19_pv_storey_countplot.jp" align="center" width ="60%"/>

## Seller
There are 12 different categories of sellers. Most of the sellers were indyvidual persons.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/20_pv_sellers_countplot.jpg" align="center" width ="60%"/>

## Buyer
There are 8 differentcategories of buyers. Most of the sellers were also indyvidual persons.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/21_pv_buyers_countplot.jp" align="center" width ="60%"/>

## Final dataframe
For the begining I decided to use almost every column in the data. Except the obious ones: 'Updated_price', 'Rooms', 'Storey', 'Rooms_sum'.

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/21a_pv_final_data.jp" align="center" width ="50%"/>

## Correlation matrix

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/22_pv_correlation_matrix.jp" align="center" width ="60%"/>

## Dependiencies

### Cities

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/23_pv_pairplot_cities.jpg" align="center" width ="60%"/>

### Floor category

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/25_pv_pairplot_storey_cat.jpg" align="center" width ="60%"/>

## Models

### Linear Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/26_pv_linear_regression_v2.jpg" align="center" width ="40%"/>

### Lasso Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/27_pv_lasso_regression_v2.jpg" align="center" width ="40%"/>

### Adaboost Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/28_pv_adaboost_regressor_v2.jpg" align="center" width ="40%"/>

### Ridge Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/29_pv_ridge_regressor_v2.jpg" align="center" width ="40%"/>

### Random Forest Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/28b_pv_random_forest_v3.jpg" align="center" width ="40%"/>

### KNeighbors Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/30_pv_kneighbors_v2.jpg" align="center" width ="40%"/>

### SVR Regression

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/31_pv_svr_v2.jpg" align="center" width ="40%"/>

### Ranking table

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/32_pv_scores_mae_ranking_table.JPG" width ="40%"/>

### Barplot charts

* Coefficient of determination - R2-score

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/33_pv_r2_barplot.jpg" width ="40%"/>

* Mean Absolute Error - MAE

<img src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/34_pv_mae_barplot.jpg" width ="40%"/>

## Summary

<img align="center" width ="30%" src="https://github.com/MarekLas/3city_Property_Values/blob/main/readme_files/work_in_progress.webp" />


![GitHub last commit](https://img.shields.io/github/last-commit/MarekLas/3city_Property_Values)









