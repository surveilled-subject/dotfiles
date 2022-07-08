set nocompatible

call plug#begin()

Plug 'sainnhe/everforest'

Plug 'chrisbra/colorizer'

call plug#end()

set hlsearch
set incsearch
set nohls

set noswapfile

if has('termguicolors')
  set termguicolors
endif

set background=dark
let g:everforest_disable_italic_comment = 1
let g:everforest_background = 'hard'
let g:everforest_better_performance = 1

colors everforest

hi Comment ctermfg=cyan guifg=#70e0e0
hi SpecialKey guifg=#70e0e0
