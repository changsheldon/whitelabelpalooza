from __future__ import division
import json
import collections
import numpy as np



string1 = 'Comedy'
string2 = 'Auto'
string3 = 'Car'

ontology1 = []
ontology2 = []
ontology3 = []

thevalues = []
entity2values = []
entity3values = []

entity1name = []
entity2name = []
entity3name = []

with open('new_pedia.json', 'r') as f:
	#data = f.readlines()
	#data = [json.loads(line) for line in f]
	data = json.load(f)

	#print value	

	for value in data:

			for stuff in data[value]:
				find = stuff['ontology'].find(string1)
				find2 = stuff['ontologyvalue'].find(string1)
				if find > -1 or find2 > -1:

					ontology1.append(value)
					
					ontology2.append(stuff['ontology'])
					if stuff['ontology'] == 'type':
						ontology3.append(stuff['ontologyvalue'])
				else:
					pass
				# if stuff['ontology'] == 'type':
				# 	ontology3.append(stuff['ontologyvalue'])
				# else:
				# 	pass
				#ontology2.append(stuff['ontology'])

		#print data[value]['ontology']
		# find = value.find(string1)
		# if find > -1:
		# 	for stuff in data[value]:
		# 		#print stuff['ontology']
		# 		print stuff
		# 		ontology1.append(stuff['ontology'])
		# else:
		# 	pass

#ontologycount3 = collections.Counter(ontology3)
#print ontologycount3
ontologycount2 = collections.Counter(ontology2)
#maxnum = max(ontologycount2)
#print ontologycount2[0]
#print maxnum

value1 = 0
value2 = 0
for key in ontologycount2:
	#print value2
	if ontologycount2[key] > value2:
		
		value2 = ontologycount2[key]
		topkey = key
	else:
		pass

print topkey

for value in data:

	for stuff in data[value]:
		#finds if the ontologyvalue == string1
		find = stuff['ontologyvalue'].find(string1)

		if stuff['ontology'] == topkey and find > -1:

			thevalues.append(value)
			
			#ontology2.append(stuff['ontology'])
			#if stuff['ontology'] == 'type':
			#	ontology3.append(stuff['ontologyvalue'])
		else:
			pass

print thevalues

	# if ontologycount2[key] == maxnum:
	# 	print key
	# else:
	# 	pass

#maxvalue = ontologycount2[maxnum]
#print ontologycount2
#ontologycount1 = collections.Counter(ontology1)
#print ontologycount1
#print ontology2
	#stringcheck1 = line['value'].find(string1)