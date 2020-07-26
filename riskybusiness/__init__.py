import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pct change of returns
def returns(dataset):
   returns = dataset.pct_change()
   returns = returns*100
   returns = returns.dropna()
   print(returns)

#compounded percentage product of returns
def product(dataset):
    returns = dataset.pct_change()
    x = (((returns+1).prod()-1)*100).round(2)
    print('compounded percentage product of returns is :')
    print(x)

def month_annualize(month_risk):
    x = (1+month_risk)**12 - 1
    print('The annualized return given the monthly returns is:')
    print(x)


def annual_volatility(dataset):
    returns = dataset.pct_change()
    returns = returns.dropna()
    deviations = returns - returns.mean()
    squared_deviations = deviations**2
    number_of_obs = returns.shape[0]
    mean_squared_deviations = squared_deviations.sum()/(number_of_obs-1)
    volatility = mean_squared_deviations**0.5
    annualized_vol = volatility*(12**0.5)
    print('volatility is : ' , volatility)
    print('Annual Volatility is : ', annualized_vol)

def returns_month(dataset):
    returns = dataset/100
    n_months = returns.shape[0]
    return_per_month = (returns+1).prod()**(1/n_months) - 1
    print('The Return Per Month is : ' , return_per_month)

def annualized_ret(dataset):
    returns = dataset/100
    n_months = returns.shape[0]
    #return_per_month = (returns+1).prod()**(1/n_months) - 1
    annualized_return = (returns+1).prod()**(12/n_months) - 1
    print('Ann Ret is : ' , annualized_return)

#def sharpe(dataset = 'dataset' , riskfree_rate = 'riskfree_rate'):
def sharpe(dataset,riskfree_rate):
    returns = dataset/100
    n_months = returns.shape[0]
    return_per_month = (returns+1).prod()**(1/n_months) - 1
    annualized_return = (returns+1).prod()**(12/n_months) - 1
    annualized_vol = returns.std()*(12**0.5)
    excess_return = annualized_return - riskfree_rate
    sharpe_ratio = excess_return/annualized_vol
    print('The Monthly Returns is : ', return_per_month)
    print('The Annual Returns is : ', annualized_return)
    print('The Sharpe Ratio is : ', sharpe_ratio)


'''
Drawdown:
Takes a time series of asset returns
Computes & returns a Dataframs that contains:
Wealth index
Previous Peaks
'''

def date(dataset):
    dataset.index = pd.to_datetime(dataset.index, format="%Y%m")
    dataset.index = dataset.index.to_period('M')
    return dataset

def drawdown(dataset : pd.Series):
    date(dataset)
    returns = dataset
    wealth_index = 1000*(1+returns).cumprod()
    #print(wealth_index.head())
    #print(wealth_index.plot.line())
    previous_peaks = wealth_index.cummax()
    #print(previous_peaks.head())
    #print(previous_peaks.plot.line())
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    print("The Annual Drawdown : ")
    print( pd.DataFrame({
        "wealth" : wealth_index.head(),
        "Peaks" : previous_peaks.head(),
        "Drawdown Value" : drawdowns.head()
    }))
    #return drawdowns.plot.line()
