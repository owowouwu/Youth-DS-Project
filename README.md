# COMP20008 Assignment 2 - Data Science Project

## Overview

The prevention and treatment of depression and mental health issues is increasing its significance in contemporary society. This raises this question: how do different childhood developmental factors impact an individual’s susceptibility to depression? By asking this question we aim to identify and isolate external childhood developmental factors that may impact on the health and wellbeing of our communities. Our focus on childhood and youth development also allows us to understand the liveability of Victorian communities, as we will potentially be able to identify areas that need improved living conditions for young people. 

In this project we use a variety of data to identify links between depression rate experiences during school.

## Dependencies

`pandas`, `numpy`, `python-docx`, `geopandas` (and dependencies), `matplotlib`, `sklearn`, `seaborn`

## Usage

* `step1.py` processes raw documents from `./raw_data` into readable csv formats and places them into `./wrangled`.
* `step2.py` processes VCAMs data (see below) and combines all processed documents into two CSVs, `LGA_data.csv` and `DHS_data.csv`.
* `visualisations.py` produces all visualisations.
* `minmaxscores.py` produces our liveability metric and its relevant plots.

## Data Sources

* AEDC - Australian Early Development Census. This gives a range of developmental indices for young children, with factors ranging from their development in language, emotions, physical ability, and more.
* VPHS - Victorian Public Health Survey.

#### Victorian Department of Education and Training Data

* VCAMS - Victorian Child and Adolescent Monitoring System. See below.
* TSDR - Teacher Supply and Demand Report. 

#### VCAMS Indicators Used

##### LGA

* `behavourial` - Proportion of children whose parents report behavourial difficulties at school entry.
* `bullying` - Proportion of young people who report being bullied .
* `childabuse` - Child abuse substantiations per 1000.
* `connectedness` - Proportion of young people who feel connected with their school.
* `familystress` - Proportion of young people whose family report a high level of stress.
* `outofhome` - Number of children out of home per LGA.
* `youngUnemployed` - Unemployment rate in the first 6 months for school leavers.
* `year12completion` - Rate of year 12 completion in an area.

##### DHS AREA

* `cyberbullying` - Proportion of young people experiencing cyberbullying.
* `electronicMedia` - Proportion of people who spend over 2 hours on electronic media a day.
* `financial` - Proportion of young people whose families are experiencing financial hardship.
* `food` - Proportion of young people who ran out of food at home.
* `healthyFamily` - Proportion of young people living in families with healthy functioning.
* `mental_health_access` - Proportion of young people with access to meantal health services.
* `trustedAdult` - Proportion of young people who report having a trusted adult in their lives.
* `support` - Proportion of children from families who are able to get support in a time of crisis/when needed.
* `safety` - Proportion of young people who feel safe.
* `psychological` - Proportion of young people who showed high levels of psychological stress.
* `qolSatisfaction` - Proportion of young people who feel satisfied with their quality of life.
* `physicalAcitivity` - Proportion of young people who do the recommended amount of physical activity every day

## Contributors
Steven Nguyen (1081716), Lina Zhu, Sen Turner 



