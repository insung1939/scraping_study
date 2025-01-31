import csv

def save_to_file(file_name, jobs_db):
    file = open(f"{file_name}.csv", "w")
    writter = csv.writer(file)
    writter.writerow(["Title", "Company", "Position", "Location", "Link"])  # header
    for job in jobs_db:
        writter.writerow(job.values())

    file.close()