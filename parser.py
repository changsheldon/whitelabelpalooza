
import json

string1 = 'Children'
string2 = 'Family'
string3 = 'Life Stages'

valuearray1 = []
weightarray1 = []
valuearray2 = []
weightarray2 = []
valuearray3 = []
weightarray3 = []

extraarray1 = []
extraarray2 = []
extraarray3 = []

extraextra = []


with open('jsonfile') as f:
	data = [json.loads(line) for line in f]

	#print data[0]
for line in data:
		#print line['name']
		#print line['condition']
	for value in line['condition']['query']:
		stringcheck = line['name'].find(string1)
		lowerstringcheck = line['name'].find(string1.lower())
		stringcheck2 = line['name'].find(string2)
		lowerstringcheck2 = line['name'].find(string2.lower())
		stringcheck3 = line['name'].find(string3)
		lowerstringcheck3 = line['name'].find(string3.lower())

		if value.has_key('weight') == False:
			continue

		
		if stringcheck3 > -1 or lowerstringcheck3 > -1:
			if value['weight'] > 1:
				extraarray3.append(value['value'])
				extraextra.append(value['weight'])
			else:
				pass

			if value['weight'] >= .2:
				valuearray3.append(value['value'])
				weightarray3.append(value['weight'])


			else:
				pass
		else:
			pass

		if stringcheck2 > -1 or lowerstringcheck2 > -1:
			if value['weight'] >= .1:
				extraarray2.append(value['value'])
				extraextra.append(value['weight'])

					#print line['name']
					#print value['weight']
					#print value['value']
			else:
				pass

			if value['weight'] >= .2:

				valuearray2.append(value['value'])
				weightarray2.append(value['weight'])

			else:
				pass
		else:
			pass



		if stringcheck > -1 or lowerstringcheck > -1:
			if value['weight'] >= .1:
				extraarray1.append(value['value'])
				extraextra.append(value['weight'])
			else:
				pass

			if value['weight'] >= .2:
				valuearray1.append(value['value'])
				weightarray1.append(value['weight'])
			else:
				pass


					#print line['name']
					#print value['weight']
					#print value['value']

		else:
			pass

			#print type(condition[1])



finalarray = set()
finaltestarray = set()
extrafinalarray = set()
extrafinaltestarray = set()

for item_c in valuearray3:
	for item_b in valuearray2:
		if item_c == item_b:
			finaltestarray.add(item_c)
for item_c in valuearray3:
	for item_a in valuearray1:
		if item_c == item_a:
			finalarray.add(item_c)
for item_b in valuearray2:
	for item_a in valuearray1:
		if item_b == item_a:
			finalarray.add(item_b)
for item_d in finaltestarray:
	for item_a in valuearray1:
		if item_d == item_a:
			finalarray.add(item_d)

for item_c in extraarray3:
	for item_b in extraarray2:
		if item_c == item_b:
			extrafinaltestarray.add(item_c)
for item_c in extraarray3:
	for item_a in extraarray1:
		if item_c == item_a:
			extrafinalarray.add(item_c)
for item_b in extraarray2:
	for item_a in extraarray1:
		if item_b == item_a:
			extrafinalarray.add(item_b)
for item_d in extrafinaltestarray:
	for item_a in extraarray1:
		if item_d == item_a:
			extrafinalarray.add(item_d)


#return (finalarray,extrafinalarray)
print finalarray
print extrafinalarray

#print extraextra
#print valuearray1
#print valuearray2
#print valuearray3
		#print line['kind']
	#print line[u'value']
	#for values in line:
	#	print values[5]
	#	for conditions in values:
#print conditions
		#print condition
#		print condition[1]['value']
		#for query in condition:
		#	for line in query:
		#		print line['kind']
			#if query['weight'] > .5:
				#print query['value']
			#else:
				#pass