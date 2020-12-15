import xml.etree.ElementTree as ET
import csv

tree = ET.parse('15216APR19CKP.XML')
root = tree.getroot()

f = open('15216APRCKP.csv', 'w')
csvwriter = csv.writer(f)
head = ['SubHost', 'FlightNumber', 'Surname', 'Firstname']
csvwriter.writerow(head)

subHostElem = root.find('./Airline').attrib['SubHost']
flightNumElem = root.find('./Airline/Flight').attrib['FlightNumber']


for i in root:
    print(i.tag, i.attrib)



"""
for airline in root.findall('./Airline'):
    row = []
    subHost = airline.attrib['SubHost']
    row.append(subHost)
    print(row)
"""

# print(root.find('./Airline').attrib['SubHost'])
# csvwriter.writerow(row)
# print(row)

f.close()

# for airline in root.iter('Airline'):
#    print(airline.attrib)

# for paxname in root.iter('Paxname'):
#    print(paxname.attrib)


"""
for i in root.iter('Airline'):
    subHost = i.attrib['SubHost']
    # row.append(subHost)


for i in root.iter('Flight'):
    flightNum = i.attrib['FlightNumber']
    # row.append(flightNum)
"""

#
