# Test Hypothesis
So you got you machine learning idea and want to turn it into an ML powered application, what is the best way to get to 
a finished product?

For now let's split the process into 4 mayor parts:
1. Identifying the right ML approach
2. Building an initial prototype
3. Iterating on models
4. Deployment and monitoring

in this summary we will be focusing  on the first two bullet points:


# Most important

1. Think about how to implement your idea
    * What data do you need?
    * Where to get the data?
    * What should the algorithm be able to perform?
    * What are the most useful features from the dataset?
2. Go though the steps by yourself
    * Try gather the data manually
    * Use gathered features only to make a prediction
    * Create graphs to visualize correlations
    * predict with the gained knowledge the outcome
    * Check if your prediction was correct (if not, maybe you approach is wrong)
3. Implement project in the most basic way
    * this serves as "ground truth" that can be compared to other more sophisticated algorithms
    * When success metrics are installed improve the model, change feature engineering approach or improve/broaden the data collection

## Most significant challenges:
* **Data**:
    to acquire the right data can be time consuming, costly and sometimes even impossible
* **Model**:
    How low does it take to train?\
    How often do you retrain the model?\
    How hard is it to implement it?\
* **Latency**:
    How long and how computation intensive is the ml model?
* **Ease of implementation**:
    Is it feasible to implement it into an actual product and are there wrong doings of the algorithm that could be exploited in any form?

# Definitions

* **Forecasting** mean predicting from a series of data points
* **Anomaly detection** means detecting unusual events from a given dataset
* **Feature selection** is the process of identifying a subset of features, that have the best prediction rate
* **Feature generation** is the process of modifying and combining features to create better predictors
* **Data availability**
    * **Labeled data exists**: Labels are exactly what we are trying to measure (least common)
    * **Weakly labeled data exists**: Labels are slightly correlated with our production goal
    * **Unlabeled data exists**: Data must be labeled by our self's
    * **We need to acquire data**: Data must be gathered and labeled (most common)

# Advice for ML Projects
Q:  How do you scope out an ML product?
A:  Try to use the best most fitting tools to solve the problem, use ML only if needed

Q:  How do you decide what to focus on in an ML project?
A:  Find the **impact bottleneck**, the part of your project, that gives the most value if you improve it.
    To find it, replace to model with something simple and debug the whole pipeline

Q:  Why do you usually recommend starting with a simple model?
A:  One important factor is to derisk the model. The best way to do it, is to start with a simple model as a baseline

Q:  Once you have your whole pipeline, how do you identify the impact bottleneck?
A:  Set yourself a tight deadline, so you will automatically select the tasks, that are most relevant for your project.
    In addition imaging the impact bottleneck solved, and ask yourself, if it was worth it. If not select something else.

Q:  How do you decide which modeling techniques to use?
A:  look at the input and output data and decide from there which model fits the data best.
    If you are using Heuristic models, rank features after frequency, you can quickly identify and label 80% of your use cases

# Conclusion

First we need to evaluate the feasibility of your project and approach. The rule of thumb is, to use heuristic or 
deterministic approach to solve the problem if possible. If not first try an supervised model approach, because it's simple 
and easier to explain what the model is doing.
In addition try to start with an heuristics or classification based approach and move to more complex algorithms if needed

Next you should find ways to scrape strongly or weakly labeled data (sometimes one of the hardest tasks)

Set success metrics and start tracking progress with the most simple model as baseline. 
Then update the model, change feature engineering and data collection to improve model.

# Ressources
https://www.oreilly.com/library/view/building-machine-learning/9781492045106/