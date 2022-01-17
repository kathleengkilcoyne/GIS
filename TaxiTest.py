def CartoTaxiTestPandas():
    #This is an exercise based on an employment test for backend developers
    #The test and data for the test can be found here: https://gist.github.com/jorgesancha/2a8027e5a89a2ea1693d63a45afdd8b6

    #Import libraries
    import pandas as pd

    #Complete test with Pandas
    #CSV to Data Frame
    readtaxi = pd.read_csv('taxi.csv', header=0)
    #count the rows. shape method returns tuple w df dimension like so: (rows, columns)
    countrows = (readtaxi.shape)[0]
    #find sum of "tip_amount" column. Divide by # of rows for avg.
    tipmean = (readtaxi["tip_amount"].sum())/(countrows)
    #testing to see how mean method compares in pandas
    tipmeanAGAIN = readtaxi["tip_amount"].mean()
    #print results
    print(countrows)
    print(tipmean)
    print(tipmeanAGAIN)

def TaxitestPandas():
    # This is an exercise using taxi data found on https://gist.github.com/jorgesancha/2a8027e5a89a2ea1693d63a45afdd8b6
     # Import libraries
    import pandas as pd
    # CSV to Data Frame
    readtaxi = pd.read_csv('taxi.csv', header=0)
     # Change display settings to see all columns. Otherwise columns will be truncated
    pd.set_option('display.max_columns', None)
    #Display first five rows in table
    print(readtaxi.head())

def CartoTaxiTestNumpy():
    #complete same test but with Numpy. Spoiler alert: it takes longer than using Pandas w my current program
    #Import libraries
    import numpy as np
    #generate Numpy array from csv. Skip header for accurate calculations
    taxiarray = np.genfromtxt("taxi.csv", delimiter=",", skip_header=1)

    # count the rows. shape method returns tuple w df dimension like so: (rows, columns)
    arrayrow = (np.shape(taxiarray)[0])

    #The commented out line below will eventually test if indexing the array will make the program run faster
    #arrayrowindex = np.index

    #slice out tip_amount column and store in variable. Index found w Pandas head function above
    tip_array = np.array(taxiarray[:, 15])
    #find sum of column and divide by # of rows
    meantiparray = np.sum(tip_array)/arrayrow
    #print results
    print(arrayrow)
    print(meantiparray)

#CartoTaxiTestNumpy() results:
#10906858 (rows)
#1.750663115812088 (mean)

#CartoTaxiTestPandas() results:
#10906858 (rows)
#1.750663115812088 (mean)

#Question: Is using Pandas "vanilla python"? What about Numpy?
#Can I do this without importing any libraries?
