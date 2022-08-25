# initializing the list
itemsList = [25, 2, 3, 57, 38, 41]


def split_array(listItems):
    listString = []
    lisIntegers = []
    d = []
    # looping throuh the original list and creating the a new list with string values
    for item in listItems:
        listString.append(str(item).split())

    for string in listString:
        d.append(*string)

    for a in d:
        for i in a:
            lisIntegers.append(int(i))

    return lisIntegers


def most_frequent(arrayItems):
    occurrence = {}

    for num in arrayItems:
        curr_frequency = arrayItems.count(arrayItems[num])

        occurrence['number ' +  str(arrayItems[num]) + 'occurence '] = curr_frequency

    return occurrence


items = split_array(itemsList)

print(items)
print(most_frequent(items))
