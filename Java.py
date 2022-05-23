import subprocess
class JavaApplication:

     """
     
     Bu class java dosyalarını,jar dosyalarını ver yaratmakta kullanır

     RunClass [class name]

     RunJarFile [jarFile]

     createJarFile [jarFile name, javaFileName ,javaFileClass ]
     
     
     
     """

     def RunClass(self,clas):
          self.cmd=subprocess.run("javac"+" "+clas,shell=True)
          self.cmd=subprocess.run("java"+" "+clas,shell=True)

     
     def RunJarFile(self,jarFile):
          subprocess.run("java -jar"+" "+jarFile,shell=True)


     def createJarFile(self,name,jarFileName,jarFileClass):
          subprocess.run("jar cfe "+" "+" "+name+" "+jarFileName+" "+jarFileClass,shell=True)


     def ReadFile(self,file):
          File=open(file,"r")
          self.text=[]
          if file in ".class" or ".java":
               print("[INFO] FILE READ SUCCESSFULLY")
               self.text=File.readlines()
          else:
               print("[INFO] FİLE NOT FOUND ERROR")
     

     def print(self,file):
          File=open(file,"w")
          File.write(str(self.text))

     def OutPut(self):
          print(subprocess.getoutput(str(self.cmd.args)))