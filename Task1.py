#Libraries
import csv
import requests
import time

#URL to get the POI data in a specified radius around the mentioned point
#The unit of radius is meters
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=30.1575,71.5249&radius=150000&type=point_of_interest&key=AIzaSyAQbBkAi3FghRWDkFbRnMDLLH4mXPRWG38'

#Function to write the file
def write_file():
    csvfile =open('google_maps.csv','w', newline="") #open the file
    writer = csv.writer(csvfile, delimiter=',') #Use to return the writing object of the csv file
    writer.writerow(["name","lat","long"]) #Calling the function writing row of the object writer to write the first row of the CSV file mentioning the columns
    response = requests.get(url=url).json()#Sending the GET request to get data
    for obj in response['results']:# Get the results from the first page of the search gives up to 20 results 
        writer.writerow ([obj['name'],obj['geometry']['location']['lat'],obj['geometry']['location']['lng']])
        print([obj['name']])
    print("...")#To Check if program is working
    time.sleep(6)#Sleep time to slow the program down so that it doesn't go ahead without next page token key
    print ('next_page_token' in response)
    time.sleep(6)
    while 'next_page_token' in response: #Using while loop to Get more results 
        URL = url + '&pagetoken=' + response['next_page_token']
        time.sleep(5)
        response = requests.get(url=URL).json()
        for obj in response['results']:
            writer.writerow ([obj['name'],obj['geometry']['location']['lat'],obj['geometry']['location']['lng']])
            print([obj['name']])
        break #Using break so the loop ends after second page
    else:
        print(response)
#Main Function
if __name__ == '__main__':
    write_file()