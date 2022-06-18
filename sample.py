names = ['file1', 'file2', 'file3', 'file4', 'file5', 'file6', 'file7', 'file8', 'file9', 'file10']
for name in names:
    f_name = name+".html"
    path = './templates/'+f_name
    with open(path, 'w') as myfile:
        myfile.writelines('<!DOCTYPE html>\n<html><body><h1><hello></h1><button type="button" ></body></html>')
    myfile.close()
        