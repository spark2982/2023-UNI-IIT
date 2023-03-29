# Challenge 1 - Bond Yield

# User input
faceValue = int(input("What is the face value of the bond? "))
marketPrice = int(input("What is the current market price? "))
yearsToMature = int(input("How many years until it matures? "))
interest = float(input("What is the interest earned per year? ")) * 1000

# Calculation of a and b
a = (faceValue - marketPrice) / yearsToMature
b = (faceValue + marketPrice) / 2

# Years to mature
ytm = (interest + a) / b

# Years to mature in percentage and rounding
ytmPercent = ytm * 100
ytmRound = round(ytmPercent, 2)

# Final output
print("The approximate Years to Mature will be ", ytmRound, "%")
