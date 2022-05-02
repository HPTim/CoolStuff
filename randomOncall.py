#Oncall Random Generator
import random

teamList = ['Nupur','Andrew','Jeff', 'Tim', 'Martins', 'Joe']
def ruinNYD(thxOncall, id4Oncall, labOncall):
    print("New Year Oncall Selection")
    nydList = teamList
    #print("team list: " + nydList)
    nydList.append('Andrew')
    nydList.append('Ben')
    nydList.append('Tim')
    print("nyd list with pref: ")
    print(nydList)
    #print("removals")
    print("remove " +thxOncall)
    print("remove " +id4Oncall)
    nydList.remove(thxOncall)
    nydList.remove(id4Oncall)
    nydList.remove(labOncall)
    print(nydList)
    nydOncall = random.choice(nydList)
    print("New Years Day: "+ nydOncall)
    print("-----------------------------")
    return(nydOncall)
def ruinMemDay(id4Oncall, thxOncall, nydOncall, xmasOncall, labOncall):
    print("Memorial Day Oncall Selection")
    memList = teamList
    #print("team List: " + memList)
    #memList.append('Martins')
    #memList.append('Martins') 
    print("Memorial list with Pref: ")
    print(memList)
    print("remove " + nydOncall)
    print("remove " + id4Oncall)
    print("remove " + thxOncall)
    memList.remove(nydOncall)
    memList.remove(id4Oncall)
    memList.remove(thxOncall)
    memList.remove(xmasOncall)
    memList.remove(labOncall)
    print(memList)
    memOncall = random.choice(memList)
    print("Memorial Day: "+ memOncall)
    print("-----------------------------")
    return(memOncall)
def ruinID4(labOncall, thxOncall):
    print("Independance Day Oncall Selection")
    id4List = teamList
    #print("Team list: " + id4List)
    id4List.append('Martins')
    id4List.append('Andrew')
    id4List.append('Andrew')
    print("ID4 list with pref: ")
    id4List.remove(labOncall)
    id4List.remove(thxOncall)
    print(id4List)
    id4Oncall = random.choice(id4List)
    print("Independance Day: "+ id4Oncall)
    print("-----------------------------")
    return(id4Oncall)
def ruinLabday():
    print("Labor Day Oncall Selection")
    labList = teamList
    #print("Team List: " + labList)
    labList.append('Joe')
    labList.append('Joe')
    labList.append('Martins')
    labList.append('Martins')
    labList.append('Ben')
    labList.append('Ben')
    print("Labor Day List wit Pref: ")
    print(labList)
    '''print("remove " + nydOncall)
    print("remove " + memOncall)
    print("remove " + id4Oncall)
    print("remove " + thxOncall)
    labList.remove(nydOncall)
    labList.remove(memOncall)
    labList.remove(id4Oncall)
    labList.remove(thxOncall)'''
    #print(labList)
    labOncall = random.choice(labList)
    print("Labor Day: "+ labOncall)
    print("-----------------------------")
    return(labOncall)
def ruinThx(labOncall):
    print("Thanksgiving Day Oncall Selection")
    thxList = teamList
    #print("team list: " + thxList)
    thxList.append('Tim')
    thxList.append('Tim')
    thxList.append('Jeff')
    thxList.append('Jeff')
    print("Thanksgiving list with Pref: ")
    print(thxList)
    print("remove " + labOncall)
    thxList.remove(labOncall)
    print(thxList)
    thxOncall = random.choice(thxList)
    print("Thanksgiving Day: "+ thxOncall)
    print("-----------------------------")
    return(thxOncall)
def ruinXmas(id4Oncall, thxOncall, nydOncall, labOncall):
    print("Christmas Day Oncall Selection")
    xmasList = teamList
    #print("Team List: " + xmasList)
    xmasList.append('Joe')
    xmasList.append('Jeff')
    print("Xmas list with Pref: ")
    print(xmasList)
    print("remove " + id4Oncall)
    print("remove " + thxOncall)
    print("remove " + nydOncall)
    #print("remove " + memOncall)
    print("remove " + labOncall)
    xmasList.remove(id4Oncall)
    xmasList.remove(thxOncall)
    xmasList.remove(nydOncall)
    #xmasList.remove(memOncall)
    xmasList.remove(labOncall)
    print("Xmas List with Pref: ")
    print(xmasList)
    xmasOncall = random.choice(xmasList)
    print("Christmas Day: "+ xmasOncall)
    print("-----------------------------")
    return(xmasOncall)


print('Holiday Order: ' + 'Labor Day, Thanksgiving, ID4, NYD, Xmas, Memorial')
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins', 'Ben']
labOncall = ruinLabday()
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins', 'Ben']
thxOncall = ruinThx(labOncall)
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins', 'Ben']
id4Oncall = ruinID4(labOncall, thxOncall)
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins', 'Ben']
nydOncall = ruinNYD(labOncall, thxOncall, id4Oncall)
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins', 'Ben']
xmasOncall = ruinXmas(labOncall, thxOncall, id4Oncall, nydOncall)
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins', 'Ben']
memOncall = ruinMemDay(labOncall, thxOncall, id4Oncall, nydOncall, xmasOncall)
print('---oncall list---')
print('Labor Day: ' + labOncall)
print('Thanksgiving: ' +thxOncall)
print('Independence Day: ' +id4Oncall)
print('NewYears Day: ' + nydOncall)
print('Xmas: '+ xmasOncall)
print('Memorial Day: '+memOncall)

'''
id4Oncall = ruinID4()
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins']
thxOncall = ruinThx(id4Oncall)

teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins']
nydOncall = ruinNYD(id4Oncall, thxOncall)

teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins']
memOncall = ruinMemDay(id4Oncall, thxOncall, nydOncall)

teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins']
labOncall = ruinLabday(id4Oncall, thxOncall, nydOncall, memOncall)
teamList = ['Nupur','Andrew','Joe','Jeff', 'Tim', 'Martins']
xmasOncall = ruinXmas(id4Oncall, thxOncall, nydOncall, memOncall, labOncall)
'''
