file = open('testFile_With_Scores.vcf',mode='r')
vcfContents = file.readlines()[5:] # Ignore first 5 lines
file.close()

import re
for csvContent in vcfContents:
  # Turn all starting characters to "
  csvContent = re.sub(r'^', '"', csvContent)
  # Turn all ending characters to "
  csvContent = re.sub(r'\n', '', csvContent)
  # Turn all ending characters to "
  csvContent = re.sub(r'\t$', '"', csvContent)
  if not re.search(r'"$', csvContent):
    # Turn all ending characters to "
    csvContent = re.sub(r'$', '"', csvContent)
  # Turn all whitespaces to ","
  csvContent = re.sub(r'\t', '","', csvContent)
  with open("testFile_With_Scores.csv", "a") as csvFile:
    csvFile.write(csvContent)
    csvFile.write('\n')