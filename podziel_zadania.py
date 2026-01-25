#!/usr/bin/env python3
outputfile = False

with open('zadania_sql.org') as file:
    line = file.readline()
    while line:
        if line.startswith('* Zadanie'):
            if outputfile:
                outputfile.close()
            nazwa = line[2:9] + line[10] + '_IgaJancewicz.txt'
            outputfile = open(nazwa, 'w')
            outputfile.write(line)
        elif outputfile:
            if not line.startswith('#+'):
                outputfile.write(line)
        line = file.readline()
    outputfile.close()
