# Analyse the risk of a business using Risky Business

## Functions :
1. Sharpe Ratio
2. Returns & Volatility
3. Risk by Return Ratio
4. Compounded Percentage
5. Annual Drawdown
6. Skewness & Kurtosis
7. Value Added Risk (VaR - Historic, Gaussian, Cornish-Fisher)
8. CVaR - Historic
9. VaR Comparison Plot

**Important** : Read the DOCUMENTATION.md file before implementing any of the functions.

## Installation  

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install riskybusiness

```bash
pip install riskybusiness
```

## Usage

```python
import riskybusiness as rb
rb.FunctionName(dataset = Your_Dataset)
```
> Make sure the dataset is loaded using pandas with the necessary columns.

A sample program using all the functions is displayed in risky.ipynb
> Open using Jupyter NB or Google Colab

This file contains the output samples of all the functions present in the library.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

--------------------------------------------------------------------

## Update 0.0.2

### Added New Functions : 

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

---------------------------------------------------------------

## Find the description of all the functions in the DOCUMENTATION.md file. 
