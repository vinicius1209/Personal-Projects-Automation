import os

class VueProject():

    def __init__(self, path):
        self.path = path
        self.folders()
        self.files()
        
    def folders(self):
        try:
            os.chdir(self.path)
            os.makedirs('router')
            os.chdir(self.path + '/templates')
            os.makedirs('components')
            print('Vue Folders created!')
        except Exception as e:
            print('Error while creating Vue project tree {}: {} \n'.format(self.path, e))

    def files(self):
        try:
            os.chdir(self.path)

            # Create router.js file
            os.chdir(self.path + '/router')                   
            router_file = open(self.path + "/router/index.js", "w+")
            router_file.write(
                "const Home = {\n" +
                "   template: '<h2> {{ title }} </h2>', \n" +
                "   data() { \n" +
                "       return { \n" 
                "           title: 'Home Page' \n" +
                "       } \n" +
                "   }, \n" +
                "   methods: { \n" +
                "   } \n" + 
                "} \n\n" +
                "const routes = [ \n" +
                "   { path: '/', component: Home } \n" +
                "] \n\n" +
                "const router = new VueRouter({\n" +
                "   routes, \n" +
                "   mode:'history' \n" + 
                "})"
            )
            router_file.close() 

            # Create main.js file
            os.chdir(self.path + '/templates/components')                   
            main_file = open(self.path + "/templates/components/main.js", "w+")
            main_file.write(
                "var home = new Vue({\n" +
                "   router, \n" +
                "   el: '#home'\n" +
                "})"
            )
            main_file.close()             

            print('Vue Files created!')
        except Exception as e:
            print('Error while creating Vue Files {}: {} \n'.format(self.path, e))     
    
