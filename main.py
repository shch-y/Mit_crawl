import os
from down_load import down_load


url_base = input("Please enter the \"base\" url of mit ocw: ")
save_path = input("Please enter the directory you want to save the files: ")

os.mkdir(save_path+"\\assignments")
down_load(url_base+"resources/assignments/", save_path+"\\assignments")

os.mkdir(save_path+"\\exams")
down_load(url_base+"resources/exams/", save_path+"\\exams")

os.mkdir(save_path+"\\lecture-notes")
down_load(url_base+"resources/lecture-notes/", save_path+"\\lecture-notes")

os.mkdir(save_path+"\\recitations")
down_load(url_base+"resources/recitations/", save_path+"\\recitations")

print("Download finished!")

