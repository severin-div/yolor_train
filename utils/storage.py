import argparse
import datetime
import shutil
import os


def save_results(path):
    now = datetime.datetime.now()
    path_out = os.path.join(path, 'runs', now.strftime('%Y-%m-%d--%H-%M-%S'))
    if os.path.exists(path_out):
        shutil.rmtree(path_out)
    shutil.copytree('/content/yolor_train/runs/train/', path_out)
    print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----")
    print()
    print(f'RESULTS SAVED to {path_out}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='', help='NN run save path')
    opt = parser.parse_args()
    save_results(opt.path)

