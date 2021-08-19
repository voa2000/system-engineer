# Task 1: Read timezones.csv into memory, count and remove the deprecated time zones
import csv

def process_timezone_file():
    all_data = 0
    deprecated_count = 0
    
    with open('time_zone.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
        for deprecated in data:
            all_data+=1
            if deprecated[4] == "Deprecated" :
                deprecated_count+=1
    return all_data, deprecated_count
            
def print_timezone(all_data, deprecated_count):

    print('--------------------------------------------------------------------------')
    print('Read timezones.csv into memory, count and remove the deprecated time zones')
    print()
    print('Total Number of rows ', all_data,' in csv file.')

    print ('Total Number of rows with the word deprecated is', deprecated_count, ' occurances')
    print('--------------------------------------------------------------------------')

if __name__ == '__main__':
    all_data, deprecated_count = process_timezone_file()
    print_timezone(all_data, deprecated_count)
