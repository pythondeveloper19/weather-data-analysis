import glob

path = 'wx_data/*.txt'  # for searching only txt files
files = ((sorted(glob.glob(path))))  # stores name of all the txt files
pr_1 = open('ans/MissingPrcpData.out', 'a')  # object for output file opened in append mode


def prob_1(filedata):  # function for finding count of files having missing data
    count = 0   # store count of files
    for k in filedata:
        d = (k.strip('\n')).split('\t')   # splitting row and finding value

        if d[3] == '-9999' and d[1] != '-9999' and d[2] != '-9999':  # check for not null value
            count += 1

    if count != 0:
        name = file.strip('wx_data/')
        pr_1.writelines(str(name) + "txt    " + str(count) + "\n")       #write output to file


for i, file in enumerate(files):
    f = open(file, 'r')
    filedata = f.readlines()

    prob_1(filedata)      # problem1 function
    f.close()

pr_1.close()  # output file closed
