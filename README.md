# Capstone Project 2023

To reproduce the development environment, create the conda environment as follows:

```shell
$ yes | conda create -n capstone_env python==3.10.11
$ conda activate capstone_env
$ pip install -r requirements.txt
```

## Directory Tree

The structure of the directory is as follows:

```
.
├── README.md
├── app: Source code of a web application that allows users to interact with a Bayesian Network model
├── notebooks
├── requirements.txt
└── src: Source code containing utilities and helpers
```