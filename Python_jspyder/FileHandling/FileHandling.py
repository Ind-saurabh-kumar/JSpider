import os
class FileHandling:

    def fileName(self):
        self.name=input("Enter file name Please \n ")
        self.fileType=input("Give Extension of the file. Example- .py, .java, .txt etc. \n")
        #path and the name of the file and file type code
        self.filePath=f"F:/JSpider/Python_jspyder/FileHandling/Files/{self.name}{self.fileType}" 
    
    def fileCreate(self):
        
        self.fileName()
        
        try:
            #creation of file code
            file=open(self.filePath,'x')
            print(f"Hi, {self.name} {self.fileType} File is Created Successfully........")
        except FileExistsError:
            print(f"This {self.name} {self.fileType}, File is already exist with this name.")

    def writeFile(self):
        #Calling creation of file
        self.fileCreate()
        try:
            file=open(self.filePath,'w')
            info =(input("Enter your info. what you want to write \n"))
            file.write(info)
            print(f"In {self.name}, information are stored.....")

        except BaseException:
            print("Please try again......")

        finally:
            file.close()
            
    def readFile(self):
        
        self.fileName()
        
        try:
            file=open(self.filePath, 'r' )
            print(file.read())
        
        except FileNotFoundError:
            print(f"There is no file available with {self.name}{self.fileType} name.")
        
        finally:
            file.close()
    
    
    def appendFile(self):
        self.fileName()
        
        name = self.name + self.fileType
        name = name.lower()
        
        # Specify the directory
        directory = 'F:/JSpider/Python_jspyder/FileHandling/Files/'
        
        # Flag to check if file exists
        file_exists = False
        
        # List only files in the specified directory
        for filename in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, filename)):
                if filename == name:
                    file_exists = True
                    break
        
        if file_exists:
            try:
                file=open(self.filePath, 'a')
                info = " " + input("Please enter your information below: \n")
                file.write(info)
                print("Information is Stored Successfully....")
            except FileNotFoundError:
                print("File not found....")
        else:
            print(f"Create New file.... No file available with {self.name}{self.fileType} name")
            
    
                         
                  
            
                    
                     
                
                
            
                

        
    
            
        

        
        
            
        
        
        
        
        
        
        
        
            
            
            
        
        
        
        
        
        
        
        
        
            
    
    
            
        



f=FileHandling()
f.appendFile()
