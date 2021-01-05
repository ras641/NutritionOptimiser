import random

import math

def maximumProduct(singleProductData, nutritionProfile):  #check maximum possible units of all products

    maxPerNutrient = []

    for nutrient in range(len(singleProductData)):

        if float(singleProductData[nutrient]) > 0:

            maxPerNutrient.append(nutritionProfile[nutrient]/float(singleProductData[nutrient]))

        else:

            maxPerNutrient.append(100)

    maxProduct = int(min(list(map(int,(maxPerNutrient)))))+2

    return maxProduct

def totalNutrientValues(productQuanity): #return total nutritional information of a specified amount of each food

    nutrients = [0] * len(productQuanity[0][0])

    for product in productQuanity:

        for nutrient in range(len(product[0])):

            nutrients[nutrient] += product[0][nutrient]*product[1]

    return nutrients

def randomSelection(productData, numberProducts, nutritionProfile): # return a random combination of portions of all foods up the their respective maximum sizes

    productQuantity = []

    positions = []

    for product in range(numberProducts):

        productSelection  = []
        
        productNumber = random.randint(0,len(productData)-1)

        positions.append(productNumber)

        productSelection.append(productData[productNumber])

        productSelection.append(random.randint(0,maximumProduct(productData[productNumber], nutritionProfile)))
        
        productQuantity.append(productSelection)
        
    return productQuantity, positions

def checkFitness(productQuantity, nutritionProfile, relevantNutrients): # check the fitness function of this series of portions

    totalNutrients = totalNutrientValues(productQuantity)

    #print (nutritionProfile)

    #print (totalNutrients)
    
    proportions = []


    for nutrient in range(46):

        #len(totalNutrients)

        if relevantNutrients[nutrient] == 1:

            score = math.fabs((totalNutrients[nutrient]-nutritionProfile[nutrient])/nutritionProfile[nutrient])

            #print (score)

            proportions.append(score)

    averageScore = sum(proportions)/float(len(proportions))

    #print ('avg: ' + str(averageScore))

    return (averageScore)



    #print ([ '%.2f' % elem for elem in proportions ])

    #return max(proportions)

test = [[[22.17,22.35,2.19,300,0,0.03,0.56,0.15,0.07,0.08,1.03,0.15,0,505,0.44,20,354,76,627,2.92,0.011,0,0.03,17,676,174,179,57,0,0.19,0.4,0,0.4,0,0,0,0,0.03,0.283,0.104,0.141,0.037,7,2.28,15.4,79,13.152,2.19],1],

        [[3.52,2.34,10.74,77,0,5,0.01,0.01,4.63,0.01,9.66,0.01,1,114,0.42,23,105,197,44,0.63,0.103,3.1,0.013,2.7,176,51,51,4,0,0.03,1.1,0,1.1,0,0,0,0.2,0.039,0.182,0.133,0.328,0.04,5,0.49,15.6,8,1.431,9.74],1],

        [[9.58,0.99,75.37,296,0,0,0,0,0,0,2.21,0,11.5,11,1.72,132,294,1534,13,7.66,5.165,0,1.176,46.1,0,0,0,0,0,0,3.9,3.9,0,0,0,0,3.5,0.3,1.27,14.1,21.879,0.965,163,0,201.7,0,0.225,63.87],1],

        [[23.91,2.17,63.1,358,47.62,0,0,0,0,0,0,0,10.8,48,7.39,59,294,668,7,3.6,1.303,0,1.716,0,58,0,3,35,0,0,0,0,0,0,0,0,1.7,0.51,0.106,1.495,0.348,0.403,204,0,0,0,0.379,52.3],1],

        [[26.96,30.99,1.44,393,0,0,0,0,0,0,0,0,0,890,0.13,33,574,72,187,4.37,0.047,0,0.026,30,1047,283,288,61,1,0.6,0,0,0,2,1,8,0,0.011,0.302,0.064,0.353,0.071,10,3.06,15.5,93,18.227,1.44],1]]

testProfile = 200,50,20,1700,80,5,5,5,50,5,20,1,20,1000,8,400,1000,3800,600,14,1.7,2000,5,60,10000,300,300,300,300,10,5,2,2,50,10,50,30,1,1,15,5,1,400,2.4,500,300,50,40

#print(checkFitness(test, testProfile))

def guessOptimal(guesses, productData, nutritionProfile, output, maxItems, relevantNutrients): # guess a combination and compare its fitness to the previous best, first parameter how many guessies it makes

    maxFitness = 1000 #lower is better

    maxFitnessProfile = []

    bestPositions = []

    for guessCount in range(guesses):

        if output and guessCount % 100000 == 0: print (guessCount)

        guess, positions = randomSelection(productData, maxItems, nutritionProfile)

        guessFitness = checkFitness(guess, nutritionProfile, relevantNutrients)

        if guessFitness < maxFitness:

            if output == True:

                print ('new maximum fitness', guessFitness)

                #for product in range(len(positions))

            maxFitness = guessFitness

            maxFitnessProfile = guess

            bestPositions = positions

    return maxFitnessProfile,totalNutrientValues(maxFitnessProfile), bestPositions

