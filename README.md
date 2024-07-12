## emex

Emex helps you run a chat with an LLM locally, via a terminal.

![Demo Video](./demo.gif)

### Usage
Future plans to integrate with a package manager (brew/pip)

- first clone this repo & cd into project root
- create a python environment (preferred) 
```
python3 -m venv create .env
source .env/bin/activate
```
- install the dependencies
```
pip install .
```
- simply run using 
```
emex run username/modelname
```
Here, username/modelname refers to the huggingface model you choose to run locally. To browse the list of compatible models, you can browse all the models on HugginFace under the [mlx-community here](https://hugginface.co/mlx-community)

### Currently Supported Models:

- microsoft/phi-2
- gemma-2b

All models currently used are using models from the mlx-community. Other models from mlx-community within hugginface should work out of the box but are yet to be tested. 

The cli uses mlx_lm and mlx to generate text

### Features

- Generate text using local LLMs via MLX
- Verbose mode to print metrics like Tokens/Sec, (TTFS) Time to first token & Total Time taken for generation

