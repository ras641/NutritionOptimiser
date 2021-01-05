import generateDiet

import getData

def getPosition(name, records):

    for record in range(len(records)):

        if records[record][0] == name:
             return record

    return 0

def main():

    productDataSource = 'productDataUse.csv'

    productData = getData.getData(productDataSource)

    productDataUpdate = []

    for product in productData:

        productIn = []

        for nutrient in product:

            if nutrient == 'NULL': productIn.append(0)

            else: productIn.append(nutrient)

        productDataUpdate.append(productIn)

    productData = productDataUpdate

    nutritionProfilesSource = 'nutritionProfilesUse.csv'

    nutritionProfiles = getData.getData(nutritionProfilesSource)

    nutritionProfilesUpdate = []

    for profile in nutritionProfiles:

        profileIn = []

        for nutrient in profile:

            if nutrient == '0': profileIn.append(0.001)

            else: profileIn.append(nutrient)

        nutritionProfilesUpdate.append(profileIn)

    nutritionProfiles = nutritionProfilesUpdate

    selectedProfile = 1


    relevantNutrients = [1,1,1,1,0, 0,0,0,0,0 ,0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0,0,0,0,0, 0]

    user = input('\n1 - Check products\n2 - Input product\n3 - Check/change nutrition profiles\n4 - Check/change relevant nutrients\n6 - Generate Diet\n0 - Close\nEnter: ')


    while user != '0':

        

        print ('')

        if user == '1': #---------------------------------------------------list products----------------------------------------------

            for product in range(len(productData)): print (productData[product])

        elif user == '2': #-------------------------------------------------Input product----------------------------------------------

            newProduct = []

            for productInput in range(len(productData[0])):

                newProduct.append(input(productData[0][productInput]+ ': '))

            print ("\nEntered '" + newProduct[0] + "'")

            getData.appendRecord(productDataSource, newProduct)

            productData = getData.getData(productDataSource)

        elif user == '3': #------------------------------------------check/change nutrition profiles-------------------------------------

            print ('Profile ' + nutritionProfiles[selectedProfile][0] + ' is selected\n')

            for entry in range(len(nutritionProfiles[0])):

                if entry == 0 or relevantNutrients[entry-1] == 1: 
                    print (nutritionProfiles[0][entry] + ': ' + str(nutritionProfiles[selectedProfile][entry]))

            user2 = input('1 - Change selected profile\n2 - Edit profile\n3 - Enter new profile\n0 - Back')

            while user2 != '0':

                if user2 == '1':

                    selectedProfile = getPosition(input('Select profile: '), nutritionProfiles)

                elif user2 == '2':

                    profilePosition = getPosition(input('Edit profile with name:'), nutritionProfiles)

                    if profilePosition != 0:

                        for profileInput in range(len(nutritionProfiles[0])):

                            #print (profileInput, relevantNutrients[profileInput-1])

                            if (profileInput == 0) or (relevantNutrients[profileInput-1] == 1):

                                #print (profileInput, relevantNutrients[profileInput])
                                
                                userIn = input(nutritionProfiles[0][profileInput] + '(Currently: ' + str(nutritionProfiles[profilePosition][profileInput]) + ') new: ')

                                if userIn != '': nutritionProfiles[profilePosition][profileInput] = userIn

                        getData.updateTable(nutritionProfilesSource, nutritionProfiles)

                    else: print ('Profile not found') 
                    
                elif user2 == '3':

                    newProfile = []

                    for profileInput in range(len(nutritionProfiles[0])):

                        newProfile.append(input(nutritionProfiles[0][profileInput] + ': '))

                    getData.appendRecord(nutritionProfilesSource, newProfile)

                    nutritionProfiles = getData.getData(nutritionProfilesSource)

                user2 = input('1 - Change selected profile\n2 - Edit profile\n3 - Enter new profile\n0 - Back')

        elif user == '4':

            for nutrient in range(46):

                if relevantNutrients[nutrient] == 1:

                    print (nutritionProfiles[0][nutrient+1])

            user2 = input('\n1 - Change\n0 - Back')

            while user2 != '0':

                if user2 == '1':

                    

                    for nutrient in range(46):

                        relevantNutrients[nutrient] = int(input(nutritionProfiles[0][nutrient+1]))

                    print ('\nNew relevant nutrients:\n')

                    for nutrient in range(46):

                        if relevantNutrients[nutrient] == 1:

                            print (nutritionProfiles[0][nutrient+1])


                user2 = input('\n1 - Change\n0 - Back')

            

        elif user == '6': # -----------------------------------------generate diet-----------------------------------------------------

            productDataPure = [] #strips column names, product names and portion sizes

            for product in productData[1:]:

                #productDataPure.append(product[1:])

                productDataIn = []

                for nutrient in range(len(product)-1):

                    productDataIn.append(float(product[nutrient+1])/10.0)

                productDataPure.append(productDataIn)

            nutritionProfilePure = list(map(float, nutritionProfiles[selectedProfile][1:])) # strips profile names converts to floats

            bestDiet, bestNutrients, positions = generateDiet.guessOptimal(50000, productDataPure, nutritionProfilePure, True, 10, relevantNutrients) #first paremeter is amount of guesses, 50000 usually gives near best results but the more the better

            #bestDiet.sort(key=lambda x: x[1], reverse = True)

            print ('')

            for productQuantity in range(len(bestDiet)):

                if bestDiet[productQuantity][1] > 0: print (str(bestDiet[productQuantity][1]) + '0 grams of ' + productData[positions[productQuantity]+1][0])

            print ('')

            for nutrient in range(len(nutritionProfiles[0])-1):

                if relevantNutrients[nutrient] == 1: print (nutritionProfiles[0][nutrient+1] + ': ' + str(bestNutrients[nutrient]) + ' (Optimal: ' + str(nutritionProfiles[selectedProfile][nutrient+1] + ')'))
                       
        user = input('1 - Check products\n2 - Input product\n3 - Check/change nutrition profiles\n4 - Check/change relevant nutrients\n6 - Generate Diet\n0 - Close\nEnter: ')

if __name__ == "__main__":
    
    main()
          
