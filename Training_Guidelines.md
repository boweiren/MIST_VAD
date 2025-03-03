# Training Guideline
## 1. Overview of MIST framework
![Structure of MIST](Structure_New-1.png)
The framework consists of two stages, i.e., Pseudo labels generation and Feature Encoder Finetuning.
For the first stage, we train a MIL-based pseudo labels generator with pre-extracted features. 
As for the other stage, we train the self-guided attention enhanced feature encoder with the pseudo labels.

## 2. Environment Preparation
- python>=3.6
- apex
- pytorch=1.5.0+cu101
- torchvision=0.6.0+cu101
- tensorboardX
- h5py
- opencv
- scikit-learn
- yacs


**[ Attention!! ] Before doing any further, remember that the paths in the codes may need to be modified to adapt to your environment.**

## 3. Data Preparation
Pre-extracted features for ShanghaiTech are uploaded on [SHT_Feats_for_MIL](https://1drv.ms/u/s!Ai48CHyipiNUkFTHTQGze7QLY1Fn?e=lhkr0i).
Moreover the Kinetics pretrained I3D model and Sport-100M pretrained C3D model are uploaded on [pretrained_models](https://1drv.ms/u/s!Ai48CHyipiNUkFTHTQGze7QLY1Fn?e=lhkr0i).
You should download all of them and place them in the proper place as `configs/constant.py` indicates.

~~Specifically, the `test_frame_mask` of ShanghaiTech is downloaded from [Download](https://svip-lab.github.io/dataset/campus_dataset.html).~~
`test_frame_mask` is uploaded in `data/test_frame_mask/` now.

**[Update!]** As the original ShanghaiTech dataset link is not worked now. I uploaded the h5py file for ShanghaiTech and its corresponing annotations are uploaded on `[BaiduYun]` with multiple sub-files, you can open/unzip it with `WinRAR`

[BaiduYun link](https://pan.baidu.com/s/1sQUGXj-BnLDGczWuGkBWdA), code：`kym5`

## 4. Stage 1 training
The stage 1 is to generate pseudo labels.
First we train the MIL-based generator.
```shell script
python stage1training/train_MIL_generator.py 
```
Then, generate pseudo labels with the command below:
```shell script
python stage1training/train_MIL_generator.py --generate_PL 
```

## 5. Stage 2 training
You are recommend to use the pseudo labels generated by us, which is placed in `data/`.

The commands of training C3D/I3D for ShanghaiTech and UCF-Crime dataset are writen in bash files.
You can execute the command as below:
```shell script
cd stage2training
% for SHT_C3D
bash SHT_C3D_train.sh
% for SHT_I3D
bash SHT_I3D_train.sh
% for UCF_C3D
bash UCF_C3D_train.sh
``` 
