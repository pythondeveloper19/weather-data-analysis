import glob

path = 'wx_data/*.txt'  # for searching only txt files
files = ((sorted(glob.glob(path))))  # stores name of all the txt files
pr_2 = open('ans/YearlyAverages.out', 'a')  # object for output file opened in append mode

for file in files:  # loop through every file
    f = open(file, 'r')  # object for opening file in read mode
    filedata = f.readlines()
    for year in range(1985, 2015):
        maxt_sum, mint_sum, precpt_sum, no1, no2 = 0, 0, 0, 0, 0  # for storing sum of all the values per year per file.
        for k in filedata:
            d = (k.strip('\n')).split('\t')  # splitting every value in the row
            current_year = int((d[0][:4]))
            if int(current_year) == year:  # check for value only in the year
                if d[1] != '-9999':
                    maxt_sum += int(d[1])
                    no1 += 1
                if d[2] != '-9999':
                    no2 += 1
                    mint_sum += int(d[2])
                if d[3] != '-9999':
                    precpt_sum += int(d[3])

        if no1 == 0 or no2 == 0:  # to prevent Division  By ZERO Error
            continue
        else:
            no1 = no1 * 10
            no2 = no2 * 10
            xx, yy, zz = 0, 0, 0
            xx = round(((maxt_sum) / float(no1)), 2)  # annual average max temp
            yy = round(((mint_sum) / float(no2)), 2)  # annual average min temp
            zz = round((precpt_sum / float(100)), 2)  # annual average precpt

            name = file.strip('wx_data/')
            pr_2.write(str(name) + "txt    " + str(year) + "    " + str(xx) + "    " + str(yy) + "    " + str(
                zz) + "\n")  # write to output file

    f.close()

pr_2.close()  # close output file
