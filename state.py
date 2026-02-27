import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

np.random.seed(42)
data={
    'product_id': range(1,21),
    'product_name':[f'product{i}' for i in range(1,21)],
    'category':np.random.choice(['electronics','closting','home','sports'],20),
    'unit_sold':np.random.poisson(lam=100,size=20),
    'sale_date':pd.date_range(start='2023-01-01',periods=20,freq='D')

}

sales_data=pd.DataFrame(data)
print('sales data')
print(sales_data)

sales_data.to_csv('sales_data.csv',index=True)

import os
os.getcwd