import json

def http_headers_to_json(headers, results):
	data = {}
	with open(headers) as f:
		element = f.readline().strip().split(' ')
		
		if element[0].startswith('HTTP/1.0'): 
			if len(element)>1:
				data['protocol'] = element[0]
				data['status_code'] = element[1]
			elif len(element)>2:
				data['status_message'] = ' '.join(element[2::])
				
		elif element[0].startswith('HTTP/1.1'):
			if len(element)>1:
				data['protocol'] = element[0]
				data['status_code'] = element[1]
			elif len(element)>2:
				data['status_message'] = ' '.join(element[2::])
				
		elif element[0].startswith('HTTP/2'):
			data['protocol'] = element[0]
			data['status_code'] = element[1]
			
		else:
			data['method'] = element[0]
			data['uri'] = element[1]
			data['protocol'] = element[2]
			
		for string in f:
			elem = string.replace('\n', '').split(': ')
			if len(string) > 1:
				data[elem[0]] = elem[1]
		
	with open(results, 'w') as f:
		json.dump(data, f, indent=4)
	
	
		