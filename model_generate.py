from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Your code using RandomForestRegressor here...

def generate_model(data):
    y = data.Classification

    features = ['Mean R', 'Mean G', 'Mean B']

    # Select columns corresponding to features, and preview the data
    X = data[features]
    X.head()

    # Split into validation and training data
    global train_X, val_X, train_y, val_y
    
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
    
        # instantiate the model
    logreg_model = LogisticRegression(solver='liblinear', random_state=0)


    # fit the model
    logreg_model.fit(train_X, train_y)
    
    y_pred_test = logreg_model.predict(val_X)

    print(y_pred_test)
    
    # probability of getting output as 0 - no rain

    logreg_model.predict_proba(val_X)[:,0]
    logreg_model.predict_proba(val_X)[:,1]

    print('Model accuracy score: {0:0.4f}'. format(accuracy_score(val_y, y_pred_test)))