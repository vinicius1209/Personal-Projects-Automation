import os

class FlaskProject():

    def __init__(self, path):
        self.path = path
        self.folders()
        self.files()

    def folders(self):
        try:
            os.chdir(self.path)
            os.makedirs('static')
            os.makedirs('templates')
            os.makedirs('venv')
            os.chdir(self.path + '/static')
            os.makedirs('img')
            os.makedirs('js')
            print('Flask Folders created!')
        except Exception as e:
            print('Error while creating Flask project tree {}: {} \n'.format(self.path, e))
    
    def files(self):
        try:
            # Create config.py file
            config_file = open(self.path + "/config.py", "w+")
            config_file.write("class Config(object):\n")
            config_file.write("	SECRET_KEY='123456'\n\n")
            config_file.close()

            # Create routes.py file
            routes_file = open(self.path + "/routes.py", "w+")
            routes_file.write("from . import app, session\n")
            routes_file.write("from flask import render_template, flash, url_for, request, abort, redirect, jsonify\n\n\n")
            routes_file.write("# Home route\n")
            routes_file.write("@app.route('/')\n")
            routes_file.write("def home():\n")
            routes_file.write(" return render_template('index.html') \n\n")
            routes_file.close()

            # Create __init__.py file
            flask_file = open(self.path + "/__init__.py", "w+")
            flask_file.write("from flask import Flask, session\n")
            flask_file.write("from . import config \n\n")
            flask_file.write("# Flask Definitions\n")
            flask_file.write("app = Flask(__name__)\n")
            flask_file.write("app.config.from_object(config.Config) \n\n")
            flask_file.write("# Routes\n")
            flask_file.write("from . import routes \n\n")
            flask_file.write("if __name__ == '__main__':\n")
            flask_file.write("  app.run()\n\n")
            flask_file.close()

            # Template #
            if os.path.isdir(self.path + '/templates'):
                index_file = open(self.path + "/templates/index.html", "w+")
                index_file.write('<head>\n')
                index_file.write('  <title>Personal Project Automation</title>\n')
                index_file.write('  <meta charset="utf-8">\n')
                index_file.write('  <script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.js"></script>\n')
                index_file.write('  <script src="https://unpkg.com/vue-router@2.0.0/dist/vue-router.js"></script>\n')
                index_file.write('</head>\n')
                index_file.write('<body>\n')
                index_file.write('  <div id="home">\n')                
                index_file.write('      <router-view></router-view>\n')
                index_file.write('  </div>\n')
                index_file.write('</body>\n')
                index_file.write('<script>\n')
                index_file.write('  {% include "../router/index.js" %}\n') 
                index_file.write('  {% include "components/main.js" %}\n')                    
                index_file.write('</script>\n')                   
                index_file.close()   
            print('Flask Files created!')
        except Exception as e:
            print('Error while creating Flask files {}: {} \n').format(self.path, e)

