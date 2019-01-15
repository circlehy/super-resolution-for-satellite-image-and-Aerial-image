from easydict import EasyDict as edict
import json

config = edict()
config.TRAIN = edict()

## Adam
config.TRAIN.batch_size = 144
config.TRAIN.lr_init = 1e-4
config.TRAIN.beta1 = 0.9

## initialize G
config.TRAIN.n_epoch_init = 50
    # config.TRAIN.lr_decay_init = 0.1
    # config.TRAIN.decay_every_init = int(config.TRAIN.n_epoch_init / 2)

## adversarial learning (SRGAN)
config.TRAIN.n_epoch = 100
config.TRAIN.lr_decay = 0.1
config.TRAIN.decay_every = int(config.TRAIN.n_epoch / 2)

## train set location
#config.TRAIN.hr_img_path = '/home/huangyuan/Pictures/train data for stapics/city_17_6000/'
#config.TRAIN.hr_img_path = '/home/huangyuan/Pictures/train data for stapics/16_17/'
#config.TRAIN.hr_img_path = '/media/hy/hy/new_17/Japan17/input_test/'
config.TRAIN.hr_img_path = '/home/hy/face_attribute/'
#config.TRAIN.hr_img_path = '/home/hy/for_face/temp_test/'
#config.TRAIN.lr_img_path = '/data/dataset/pr/DIV2K_train_LR_bicubic/X4/'
#config.TRAIN.lr_img_path = '/data/dataset/pr/DIV2K_train_LR_bicubic_X2/DIV2K_train_LR_bicubic/X2/'
#config.TRAIN.lr_img_path = '/data/dataset/pr/bpg_x2_train_1616mode/'
#config.TRAIN.lr_img_path = '/data/dataset/pr/DIV2K_train_LR_bicubic_X3/DIV2K_train_LR_bicubic/X3/'

config.VALID = edict()
## test set location
#config.VALID.hr_img_path = '/data/dataset/pr/DIV2K_valid_HR/'
#config.VALID.lr_img_path = '/data/dataset/pr/DIV2K_valid_LR_bicubic/X4/'
#config.VALID.lr_img_path = '/data/dataset/pr/DIV2K_valid_LR_bicubic_X2/DIV2K_valid_LR_bicubic/X2/'
#config.VALID.lr_img_path = '/data/dataset/pr/bpg_x2_valid_1616mode/'
#config.VALID.lr_img_path = '/home/huangyuan/workspace/project for SR  satpic/test_img_level15/'

def log_config(filename, cfg):
    with open(filename, 'w') as f:
        f.write("================================================\n")
        f.write(json.dumps(cfg, indent=4))
        f.write("\n================================================\n")
