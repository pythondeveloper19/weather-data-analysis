import glob
import matplotlib.pyplot as plt
import numpy as np


max_dict = {}
min_dict = {}
prec_dict = {}
pr_3=open('ans/YearHistogram.out','a')   # open output  file

for year in range(1985, 2015):
    max_temps = []      # for storing maximum temperature per year
    min_temps = []      # for storing  minimum temperature per year
    pres = []           # for storing precpt per year
    for row in open('ans/YearlyAverages.out'):
        if int(row.strip('\n').split('    ')[1]) == year:
            max_temps.append(float(row.strip('\n').split('    ')[2]))
            min_temps.append(float(row.strip('\n').split('    ')[3]))
            pres.append(float(row.strip('\n').split('    ')[4]))
    max_dict.update({year: max(max_temps)})     # update with highest max temp value of that year
    min_dict.update({year: max(min_temps)})     # update with highest min temp value of that year
    prec_dict.update({year: max(pres)})         # update with highest precpt value of that year


    path = 'wx_data/*.txt'
    files=((sorted(glob.glob(path))))

    filename_string1,filename_string2,filename_string3="","",""     #storing year and filename
    count1,count2,count3=0,0,0          # storing count of no of files having the value

    for i, file in enumerate(files):
        f=open(file, 'r')   # open fiel in read mode
        filedata=f.readlines()

        for row_no,row in enumerate(filedata):
            row_values=row.strip('\n').split('\t')
            # print row_values
            current_year=row_values[0][:4]          # FINDING YEAR
            final_str=current_year+str(file)
            if str(year) in row_values[0]:          # check for matching year

                max_t_val= (int(row_values[1])/float(10))
                min_t_val=  (int(row_values[2])/float(10))
                prec_val= (int(row_values[3])/float(100))
                if max_dict[year] == max_t_val and final_str not in filename_string1:
                    filename_string1+=current_year+str(file)
                    count1+=1               # count incrementing


                if min_dict[year] == min_t_val and final_str not in filename_string2:

                    filename_string2+=current_year+str(file)
                    count2+=1           # count incrementing

                if prec_dict[year] == prec_val and final_str not in filename_string3:

                    filename_string3+=current_year+str(file)
                    count3+=1               # count incrementing


        f.close()
    pr_3.writelines(str(year)+'\t'+str(count1)+'\t'+str(count2)+'\t'+str(count3)+'\n')  # write string to output



pr_3.close()


# plot graph
row_values_list=(open('ans/YearHistogram.out').readlines())

x = np.arange(1985, 2015)
y1=[int(k.strip('\n').split('\t')[1]) for k in row_values_list]
y2=[int(k.strip('\n').split('\t')[2]) for k in row_values_list]
y3=[int(k.strip('\n').split('\t')[3]) for k in row_values_list]

width = 1
bar1 = plt.bar( x, y1, width, color="y" )
bar2=plt.bar( x, y2, width, color="r" )
bar3=plt.bar( x, y3, width, color="b" )
plt.legend( (bar1[0], bar2[0], bar3[0]), ( 'hist1', 'hist2', 'hist3' ) )
plt.xlabel( 'Year' )
plt.ylabel( 'Count of files' )
plt.xticks(x + width/2.0)
plt.show()
plt.savefig('ans/YearHistogram.png')   # histogram saved