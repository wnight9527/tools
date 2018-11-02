# -*- coding: utf-8 -*-
'''
python读取文件，将文件中的空白行去掉
'''


def delblankline(infile, outfile):
    infopen = open(infile, 'r', encoding="utf-8")
    outfopen = open(outfile, 'w', encoding="utf-8")

    lines = infopen.readlines()
    for line in lines:
        if line.split():
            outfopen.writelines(line)
        else:
            outfopen.writelines("")

    infopen.close()
    outfopen.close()


delblankline("LcdBoardDriver.c", "LcdBoardDriver-1.c")