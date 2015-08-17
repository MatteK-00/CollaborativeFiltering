__author__ = 'matteo'
import io, json, csv, datetime


#
# with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/tmpNFvucr', 'r') as f:
#     g = open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/tmpNFvucrParsed.json', 'w')
#     for line in f.readlines():
#         if '"type": "business"' not in line:
#             l = line.replace('"votes": {', '')
#             l = l.replace('}, "user_id":', ', "user_id":')
#             g.write(l)
#         else:
#             g.write(line)
# f.close()
# g.close()
#
# with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/tmpNFvucrParsed.json', 'r') as f:
#     user_key = 0
#     business_key = 0
#     with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/u.user','w') as w1:
#         with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/u.business','w') as w2:
#             wr1 = csv.writer(w1, dialect='excel')
#             wr2 = csv.writer(w2, dialect='excel')
#             for line in f:
#                 data = json.loads(line)
#                 if data['type'] == 'user':
#                     user_key += 1
#                     line = [str(user_key)]
#                     line.append(data['user_id'])
#                     line.append(data['name'].encode('ascii', 'replace'))
#                     line.append(data['average_stars'])
#                     line.append(data['review_count'])
#                     line.append(data['funny'])
#                     line.append(data['useful'])
#                     line.append(data['cool'])
#                     wr1.writerow(line)
#                 elif data['type'] == 'business':
#                     business_key += 1
#                     line = [str(business_key)]
#                     line.append(data['business_id'])
#                     line.append(data['name'].encode('ascii', 'replace'))
#                     line.append(data['city'])
#                     line.append(data['stars'])
#                     line.append(data['review_count'])
#                     line.append(data['open'])
#                     wr2.writerow(line)
#         w1.close()
#         w2.close()
#     f.close()


list_u = []
list_b = []
list_d = []
with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/u.user', 'r') as r1:
    for line in csv.reader(r1, dialect="excel"):
        list_u.append(line)
r1.close()
with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/u.business', 'r') as r2:
    for line in csv.reader(r2, dialect="excel"):
        list_b.append(line)
r2.close()

with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/tmpNFvucrParsed.json', 'r') as f:
    for line in f:
        list_d.append(line)
f.close()
with open('/home/matteo/Desktop/DataMining/yelp_dataset_academic/u.data', 'w') as w3:
    wr3 = csv.writer(w3, dialect='excel')
    for line in list_d:
        review = []
        data = json.loads(line)
        if data['type'] == 'review':
            for l1 in list_u:
                if data['user_id'] in l1:
                    review.append(l1[0])
                    break
            for l2 in list_b:
                if data['business_id'] in l2:
                    review.append(l2[0])
                    break
            if len(review) != 2:
                print 'WARNING review len < 2'
            else:
                review.append(data['stars'])
                review.append(datetime.datetime(int(data['date'][0:4]), int(data['date'][5:7]),int(data['date'][8:10])).strftime('%s'))
                review.append(data['review_id'])
                review.append(data['funny'])
                review.append(data['useful'])
                review.append(data['cool'])
                wr3.writerow(review)




