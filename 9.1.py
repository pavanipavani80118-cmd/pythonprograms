file_path="Example.txt"
#open the file in read mode
with open(file_path,"r")as file:
    #Read the entire content of the file
    content=file.read()
    #print the content
    print(content)
