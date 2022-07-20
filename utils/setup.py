import os
import torch

def load_cfg(cfg):
    if cfg == 'p6':
        return '/content/yolor_train/cfg/yolor_p6.cfg'
    elif cfg == 'w6':
        return '/content/yolor_train/cfg/yolor_w6.cfg'
    elif cfg == 'csp':
        return '/content/yolor_train/cfg/yolor_csp.cfg'
    elif cfg == 'csp_x':
        return '/content/yolor_train/cfg/yolor_csp_x.cfg'
    else:
        return ''

def load_hyp(imgsz):
    if isinstance(imgsz, list):
        imgsz = imgsz[0]
    if imgsz >= 960 :
        return '/content/yolor_train/data/hyp.scratch.1280.yaml'
    else:
        return '/content/yolor_train/data/hyp.scratch.640.yaml'

def load_weights(data):
    if data['pretrained']:
        return os.path.join(data['folder'], data['pretrained'])
    elif data['base_nn']:
        return data['base_nn']
    else:
        if data['cfg'] == 'p6':
            return '/content/yolor_train/models/behAI_pretrained_yolor_p6.pt'
        elif data['cfg'] == 'w6':
            return '/content/yolor_train/models/behAI_pretrained_yolor_w6.pt'
        else:
            return ''

def load_batch_size():
    name = torch.cuda.get_device_properties(0).name
    if name == 'Tesla T4':
        return 5
    if name == 'Tesla K80':
        return 4
    else:
        return 4

def load_info(opt):
    print('TRAINING STARTED')
    print()
    print('Configuration:')
    print(f'Epochs:\t\t{opt.epochs}')
    print(f'Batch size:\t{opt.batch_size}')
    print(f'Image size:\t{opt.img_size}')
    print(f'Data:\t\t{opt.data}')
    print(f'Weights:\t{opt.weights}')

    print()
    print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----")
    print()

if __name__ == '__main__':
    print()
    print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----")
    print(f"SETUP COMPLETE. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")
