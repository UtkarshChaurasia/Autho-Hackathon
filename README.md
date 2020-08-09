# COVID-19: A Boon for Nature


## Introduction
Air Pollution causes more than seven million deaths per year. In 2018, USA linked to nearly 10,000 additional deaths. More than 3/4 of annual greenhouse gases gets produced by transportation, industry, and power generation resulting in forcing the 90% of the global population to breath in unsafe air.</br>

The novel COVID-19 virus has left the world reeling with thousands of deaths and lakhs of cases. The entire human life has come to a standstill with the majority of the countries enforcing shutdown/lockdown and travel bans.</br>

Amidst this chaos, there is an unlikely beneficiary in the form of mother nature. There is a drastic reduction in air pollution
all over the world which has been a major concern over the years.

![NO2 concentration over India](images/NO2_con_over_India.jpg)

## About
This positive outcome has inspired me to research more on the datasets available and predict the impact of improved air quality on the overall ecosystem, such as by how far the melting of polar ice will be pushed which was originally predicted at 2100. The positive aspect of this pandemic could be an eye opener to reanalyze the parameters which play a vital role in a healthier environment. This might encourage people to keep the air immaculate once this lockdown is over.

## System Design And Implementation

Given data was split into the period before shelter in placestarted and after it. The data after shelter in place was setaside for comparison with the predicted data. Data from 2014 to shelter in place was used to train the time series model,which resulted in prediction of the content of pollutants if shelter in place would not have happened.

Three models naming Auto-Regression, Moving Average,Seasonal Autoregressive Integrated Moving Average were used for time series prediction. Results from these models was tested by keeping aside known testing values from January to the date of Lock-down and then later comparing this to the predicted value by the
model.

Eventually, Moving Average model came to perform best with repeat to others. RMSE value was used to check the
accuracy. Finally, Moving Average algorithm was used to predict unknown values for all other cities using complete
known dataset. Figure 7 shows the final predicted graph for the PM2.5 content with Shelter in place and without it for predicted valus of 2020.

## Tech Stack And System Design

# Algorithms

Statsmodel library of python was used to perform time series prediction. Statsmodel have numerous models, 3 of which we used are described below.

1) Auto-regression: An auto-regressive (AR) model predicts future behavior based on past behavior. The process is basically a linear regression of the data in the current series against one or more past values in the same series.
AR model usually gets “close enough” for it to be useful in most scenarios.

2) Moving Average: A moving average is a technique to get an overall idea of the trends in a data set; it is an average of any subset of numbers.

3) Seasonal Autoregressive Integrated Moving Average: Seasonal Autoregressive Integrated Moving Average,SARIMA or Seasonal ARIMA, is an extension of ARIMA that explicitly supports univariate time series data with a seasonal component. It adds three new hyperparameters to specify the autoregression (AR), differencing (I) and moving
average (MA) for the seasonal component of the series as well as an additional parameter for the period of the seasonality.

# Technologies Used

1) Programming: Python was used for programming. Python provides support to libraries like statsmodel which
make data analysis easy. Statsmodel have various time-series models to choose from.

2) Visualization: Seaborn and Matplotlib was used for visualising different graphs. Seaborn is a Python data visu-
alization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

# Architecture

![Architecture of time series prediction](images/architecture.png)
