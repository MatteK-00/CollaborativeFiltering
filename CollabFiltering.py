__author__ = 'matteo'

import json
from pprint import pprint

a = [[['A'],['B','C'],['D']],['E']]


#with open('/home/matteo/Desktop/DataMining/yelp_review_parsed.json') as data_file:
#    data = json.load(data_file)


g = open('/home/matteo/Desktop/DataMining/yelp_review_parsed.json','r')

for jsonline in g:
  data = json.loads(jsonline)

print(data)