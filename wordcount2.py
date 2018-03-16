import os
import re

def map_word(line):
    line = list(map(lambda x: (x, 1), line))
    return line


def reduce_word(line):
    dict_word = {}
    for li in line:
        if li[0] not in dict_word.keys():
            dict_word[li[0]] = li[1]
        else:
            dict_word[li[0]] += li[1]
    reduce_line = []
    for key, value in dict_word.items():
        reduce_line.append((key, value))
    return reduce_line



def splitfile(filepath, linesize=3000):
    """
    split big file to many small files
    every little file is no more than 3000 rows
    small files are stored on current_path/filename/
    """
    filedir, name = os.path.split(filepath)
    name, ext = os.path.splitext(name)
    filedir = os.path.join(filedir, name)
    if not os.path.exists(filedir):
        os.mkdir(filedir)

    partno = 0
    stream = open(filepath, 'r', encoding='utf-8')
    while True:
        partfilename = os.path.join(filedir, name + '_' + str(partno) + ext)
        print('write start %s' % partfilename)
        part_stream = open(partfilename, 'w', encoding='utf-8')

        read_count = 0
        while read_count < linesize:
            read_content = stream.readline()
            if read_content:
                part_stream.write(read_content)
            else:
                break
            read_count += 1

        part_stream.close()
        if read_count < linesize:
            break
        partno += 1

    print('done')
    return filedir


def write_file(word_list, file_dir, f):
    fo = open(file_dir + "_count/" + f, 'w', encoding='utf-8')
    for ip in word_list:
        fo.write("(" + str(ip[0]) + "," + str(ip[1]) + ")\t")
        fo.write('\n')


def read_file(file_dir, f):
    fo = open(file_dir + "/" + f, encoding='utf-8')
    w_list = []
    while True:
        line = fo.readline().strip()
        if not line:
            break
        lines = line.split(",")
        w_list.append((lines[0][1:], int(lines[1][:1])))
    return w_list



if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("please input right file and right k")
    # if len(sys.argv) == 3:
    #     filename = sys.argv[1]
    #     k = int(sys.argv[2])
        filename = "data/test.log"
        k = 5
        # set every small file has 100 rows
        file_dir = splitfile(filename, linesize=100)
        # build a dir to store count file
        if not os.path.exists(file_dir + "_count"):
            os.mkdir(file_dir + "_count")
        word_list = []
        for f in os.listdir(file_dir):
            file = open(file_dir + "/" + f, encoding='utf-8')
            line_word = []
            while True:
                line = file.readline()
                line = line.strip()
                if not line:
                    break
                # replace all special character to space
                r1 = '[’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
                line = re.sub(r1, " ", line)
                line = line.split()
                line_word.extend(map_word(line))
            write_file(reduce_word(line_word), file_dir, f)
            word_list.extend(reduce_word(line_word))

        # for f in os.listdir(file_dir + "_count"):
        #     word_list.extend(read_file(file_dir + "_count", f))
        # reduce all files
        word_list = reduce_word(word_list)
        word_list = list(sorted(word_list, key=lambda x: x[1], reverse=True))
        for i in range(k):
            print("top", i, ": ", word_list[i])






