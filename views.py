
import sys
import csv
import re
def add(i):
    with open('data.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(i)
#add(["Ashwin","8363","good@gmail","No.21 sri Ganesh Nagr"])
#add(["Ashwin","4556","good@gmail","No.21 sri Ganesh Nagr"])

def view():
    data=[]
    with open("data.csv") as file:
        reader=csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data
#view()

def remove(i):

    def save(j):
        with open("data.csv","w",newline="") as file:
            writer=csv.writer(file)
            writer.writerows(j)
    new_list = []
    phone = i
    with open('data.csv',"r") as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == phone:
                    new_list.remove(row)
    save(new_list)

remove("8363")
view()
    
def update(i):
    def update_newlist(j):
            with open('data.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(j)
    new_list = []
    phone = i[0]    
    with open('data.csv', 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == phone:
                    name=i[1]
                    phone= i[2]
                    email=i[3]
                    address=i[4]
                    data=[name,phone,email,address]
                    index=new_list.index(row)
                    new_list[index]=data
    update_newlist(new_list)
def search(i):
        data = []
        telephone=i
        with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
               for element in row:
                    if element==telephone:
                        data.append(row)
        print(data)
        return data
search("123")