#Cross validation

To use cross validation effectively, you should use pipeline for data cleaning.

```


from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
%matplotlib inline

def get_score(n_estimators):
    """Return the average MAE over 3 CV folds of random forest model.
    Keyword argument:
    n_estimators -- the number of trees in the forest
    """
    score_pipeline = Pipeline(steps=[
    ('preprocessor', SimpleImputer()),
    ('model', RandomForestRegressor(n_estimators=n_estimators, random_state=0))
    ])
    scores = -1 * cross_val_score(score_pipeline, X, y, cv=3, scoring='neg_mean_absolute_error')
    avg = scores.sum() / 3
    return avg


results = {} # Your code here
for i in range(50, 450, 50):
    results[i] = get_score(i)

plt.plot(list(results.keys()), list(results.values()))
plt.show()
```