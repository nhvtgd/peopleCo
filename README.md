peopleCo
========
This repo is designed to allow people to scrape information about people's github profiles. This includes information like number of github repositories, language preferences, readmes for projects, project names, etc. The goal of this project is to enable people filling out forms to avoid having to fill out tehcnical details of projects they have worked on. With proper authentication it is possible to extend this project to grab private repos but this is not currently a feature. 

To get information about a user simply call 'python cli.py userName' and you will get a dictionary of results.

Example:

Input:
python cli.py amruthv 

Output:
{'languagePreferences:': {'Java': '63%',
                          'M': '1%',
                          'Matlab': '10%',
                          'Perl': '1%',
                          'Python': '23%'},
 'profile': {'followers': 2,
             'following': 6,
             'public_gists': 0,
             'public_repos': 5},
 'readmes': {u'6.869-Project': '6.869-Project\n=============\n',
             u'FindAPath': 'FindAPath\n=========\n\n6.207 Final Project\n'},
 'repo': {'url': ['https://api.github.com/repos/amruthv/6.869-Project',
                  'https://api.github.com/repos/amruthv/Blast-Droid',
                  'https://api.github.com/repos/amruthv/Blast-Server',
                  'https://api.github.com/repos/amruthv/DropMixer',
                  'https://api.github.com/repos/amruthv/FindAPath']}}
                  
                  
There is a web interface that currently on grabs user and repo information but easily extendable to the other features.
