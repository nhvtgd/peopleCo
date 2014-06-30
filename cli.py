import sys
import languageprefs
import fetch_readmes
import grepProfile
from pprint import pprint

functions = [languageprefs.languagePrefsForUser, fetch_readmes.fetch_repo_readmes, grepProfile.grepProfile, grepProfile.grepGitRepo]

def main():
    userName = sys.argv[1]
    results = {}
    for functionToCall in functions:
        featureResults = functionToCall(userName)
        if (featureResults != None):
            results = dict(results.items() + featureResults.items())
        else:
            print 'sorry got rate limited'
    print pprint(results)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'too many arguments'
    main()