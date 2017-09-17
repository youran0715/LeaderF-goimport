" ============================================================================
" File:        Goimport.vim
" Description:
" Author:      WuHong <wuhong40@gmail.com>
" Website:     https://github.com/wuhong40
" Note:
" License:     Apache License, Version 2.0
" ============================================================================

if leaderf#versionCheck() == 0
    finish
endif

exec g:Lf_py "import vim, sys, os.path"
exec g:Lf_py "cwd = vim.eval('expand(\"<sfile>:p:h\")')"
exec g:Lf_py "sys.path.insert(0, os.path.join(cwd, 'python'))"
exec g:Lf_py "from goimportExpl import *"

function! leaderf#Goimport#Maps()
    nmapclear <buffer>
    nnoremap <buffer> <silent> q    :exec g:Lf_py "goimportExplManager.quit()"<CR>
    nnoremap <buffer> <silent> i    :exec g:Lf_py "goimportExplManager.input()"<CR>
    nnoremap <buffer> <silent> <F1> :exec g:Lf_py "goimportExplManager.toggleHelp()"<CR>
endfunction

function! leaderf#Goimport#startExpl(win_pos, ...)
    call leaderf#LfPy("goimportExplManager.startExplorer('".a:win_pos."')")
endfunction
