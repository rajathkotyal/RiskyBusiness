! DOCUMENTATION !

# Welcome!
In order to use the RiskyBusiness library make sure you have installed it using :
```bash
pip install riskybusiness
```

To use the functions, Please import the library into your ipynb file using :
```python
import riskybusiness as rb
```

### Additional Libraries that need to be imported :
1) pandas
2) numpy
3) matplotlib.pyplot
4) from scipy.stats import norm

### Important :
1) Make sure the dataset is imported with pandas.
2) There are NaN values present (tip : use the dropna() function*)
3) Specify the required columns during/after import but BEFORE running the functions.

## List of Functions available in the Risky Business Library :


### 1.
```python
rb.annual_volatility(dataset)
```
### Description
Returns the Annual Volatility of each column in the Dataset.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 2.
```python
rb.compoundperc(dataset)
```
### Description
Returns the Compound percentage of each column in the Dataset.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 3.
```python
rb.month_annualize(month_risk)
```
### Description
Returns the annualized return of each column in the Dataset given the monthly risk.

### Parameters
month_risk - the monthly risk factor.

--------------------------------------------------------------------

### 4.
```python
rb.annual_volatility(dataset)
```
### Description
Returns the annualized volatility of each column in the Dataset.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 5.
```python
rb.returns_month(dataset)
```
### Description
Returns the Monthly returns of each column in an Annual Dataset.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 6.
```python
rb.annualized_ret(dataset)
```
### Description
Returns the Annualized returns of each column in a Monthly Dataset.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 7.
```python
rb.sharpe(dataset,riskfree_rate):
```
### Description
Returns the Annualized returns of each column in a Monthly Dataset.

### Parameters
dataset - Name of the dataset you imported.
riskfree_rate - the riskfree_rate of your country.

--------------------------------------------------------------------

### 8.
```python
rb.get_date(dataset):
```
### Description
Use if your dataset has unorganised date formats.
Returns the dataset with yyyy-mm-dd format.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 9.
```python
rb.drawdown(dataset)
```
### Description
Takes a time series of asset returns.
Computes & returns a Dataframe that contains Wealth index , Previous Peaks & Drawdown Value.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 10.
```python
rb.skewness(dataset)
```
### Description
Computes & returns the skewness of each column.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 11.
```python
rb.kurtosis(dataset)
```
### Description
Computes & returns the kurtosis of each column.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 12.
```python
rb.var_historic(dataset)
```
### Description
Computes & Returns the historic Value at Risk at a specified level
i.e. returns the number such that "level" percent of the returns
fall below that number, and the (100-level) percent are above.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 13.
```python
rb.cvar_historic(dataset)
```
### Description
Computes & Returns the Conditional VaR of a Series or DataFrame.

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 14.
```python
rb.var_gaussian(dataset)
```
### Description
Computes & Returns the Parametric Gauusian VaR of a Series or DataFrame

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 15.
```python
rb.var_fisher(dataset)
```
### Description
The VaR is returned using the Cornish-Fisher modification

### Parameters
dataset - Name of the dataset you imported.

--------------------------------------------------------------------

### 16.
```python
rb.plotvar(dataset)
```
### Description
Plots the comparison bar graph between the 3 VaR methods - Historic, Gaussian, Cornish-Fisher.

### Parameters
dataset - Name of the dataset you imported.
