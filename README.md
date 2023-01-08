# Predictive-Modelling-Using-Social-Profile-in-Online-P2P-Lending-Market 15 August

In this project the status of the borrower was analyzed based on the features given in the loan dataset to predict if the loan will be completed or defaulted.


## Understanding the Dataset
The dataset contains 81 features and 113937 rows.

- We are working on listings or records after 2008

- The target of the dataset is the "LoanStatus". We renamed it as "Success" whose value is "NO"(0) if the value in LoanStatus is (chargedoff or defaulted) otherwise it will be "Yes" (1).


## Preprocessing and Sentiment Analysis

Missing values in categorical features ('CreditGrade', ‘ClosedDate', 'ProsperRating (Alpha)', 'BorrowerState', 'Occupation', 'EmploymentStatus', 'GroupKey', 'FirstRecordedCreditLine) were filled by the most frequent value of each feature. For the 'CreditGrade' it turned out to be unbalanced.
So, it was filled by the values in average score columns (upper and lower) to get the suitable Letter grade for each value.
 For the numerical features ('BorrowerAPR', 'EstimatedEffectiveYield', 'EstimatedLoss', 'EstimatedReturn', 'ProsperRating (numeric)', 'ProsperScore', 'EmploymentStatusDuration', 'CreditScoreRangeLower', 'CreditScoreRangeUpper', 'CurrentCreditLines', 'OpenCreditLines', 'TotalCreditLinespast7years', 'InquiriesLast6Months', 'TotalInquiries', 'CurrentDelinquencies', 'AmountDelinquent', 'DelinquenciesLast7Years', 'PublicRecordsLast10Years', 'PublicRecordsLast12Months', 'RevolvingCreditBalance', 'BankcardUtilization', 'AvailableBankcardCredit', 'TotalTrades',
'TradesNeverDelinquent (percentage)', 'TradesOpenedLast6Months', 'DebtToIncomeRatio', 'TotalProsperLoans', 'TotalProsperPaymentsBilled', 'OnTimeProsperPayments', 'ProsperPaymentsLessThanOneMonthLate', 'ProsperPaymentsOneMonthPlusLate', 'ProsperPrincipalBorrowed', 'ProsperPrincipalOutstanding', 'ScorexChangeAtTimeOfListing', 'LoanFirstDefaultedCycleNumber') the missing values were replaced by the mean.


## Feature Engineering

For EDA, the features were analyzed and the relation between the features was shown, then started plotting histograms and heatmaps between features to get relations to help in defining features.
For feature engineering, features of correlation > 0.8 were dropped leaving only one feature of each correlated group. Features causing data leakage were dropped (data which will not be able in the real life).
All features were trasformed into numeric features and the remaining non-numeric was dropped. 
SelectKbest method was used to get the best features to use.
The dataset ended up with only 27 features.
The outliers were put at threshold for all features.


## Data Standarization

Before modelling and after splitting the data was scaled using standardization to shift the distribution to have a mean of zero and a standard deviation of one.

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(X_train)
rescaledX = scaler.transform(X_train)
rescaledValidationX = scaler.transform(X_valid)
```
**fit_transform()** is used on the training data so that we can scale the training data and also learn the scaling parameters of that data. Here, the model built by us will learn the mean and variance of the features of the training set. These learned parameters are then used to scale our test data.

**transform()** uses the same mean and variance as it is calculated from our training data to transform our test data. Thus, the parameters learned by our model using the training data will help us to transform our test data. As we do not want to be biased with our model, but we want our test data to be a completely new and a surprise set for our model.
```

## Model building

#### Metrics considered for Model Evaluation
**Accuracy, Precision, Recall and F1 Score**
- Accuracy: What proportion of actual positives and negatives is correctly classified?
- Precision: What proportion of predicted positives are truly positive?
- Recall: What proportion of actual positives is correctly classified?
- F1 Score: Harmonic mean of Precision and Recall

#### Logistic Regression
- Logistic Regression helps find how probabilities are changed with actions.
- The function is defined as P(y) = 1 / 1+e^-(A + By) 
- Logistic regression involves finding the **best fit S-curve** where A is the intercept and B is the regression coefficient. The output of logistic regression is a probability score.

##### **logistic regression** was applied with hyperparameters as following:
- solver='liblinear'
- C=120
- penalty='l1'

##### The metrics of the resulting model was as following:
- Accuracy=81%
- Precision=81%
- Recall=81%
- F1 Score=81% 

#### Random Forest Classifier
- The random forest is a classification algorithm consisting of **many decision trees.** It uses bagging and features randomness when building each individual tree to try to create an uncorrelated forest of trees whose prediction by committee is more accurate than that of any individual tree.
- **Bagging and Boosting**: In this method of merging the same type of predictions. Boosting is a method of merging different types of predictions. Bagging decreases variance, not bias, and solves over-fitting issues in a model. Boosting decreases bias, not variance.
- **Feature Randomness**:  In a normal decision tree, when it is time to split a node, we consider every possible feature and pick the one that produces the most separation between the observations in the left node vs. those in the right node. In contrast, each tree in a random forest can pick only from a random subset of features. This forces even more variation amongst the trees in the model and ultimately results in lower correlation across trees and more diversification.

##### A grid search was applied for the following hyperparameters values:
- 'n_estimators': [10, 25, 41, 56, 72, 87, 103, 118, 134, 150]
- 'max_features': ['auto', None]
- 'max_depth': [2, 4, None]
- 'min_samples_split': [2, 5]
- 'min_samples_leaf': [1, 2]
- 'bootstrap': [True, False]

The best parameters resulted from the grid search were as following:
- 'bootstrap': True
- 'max_depth': None
- 'max_features': None
- 'min_samples_leaf': 2
- 'min_samples_split': 5
- 'n_estimators': 118

##### The metrics of the resulting model was as following:
- Accuracy=86%
- Precision=88%
- Recall=82%
- F1 Score=85% 

## Deployment
you can access our app by following this link [prosper-loan-success-application-Django] (https://team-b-django.herokuapp.com/) or by click [prosper-loan-success-application flask] (https://prosperwebapp.herokuapp.com/)


### Django
- We created a simple Django project.
- We saved the random forest model to model.sav and the standard scaler to scaler.sav previously to import them into the Django project.
- We deployed the app to Heroku (https://team-b-django.herokuapp.com/)


### Flask 
We also create our app by using flask for the logistic regression model, then deployed it to Heroku. The files of this part are located into (TEAM-B-DEPLOYED-FLASK-APP) folder. You can access the app by following this link[prosper-loan-success-application-flask]
(https://prosperwebapp.herokuapp.com/)

### Heroku
We deployed our Django and Flask apps to [Heroku.com] (https://www.heroku.com/). In this way, we can share our app on the internet with others. 
We prepared the needed files to deploy our app successfully:
- Procfile: contains run statements for app file.
- requirements.txt: contains all the libraries must be downloaded by Heroku to run app file (run.py for Flask app and Deploy for Django app).
- runtime.txt: contains python version to interpret the code (For Django).

### User Interface

![alt text](https://drive.google.com/file/d/1ODvbxd9q_vzRtYC5aSBESGnC-0wmKCFl/view?usp=sharing)
