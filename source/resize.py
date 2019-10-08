"""
https://github.com/Penguin8885/img_resizer/blob/master/resize.py
"""
import numpy as np
import os, sys, time
import argparse, shutil
import cv2
from PIL import Image
import matplotlib.pyplot as plt

def delete_files(directory):
    file_names = os.listdir(directory)
    for file_name in file_names:
        if file_name == ".gitkeep":
            continue
        os.remove("{}/{}".format(directory, file_name))

def resize(img, base_w, base_h):
    base_ratio = base_w / base_h   #リサイズ画像サイズ縦横比
    img_h, img_w = img.shape[:2]   #画像サイズ
    img_ratio = img_w / img_h      #画像サイズ縦横比

    white_img = np.zeros((base_h, base_w, 3), np.uint8) #白塗り画像のベース作成
    white_img[:,:] = [255, 255, 255]                    #白塗り

    ###画像リサイズ, 白塗りにオーバーレイ
    if img_ratio > base_ratio:
        h = int(base_w/img_ratio)           #横から縦を計算
        w = base_w                          #横を合わせる
        resize_img = cv2.resize(img, (w,h)) #リサイズ
    else:
        h = base_h                          #縦を合わせる
        w = int(base_h*img_ratio)           #縦から横を計算
        resize_img = cv2.resize(img, (w,h)) #リサイズ

    white_img[int(base_h/2-h/2):int(base_h/2+h/2),int(base_w/2-w/2):int(base_w/2+w/2)] = resize_img #オーバーレイ
    resize_img = white_img #上書き

    return resize_img

#inputディレクトリ内の画像を連続リサイズ
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir', '-i', help='Directory to input directory')
    parser.add_argument('--output_dir', '-o', help='Directory to output the result')
    parser.add_argument('--base_w', type=int)
    parser.add_argument('--base_h', type=int)
    args = parser.parse_args()

    base_w = args.base_w
    base_h = args.base_h

    #inputディレクトリの画像を読み込み，リサイズ，outputディレクトリに保存
    input_dir = args.input_dir
    output_dir = args.output_dir
    delete_files(output_dir) #outputに入っている全ファイルを削除
    file_names = os.listdir(input_dir)
    for file_name in file_names:
        if file_name == ".gitkeep":
            continue
        print(file_name)

        #名前を変更した一時ファイルを保存(日本語名の画像をOpenCVが読み込めないため)，画像読み込み
        root, ext = os.path.splitext(file_name)
        read_tmp = "{}/tmp{}".format(input_dir, ext)
        shutil.copyfile("{}/{}".format(input_dir, file_name), read_tmp)

        def pil2cv(image):
            """https://qiita.com/derodero24/items/f22c22b22451609908ee
            """
            ''' PIL型 -> OpenCV型 '''
            new_image = np.array(image, dtype=np.uint8)

            if new_image.ndim == 2:  # モノクロ
                return cv2.cvtColor(np.array(image.convert("RGB"), dtype=np.uint8), cv2.COLOR_RGB2BGR)
            elif new_image.shape[2] == 3:  # カラー
                new_image = cv2.cvtColor(new_image, cv2.COLOR_RGB2BGR)
            elif new_image.shape[2] == 4:  # 透過
                background = Image.new("RGB", image.size, (255, 255, 255))
                background.paste(image, mask=image.split()[3])
                return cv2.cvtColor(np.array(background, dtype=np.uint8), cv2.COLOR_RGB2BGR)
            return new_image

        def cv2pil(image):
            ''' OpenCV型 -> PIL型 '''
            new_image = image.copy()
            if new_image.ndim == 2:  # モノクロ
                pass
            elif new_image.shape[2] == 3:  # カラー
                new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
            elif new_image.shape[2] == 4:  # 透過
                new_image = cv2.cvtColor(new_image, cv2.COLOR_BGRA2RGBA)
            new_image = Image.fromarray(new_image)
            return new_image

        if ext == ".gif":
            img = pil2cv(Image.open(read_tmp))
        else:
            img = pil2cv(cv2pil(cv2.imread(read_tmp, -1)))
        os.remove(read_tmp)

        #リサイズ
        resize_img = resize(img, base_w, base_h)

        #名前を変更した画像を書き込み(日本語名の画像をOpenCVが書き込めないため)，リネーム
        write_tmp = "{}/tmp.png".format(output_dir)
        cv2.imwrite(write_tmp, resize_img)
        os.rename(write_tmp, "{}/{}.png".format(output_dir, root))

if __name__ == '__main__':
    main()
