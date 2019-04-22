import csv
with open('data.csv', mode = 'r') as csvdata:
	data = {}
	reader = csv.DictReader(csvdata)
	for row in reader:
		for key,value in row.items():
			data.setdefault(key, []).append(value)
print(data.keys())
def predict(outlook, temperature, humidity, windy):
	n_yes = len(list(x for x in data['PLAY GOLF'] if x == 'Yes'))
	n_no = len(list(x for x in data['PLAY GOLF'] if x == 'No'))
	n = len(data['PLAY GOLF'])
	p_yes = n_yes/n
	p_no = n_no/n
	print(p_yes,p_no)

	n_outlook_yes = len(list(x for x in data['OUTLOOK'] if x == 'Yes'))
	n_temp_yes =
	n_humid_yes =
	n_wind_yes =
	n_outlook_no =
	n_temp_no =
	n_humid_no =
	n_wind_no = 

predict('a','b','c','d')
