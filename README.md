# E-NeRV: Expedite Neural Video Representation with Disentangled Spatial-Temporal Context  (ECCV 2022)

### [Paper](https://arxiv.org/abs/2207.08132)


[Zizhang Li](https://kyleleey.github.io),
Mengmeng Wang,
Huaijin Pi,
Kechun Xu,
Jianbiao Mei,
Yong Liu

This is the official implementation of the paper "E-NeRV: Expedite Neural Video Representation with Disentangled Spatial-Temporal Context".

## Abstract
Recently, the image-wise implicit neural representation of videos, NeRV, has gained popularity for its promising results and swift speed compared to regular pixel-wise implicit representations. However, the redundant parameters within the network structure can cause a large model size when scaling up for desirable performance. The key reason of this phenomenon is the coupled formulation of NeRV, which outputs the spatial and temporal information of video frames directly from the frame index input. In this paper, we propose E-NeRV, which dramatically expedites NeRV by decomposing the image-wise implicit neural representation into separate spatial and temporal context. Under the guidance of this new formulation, our model greatly reduces the redundant model parameters, while retaining the representation ability. We experimentally find that our method can improve the performance to a large extent with fewer parameters, resulting in a more than 8$\times$ faster speed on convergence

## Method overview
<img src=./assets/method.png width="800"  />

## Get started
We run with Python 3.8, you can set up a conda environment with all dependencies like so:

```shell
conda create -n enerv python=3.8
conda activate enerv
pip install -r requirements.txt 
```

## Data
The paper's main experiments were conducted on:
* [data/bunny](./data/bunny) directory contains big buck bunny video sequence
* [UVG](http://ultravideo.fi/#testsequences) video sequences can be found in official website

## Training

### Training experiments
For now, we provide training and evaluation on original NeRV and our E-NeRV, by running following command with different configs and specified ```EXP_NAME```:

```shell
bash scripts/run.sh ./cfgs/E-NeRV-bunny.yaml EXP_NAME 29500
```

The logs and other outputs will be automaically saved to the output directory ```./outputs/EXP_NAME```

## Acknowledgement
Thanks to Hao Chen for his excellent work and implementation [NeRV](https://github.com/haochen-rye/NeRV).

## Contact
If you have any questions, please feel free to email the authors.


## Google Colab
Install python 3.8
```
# first install python 3.8
!sudo apt-get update -y
!sudo apt-get install python3.6
# change alternatives
!sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
# select python version
!sudo update-alternatives --config python3
# check python version
!python --version
# install pip for new python 
!sudo apt-get install python3.6-distutils
!wget https://bootstrap.pypa.io/get-pip.py
!python get-pip.py
# upgrade pip
!sudo apt install python3-pip
!python -m pip install --upgrade pip
```

Install pytorch for cuda11.7
```
!pip uninstall torch
!pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
```