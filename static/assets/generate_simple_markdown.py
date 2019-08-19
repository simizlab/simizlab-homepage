#coding:utf-8
import os, sys, time
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--generate_date_list', '-g',
                            nargs='*', type=str, action='store',
                            help='format is YYYY-MM-DD')
    parser.add_argument('--output_dir', '-o',
                        help='Directory to output the result')
    args = parser.parse_args()

    output_dir = args.output_dir
    generate_date_list = args.generate_date_list

    for generate_date in generate_date_list:
        print(generate_date)
        with open('{}/{}.md'.format(output_dir, generate_date), 'w') as f:
            f.write('---\n')
            f.write('date: {}\n'.format(generate_date))
            f.write('description: ""\n')
            f.write('auther: ""\n')
            f.write('banner: "img/banners/{}.png"\n'.format(generate_date))
            f.write('draft: false\n')
            f.write('---\n')
