# This is an exercise based on an employment test for backend developers
#The test and data for the test can be found here:
#https://gist.github.com/javitonino/7f6f1183163d09b4c1817470e906ac4a
def downloadfromwebsite():
    #import requests library to download data also import psycopg2 and GDAL to connect to Postgres/PostGIS later on
    import psycopg2 as psy
    import requests
    import GDAL
    #links in array so for loop can be used to 1) download data 2) split file names and append to new array
    linkarray= ('https://www.ine.es/censos2011_datos/indicadores_seccen_rejilla.xls',
                'https://www.ine.es/censos2011_datos/indicadores_seccion_censal_csv.zip',
                'https://www.ine.es/censos2011_datos/cartografia_censo2011_nacional.zip')
    #Create array for file names to be appended to
    namearray = ()
    #for loop to ease process if additional data sources are found
    for i in range(len(linkarray)):
        #1) download data
        req = requests.get(linkarray[i])
        #2) split file names and append to new array (for ease of access in next step)
        namearray += (((linkarray[i]).split('/')[-1]),)
        #i should work in the nested with statement bc there are now as many objects in name array as there are in link array
        #nested with statement should keep the names of the files and the links in sync w each other
        with open(namearray[i], 'wb') as output_file:
            output_file.write(req.content)
        print('Downloading Completed')
    #psycop2g library? to prepare the data for Postgres
    #https://www.dataquest.io/blog/loading-data-into-postgres/
    #unzip first?
    #https://www.geeksforgeeks.org/working-zip-files-python/
    #Connect to DB
    conn = psycopg2.connect("host=localhost dbname=Carto_Test_DB user=postgres password=#JonGr0ce port=5433")

    print(conn)

def importPostGres():
    import psycopg2 as psy
    conn = psy.connect("host=localhost dbname=Carto_Test_DB user=postgres ")
    curs = conn.cursor()

importPostGres()



