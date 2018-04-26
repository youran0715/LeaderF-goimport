" ============================================================================
" File:        leaderf.vim
" Description:
" Author:      Wu Hong <wuhong40@gmail.com>
" Website:     https://github.com/wuhong40
" Note:
" License:     Apache License, Version 2.0
" ============================================================================

command! -bar -nargs=0 LeaderfGoimport call leaderf#Goimport#startExpl(g:Lf_WindowPosition)
command! -bar -nargs=0 LeaderfGoimportCword call leaderf#Goimport#startExplPattern(g:Lf_WindowPosition, expand('<cword>'))

call g:LfRegisterSelf("LeaderfGoimport", "navigate the goimport")
