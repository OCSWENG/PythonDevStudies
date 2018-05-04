
#pip install pyyaml

import argparse
import re
import yaml
import urllib
import urllib2

class Wikipedia:

	def __init__(self, lang='en'):
		self.lang = lang

	def _get_content(self, url):
		request = urllib2.Request(url)
		request.add_header('User-Agent', 'Chrome/51.0.2704.103')

		try:
			result = urllib2.urlopen(request)
		except urllib2.HTTPError as e :
			print ("HTTP Error:%s" %((e.reason)))
		except Exception as e:
			print ("Error occurred: %s" %(str(e)))
     
	def search_content(self, query, page=1, limit=10):
		offset = (page - 1) * limit
		url = SEARCH_URL % (self.lang, urllib.quote_plus(query),offset, limit)

		content = self._get_content(url).read()
		parsed = yaml.load(content)
		search = parsed['query']['search']

		if not search:
			return

		results = []

		for article in search:
			snippet = article['snippet']
			snippet = re.sub(r'(?m)<.*?>', '', snippet)
			snippet = re.sub(r'\s+', ' ', snippet)
			snippet = snippet.replace(' . ', '. ')
			snippet = snippet.replace(' , ', ', ')
			snippet = snippet.strip()
		results.append({'title' : article['title'].strip(),'snippet' : snippet})
		return results


# --query='surfing'
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Wikipedia search')
	parser.add_argument('--query', action="store", dest="query",required=True)

	given_args = parser.parse_args()
	wikipedia = Wikipedia()
	search_term = given_args.query
	print ("Searching Wikipedia for %s" %(search_term))

	results = wikipedia.search_content(search_term)
	print ("*** %s search results..." %(len(results)))

	for result in results:
		print ("==%s== \n \t%s" %(result['title'], result['snippet']))

	print (" End of search results ")

