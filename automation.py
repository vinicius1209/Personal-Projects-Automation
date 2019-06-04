import os
import sys
import subprocess
from github import Github

class ProjectAutomation():

    def __init__(self, args):
        self.args = args
        self.path = "C:/Users/Vinícius Machado/Documents/GitHub/"
        self.virtualenv = '"C:/Users/Vinícius Machado/AppData/Local/Programs/Python/Python37/Scripts/virtualenv.exe"'
        self.__create()
    
    def __create(self):
        self.path = self.path + self.args['proj_name']

        print('\n***********************************\n')

        try:
            print("\n----------ROOT FOLDER---------\n")
            os.makedirs(self.path)
        except Exception as e:
            print('Error while creating root folder: {}'.format(e))  
            sys.exit()
        
        if self.args['flask'] is not None:
            self.__flask()
            self.__venv()
        else:
            self.__venv()
        
        if self.args['github'] is not None:
            self.__gitHub()
        
    def __flask(self):
        try:
            print("\n------------FLASK-------------\n")
            os.chdir(self.path)
            os.makedirs('static')
            os.makedirs('templates')
            os.makedirs('venv')
            os.chdir(self.path + '/static')
            os.makedirs('img')
            os.makedirs('js')
            
        except Exception as e:
            print('Error while creating Flask project folders {}: {} \n'.format(self.path, e))
            sys.exit()
        try:
            # Create config.py file
            config_file = open(self.path + "/config.py", "w+")
            config_file.write(
            "class Config(object):\n"
            "	SECRET_KEY='123456'\n\n"
            )
            config_file.close()

            # Create routes.py file
            routes_file = open(self.path + "/routes.py", "w+")
            routes_file.write(
                "from . import app, session\n" 
                "from flask import render_template, flash, url_for, request, abort, redirect, jsonify\n\n\n" 
                "# Home route\n" 
                "@app.route('/')\n" 
                "@app.route('/home')\n" 
                "def home():\n" 
                " return render_template('index.html') \n\n"
            )
            routes_file.close()

            # Create __init__.py file
            flask_file = open(self.path + "/__init__.py", "w+")
            flask_file.write(
                "from flask import Flask, session\n" 
                "from . import config \n\n"
            )

            if self.args['vue'] is not None:
                print("\n-------------VUE-------------\n")
                os.chdir(self.path + '/templates')
                os.makedirs('components')
                os.chdir(self.path + '/templates/components')
                os.makedirs('router')
                
                # Create router.js file                  
                router_file = open(self.path + "/templates/components/router/index.js", "w+")
                router_file.write(
                    "const Home = {\n" 
                    "   template: '<h2> {{ title }} </h2>', \n" 
                    "   data() { \n" 
                    "       return { \n" 
                    "           title: 'Home Page' \n" 
                    "       } \n" 
                    "   }, \n" 
                    "   methods: { \n" 
                    "   } \n" 
                    "} \n\n" 
                    "const routes = [ \n" 
                    "   { path: '/', component: Home } \n" 
                    "] \n\n" 
                    "const router = new VueRouter({\n" 
                    "   routes, \n" 
                    "   mode:'history' \n" 
                    "})"
                )
                router_file.close() 

                # Create main.js file
                os.chdir(self.path + '/templates/components')                   
                main_file = open(self.path + "/templates/components/main.js", "w+")
                main_file.write(
                    "var home = new Vue({\n"
                    "   router, \n"
                    "   el: '#home'\n"
                    "})"
                )
                main_file.close()  

                # Change flask default uses of {{ }} that's vue uses
                flask_file.write(
                    "# Custum Class \n" 
                    "class FlaskVue(Flask):\n" 
                    "    jinja_options = Flask.jinja_options.copy()\n" 
                    "    jinja_options.update(dict(\n" 
                    "        variable_start_string='%%',\n" 
                    "        variable_end_string='%%',\n" 
                    "    ))\n\n"
                )
                flask_file.write(
                    "# Flask Definitions\n" 
                    "app = FlaskVue(__name__)\n" 
                    "app.config.from_object(config.Config) \n\n" 
                    "# Routes\n" 
                    "from . import routes \n\n" 
                    "if __name__ == '__main__':\n" 
                    "  app.run()\n\n"
                )
                flask_file.close()

                # Template #
                if os.path.isdir(self.path + '/templates'):
                    index_file = open(self.path + "/templates/index.html", "w+")
                    index_file.write(
                        '<head>\n'
                        '  <title>Personal Project Automation</title>\n'
                        '  <meta charset="utf-8">\n'
                        '  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>\n' 
                        '  <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>\n'
                        '</head>\n'
                        '<body>\n'
                        '  <div id="home">\n'        
                        '      <router-view></router-view>\n'
                        '  </div>\n'
                        '</body>\n'
                        '<script>\n'
                        '  {% include "components/router/index.js" %}\n'
                        '  {% include "components/main.js" %}\n'         
                        '</script>\n'
                    )
                    index_file.close()   
            else:
                flask_file.write(
                    "# Flask Definitions\n" 
                    "app = Flask(__name__)\n" 
                    "app.config.from_object(config.Config) \n\n" 
                    "# Routes\n" 
                    "from . import routes \n\n" 
                    "if __name__ == '__main__':\n" 
                    "  app.run()\n\n"
                )
                flask_file.close()

                # Template #
                if os.path.isdir(self.path + '/templates'):
                    index_file = open(self.path + "/templates/index.html", "w+")
                    index_file.write(
                        '<head>\n'
                        '  <title>Personal Project Automation</title>\n'
                        '  <meta charset="utf-8">\n'
                        '</head>\n'
                        '<body>\n'
                        '  <h2> Home Page </h2>\n'        
                        '</body>\n'
                        '<script>\n'      
                        '</script>\n'
                    )
                    index_file.close()   

        except Exception as e:
            print('Error while creating Flask/Vue files {}: {} \n').format(self.path, e)


    def __venv(self):
        try:
            print("\n------------Venv--------------\n")

            # Install virtualenv
            subprocess.call(self.virtualenv +  "  " + '"' + self.path + '/venv"' + " --no-site-packages", shell=True)   

            # Create setup.py file
            itl_flask_file = open(self.path + "/venv/Scripts/setup.py", "w+")
            itl_flask_file.write(
                "from setuptools import setup\n\n"
                "setup(\n"
                "  name='" + self.args['proj_name'] + "',\n"
                "  version='1.0',\n"
            )
            
            if self.args['flask'] is not None:
                itl_flask_file.write("  install_requires=['FLASK']\n")

            itl_flask_file.write(")\n")
            itl_flask_file.close()

            os.chdir(self.path + "/venv/Scripts")

            # Install setup.py files with requires
            subprocess.call("python.exe setup.py install", shell=True)
            
        except Exception as e:
            print('Error While Creating Virtualenv Setup: {}'.format(e))  


    def __gitHub(self):
        print("\n-----------GitHub-------------\n")

        username = input("Username:")
        password = input("Password:")
        try:
            user = Github(username, password).get_user()
            repo = user.create_repo(self.args['proj_name'])
            print('GitHub repository created!')
        except Exception as e:
            print('Error while creating GitHub repository {}: {} \n'.format(self.args['proj_name'], e))