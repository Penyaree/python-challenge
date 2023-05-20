#import os and csv
import os
import csv
from pathlib import Path

# Open and read the csv file
budget_data = Path("C:/Users/Penny/Documents/Data Analytics Bootcamp/Module Challenge/Starter_Code(Python)/Starter_Code/PyBank/Resources/budget_data.csv")

with open(budget_data,'r')as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header=next(csvreader)
    print(f"header:{csv_header}")

    #Calculate net amount of profit and loss
    P =[]
    months=[]
    
    #read each row of data afetr header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    #Calculate revenue change
    revenue_change=[]
    for x in range(1,len(P)):
        revenue_change.append((int(P[x]-int(P[x-1]))))

    #Calculate average revenue change
    revenue_average_change=sum(revenue_change)/len(revenue_change)
    revenue_average=round(revenue_average_change,2)

    #Calculate total length of months
    total_months=len(months)

    #Greatest increase in revenue
    greatest_increase=max(revenue_change)

    #Greatest decrease in revenue
    greatest_decrease=min(revenue_change)

    #print result
    print("Financial Analysis")
    print(".......................................................")
    print("total_months :"+str(total_months))
    print("Total:"+"$"+str(sum(P)))
    print("Average change:"+"$"+str(revenue_average))
    print("Greatest Increase in Profit"+str(months[revenue_change.index(max(revenue_change))+1])+" "+"($"+str(greatest_increase)+")")
    print("Greatest Decrease in Profit"+str(months[revenue_change.index(min(revenue_change))+1])+" "+"($"+str(greatest_decrease)+")")



