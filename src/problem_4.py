import glob
import numpy

path = 'wx_data/*.txt'  # for searching only txt files
files = ((sorted(glob.glob(path))))  # stores name of all the txt files
pr_2 = open('ans/Correlations.out', 'a')  # object for output file opened in append mode

for file in files:  # loop through every file
    f = open(file, 'r')  # object for opening file in read mode
    filedata = f.readlines()
    for year in range(1985, 2015):
        yield_list = [0, 0]
        maxt_sum, mint_sum, precpt_sum, no1, no2 = 0, 0, 0, 0, 0  # for storing sum of all the values per year per file.
        for k in filedata:
            d = (k.strip('\n')).split('\t')   # splitting every value in the row
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
            x1, x2, x3 = 0, 0, 0
            x1 = round(((maxt_sum) / float(no1)), 2)  # annual average max temp
            x2 = round(((mint_sum) / float(no2)), 2)  # annual averaghe min temp
            x3 = round((precpt_sum / float(100)), 2)  # total precpt value
            for crop_row in open('yld_data/US_corn_grain_yield.txt'):  # open file
                if int(crop_row.strip('\n').split('\t')[0]) == year:
                    yield_list.insert(0, int(crop_row.strip('\n').split('\t')[1]))  # inserting crop_yield value for that year

            corr_val1 = round(numpy.corrcoef([x1, 0, 0], yield_list)[0, 1], 2)  # correlation value for max_temp
            corr_val2 = round(numpy.corrcoef([x2, 0, 0], yield_list)[0, 1], 2)  # correlation value for min_temp
            corr_val3 = round(numpy.corrcoef([x3, 0, 0], yield_list)[0, 1], 2)  # correlation value for precpt value

            name = file.strip('wx_data/')
            pr_2.writelines(str(name) + "txt\t" + str(corr_val1) + "\t" + str(corr_val2) + "\t" + str(
                corr_val3) + "\n")  # write to output file

    f.close()

pr_2.close() # close output file



