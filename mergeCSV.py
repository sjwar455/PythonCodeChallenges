##############################################################################################
#
#
##############################################################################################
import sys
import csv

def merge_csv(files, output):
	
	allFiles = [] 
	fieldnames = set()

	for filePath in files:
		csvFile = csv.DictReader(open(filePath, 'r')) 		# convert csv file to csv.DictReader object
		allFiles.append(csvFile)							# add object to list of csv files 
		fieldnames.update(csvFile.fieldnames)				# update the set of fieldnames 
		
	mergedCSV = csv.DictWriter(open(output, 'w'), fieldnames=fieldnames)
	mergedCSV.writeheader()

	for csvFile in allFiles: 
		for row in csvFile: 
			mergedCSV.writerow(row)

	





def usage(): 
    print("TBD")

if __name__ == "__main__":
	if len(sys.argv) < 3: 
		usage()
		exit()

	n = len(sys.argv)
	files = sys.argv[1:n-1]
	output = sys.argv[n-1]

	merge_csv(files, output)
