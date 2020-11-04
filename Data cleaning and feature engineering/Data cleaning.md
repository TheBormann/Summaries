# Data Cleaning Cheatsheet

In this Cheatsheet we will be covering the most important ways to improve the quality of datasets.

This means, that we need to clean up up the data set in general and only select the features, that could help us make a better 
prediction. The other way of improving the dataset is [Feature engineering](./Feature%20engineering)

In an production environment the strategies used here, should be converted into an pipeline,
to optimize the workflow and minimize data leakage.

After you have cleaned and trained your data for the first time, you can use these methods to improve you model
with feature engineering.

## Import data
If your data has inconsistent null-values, you can tell pandas to add strings to the null value detection:

```
missing_values = ["n/a", "na", "--"]
df = pd.read_csv('./your/link/to/yourDataset.csv', na_values = missing_values)
```
When you want to load sql data, use the following:
```
import  sqlite3
import pandas as pd

try:
    conn = sqlite3.connect('../data/gathered/Database.db')
    cursor = conn.cursor()
except:
    print("Database  couldn ’t get  created/be found")

df = pd.read_sql("select * from  table_name", con=conn)
```

## 1. Understanding the dataset

To clean data properly you need to understand what each column means and how it's presented in the dataset.
For this it's best to create a  summary table for every column:
* Type: numerical or categorical
* Segment: Divide columns in different topics of information
* Expectation: low, high, medium
* Conclusion: After working with the date reevaluate Expectation (this column stays empty until I have trained the 
dataset and can confirm my expectations)
* Comments: Note some important information about the column


| Variable                               | Type        | Segment | Expectation | Conclusion | Comments                                |
|----------------------------------------|-------------|---------|-------------|------------|-----------------------------------------|
| ID                                     | numerical   | organize| medium      | low        | unnecessary                             |
| label                                  | categorical | object  | high        | high       | y variable                              |
| feature                                | numerical   | object  | high        | high       |                                         |

Normally visualizations are key to understand the dataset, but visualizations are hard as long as we have missing values
and uncleaned data.
So our strategy will be, to get basic cleaning done, than visualize what we got and maybe change/ optimize the cleanig 
later on.

## 2. Handling missing values

Even though we might not need every column in the dataset, it is important to clean the whole data set instead of only 
the columns we evaluated as promising. 
The reason is, with a fully cleaned dataset we can visualize more and this means we can see correlations between columns, 
which we can use to reevaluate our expectations.

### Workflow for treating missing values
1. Convert all missing values to np.nan values
2. Analyze the amount and type of missingness in the data
3. Appropriately delete or impute missing values
4. Evaluate and compare the performance of the treated/imputed dataset 

### Some handy functions for finding missing values

```
def missing_values(data):
    total=data.isnull().sum().sort_values(ascending=False)
    percentage=round(total/data.shape[0]*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])
```
Missing_values creates a table, that shows every column, the amount of missing values and the percentage in relation to 
the whole dataset.

```
def count_values_in_column(data,feature):
    total=data.loc[:,feature].value_counts()
    percentage=round(data.loc[:,feature].value_counts(normalize=True)*100,2)
    return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])
```
This method shows the different values that a column has in absolute and relative perspective.

### Use missingno library for visualization
Missingno creates chars for visualizing missing data. As you can see in the following example, it's pretty simple.\
More about Missingno [here](missingno.md)

#### Quick and dirty
 * get sum of missing values:
     ```
      df.isnull().sum()
     ```
* get percentage of missing values:
     ```
      df.isnull().mean() * 100
     ```

### Different methods of removing missing values
To change this there are different techniques

1. **Delete columns**:\
   This is viable, if there are to many missing values. Otherwise it's hard filling the gaps 
   without any bias, but there is a catch. If the column is important for your prediction, try to find the reason for the
   NaN values, if they aren't random you can use utilize it for your prediction.
   ```
    df.drop(['col1', 'col2'], axis=1, inplace=True)
    ```
   
2. **Drop rows with missing data:**
    This strategy isn't perfect as well. Deleting rows means less data to train with.
    It should be used if some rows have multiple missing values or the missing values you want to get rid of are only a 
    very low percentage of the dataset. 
   ```
    df.dropna(inplace=True)
    ```
   
3. **Filling in missing values**, there are different options:
    * Fill with a specific value (for example 0)
    * Fill with a calculated value like median or most common
        ```
        df.fillna({'col1':0, 'col2':df['col2'].mean(), 
                    'col3':df['col3'].value_counts().index[0], 'col4':"test"}, inplace=True)
        ```
    * If the column is sorted, fill with the next or previous value:
        * ffill (forward fill)= replaces NaN with last valid value
        * bfill (backward fill)= replaces NaN  with next valid value
        ```
        df.fillna(method='bfill', axis=0)
        ```
    * Simple Imputer, for easy replacement of missing values Strategies:
        * strategy='median'
        * strategy='most_frequent'
        * strategy='constant', fill_value=0
        ```
        from sklearn.impute import SimpleImputer
        
        mean_imputer = SimpleImputer(strategy='mean')
        df = mean_imputer.fit_transform(df)
        ```
    * Filling with the next or previous value is often not optimal. A better way is the
        * Linear Interpolation
        * Quadratic Interpolation (only in specific cases)
        * Nearest Interpolation
        ```
        # Visualization of the way NaN values are filled
      
        df_interpolation["column"].plot(color="red", marker='o', linestyle='dotted', figsize(30,5))
        df["column"].plot(title="column name", maker='o')
      
        # Use Interpolation
      
        df.interpolate(method='linear', inplace=True)
        ```
    * Finally there are more fancy Imputation techniques, some shown here:
        * **KNN** finds most similar points for imputing
        ```
        from fancyimputer import KNN
        knn_imputer = KNN()
        df_knn.iloc[:, :] = knn_imputer.fit_transfrom(df)
        ```
        * **MICE** performs multiple regression for imputing
        ```
        from fancyimputer import Iterativeimputer
        MICE_imputer = IterativeImputer()
        df_MICE.iloc[:, :] = MICE_imputer.fit_transfrom(df)
        ```
        * Impute missing categorical values, there are 3 steps we need to follow:
            1. Convert non-missing categorical columns to ordinal values
            2. Impute the missing values in the ordinal dataframe
            3. Convert back to categorical
            
            * **Ordinal encoding** 
            ```
            # Create an empty dictionary ordinal_enc_dict
            ordinal_enc_dict = {}
            
            for col_name in df:
                # Create Ordinal encoder for col
                ordinal_enc_dict[col_name] = OrdinalEncoder()
                col = df[col_name]
                
                # Select non-null values of col
                col_not_null = col[col.notnull()]
                reshaped_vals = col_not_null.values.reshape(-1, 1)
                encoded_vals = ordinal_enc_dict[col_name].fit_transform(reshaped_vals)
                
                # Store the values to non-null values of the column in users
                df.loc[col.notnull(), col_name] = np.squeeze(encoded_vals)
            ```
            * **KNN**
            ```
            # Create KNN imputer
            KNN_imputer = KNN()
            
            # Impute and round the DataFrame
            df.iloc[:, :] = np.round(KNN_imputer.fit_transform(users))
            
            # Loop over the column names in users
            for col_name in df:
                
                # Reshape the data
                reshaped = df[col_name].values.reshape(-1, 1)
                
                # Perform inverse transform of the ordinally encoded columns
                df[col_name] = ordinal_enc_dict[col_name].inverse_transform(reshaped)
            ```

### Evaluate the different Imputation methods
1. Get unimputed data, for reference. The different Imputation models, should be as close to this model as they can get.
    ```
    import statsmodels.api as sm
    
    
    df_cc = df.dropna(how='any')
    X = sm.add_constant(df_cc.iloc[:, :-1])
    y = df_cc['column']
    lm = sm.OLS(y, X).fit()
    
    # print all stats
    print(lm.summary())
    
    # print R-squared, which explains accuracy (The higher the better the model)
    lm.rsquared_adj
    
    # print Coefficients, which explains if the model itselfs interferes
    lm.params
    ```
2. Fit linear model on different imputed dataframes:
    ```
    # Mean Imputation
    X = sm.add_constant(df_mean_imputed.iloc[:, :-1])
    y = df['column']
    lm_mean = sm.OLS(y, X).fit()
    
    # KNN Imputation
    X = sm.add_constant(df_knn_imputed.iloc[:, :-1])
    lm_KNN = sm.OLS(y, X).fit()
    
    # MICE Imputation
    X = sm.add_constant(df_mice_imputed.iloc[:, :-1])
    lm_MICE = sm.OLS(y, X).fit()
    
    ```
3. Comparing R-squared of different imputations
    ```
    print(pd.DataFrame({'Complete': lm.rsquared_adj, 
                'Mean Imp.': lm_mean.rsquared_adj, 
                'KNN Imp.': lm_KNN.rsquared_adj, 
                'MICE Imp.': lm_MICE.rsquared_adj},
               index=['R_squared_adj']))
    
    print(pd.DataFrame({'Complete': lm.params, 'Mean Imp.': lm_mean.params,
                             'KNN Imp.': lm_KNN.params,
                             'MICE Imp.': lm_MICE.params}))
    ```
4. Visualize Imputations, to see which imputation resembles the original data (the Baseline) the most.
    ```
    df_cc['column'].plot(kind='kde', c='red', linewidth=3)
    df_mean_imputed['column'].plot(kind='kde')
    df_knn_imputed['column'].plot(kind='kde')
    df_mice_imputed['column'].plot(kind='kde')
    
    labels = ['Baseline (Complete Case)', 'Mean Imputation', 'KNN Imputation', 'MICE Imputation']
    
    plt.legend(labels)
    plt.xlabel('column')
    ```

In a production environment it's highly advised to look at each column and decide which method to use, otherwise a lot of information could be lost.
If you aren't sure if dropping or imputing will yield better results, than implement both and compare via Mean average error.

## 3. Scaling and normalization
Scaling and normalization can improve your prediction result immensely, if you use certain types of algorithms.
* Gradient Descent Based Algorithms: \
    These algorithms improve step by step. To find the minimum an algorithm must step closer and closer to the minimum, 
    without overstepping the minimum to much, otherwise it can't find the optimal result. But if there are different
    values with different step sizes, it's hard to find the minimum.
* Distance-Based Algorithms: \
    These algorithms rely on the distance of the new variable to the other variables in the dataset. If variables are 
    closer together, because of wrong scaling, this could lead to and overemphasis of one category in the dataset.

Algorithms that don't need to be scaled/ normalized,  are **Tree-Based Algorithms**.

The difference between scaling and normalization is, that Scaling changes the range of the values, while normalization
changes the shape of the distribution itself.
#### Scaling
Scaling squishes the shape of the distribution into another range, like 0-1 or 0-100.
```
from sklearn.preprocessing import minmax_scale
scaled_data = minmax_scaling(original_data, columns=[0])

# or

from sklearn.preprocessing import MinMaxScaler
norm = MinMaxScaler().fit(X_train)
X_train_norm = norm.transform(X_train)
X_test_norm = norm.transform(X_test)
```

#### Normalization
Normalization uses the first derivative of the shape of the function to scale it all values between 1 and 0.
1 is the maximum value and 0 is the minimum.
```
# for Box-Cox Transformation
from scipy import stats

normalized_data = stats.boxcox(original_data)
```

#### Standardization
This is another scaling technique, where the mean value is set to the value 0 and  the standard deviation is changed to 
fit the function to a specific scale. This helps to reduce the influence of outliers
```
from sklearn.preprocessing import StandardScaler

scale = StandardScaler().fit(X_train)
X_train = scale.transform(X_train)
```


## 4. Parse dates
when loading a dataset, dates are saved as Strings in the dataframe.
[Here are all the different format types that can be used.](https://strftime.org/)
```
df['column'] = pd.to_datetime(df['column'], format="%m/%d/%y")
```
If there are different types of format in one column, you can use **infer_datetime_format=True** to let pandas find out
the right format by itself. (Don't use it if not necessary, because it is more time consuming than defining the right 
format before hand.)

When parsed correctly it is possible to interact with the dates now,  for example get the day of a date:
```
df['date'].dt.day
```

## 5. Character encodings


If loading the dataset gets and error like this: 
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0x99 in position 11: invalid start byte
```
You can use the method, Rachael Tatman has described, load the data as rawdata and use chardet to detect the encoding.
```
import chardet

# look at the first ten thousand bytes to guess the character encoding
with open("../input/kickstarter-projects/ks-projects-201801.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(10000))

# check what the character encoding might be
print(result)
```


## 6. Inconsistent data entry
Data can be entered in very creative and different forms. To see inconsistent values, use:
```
df['Column'].unique()
```
1. Remove white spaces and turn everything to lower case.
    ```
    df['column'] = df['column'].str.lower()
    df['column'] = df['column'].str.strip()
    ```
2. Use fuzzywuzzy library\
    The **extract()** function gives out Strings in the column that are similar to the one passed. The score can be
    used to correctly identify the change threshold.
    ```
    import fuzzywuzzy
    from fuzzywuzzy import process
    import chardet
   
   matches = fuzzywuzzy.process.extract("example value", column, limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
    ```
   This function helps to change variables with an high enough similarity-ratio:
    ```
    def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):
        # get a list of unique strings
        strings = df[column].unique()
        
        # get the top 10 closest matches to our input string
        matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                             limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)
    
        # only get matches with a ratio > 90
        close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]
    
        # get the rows of all the close matches in our dataframe
        rows_with_matches = df[column].isin(close_matches)
    
        # replace all rows with close matches with the input matches 
        df.loc[rows_with_matches, column] = string_to_match
        
        # let us know the function's done
        print("All done!")
    ```

# References
These other kernels helped me write this cheatsheet:
* https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python/data
* https://www.kaggle.com/rtatman/data-cleaning-challenge-handling-missing-values
* https://www.kaggle.com/raenish/cheatsheet-text-helper-functions
* https://www.analyticsvidhya.com/blog/2020/04/feature-scaling-machine-learning-normalization-standardization/
* https://github.com/ResidentMario/missingno