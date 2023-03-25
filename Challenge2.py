# input coefficient of restitution and initial height in m
# report how many times ball bounces when dropped from height
# before it rises to a height of less than 10 cm
# also report total distance travelled by the ball

# coRe = Coefficient of Restitution
# tennis ball, basketball, super ball and softball respectively
tBall = 0.7
bBall = 0.75
supBall = 0.9
sofBall = 0.3

coRe = {"Tennis ball" : tBall,
        "Basketball"  : bBall,
        "Super ball"  : supBall,
        "Softball"   : sofBall}

ball = input("Which ball would you like to bounce? ")
if ball in coRe:
    coReAns = coRe[ball]
print("You have chosen", [ball],".")



height = int(input("What is the height of the initial height in meters? "))

numOfBounce = height *