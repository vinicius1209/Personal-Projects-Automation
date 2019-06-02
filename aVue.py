import os

class VueProject():

    def __init__(self, path):
        self.path = path
        self.folders()
        
    def folders(self):
        try:
            os.chdir(self.path)
            if os.path.isdir(self.path + '/templates'):
                os.chdir(self.path + '/templates')
                os.makedirs('components')
            else:
                os.makedirs('components')
            print('Vue Folders created!')
        except Exception as e:
            print('Error while creating Vue project tree {}: {} \n'.format(self.path, e))

