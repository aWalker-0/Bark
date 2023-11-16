# Installing the Prerequisites

Install packages via the `requirements.txt` file (include IPython if you want):

> `pip install -r requirements.txt`

Or

> `pip install git+https://github.com/suno-ai/bark.git`


In order to use the GPU, you need to install [Pytorch CUDA](https://pytorch.org/get-started/locally/).
![[gettin-started-locally-pytorch.png]]


If you don't know what version of CUDA you have, then use `nvidia-smi` in the Windows Terminal: 
![[terminal_nvidia-smi.png]]


If it doesn't display anything, then the CUDA toolkit probably isn't installed. Download and install it [here](https://developer.nvidia.com/cuda-downloads).


With those things installed, create a new python file and paste this code inside of it (comment out the IPython stuff if you don't use it).