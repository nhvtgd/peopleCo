import sys
import languageprefs

functions = [languageprefs.languagePrefsForUser, fetch_readmes.fetch_repo_readmes]

def main():
    userName = sys.argv[1]
    results = {}
    for functionToCall in functions:
        featureResults = functionToCall(userName)
        print featureResults
        if (featureResults != None):
            results = dict(results.items() + featureResults.items())
        else:
            print 'sorry got rate limited'
    print results

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'too many arguments'
    print functions
    main()