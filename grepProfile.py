__author__ = 'vnguyen'
import requests

dicData = ["public_repos" , "public_gists", "followers", "following", "company"]
repoData = ["name", "url"]

def grepProfile(userName):
    return Util("https://api.github.com/users/"+userName, dicData)

def Util(link, grepDic):
    requestAPI = requests.get(link, auth=('techdraft', 'techdraft1'))
    result = {}
    if requestAPI.text:
        dict = eval(requestAPI.text, {'false': 'False', 'true': 'True', 'null': "None"})
        for i in grepDic:
            if i in dict:
                result[i] = dict[i]
    return result

def grepGitRepo(userName):
    requestAPI = requests.get("https://api.github.com/users/" + userName + "/repos", auth=('techdraft', 'techdraft1'))
    result = []
    dic = {}
    if requestAPI.text:
        dict = eval(requestAPI.text, {'false': 'False', 'true': 'True', 'null': "None"})
        for i in dict:
            result.append(i["url"])
    dic["url"] = result
    return dic

def main(userName):
    print grepProfile("nhvtgd")
    print grepGitRepo("nhvtgd")