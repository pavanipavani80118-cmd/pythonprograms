file_path="output.txt"
with open(file_path,"a")as file:
    file.write("\n This is an additional line.")
print("content appended to",file_path)
