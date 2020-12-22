import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTENC
from sklearn.metrics import accuracy_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import StratifiedKFold
from collections import Counter

def validation_pipeline(model, cv, X_train, y_train):
    
    oversample = SMOTENC(categorical_features=[2,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
            23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44], random_state=42)
    
    cv_scores = []
    i = 1
    for train_index_fold, validation_index_fold in cv.split(X_train, y_train):
        
        #Training Data
        X_train_fold, y_train_fold = X_train[train_index_fold], y_train[train_index_fold]
        
        #Validation Data
        X_validation_fold, y_validation_fold = X_train[validation_index_fold], y_train[validation_index_fold]
        
        #Apply SMOTE to upsample training data
        X_upsampled_train_fold, y_upsampled_train_fold = oversample.fit_resample(X_train_fold, y_train_fold)
        
        #Fit the model
        clf = model.fit(X_upsampled_train_fold, y_upsampled_train_fold)
        
        #Compute score on validation set
        score = balanced_accuracy_score(y_validation_fold, clf.predict(X_validation_fold))
        print("Fold " + str(i) + " accuracy: " + str(score))
        i+=1
        cv_scores.append(score)
    
    
    mean = 0
    
    for elem in cv_scores:
        mean += elem
    
    mean = mean / 10
    
    return mean