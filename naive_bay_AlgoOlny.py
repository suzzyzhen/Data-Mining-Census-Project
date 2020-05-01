#naive bay
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X_df_train, Y_df_train)

y_pred = nb.predict(X_df_test)

print(confusion_matrix(Y_df_test,y_pred))
print(classification_report(Y_df_test,y_pred))
