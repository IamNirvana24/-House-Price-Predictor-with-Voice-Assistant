from sklearn.linear_model import LinearRegression
import pyttsx3


engine = pyttsx3.init()

X = [
    [1000, 2, 5], # Area, Bedrooms, Age
    [1500, 3, 10],
    [800, 2, 15],
    [2000, 4, 8],
    [1200, 2, 7],
    [1800, 3, 12],
    [1600, 3, 6],
    [2200, 4, 3],
]

y = [50, 65, 35, 85, 55, 75, 70, 95] #Price in Lakhs


model = LinearRegression()
model.fit(X,y)


user_input = model.predict([[1232,10,20]])
print(f"The Predicted cost Which I can tell you for this Area, Bedrooms and Age iis {user_input}")
engine.say(f"The Predicted cost Which I can tell you for this Area, Bedrooms and Age iis {user_input}")
engine.runAndWait()