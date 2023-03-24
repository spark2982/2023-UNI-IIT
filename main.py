# user input
faceValue = int(input("What is the face value for the bond? "))
marketPrice = int(input("What is the current market price? "))
yearsToMature = int(input("How many years will it mature? "))
Interest = float(input("What is the interest earned per year? ")) * 1000

# Calculation of a and b
a = (faceValue - marketPrice) / yearsToMature
b = (faceValue + marketPrice) / 2

# Years to mature
ytm = (Interest + a) / b

# Years to mature in percentage
ytmPercent = ytm * 100

# Final output
print("The approximate Years to Mature will be ", ytm, "%")
