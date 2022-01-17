# This is an exercise based on an employment test for backend developers
#The test and data for the test can be found here:
#https://gist.github.com/javitonino/7f6f1183163d09b4c1817470e906ac4a
def downloadfromwebsite():
    #import requests library to download data
    #also import psycopg2 and GDAL to connect to Postgres/PostGIS later on
    #still deciding if I even need psycopg2
    import psycopg2 as psy
    import requests
    from zipfile import ZipFile
    import numpy as np
    #import GDAL
    #links in array so for loop can be used to 1) download data 2) split file names and append to new array
    linkarray= ['https://www.ine.es/censos2011_datos/indicadores_seccion_censal_csv.zip',
                'https://www.ine.es/censos2011_datos/cartografia_censo2011_nacional.zip',
                'https://www.ine.es/censos2011_datos/indicadores_seccen_rejilla.xls',]
    #Create array for file names to be appended to
    namearray = []
    #for loop to ease process if additional data sources are found
    for i in range(len(linkarray)):

        #1) split file names and append to new array (for ease of access in next step)
        namearray += [(linkarray[i]).split('/')[-1],]


        #2) access data
        req = requests.get(linkarray[i])

        #3) write to file
        #iteration should work in the nested with statement bc there are now as many objects in name array as there are in link array
        #nested with statement should keep the names of the files and the links in sync w each other
        with open(namearray[i], 'wb') as output_file:
            output_file.write(req.content)
        #4) print message to see how program is going
        print('Downloading Completed')
    print(namearray)

    #psycop2g library? to prepare the data for Postgres
    #https://www.dataquest.io/blog/loading-data-into-postgres/
    #unzip first?
    #https://www.geeksforgeeks.org/working-zip-files-python/
    #If file extension is .zip un
    #create empty tuple to store the lists of files within each zipfile
    ziptruerange = []
    for i in range(len(namearray)):
        extension = ((namearray[i]).split('.')[-1])
        if extension == 'zip':
            ziptruerange += [namearray[i], ]
            print('yes')
        else:
            print('no')
    print(ziptruerange)
    print('ziptruerange: ')
    print(len(ziptruerange))
    filesinzip = []
    filesinzipall = []
    for i in range(len(ziptruerange)):
        with ZipFile(ziptruerange[i], 'r') as zipObj:
            filesinzip += zipObj.namelist()
            filesinzipall += [filesinzip, ]
            #reset list to hold next list
            filesinzip = []
            # Extract all the contents of zip file in current directory
            zipObj.extractall()
    print(filesinzipall)
    print(filesinzipall[1])
    print(filesinzipall[0])
    #Connect to DB
    #conn = psycopg2.connect("host=localhost dbname=Carto_Test_DB user=postgres password=#JonGr0ce port=5433")

    #print(conn)
#maybe use a function w parameters to
def importPostGres(filename):
    import psycopg2 as psy
    import GDAL
    conn = psy.connect("host=localhost dbname=Carto_Test_DB user=postgres ")
    curs = conn.cursor()

downloadfromwebsite()



