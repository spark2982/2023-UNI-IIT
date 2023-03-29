# Challenge 2 - Bouncing Ball
# # Author: Sean Park
# # Date created: 27 Mar 2023
# # This program takes the users input of choosing a ball and taking the coefficient of restitution of said ball,
# calculates how many times that ball will bounce from a given height and
# outputs the distance travelled as well as how many times it bounced

# coRe = Coefficient of Restitution
# dictionary for tennis ball, basketball, super ball and softball respectively
tBall = 0.7
bBall = 0.75
supBall = 0.9
sofBall = 0.3

coRe = {"Tennis ball": tBall,
        "Basketball": bBall,
        "Super ball": supBall,
        "Softball": sofBall}

# Resetting variables
bounce = 0
height = 0
distance = 0

# Choosing a ball
ball = input("Which ball would you like to bounce?" 
             "\nOptions - Tennis ball, Basketball, Super ball, Softball"
             "\n")
if ball in coRe:
    coReChoice = coRe[ball]
    print("You have chosen", ball, ".")
else:
    print("Sorry, that isn't an option or you have spelt it wrong.")
    exit()

# Choosing height
initialHeight = int(input("What is the initial height in meters? "))
height = initialHeight

# bouncing loop
while initialHeight >= .1:
    bounce += 1
    afterBounce = coRe[ball] * initialHeight
    distance += afterBounce * 2
    initialHeight = afterBounce

# Rounding the answer instead of rounding every bounce
finalDistance = round(distance + height, 2)

print(f"The {ball} bounced {bounce} times and travelled a distance of {finalDistance} meters.")
