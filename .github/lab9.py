#Programmers: Callie Walker, Lesdy Galvez, Hanna Magan
#Course: CS151, Dr. Rajeev
#Date: 11/18/21
#Lab Number: 9
#Program Inputs: The file with the data of the movies
#Program Outputs: A new file with the data of the movies and a row of their profit

DATE = 0
TITLE = 1
BUDGET_BOX = 2
OFFICE_GROSS = 3

def read_file(filename):
    data = []
    try:
        f = open(filename, 'r')
        count = 0
        for line in filename:
            try:
                count +=1
                line_data = line.split(",")
                line_data[DATE] = line_data[DATE]
                line_data[TITLE] = line_data[TITLE]
                line_data[BUDGET_BOX] = float(line_data[BUDGET_BOX])
                line_data[OFFICE_GROSS] = float(line_data[OFFICE_GROSS])

                data.append(line_data)
            except ValueError:
                print("Error, skipping line ", count, "for bad value.")
        f.close()
    except FileNotFoundError:
        print("Error File:", filename, "not found.")
    return data
#This function reads the data of the old file and appends the data to an output file
def create_output(oldFile, newFile):
    data = read_file(oldFile)
    output = open(newFile, 'w')
    for line in newFile:
        newFile.append(data)
    output.close()
#This function creates a new line for profit and appends the line to the new output file
def movie_profit(data, newfile):
    MOVIE_PROFIT = 4
    profit = 0
    newOutput = open(newfile, 'a')
    for row in data:
        profit = data[row][OFFICE_GROSS]- data[row][BUDGET_BOX]
    for line in data:
        newline = line
        newline = newline[MOVIE_PROFIT]
        #maybe put this in main
        #newOutput.append(newline)

    return profit

def main():
    #need to append data to outputfile first
    #maybe use the ospath 
    movieFile = open("movies.csv", 'r')
    outputMoviesFile = open("movies_output", 'w')
    #create_output(read_file(movieFile), outputMoviesFile)
    newColumn = movie_profit(read_file(movieFile), outputMoviesFile)
    print(outputMoviesFile)
main()