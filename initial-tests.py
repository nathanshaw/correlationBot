# read through one data-set
# rescale data 0-1
# read through another data-set
# rescale data 0-1

# calculate simularity between two datasets over x number of points

# if simularity is below a certain threshold return that it is true

def rescaleData(dataList):
    """
    finds the lowest and highest value elements in the list
    Sets those as 0 and 1
    proportionally rescale the other elements
    return the rescaled list

    INPUTS
    ------
    dataList    :   a list of ints or floats which will be rescaled

    OUTPUTS
    -------
    rescaledList:   the rescaled data from dataList from a scale 0-1
    """
    rescaledList = [(v-min(dataList))/max(dataList)for v in dataList ]
    return rescaledList

def calculateSimularity(data1, data2):
    """
    On a scale of 0 to 1 returns how simular the two datasets are

    INPUTS
    -------
    data1       :   list of numbers - ranging from 0 - 1
    data2       :   list of numbers - ranging from 0 - 1

    OUTPUTS
    -------
    simularity :    how similar are the two datasets?
                    0 is totally different 1 is the same data

    """
    total = 0
    if len(data1) != len(data2):
        return 0
    for i, d  in enumerate(data1):
        total += abs(d-data2[i])

    return total/len(data1)

data1 = rescaleData([0,23,43,55])
print('data1 : ', data1)
data2 = rescaleData([0,23,23,55])
print('data2 : ', data2)
print(calculateSimularity(data1,data2))
