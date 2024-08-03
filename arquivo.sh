#!/bin/bash

PROJECT_DIR=$(pwd)
VENV_DIR="$PROJECT_DIR/venv"

echo "Atualizando o sistema..."
sudo apt update && sudo apt upgrade -y

echo "Instalando pacotes básicos..."
sudo apt install -y python3 python3-venv python3-pip

echo "Criando ambiente virtual..."
python3 -m venv $VENV_DIR

echo "Ativando o ambiente virtual..."
source $VENV_DIR/bin/activate

echo "Instalando dependências..."
pip install --upgrade pip
pip install Pillow

echo "Dependências instaladas. Para iniciar o aplicativo, execute:"
echo "source $VENV_DIR/bin/activate"
echo "python3 arquivo.py"

echo "Instalação concluída!"

