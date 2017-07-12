#Mahataz Khandaker
#My goal in this program was to:
#make sure that job listings do not show twice as they do in the dataset
#exclude 18 unnecessary columns 
#add a salary range column
#only select jobs that have an annual salary

import codecs
def jobs_conversion():
    source = "NYC_Jobs.csv"
    target = "New_nycjobs.csv"
    salary_ranges = []
    job_id = []
    # This array contains the indexes that represent job id, agency, number of positions, civil service title,
    # salary range from, salary range to , salary frequency.
    my_column_indices = [0, 1, 3, 5, 8, 9, 10]
    try:
        src = codecs.open(source, "r", encoding = 'utf-8')
    except Exception as e:
        print("There was an issue with opening the file")
        print(e)
    else:
        t = codecs.open(target, "w", 'utf-8')
        records_processed = 0
        records_written = 0
        look = 0
        salary_from_index = 8
        salary_to_index = 9
        salary_frequency_index = 10
        salary_range = 0
        #This for loop looks for the appropriate fields using my_columnn_indices and calculates the salary range, maximum start salary,
        #and minimum start salary.
        for row in src:
            d = row.rstrip("\n")
            output = ''
            data = d.split(",")
            if data[10] == "Annual" or look == 0:
                records_processed += 1
                if (data[my_column_indices[0]] not in job_id):
                    job_id.append(data[my_column_indices[0]])
                    for i in range(7):
                        output += data[my_column_indices[i]]
                        output += ","
                    if look == 0:
                        output += "Salary Range"
                        look += 1
                    else:
                        salary_range = int(data[salary_to_index]) - int(data[salary_from_index])
                        salary_ranges.append(salary_range)
                        output += str(salary_range)
                    t.write(output + "\n")
                    records_written += 1
                    
        src.close()
        t.close()

jobs_conversion()
                

