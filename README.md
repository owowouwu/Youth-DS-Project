# COMP20008 Assignment 2 - Data Science Project

## Authors
Steven Nguyen (1081716), Lina Zhu, Sen Turner 

## Overview

blah - talk about research proposal

## Package Dependencies

`pandas`, `numpy`, `python-docx`, `geopandas` (and dependencies), `matplotlib`, `sklearn`

## Explanation of Raw Data and Wrangled Data Files

Data in `./raw_data` consists purely of data that was pulled from the sources listed below, whereas data files in `./wrangled` consists of files that were produced manually or from scripts. Some files are named `X_raw.xlsx`. These were files that were created manually by copying tables in Excel, and are processed further in the scripts - those without `_raw` are the final form which the data analysis scripts we run use.

### Data Sources
* AEDC - Australian Early Development Census
* VPHS - Victorian Public Health Survey (from 2011-12)

#### Victorian Department of Education and Training Data

* VCAMS - Victorian Child and Adolescent Monitoring System
* TSDR - Teacher Supply and Demand Report

#### VCAMS Indicators Used

##### LGA

* `behavourial` - Proportion of children whose parents report behavourial difficulties at school entry.
* `bullying` - Proportion of young people who report being bullied 
* `childabuse` - Child abuse substantiations per 1000.
* `connectedness` - Proportion of young people who feel connected with their school.
* `familystress` - Proportion of young people whose family report a high level of stress.
* `outofhome` - Number of children out of home per LGA.
* `youngUnemployed` - Unemployment rate in the first 6 months for school leavers.
* `year12completion` - Rate of year 12 completion in an area.

##### DHS AREA


