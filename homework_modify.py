import os
import shutil

def Homework_modify(target_path : str):

    os.mkdir(target_path + "\\" + "Solutions")
    os.mkdir(target_path + "\\" + "Problems")


    pdfso_name_lst = [f for f in os.listdir(target_path) if (f.endswith('s.pdf') or f.endswith("sol.pdf") )]
    pdfso_dir_lst = [os.path.join(target_path, filename) for filename in pdfso_name_lst]

    for i in range(len(pdfso_dir_lst)):
        shutil.move(pdfso_dir_lst[i],target_path + "\\Solutions\\"+ pdfso_name_lst[i])


    pdfso_name_lst = [f for f in os.listdir(target_path) if f.endswith('.pdf') ]
    pdfso_dir_lst = [os.path.join(target_path, filename) for filename in pdfso_name_lst]

    for i in range(len(pdfso_dir_lst)):
        shutil.move(pdfso_dir_lst[i],target_path + "\\Problems\\"+ pdfso_name_lst[i])


