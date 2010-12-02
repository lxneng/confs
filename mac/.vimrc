set guifont=Monaco\ 16
"colorscheme desert
colorscheme vividchalk
set nocompatible
set number
filetype on
set history=1000
set background=dark
syntax enable
syntax on
set autoindent
set smartindent
set tabstop=4
set shiftwidth=4
set showmatch
set guioptions-=T
set vb t_vb=
set ruler
set nohls
set incsearch
set nobackup
set helplang=cn
set nocompatible
filetype plugin indent on
let Tlist_Show_One_File=1
let Tlist_Exit_OnlyWindow=1
"let g:winManagerWindowLayout='FileExplorer|TagList'
"let g:winManagerWindowLayout='NERDTree|TagList'
nmap wm :WMToggle<cr>
nmap nt :NERDTree<cr>
ino <c-j> <c-r>=TriggerSnippet()<cr>
snor <c-j> <esc>i<right><c-r>=TriggerSnippet()<cr>
let g:pydiction_location = '/Users/eric/.vim/ftplugin/pydiction/complete-dict'
" vimwiki
let g:vimwiki_use_mouse = 1
let g:vimwiki_list = [{'html_header': '~/vimwiki_html/header.tpl'}]
