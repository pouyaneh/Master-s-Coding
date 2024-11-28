def fieldDictBuild():
    fieldDict = dict.fromkeys([0, 1, 2, 3, 11, 12, 13, 14])
    fieldDict[0] = {'bmi':(862,864),'weight':(832,841)}
    fieldDict[1] = {'bmi':(725, 730), 'weight':(686, 695)}
    fieldDict[2] = {'bmi':(933, 936), 'weight':(822, 831)}
    fieldDict[3] = {'bmi':(854, 857), 'weight':(745, 754)}
    fieldDict[11] = {'bmi':(1533,1536),'weight':(1475,1484)}
    fieldDict[12] = {'bmi':(1644,1647),'weight':(1449,1458)}
    fieldDict[13] = {'bmi':(2192,2195),'weight':(1953,1962)}
    fieldDict[14] = {'bmi':(2247,2250),'weight':(2007,2016)}
    return fieldDict

'''
def convertBMI(bmiString, shortYear):
    bmi = 0
    if shortYear == 0 and bmiString != '999':
        bmi = .1*float(bmiString)
    if shortYear == 1 and bmiString != '999999':
        bmi = .0001*float(bmiString)
    if 2 <= shortYear <= 10 and bmiString != '9999':
        bmi = .01*float(bmiString)
    if shortYear > 10 and bmiString != ' ':
        bmi = .01*float(bmiString)
    #print(bmiString, bmi)
    return bmi
'''
def convertBMI(bmiString, shortYear):
    bmi = 0
    bmiString = bmiString.strip()  # Remove any leading or trailing spaces
    if shortYear == 0 and bmiString != '999':
        bmi = .1 * float(bmiString)
    elif shortYear == 1 and bmiString != '999999':
        bmi = .0001 * float(bmiString)
    elif 2 <= shortYear <= 10 and bmiString != '9999':
        bmi = .01 * float(bmiString)
    elif shortYear > 10 and bmiString != '':
        bmi = .01 * float(bmiString)
    #print(bmiString, bmi)
    return bmi