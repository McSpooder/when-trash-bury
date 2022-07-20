import requests #for fetching web data
import re #for make a regular expression to clean html tags



res = requests.get("https://www.bury.gov.uk/index.aspx?articleid=10493&RId=649929&pc=BL9%208PB&hn=67&sr=Swinton%20Crescent&hn2=67S")

for line in res.text.split("\n"):
    if "grey bin" in line:
        col_str = line
        break

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
numbers = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
years = ["2020", "2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]

grey_b_date = "" #grey bin date
brown_b_date = "" #brown/red bin date
green_b_date = "" #green bin date
blue_b_date = "" #blue bin date

def parse_line(line):
    line = line.replace(".", "")
    line = re.sub('<[^<]+?>', '', line)
    for word in line.split(" "):
        if word in days_of_week:
            day = word
        if word in numbers:
            num = word
        if word in months:
            month = word
        if word in years:
            year = word
    return day + " " + num + " " + month + " " + year

for line in col_str.split("</li><li>"):
    day = ""
    num = ""
    month = ""
    year = ""
    if "grey bin" in line:
        grey_b_date = parse_line(line)
    elif "brown bin" in line:
        brown_b_date = parse_line(line)
    elif "green bin" in line:
        green_b_date = parse_line(line)
    elif "blue bin" in line:
        blue_b_date = parse_line(line)

print("grey bin: ", grey_b_date)
print("brown bin: ", brown_b_date)
print("green bin: ", green_b_date)
print ("blue bin: ", blue_b_date)



