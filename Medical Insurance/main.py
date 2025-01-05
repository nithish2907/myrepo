import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data = pd.read_csv("C:\\Users\\shikh\\OneDrive\\Desktop\\Medical Insurance.csv")
data = pd.get_dummies(data, columns=['sex', 'smoker', 'region'])
X = data.drop('charges', axis=1)
y = data['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
def predict_insurance_cost(age, sex, bmi, children, smoker, region):
    input_data = pd.DataFrame({
        'age': [age],
        'bmi': [bmi],
        'children': [children],
        'sex_female': [1 if sex == 'female' else 0],
        'sex_male': [1 if sex == 'male' else 0],
        'smoker_no': [1 if smoker == 'no' else 0],
        'smoker_yes': [1 if smoker == 'yes' else 0],
        'region_northeast': [1 if region == 'northeast' else 0],
        'region_northwest': [1 if region == 'northwest' else 0],
        'region_southeast': [1 if region == 'southeast' else 0],
        'region_southwest': [1 if region == 'southwest' else 0]
    })
    predicted_cost = model.predict(input_data)
    return predicted_cost[0]
print("Give the following details:")
age = int(input("Age: "))
sex = input("Sex (male/female): ").lower()
bmi = float(input("BMI: "))
children = int(input("Number of children: "))
smoker = input("Smoker (yes/no): ").lower()
region = input("Region (northeast, northwest, southeast, southwest): ").lower()
predicted_cost = predict_insurance_cost(age, sex, bmi, children, smoker, region)
print(f'Predicted Insurance Cost: {predicted_cost}')
