import requests
import json
firstHalfRepoUrl = 'https://api.github.com/users/'
secondHalfRepoUrl = '/repos'
def languagePrefsForUser(userName):
    userUrl = firstHalfRepoUrl + userName + secondHalfRepoUrl
    r = requests.get(userUrl)
    languageMetrics = {}
    if(r.ok):
        repos = json.loads(r.text or r.content)
        numPublicRepos = len(repos)
        for i in range(numPublicRepos):
            repoDetails = extractDetailsForRepo(i, repos)
            if repoDetails == None:
                print 'couldnt get repo details'
                return
            else:
                for language in repoDetails:
                    currAmount = languageMetrics.get(language, 0)
                    languageMetrics[language] = currAmount + repoDetails[language]
    else:
        print 'couldnt make user repos requests'
        return None
    totalAmounts = sum(languageMetrics.values())
    languagePercentages = {}
    for language in languageMetrics:
        languagePercentages[str(language)] = int(100 * float(languageMetrics[language]) / totalAmounts)
    return languagePercentages


def extractDetailsForRepo(repoNum, repos):
    repo = repos[repoNum]
    repoLanguagesUrl = repo['languages_url']
    r = requests.get(repoLanguagesUrl)
    if (r.ok):
        repoLangaugeDetails = json.loads(r.text or r.content)
        return repoLangaugeDetails
    else:
        return None