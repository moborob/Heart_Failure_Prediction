print("   ")
print("Greetings Doctor. Thank you for choosing Anova's Service")
print("   ")
print('Anova is a product that predicts the likelihood of a patient having heart disease, powered by Machine Learning Decision Trees')
print("   ")
print("   ")
print("Does the patient have an upsloping ST_slope? Please enter either yes or no")
ST_slope = input()

if ST_slope == 'yes':
    print('Does the patient suffer from exercise Agnina? Please enter either yes or no')
    exer_agnina = input()
    if exer_agnina == 'yes':
        print('Does the patient have Asymptomatic Chest Pain? Please enter either yes or no')
        ASY = input()
        if ASY == 'yes':
            print("what is the patient's Oldpeak?")
            oldpeak = int(input())
            if oldpeak > 0.05:
                print('the patient likely has heart disease')
            else:
                print('the machine learning algorithm cannot make an accurate prediction')
        elif ASY == 'no':
            print("the paitent likely doesn't have heart disease")
        else:
            print('wrong input!')
    elif exer_agnina == 'no':
        print("what is the patient's Oldpeak?")
        oldpeak = int(input())
        if oldpeak > 2.35:
            print('the patient likely has heart disease but data sample was quite small to make this prediction')
        else:
            print('Does the patient have Asymptomatic Chest Pain? Please enter either yes or no')
            ASY = input()
            if ASY == 'yes':
                print("the patient likely doesn't have heart disease with a possible chance of still having it")
            elif ASY == 'no':
                print("the patient likely doesn't have heart disease with little chance of them having it")
            else:
                print('wrong input!')
    else:
        print('wrong input!')
elif ST_slope == 'no':
    print('Does the patient have Asymptomatic Chest Pain? Please enter either yes or no')
    ASY = input()
    if ASY == 'yes':
        print("What is the patient's sex? male or female?")
        sex = input()
        if sex == 'male':
            print("the patient very likely has a heart disease present with little chance of not having it")
        elif sex == 'female':
            print("the patient very likely has a heart disease present with some chance of not having it")
        else:
            print('wrong input!')
    elif ASY == 'no':
        print("What is the patient's sex? male or female?")
        sex = input()
        if sex == 'male':
            print("What is the patient's Max Heart Rate?")
            MaxHR = int(input())
            if MaxHR > 136.5:
                print("the patient likely has a heart disease present. Confidence isn't as high")
            else:
                print("the patient vey likely has a heart disease present. Confidence of this decision is very high")
        elif sex == 'female':
            print("the patient likely doesn't have a heart disease present")
    else:
        print('wrong input!')
else:
    print('wrong input!')