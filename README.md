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
We will expose some interfaces of our application, trying each time to describe
the various interactive objects made available to the user.

#### Home Page

This is the first contact that the user (employee of the Prosper company) has with the platform, he
sees an image illustrating the granting of a credit to an imprinter which represents exactly
the role of our platform in assisting Prosper employees in assisting with the
customer solvency decision (imprinter) of the Prosper.com platform. The user can
then press the "Learn More" button or press the orange bar
then press the button to authenticate (Login), the two possibilities direct the user to
the authentication page.

![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/1HomePage.png?raw=true)
![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/1HomePage2.png?raw=true)

#### Login Page

On this page the user can authenticate to his account by entering his email and
his password provided that he already has an account created by the administrator of
the application (usually the manager of the Prosper team granting the credits). For the sake of
security the password must necessarily contain at least 6 characters. Then if both
entries correspond the user is directly directed to his account and precisely to the
prediction page.

![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/1LoginPage.png?raw=true)

#### Predict Page

After successful authentication, the user accesses this page where he can fill in the
information about the borrower, namely:
• The Days Delinquent: The current number of days the loan is past due.
• The Customer Principal Payments: The cumulative amount of Prepayments
(Principal payments) made by the borrower on the loan before closing the account.
• The Gross Principal Loss: The gross amount not refunded after closing the account.
• The Customer Payments: The gross amount refunded before closing the account.
• The Interest and Fees: The cumulative amount of interest and fees incurred by the loan
lender on the loan before closing the account,
• The Service Fees: The cumulative service fees paid by investors (lenders)
who invested in the loan.
• The Monthly Loan Payment: The monthly loan payment.
• The Available Loan Payment: The total credit available on the credit card at the time
where the credit profile was extracted.
• The Reviving Credit Balance: Dollars of revolving credit at the time the credit profile
credit has been withdrawn.
then pressing the "predict" button the pre-trained naive bayesian model performs the pre-
diction and redirects the user to the result interface which displays the result of the prediction.

![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/LoginSuccessfulPredictPage.png?raw=true)

#### Result Page

After completing and submitting the prediction page form, and if the prediction is
favorable, the user is sent to this result page which shows him that this borrower deserves
to have credit. (Congratulations, This user is eligible for the Loan.)

![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/CongratsResultPage.png?raw=true)
![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/UnfortunatelyPage.png?raw=true)

#### MustBeAdmin Page
Otherwise if the prediction is unfavorable, the user is sent to this same page
does not display this time that this user does not deserve to have a credit. (Unfortunately, This
user is not eligible for the Loan.)

![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/BeAdmin.png?raw=true)


#### Register Page
Only the administrator can access this page, to register new users,
the administrator fills in the following information about the new user to add:
his name, his email, the type of account (Administrator or simple user) and his password. Finally if the email is valid and has not already been used and if the password exceeds 6
characters then by pressing "Create Account", the new user and
immediately added to the SQL database.

![alt text](https://github.com/Heyyassinesedjari/Prosper_loan_prediction_simple_web_app/blob/main/Screenshots/1RegisterPage.png?raw=true)

