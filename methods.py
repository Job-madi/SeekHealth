from data import *


def findfacts():
    ran = random.randint(0, len(facts_) - 1)
    return facts_[ran]


def getQuotes():
    ran = random.randint(0, len(quotes_) - 1)
    return quotes_[ran]


def getBmi(weight, height):
    bmi = round(weight / (height ** 2), 2)
    if (bmi < 16):
        return f"Your Bmi is {bmi}: severely underweight"
    elif (bmi >= 16 and bmi < 18.5):
        return f"Your Bmi is  {bmi}: severly underweight"
    elif (bmi >= 18.5 and bmi < 25):
        return f"Your Bmi is {bmi}: Healthy"
    elif (bmi >= 25 and bmi < 30):
        return f"Your Bmi is {bmi}: Overweight"
    elif (bmi >= 30):
        return f"Your Bmi is {bmi}: severly Overweight"
