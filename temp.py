import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


#compounded percentage product of returns
def compoundperc(dataset):
    returns = dataset.pct_change()
    x = (((returns+1).prod()-1)*100).round(2)
    print('The compounded percentage is: ')
    return x

def annual_volatility(dataset):
    returns = dataset.pct_change()
    returns = returns.dropna()
    deviations = returns - returns.mean()
    squared_deviations = deviations**2
    number_of_obs = returns.shape[0]
    mean_squared_deviations = squared_deviations.sum()/(number_of_obs-1)
    volatility = mean_squared_deviations**0.5
    annualized_vol = volatility*(12**0.5)
    print('Annual Volatility is : ')
    return annualized_vol


def month_annualize(month_risk):
    x = (1+month_risk)**12 - 1
    print('The annualized return given the monthly risk is:')
    return x


def returns_month(dataset):
    returns = dataset/100
    n_months = returns.shape[0]
    return_per_month = (returns+1).prod()**(1/n_months) - 1
    print("The returns per month is :")
    return return_per_month

def annualized_ret(dataset):
    returns = dataset/100
    n_months = returns.shape[0]
    #return_per_month = (returns+1).prod()**(1/n_months) - 1
    annualized_return = (returns+1).prod()**(12/n_months) - 1
    print('Annual Return is : ')
    return annualized_return

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


def get_date(dataset):
    dataset.index = pd.to_datetime(dataset.index, format="%Y%m")
    dataset.index = dataset.index.to_period('M')
    return dataset

def drawdowns(dataset : pd.Series):
    '''
    Drawdown:
    Takes a time series of asset returns
    Computes & returns a Dataframs that contains:
    Wealth index
    Previous Peaks
    '''
    #date(dataset)
    returns = dataset
    wealth_index = 1000*(1+returns).cumprod()
    #returnwealth_index.head())
    #returnwealth_index.plot.line())
    previous_peaks = wealth_index.cummax()
    #returnprevious_peaks.head())
    #returnprevious_peaks.plot.line())
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    print("The Annual Drawdown : ")
    return pd.DataFrame({
        "wealth" : wealth_index.head(),
        "Peaks" : previous_peaks.head(),
        "Drawdown Value" : drawdowns.head()
    })
    #return drawdowns.plot.line()
def drawdown(dataset: pd.Series):
    """Takes a time series of asset returns.
       returns a DataFrame with columns for
       the wealth index,
       the previous peaks, and
       the percentage drawdown
    """

    wealth_index = 1000*(1+dataset).cumprod()
    previous_peaks = wealth_index.cummax()
    drawdowns = (wealth_index - previous_peaks)/previous_peaks
    return pd.DataFrame({"Wealth": wealth_index,
                         "Previous Peak": previous_peaks,
                         "Drawdown": drawdowns})


def skewness(r):
    demeaned_r = r - r.mean()
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**3).mean()
    return exp/sigma_r**3


def kurtosis(r):
    demeaned_r = r - r.mean()
    sigma_r = r.std(ddof=0)
    exp = (demeaned_r**4).mean()
    return exp/sigma_r**4


def var_historic(dataset, level=5):
    """
    Returns the historic Value at Risk at a specified level
    i.e. returns the number such that "level" percent of the returns
    fall below that number, and the (100-level) percent are above
    """
    if isinstance(dataset, pd.DataFrame):
        return dataset.aggregate(var_historic, level = level)
    elif isinstance(dataset, pd.Series):
        return -np.percentile(dataset, level)
    else:
        raise TypeError("Expected dataset to be a DataFrame or a Series")


def cvar_historic(r, level=5):
    """
    Computes the Conditional VaR of Series or DataFrame
    """
    if isinstance(r, pd.Series):
        is_beyond = r <= var_historic(r, level=level)
        return -r[is_beyond].mean()
    elif isinstance(r, pd.DataFrame):
        return r.aggregate(cvar_historic, level=level)
    else:
        raise TypeError("Expected r to be a Series or DataFrame")



def var_gaussian(r, level=5, modified=False):
    """
    Returns the Parametric Gauusian VaR of a Series or DataFrame
    """
    # compute the Z score assuming it was Gaussian
    z = norm.ppf(level/100)
    return -(r.mean() + z*r.std(ddof=0))



def var_fisher(r, level=5, modified=True):
    """
    Since "modified" is True, then the modified VaR is returned
    using the Cornish-Fisher modification
    """
    # compute the Z score assuming it was Gaussian
    z = norm.ppf(level/100)

        # modify the Z score based on observed skewness and kurtosis
    s = skewness(r)
    k = kurtosis(r)
    z = (z +
            (z**2 - 1)*s/6 +
            (z**3 -3*z)*(k-3)/24 -
            (2*z**3 - 5*z)*(s**2)/36
        )
    return -(r.mean() + z*r.std(ddof=0))


def plotvar(r):
    '''
    Plots the comparison bar graph between the 3 VaR methods
    '''
    var_table = [var_gaussian(r),
                 var_fisher(r),
                 var_historic(r)]
    comparison = pd.concat(var_table, axis=1)
    comparison.columns=['Gaussian', 'Cornish-Fisher', 'Historic']
    comparison.plot.bar(title="Hedge Fund Indices: VaR at 5%")
