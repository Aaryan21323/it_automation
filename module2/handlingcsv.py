import csv # csv stands for comma separated values....

def using_csv_reader():
    f=open("filename.txt")
    csv_f=csv.reader(f) #csv reader
    for row in csv_f:
        name,phone,role=row #unpacking 
        print("Name:{},Phone:{},Role:{}".format(name,phone,role)) # using format to format strings
    f.close()

def using_csv_writer():
    hosts=[["workstation.local","192.168.2.1"],["webserver.cloud","192,168,2,2"]] # making list of list
    with open('host.csv',"w") as hosts_csv: # using with open caues the file to be automatically closed
        writer=csv.writer(hosts_csv) #initializing writer
        writer.writerows(hosts) # wrting each row one at a time

def using_DictReader():
    with open("software.csv") as software:
        reader=csv.DictReader(software) # Dict Reader the csv as a key value pair
        for row in reader:
            print(("{} has { users.}").format(row["name"],row["users"]))

# we can also use DictWriter to write to a file but we need keys for that ... ( you know what i mean)