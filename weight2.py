
import json
import collections
import numpy as np
def weight(string1,string2,string3):

#string1 = 'Pop Artist'
#string2 = 'Hip Hop'
#string3 = 'Music'

	entity1 = []
	entity2 = []
	entity3 = []

	entity1values = []
	entity2values = []
	entity3values = []

	entity1name = []
	entity2name = []
	entity3name = []

	name1and2 = []
	name1and3 = []
	name2and3 = []

	with open('jsonfile.json') as f:
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

				if 'weight' not in value or 'value' not in value:
					continue
				dictionary['kw'] = value['value']
				dictionary['weight'] = value['weight']
				entity3.append(dictionary)
				entity3name.append(line['name'])

		if stringcheck2 > -1 or lowerstringcheck2 > -1:
			
			for value in line['condition']['query']:
				dictionary = {'name': 'get name' , 'kw': 'get value', 'weight': 'get weight'}
				dictionary['name'] = line['name']
				
				if 'weight' not in value or 'value' not in value:
					continue
				dictionary['kw'] = value['value']
				dictionary['weight'] = value['weight']
				entity2.append(dictionary)
				entity2name.append(line['name'])

		if stringcheck1 > -1 or lowerstringcheck1 > -1:
			
			for value in line['condition']['query']:
				dictionary = {'name': 'get name' , 'kw': 'get value', 'weight': 'get weight'}
				dictionary['name'] = line['name']
			
				if 'weight' not in value or 'value' not in value:
					continue
				dictionary['kw'] = value['value']
				dictionary['weight'] = value['weight']
				entity1.append(dictionary)
				entity1name.append(line['name'])

		if lowerstringcheck1 > -1 or stringcheck1 > -1:
			if stringcheck2 > -1 or lowerstringcheck2 > -1:
				name1and2.append(line['name'])
		if lowerstringcheck1 > -1 or stringcheck1 > -1:
			if stringcheck3 > -1 or lowerstringcheck3 > -1:
				name1and3.append(line['name'])
		if lowerstringcheck3 > -1 or stringcheck3 > -1:
			if lowerstringcheck2 > -1 or stringcheck2 >-1:
				name2and3.append(line['name'])

	if len(entity2name) == 0:
		topicscore2 = 0
	else:
		topicscore2 = len(name1and2)/len(entity2name)

	if len(entity3name) == 0:
		topicscore3 = 0
	else:
		topicscore3 = len(name1and3)/len(entity3name)

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

	for kw in newweights3:
		dictionary = {'kw': 'value', 'score':'score'}
		dictionary['kw'] = kw
		dictionary['score'] = newweights3[kw]/lentity3
		scores3.append(dictionary['score'])
		scoredvalues3.append(dictionary)

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

	numtopic3 = (1- topicscore3) * 100
	numtopic2 = ((1 - topicscore2) * 100)

	# if numtopic3 == 0:
	# 	numtopic3 = 99
	# else:
	# 	pass
	# if numtopic2 == 0:
	# 	numtopic2 = 99
	# else:
	# 	pass

	lastarray3 = set()
	lastarray2 = set()
	lastarray1 = set()

	for keyword3 in scoredvalues3:
		stringcheck1 = keyword3['kw'].find(string1)
		lowerstringcheck1 = keyword3['kw'].find(string1.lower())
		if keyword3['score'] > np.percentile(scores3,round(numtopic3,4)) or stringcheck1 > -1 or lowerstringcheck1 > -1:
				lastarray3.add(keyword3['kw'])

	for keyword2 in scoredvalues2:
		stringcheck1 = keyword2['kw'].find(string1)
		lowerstringcheck1 = keyword2['kw'].find(string1.lower())
		if keyword2['score'] > np.percentile(scores2,round(numtopic2,4)) or stringcheck1 > -1 or lowerstringcheck1 > -1:
				lastarray2.add(keyword2['kw'])

	for keyword1 in scoredvalues1:
		stringcheck1 = keyword1['kw'].find(string1)
		lowerstringcheck1 = keyword1['kw'].find(string1.lower())
		if keyword1['score'] > np.percentile(scores1,50) or stringcheck1 > -1 or lowerstringcheck1 > -1:
			lastarray1.add(keyword1['kw'])

	#print newweights1

	if len(lastarray1) == 0:
		for keyword1 in scoredvalues1:
			stringcheck1 = keyword1['kw'].find(string1)
			lowerstringcheck1 = keyword1['kw'].find(string1.lower())
			if keyword1['score'] > np.percentile(scores1,25) or stringcheck1 > -1 or lowerstringcheck1 > -1:
				lastarray1.add(keyword1['kw'])

	midarray = lastarray1.union(lastarray2,lastarray3)
	#print scoredvalues3
	#print lentity1
	#print scores1
	#print np.percentile(scores1,50)
	finalarray = []
	for words in midarray:
		cleanword = words.encode("utf-8")
		finalarray.append(cleanword)
	#print finalarray
	return finalarray
#print newweights2
#print round(topicscore3,4)
#print entity2name
#for values in scoredvalues1:
#	if values['score'] > np.percentile(scores1,50):
#		print values

# for keyword3 in scoredvalues3:
# 	stringcheck1 = keyword3['kw'].find(string1)
# 	lowerstringcheck1 = keyword3['kw'].find(string1.lower())
# 	if topicscore3 >= .75:
# 		if keyword3['score'] > upper3 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray3.append(keyword3['kw'])
# 	elif topicscore3 <.75 and topicscore3 >= .25:
# 		if keyword3['score'] > upper3 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray3.append(keyword3['kw'])
# 	elif topicscore3 < .25 and topicscore3 >= .11:
# 		if keyword3['score'] > strict3 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray3.append(keyword3['kw'])
# 	elif topicscore3 < .11 and topicscore3 >= .05:
# 		if keyword3['score'] > stricter3 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray3.append(keyword3['kw'])
# 	elif topicscore3 < .05:
# 		if keyword3['score'] > strictest3 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray3.append(keyword3['kw'])

# for keyword2 in scoredvalues2:
# 	stringcheck1 = keyword2['kw'].find(string1)
# 	lowerstringcheck1 = keyword2['kw'].find(string1.lower())
# 	if topicscore2 >= .75:
# 		if keyword2['score'] > median2 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray2.append(keyword2['kw'])
# 	elif topicscore2 >= .25 and topicscore2 < .75:
# 		if keyword2['score'] > median2 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray2.append(keyword2['kw'])
# 	elif topicscore2 < .25:
# 		if keyword2['score'] > upper2 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 			lastarray2.append(keyword2['kw'])

# for keyword1 in scoredvalues1:
# 	stringcheck1 = keyword1['kw'].find(string1)
# 	lowerstringcheck1 = keyword1['kw'].find(string1.lower())
# 	if keyword1['score'] > median1 or stringcheck1 > -1 or lowerstringcheck1 > -1:
# 		lastarray1.append(keyword1['kw'])



# if len(lastarray3) <=25:
# 	for keyword3 in scoredvalues3:
# 		if keyword3['score'] > low3 and keyword3['kw'] not in lastarray3:
# 			lastarray3.append(keyword3['kw'])

# if len(lastarray2) <=15:
# 	for keyword2 in scoredvalues2:
# 		if keyword2['score'] > low2 and keyword2['kw'] not in lastarray2:
# 			lastarray2.append(keyword2['kw'])

# if len(lastarray1) <=10:
# 	for keyword1 in scoredvalues1:

# 		if keyword1['kw'] not in lastarray1:
# 			lastarray1.append(keyword1['kw'])

# print len(lastarray3)
# print len(lastarray2)
# print len(lastarray1)

# # print lastarray1
# # print lastarray2
# # print lastarray3

# cleanarray1 = []
# cleanarray2 = []
# cleanarray3 = []

# for words in lastarray1:
# 	cleanword = words.encode("utf-8")
# 	cleanarray1.append(cleanword)

# for words in lastarray2:
# 	cleanword = words.encode("utf-8")
# 	cleanarray2.append(cleanword)

# for words in lastarray3:
# 	cleanword = words.encode("utf-8")
# 	cleanarray3.append(cleanword)

# #return cleanarray1, cleanarray2, cleanarray3

# bob = set(cleanarray1).intersection(cleanarray2)
# larry = set(cleanarray1).intersection(cleanarray3)

# tee = set(cleanarray2).intersection(cleanarray3)
# spin = set(cleanarray1).intersection(tee)

# print bob
# print larry
# print tee
# print spin
# #finalarray = set(cleanarray1).intersection(cleanarray2,cleanarray3)
# #print finalarray

# # #--------------------------old sections----------------------------------
# # finalarray = set(lastarray1).intersection(lastarray2,lastarray3)
# # finaltestarray = set()

# # #--------------------old Intersection-------------------------------
# finalarray = set()
# finaltestarray = set()

# for item_c in lastarray3:
# 	for item_b in lastarray2:
# 		if item_c == item_b:
# 			finaltestarray.add(item_c)
# for item_c in lastarray3:
# 	for item_a in lastarray1:
# 		if item_c == item_a:
# 			finalarray.add(item_c)
# for item_b in lastarray2:
# 	for item_a in lastarray1:
# 		if item_b == item_a:
# 			finalarray.add(item_b)
# for item_d in finaltestarray:
# 	for item_a in lastarray1:
# 		if item_d == item_a:
# 			finalarray.add(item_d)

# # #--------------------old Intersection-------------------------------

# # for stuff in lastarray1:
# # 	stringcheck1 = stuff.find(string1)
# # 	lowerstringcheck1 = stuff.find(string1.lower())
# # 	if stringcheck1 > -1 or lowerstringcheck1 > -1:
# # 		finalarray.add(stuff)
# # 	else:
# # 		pass

# # for stuff in lastarray2:
# # 	stringcheck1 = stuff.find(string1)
# # 	lowerstringcheck1 = stuff.find(string1.lower())
# # 	if stringcheck1 > -1 or lowerstringcheck1 > -1:
# # 		finalarray.add(stuff)
# # 	else:
# # 		pass

# # for stuff in lastarray3:
# # 	stringcheck1 = stuff.find(string1)
# # 	lowerstringcheck1 = stuff.find(string1.lower())
# # 	if stringcheck1 > -1 or lowerstringcheck1 > -1:
# # 		finalarray.add(stuff)
# # 	else:
# # 		pass


# #Clean up
# cleanfinalarray = []
# cleanfinaltestarray = []

# for words in finalarray:
# 	cleanword = words.encode("utf-8")
# 	cleanfinalarray.append(cleanword)

# for words in finaltestarray:
# 	cleanword = words.encode("utf-8")
# 	cleanfinaltestarray.append(cleanword)


# print cleanfinalarray
# print cleanfinaltestarray

# # #print len(entity3name)
# # #print set(entity3name)
# # #print set(entity2name)
# # #print set(entity1name)





