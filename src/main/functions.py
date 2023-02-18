def importData(path):
    file = open(path, 'r')
    lines = file.readlines()
    final = []
    for line in lines:
        line = line.strip()
        data = line.split(' ')
        data = [float(x) for x in data]
        final.append(data)
    final = convertData(final)
    return final

def convertData(data):
    final = []
    for x in range(len(data[0])):
        a = []
        for d in range(len(data)):
            a.append(data[d][x])
        final.append(a)
    return final
