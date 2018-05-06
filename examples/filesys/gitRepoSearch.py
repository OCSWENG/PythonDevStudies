import sys
import argparse
import json
import requests

gitRepoBase = 'https://api.github.com/repos'

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Github search')
	parser.add_argument('--author', action="store", dest="author",required=True)
	parser.add_argument('--repo', action="store", dest="repo",required=True)
	parser.add_argument('--search', action="store", dest="search", required=True)
	givenArgs = parser.parse_args()

	url = gitRepoBase +'/'+givenArgs.author+'/'+givenArgs.repo

	try:
		result = requests.get(url)

		if(result.ok):
			repoInfo = json.loads(result.text or result.content)

			print("GitHub repository info for: %s", givenArgs.repo)

			keys = []
			value = repoInfo[givenArgs.search]
			if(isinstance(value , dict)):
				print(json.dumps(value, sort_keys=True, indent=2))
			else:
				print ("Got result for %s: %s" %(givenArgs.search,value))
	except Exception as e:
		print("Exception: ",e)