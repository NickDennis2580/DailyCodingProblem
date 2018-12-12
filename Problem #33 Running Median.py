def runningAverage(x):
    medians = []
    temp = []
    for i in range(0,len(x)):
        temp.append(x[i])
        temp.sort()
        if i == 0:
            medians.append(x[0])
        elif len(temp) % 2 == 0:
            medians.append((temp[int(len(temp)/2)] + temp[int(len(temp)/2 - 1)])/2)
        else:
            medians.append(temp[int((len(temp)-1)/2)])
            
    return medians
    
x = [2, 1, 5, 7, 2, 0, 5]

print(runningAverage(x))
