import argparse
import os
def parse_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('--MODEL', type=str, default='C3D')
    parser.add_argument('--train', type=str, default='SGA')

    parser.add_argument('--expand_k',type=int,default=8)
    parser.add_argument('--label_smoothing',type=float,default=0)
    parser.add_argument('--hard_label',dest='use_hard_label',action='store_true')
    parser.set_defaults(use_hard_label=False)
    parser.add_argument('--batch_size',type=int,default=32)
    parser.add_argument('--clip_num',type=int,default=3)
    parser.add_argument('--epochs',type=int,default=301)
    parser.add_argument('--accumulate_step',type=int,default=5)

    parser.add_argument('--lr',type=float,default=1e-4)
    parser.add_argument('--weight_decay',type=float,default=5e-4)
    parser.add_argument('--optim',type=str,default='adam')
    parser.add_argument('--dropout_rate',type=float,default=0.8)
    parser.add_argument('--grad_clip',type=float,default=20)
    parser.add_argument('--warmup_epochs',type=int,default=5)

    parser.add_argument('--freeze_backbone',dest='train_backbone',action='store_false')
    parser.set_defaults(train_backbone=True)
    parser.add_argument('--freeze_blocks',type=str,default='conv1a,conv2a,conv3a,conv3b,conv4a,conv4b,conv5a,conv5b')
    parser.add_argument('--train_all',dest='pretrained_backbone',action='store_false')
    parser.set_defaults(pretrained_backbone=True)
    parser.add_argument('--freeze_epochs',type=int,default=30)

    parser.add_argument('--segment_len',type=int,default=16)

    parser.add_argument('--gpus',type=str,default='0,1,2,3')
    parser.add_argument('--gpu0sz',type=float,default=0.9)

    parser.add_argument('--loss_type',type=str,default='CE')

    # for test time augmetation
    parser.add_argument('--test_ten_crop',dest='ten_crop',action='store_true')
    parser.set_defaults(ten_crop=False)
    # loss balance hypermeters
    parser.add_argument('--lambda_base',type=float,default=1.0)
    parser.add_argument('--lambda_att',type=float,default=1.0)

    parser.add_argument('--class_reweights',type=str,default='1,1')
    parser.add_argument('--gradcam_pp',dest='grad_pp',action='store_true')
    parser.set_defaults(grad_pp=False)
    # path setting
    parser.add_argument('--machine',type=str,default='data0',help='data0 in keylab , other may different for as the environment change')

    args=parser.parse_args()
    args.machine='/'+args.machine
    os.environ['CUDA_VISIBLE_DEVICES']=args.gpus
    args.gpus=[i for i in range(len(args.gpus.split(',')))]
    args.freeze_blocks=[i for i in args.freeze_blocks.split(',')]
    args.class_reweights=[float(i) for i in args.class_reweights.split(',')]

    return args
