import json
def http_headers_to_json(headers, results):
	with open(headers) as f:
		data = {}
		element = f.readline().strip().split(' ')
		if element[0] == 'HTTP/1.0' or 'HTTP/1.1':
			data['protocol'] = element[0]
			data['status_code'] = element[1]
			data['status_message'] = element[2]
		elif element[0] == 'HTTP/2':
			data['protocol'] = element[0]
			data['status_code'] = element[1]
		else:
			data['method'] = element[0]
			data['uri'] = element[1]
			data['protocol'] = element[2]
		for string in f:
			if len(string) > 1:
				elem = string.replace('\n', '').split(': ')
				data[elem[0]] = elem[1]
	
	with open(results, 'w') as f:
		json.dump(data, f, indent=4)
	
	
	
		