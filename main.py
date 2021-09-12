file = open('testFile_With_Scores.vcf',mode='r')
vcfContents = file.readlines()[5:] # Ignore first 5 lines
file.close()

import re
for vcfContent in vcfContents:
  vcfContent = vcfContent.replace(',', '","')
  csvContent = re.sub(r'\t', ',', vcfContent)
  with open("testFile_With_Scores.csv", "a") as csvFile:
    csvFile.write(csvContent)