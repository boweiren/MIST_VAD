python UCF_I3D_train.py --gpus 0,1,2,3 --gpu0sz 0.8 --lr 1e-4 --batch_size 10 --clip_num 3 --pretrained_backbone --freeze_bn --freeze_backbone --freeze_bn_epochs 30 --freeze_epochs 30 --warmup_epochs 5 --epochs 301
