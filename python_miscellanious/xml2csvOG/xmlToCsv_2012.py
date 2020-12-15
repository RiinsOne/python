"""
def xml2csv(inputFile,outputFile,elemName,ns,columnsToExtract):
   outFile=open(outputFile,'w')
   writer=csv.DictWriter(outFile,columnsToExtract,extrasaction='ignore',restval='')

   # Write Header to CSV file
   writer.writerow(columnsToExtract)

   #Sree -Used iterparse, so that only partial xml is in memory and after usage every element is cleared out of memory.
   for  event,rec in etree.iterparse(inputFile, tag="%s%s" %(ns,elemName)):
      row=dict()
      for child in rec:
         row[child.tag[len(ns):]]=child.text.strip()
      rec.clear()
      writer.writerow(row)
      outFile.close()
"""

#
