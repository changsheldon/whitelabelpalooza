import weight2
import csv

num_lines = (sum(1 for line in open('Input.csv')))-1


with open('Input.csv', 'rU') as csv_file:
	Input_reader = csv.DictReader(csv_file)

	with open('new_input.csv', 'w') as new_file:
		fieldnames = ['string3', 'string2', 'string1','signals']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
		csv_writer.writeheader()
		i = 0
		for line in Input_reader:
			#print len(line)
			#print line
			lala = {'string3':line['string3'], 'string2':line['string2'],'string1':line['string1'],'signals': 'sub value'}
			signals = weight2.weight(line['string1'],line['string2'],line['string3'])
			lala['signals'] = signals
			#print signals
			csv_writer.writerow(lala)
			i += 1	
			print i,'/',num_lines

print 'signalfinder is finished!!'