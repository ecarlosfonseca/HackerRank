def getMoneySpent(drivers, keyboards, b):

    # Return maximum sum value for two values from two different arrays within given sum range

    bill = []
    for driver in drivers:
        for keyboard in keyboards:
            if driver + keyboard <= b:
                bill.append(driver + keyboard)

    try:
        return max(bill)
    except:
        return -1



if __name__ == '__main__':
    b = 5
    keyboards = [4]
    drivers = [5]
    print(getMoneySpent(drivers, keyboards, b))