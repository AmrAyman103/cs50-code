import csv
import sys


def main():

    check_correck_arg()
    data=[]
    try:
        with open(sys.argv[1]) as csvfile:
            reader =csv.DictReader(csvfile)
            for row in reader:
               data.append(row)
    except FileNotFoundError:
        sys.exit("Colud not read CSV file")

    output=[]
    for row in data:
       program=sel_program(row["Program_level"])
       date =sel_age(row["birth_year"])
       output.append({"name":row["name"],"program":program,"date":date})

    with open (sys.argv[2],"w") as file:
         writer = csv.DictWriter(file,fieldnames=["name","program","date"])
         writer.writerow({"name":"name","program":"program","date":"date"})
         for row in output:
             writer.writerow({"name":row["name"],"program":row["program"],"date":row["date"]})



def check_correck_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if  ".csv" not in sys.argv[1] or  ".csv" not in sys.argv[2] :
       sys.exit("Not a CSV file")


def sel_program(wight):
    if wight in ["over_wight_|","over_wight_||","over_wight_||"]:
        return "Program_2"
    elif wight in ["fit"]:
        return "Program_1"
    elif wight in ["Excessive obesity_|","Excessive obesity_||"]:
        return "Program_3"
    elif wight in ["Excessive obesity_|||"]:
        return "Program_4"

    else:
        return "No program"


def sel_age(year):
    age =2023-int(year)
    return str(age) +" year"


if __name__ == "__main__":
    main()
