import os
import subprocess

class VenvProject():

    def __init__(self, folderName, path, requires):
        self.folderName = folderName
        self.path = path
        self.requires = requires
        self.virtualenv = "C:/Users/55479/AppData/Local/Programs/Python/Python37-32/Scripts/virtualenv.exe"
        self.setup()
        
    def setup(self):
        # Setup virtualenv
        try:
            # Install virtualenv
            subprocess.call(self.virtualenv +  "  " + self.path + "/venv --no-site-packages", shell=True)    
            
            # Create setup.py file
            itl_flask_file = open(self.path + "/venv/Scripts/setup.py", "w+")
            itl_flask_file.write("from setuptools import setup\n\n")
            itl_flask_file.write("setup(\n")
            itl_flask_file.write("  name='" + self.folderName + "',\n")
            itl_flask_file.write("  version='1.0',\n")
            
            if self.requires:
                itl_flask_file.write("  install_requires=" + str(self.requires) + "\n")

            itl_flask_file.write(")\n")
            itl_flask_file.close()

            os.chdir(self.path + "/venv/Scripts")

            # Install setup.py files with requires
            subprocess.call("python.exe setup.py install", shell=True)
            
            print('Venv setup finished!')
        except Exception as e:
            print('Error While Creating Virtualenv Setup: {}'.format(e))  

