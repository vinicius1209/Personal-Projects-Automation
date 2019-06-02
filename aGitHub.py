import os
from github import Github

class GitRepo():

    def __init__(self, folderName):
        self.username = input("Username:")
        self.password = input("Password:")
        self.folderName = folderName
        self.create()
        
    def create(self):
        try:
            user = Github(self.username, self.password).get_user()
            repo = user.create_repo(self.folderName)
            print('GitHub repository created!')
        except Exception as e:
            print('Error while creating GitHub repository {}: {} \n'.format(self.folderName, e))

