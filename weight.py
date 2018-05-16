from __future__ import division
import json
import collections
from numpy import median



string1 = 'cookie dough'
string2 = 'Nestle'
string3 = 'Baking Cookie'

entity1 = []
entity2 = []
entity3 = []

entity1values = []
entity2values = []
entity3values = []

entity1name = []
entity2name = []
entity3name = []

with open('jsonfile') as f:
	data = [json.loads(line) for line in f]

for line in data:
	stringcheck1 = line['name'].find(string1)
	lowerstringcheck1 = line['name'].find(string1.lower())
	stringcheck2 = line['name'].find(string2)
	lowerstringcheck2 = line['name'].find(string2.lower())
	stringcheck3 = line['name'].find(string3)
	lowerstringcheck3 = line['name'].find(string3.lower())

	if stringcheck3 > -1 or lowerstringcheck3 > -1:
		for value in line['condition']['query']:
			dictionary = {'name': 'get name' , 'kw': 'get value', 'weight': 'get weight'}
			dictionary['name'] = line['name']
			dictionary['kw'] = value['value']
			dictionary['weight'] = value['weight']
			entity3.append(dictionary)
			entity3name.append(line['name'])


			#array = []
			#array.append(line['name'])
			#array.append(value['value'])
			#array.append(value['weight'])
			#entity3.append(array)
	elif stringcheck2 > -1 or lowerstringcheck2 > -1:
		for value in line['condition']['query']:
			dictionary = {'name': 'get name' , 'kw': 'get value', 'weight': 'get weight'}
			dictionary['name'] = line['name']
			dictionary['kw'] = value['value']
			dictionary['weight'] = value['weight']
			entity2.append(dictionary)
			entity2name.append(line['name'])

	elif stringcheck1 > -1 or lowerstringcheck1 > -1:
		for value in line['condition']['query']:
			dictionary = {'name': 'get name' , 'kw': 'get value', 'weight': 'get weight'}
			dictionary['name'] = line['name']
			dictionary['kw'] = value['value']
			dictionary['weight'] = value['weight']
			entity1.append(dictionary)
			entity1name.append(line['name'])


	#for taxonomy in entity1:
		#array = []
		#array.append(value['value'])
		#array.append(value['weight'])
		#entity1values.append(array)



#print entity1values
#print entity2
newlist3 = []
for thing in entity3:

	newlist3.append(thing['kw'])

newlist2 = []
for thing in entity2:

	newlist2.append(thing['kw'])

newlist1 = []
for thing in entity1:

	newlist1.append(thing['kw'])



newweights3 = collections.Counter(newlist3)
newweights2 = collections.Counter(newlist2)
newweights1 = collections.Counter(newlist1)

scoredvalues3 = []
scoredvalues2 = []
scoredvalues1 = []

scores3 = []
scores2 = []
scores1 = []

lentity3 = len(set(entity3name))
lentity2 = len(set(entity2name))
lentity1 = len(set(entity1name))
#print lentity3
for kw in newweights3:
	dictionary = {'kw': 'value', 'score':'score'}
	dictionary['kw'] = kw

	dictionary['score'] = newweights3[kw]/lentity3
	scores3.append(dictionary['score'])
	scoredvalues3.append(dictionary)
	#print dictionary['score']

for kw in newweights2:
	dictionary = {'kw': 'value', 'score':'score'}
	dictionary['kw'] = kw
	dictionary['score'] = newweights2[kw]/lentity2
	scores2.append(dictionary['score'])
	scoredvalues2.append(dictionary)

for kw in newweights1:
	dictionary = {'kw': 'value', 'score':'score'}
	dictionary['kw'] = kw
	dictionary['score'] = newweights1[kw]/lentity1
	scores1.append(dictionary['score'])
	scoredvalues1.append(dictionary)



median3 = median(scores3)
median2 = median(scores2)
median1 = median(scores1)

lastarray3 = []
lastarray2 = []
lastarray1 = []



for keyword3 in scoredvalues3:
	if keyword3['score'] > median3:
		lastarray3.append(keyword3['kw'])

for keyword2 in scoredvalues2:
	if keyword2['score'] > median2:
		lastarray2.append(keyword2['kw'])

for keyword1 in scoredvalues1:
	if keyword1['score'] > median1:
		lastarray1.append(keyword1['kw'])

print lastarray1
print lastarray2
print lastarray3

finalarray = set()
finaltestarray = set()

for item_c in lastarray3:
	for item_b in lastarray2:
		if item_c == item_b:
			finaltestarray.add(item_c)
for item_c in lastarray3:
	for item_a in lastarray1:
		if item_c == item_a:
			finalarray.add(item_c)
for item_b in lastarray2:
	for item_a in lastarray1:
		if item_b == item_a:
			finalarray.add(item_b)
for item_d in finaltestarray:
	for item_a in lastarray1:
		if item_d == item_a:
			finalarray.add(item_d)

for stuff in lastarray1:
	stringcheck1 = stuff.find(string1)
	lowerstringcheck1 = stuff.find(string1.lower())
	if stringcheck1 > -1 or lowerstringcheck1 > -1:
		finalarray.add(stuff)
	else:
		pass

for stuff in lastarray2:
	stringcheck1 = stuff.find(string1)
	lowerstringcheck1 = stuff.find(string1.lower())
	if stringcheck1 > -1 or lowerstringcheck1 > -1:
		finalarray.add(stuff)
	else:
		pass

for stuff in lastarray3:
	stringcheck1 = stuff.find(string1)
	lowerstringcheck1 = stuff.find(string1.lower())
	if stringcheck1 > -1 or lowerstringcheck1 > -1:
		finalarray.add(stuff)
	else:
		pass


#Clean up
cleanfinalarray = []
cleanfinaltestarray = []

for words in finalarray:
	cleanword = words.encode("utf-8")
	cleanfinalarray.append(cleanword)

for words in finaltestarray:
	cleanword = words.encode("utf-8")
	cleanfinaltestarray.append(cleanword)


print cleanfinalarray
print cleanfinaltestarray

#print len(entity3name)
#print set(entity3name)
#print set(entity2name)
#print set(entity1name)





