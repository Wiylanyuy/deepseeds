"""Filling recode book"""

from datetime import datetime
# datetime.now.strftime("%Y/%m/%D")

def write_to_file():
    title="RECORD BOOK"
    today_date=datetime.now().strftime("%Y/%m/%D")
    title2="INDIVIDUAL RECORDS"
    learning= input("What have you learned today?")
    user= input("Enter 'continue' or 'exit'")

    with open("recod_book.txt", "w ") as file:
        file.write(title)
        file.write(today_date)
        file.write(title2)
        file.write
        
    