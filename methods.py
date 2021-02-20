from data import *


def findfacts():
    ran = random.randint(0, len(facts_) - 1)
    return facts_[ran]

def getQuotes():
    ran = random.randint(0,len(quotes_)-1)
    return quotes_[ran]

