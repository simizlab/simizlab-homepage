# coding:utf-8
# https://codeday.me/jp/qa/20190102/117012.html
import os, sys, time
import argparse, glob
import fileinput

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', '-i',
                        help='Directory to input the result')
    parser.add_argument('--output_dir', '-o',
                        help='Directory to output the result')
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    filepath_list = glob.glob('{}/*.md'.format(input_dir))
    for filepath in filepath_list:
        filename = os.path.basename(filepath)
        year = filename.split('-')[0]
        # https://stackoverflow.com/questions/24754861/unicode-file-with-python-and-fileinput
        processing_flag = False
        with open('{}/{}'.format(output_dir, filename), 'w', encoding="utf-8") as outputf:
            with fileinput.input(filepath, openhook=fileinput.hook_encoded("utf-8")) as inputf:
                for line in inputf:
                    if line.startswith('auther'):
                        processing_flag = True
                    else:
                        if processing_flag:
                            outputf.write('tags: ["{}"]\n'.format(year))
                        processing_flag = False
                    outputf.write(line)
