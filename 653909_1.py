# coding=utf-8
'''
This assignment is designed to read a list of trajectory data, to compute the total length of the trace, to compute	the	
length of the trace’s longest segment, and	its	index in the trace, to compute the average sampling	rate for the trace 
and the	speed of each segment, and identify the	indices	of segments. 

The aim is to gain experience in comprehending	program requirements, designing	a small program, programming defensively 
and testing the program.

Name: Changjian Ma
Student Number: 653909
Username: changjianm
Date 09/04/2017
'''

'''
code reference link:
http://www.python-course.eu/course.php
https://www.learnpython.org/en/Loops
https://www.learnpython.org/en/Functions
https://www.learnpython.org/en/Conditions
https://www.learnpython.org/en/List_Comprehensions
http://stackoverflow.com/questions/252703/append-vs-extend
'''

# import csv module to make csv file available to use
# import math module to activate math functions to calculate related data

import csv
import math

#this function is to calculate the time difference that between two points, use if function to compare to return
#different results
def time_diff(tm1, tm2):
    if tm2 < tm1:
        return(tm2 - tm1 + 24 * 3600)
    else:
        return (tm2 - tm1)

#this function is to calculate the distance between two points
def calcu_distance(x1, y1, altitude1, x2, y2, altitude2):
    #use math related function which is square root to calculate and the precision for the lengths is two digits after
    #the decimal point
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(altitude1 - altitude2, 2))

#this function is to calculate the speed of every segment
def calcu_speed(calcu_distance, time):
    #use distance divided by time to get the speed result
    return calcu_distance / time

#this function is to calculate the max speed and the min speed in every trace data
def maxspd_and_minspd(list, length):
    minspd = 0
    maxspd = 0
    #use for loop and if function to get the max and min data of speed
    for i in range(0, length):
        if list[i] < list[minspd]:
            minspd = i
        if list[i] > list[maxspd]:
            maxspd = i;
    #get the result and wait to be called
    return minspd, maxspd

#this is to do a calculation of total length of all traces
def total_len_calcu(list):
    #set variable length
    calculength = 0
    #use for loop to calculate the result
    for i in range(0, len(list) - 1):
        calculength = calculength + list[i][0]
    # get the result and wait to be called
    return calculength

#this function is to calculate and find the longest segment in every trace data
def calcu_longest_segment(list, length):
    #set the variable index and calcu_distance
    index = 0
    calcu_distance = 0
    #use for loop to get the index and the longest distance segment
    for i in range(0, length):
        if list[i] > calcu_distance:
            index = i
            calcu_distance = list[i]
    #get the result and wait to be called
    return index, calcu_distance

#this is to get the longest trace of all trace and then to return the value of index and speed
def longest_trace(list):
    longest_spd = 0.0
    longtrace_index = 0
    #ues for loop and if function to judge and get the longest speed and index
    for i in range(0, len(list) - 1):
        if list[1][0] > list[longtrace_index][0]:
            longtrace_index = 1
        longest_spd = list[longtrace_index][0]/list[longtrace_index][3]
    # get the result and wait to be called
    return longtrace_index, longest_spd

#this is to create the output result of the entire data in the end
def totaldata_result(list):
    totaldata_len = total_len_calcu(list)
    spd = longest_trace(list)[1]
    traceindex = longest_trace(list)[0]
    #the output is to show the result of entire data, the precision	for	the
    #lengths has two digits after the decimal point
    totaloutput = "The total length of all traces is %6.2fm.\n" %(totaldata_len)
    totaloutput = totaloutput + "The index of the longest trace is %s, and the average speed along the " \
                                "trace is %4.2fm/s" %(traceindex, spd)
    #get the result and wait to be called
    return totaloutput

#this is to do the calculations to create the result of all traces
def convert_to_result(i,list):
    #the precision for the output has two digits after the decimal point
    res_output = "Trace %s's length is %6.2fm.\n" % (i+1, list[i][0])
    res_output = res_output + "The Length of its longest segment is %6.2fm, and the index is %s.\n" % (list[i][2], list[i][1])
    res_output = res_output + "The average sampling rate fot the trace is %6.2fs.\n" % (list[i][6])
    res_output = res_output + "For the segment index %s, the minimal travel speed is reached.\n" % (list[i][4])
    res_output = res_output + "For the segment index %s, the maximum travel speed is reached.\n" % (list[i][5])
    res_output = res_output + "----"
    # get the result and wait to be called
    return res_output

#this is to do the calculation of trace and store the result data
def calcu_trace(list):
    #create a list to store the data info
    tracedata_list = [[0, 0, 0, 0, 0, 0, 0]]
    #this is a nested list which is to store every segment distance
    segment_distance = [[]]
    # this is a nested list which is to store every segment speed
    segment_spd = [[]]
    # create a list to store every trace segment
    seg_length = [0]
    j = 0
    #use for loop to calculate the trace
    for i in range(0, len(list) - 2):
        #use if to judge and get the result
        if list[i][0] != list[i + 1][0]:
            # this is to create a new list of trace while there is a new trace appears
            tracedata_list.append([0, 0, 0, 0, 0, 0, 0])
            seg_length.append(0)
            # this is a nested list to store the distance and speed
            segment_spd.append([])
            segment_distance.append([])
            tracedata_list[j][1] = calcu_longest_segment(segment_distance[j], seg_length[j])[0]
            tracedata_list[j][2] = calcu_longest_segment(segment_distance[j], seg_length[j])[1]
            tracedata_list[j][4] = maxspd_and_minspd(segment_spd[j], seg_length[j])[0]
            tracedata_list[j][5] = maxspd_and_minspd(segment_spd[j], seg_length[j])[1]
            tracedata_list[j][6] = tracedata_list[j][3] / seg_length[j]
            j = j + 1
        else:
            distance = 0.0
            for element in list[i]:
                # use if to judge whether there is a empty element, if yes, print another result, if no, continue
                if element == '' or element is None:
                    print("The data is missing cells, please check the data file.")
                    exit();
                    continue
            # set these file data from original format to float format
            altitude1 = float(list[i][4])
            x1 = float(list[i][2])
            y1 = float(list[i][3])
            altitude2 = float(list[i + 1][4])
            x2 = float(list[i + 1][2])
            y2 = float(list[i + 1][3])
            # this is to transfer time data in csv file, the output format is seconds
            tm1 = int(list[i][5].split(':')[2]) + int(list[i][5].split(':')[1]) * 60 + int(
                list[i][5].split(':')[0]) * 3600
            tm2 = int(list[i + 1][5].split(':')[2]) + int(list[i + 1][5].split(':')[1]) * 60 + \
                  int(list[i + 1][5].split(':')[0]) * 3600
            # this is to calculate the time difference between two time points
            time_reslut = time_diff(tm1, tm2)
            # distance calculate with six elements between two points
            distance = calcu_distance(x1, y1, altitude1, x2, y2, altitude2)
            # calculate the speed data and store every segment data
            segment_spd[j].append(distance / time_reslut)
            # store the distance and put them into list
            segment_distance[j].append(distance)
            tracedata_list[j][3] += time_reslut
            tracedata_list[j][0] += distance
            seg_length[j] = seg_length[j] + 1

    # get the result and wait to be called
    return tracedata_list

# defines the main function to call the other functions and execute the output which is formatted
def main_function():
    #this is to store the csv data file in a path
    trajectory_data=r"./trajectory_data_proj.csv"

    #create a list called trajectory data list to store the trajectory data and read the data in the data file
    trajectory_data_list = []

    #create a list called tracedata list to store the data info and use for output
    tracedata_list = []

    #this is to open and read the trajectory data file
    with open(trajectory_data, 'rt') as dt_file:
        reader = csv.reader(dt_file)
        trajectory_data_list = list(reader)

    # delete the first line, because the first line is the title of data
    del trajectory_data_list[0]
    tracedata_list = calcu_trace(trajectory_data_list)

    #use for loop to print the data
    for i in range (0, len(tracedata_list)-1):
        print(convert_to_result(i,tracedata_list))

    #print and show the total result of trace data in the end
    print(totaldata_result(tracedata_list))

# call the main function and run the program
if __name__ == '__main__':
    main_function()