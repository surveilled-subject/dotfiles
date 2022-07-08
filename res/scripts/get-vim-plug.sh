#!/usr/bin/env bash

echo "getting vim-plug..."

curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

echo "complete!"
