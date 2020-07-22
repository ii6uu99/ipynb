" VIM filetype plugin file
" Language:	IDL (Interactive Data Language)
" Maintainer:	Luke Domanski <luke.a.domanski@gmail.com>
" Last Change:	2012 Aug 27

if exists("b:did_ftplugin") | finish | endif
let b:did_ftplugin = 1


if exists("loaded_matchit")
	let b:match_words='\<[iI][fF]\>:\<\%([tT]hen\|THEN\)\%(\s+[bB]egin\|\s+BEGIN\)\@!\>:\<\%([eE]nd[iI][fF]\s+\|ENDIF\s+\)\@<!\%([eE]lse|ELSE\)\>,'
		\ . '\<[iI][fF]\>:\<\%([tT]hen\|THEN\)\s+\%([bB]egin\|BEGIN\)\>:\<\%([eE]nd[iI][fF]\|ENDIF\)\>,'
		\ . '\<[iI][fF]\>:\<\%([tT]hen\|THEN\)\s+\%([bB]egin\|BEGIN\)\>:\<\%([eE]nd[iI][fF]\s+\|ENDIF\s+\)\%([eE]lse\s+|ELSE\s+\)\%([bB]egin\|BEGIN\)\>:\<\%([eE]nd[eE]lse\|ENDELSE\)\>,'
		\ . '\<\%([fF]or\|FOR\)\>:\<\%([eE]nd[fF]or\|ENDFOR\)\>,'
		\ . '\<\%([wW]hile\|WHILE\)\>:\<\%([eE]nd[wW]hile|ENDWHILE\)\>,'
		\ . '\<\%([rR]epeat\|REPEAT\)\>:\<\%([uU]ntil\|UNTIL\)\>,'
		\ . '\<\%([cC]ase\|CASE\)\>:\<\%([eE]lse\|ELSE\)\:\>:\<\%([eE]nd[cC]ase\|ENDCASE\)\>,'
		\ . '\<\%([sS]witch\|SWITCH\)\>:\<\%([eE]lse\|ELSE\)\:\>:\<\%([eE]nd[sS]witch\|SWITCH\)\>,'
		\ . '\<\%([pP]ro\|PRO\|[fF]unction\|FUNCTION\)\>:\<\%([eE]nd\|END\)\>,'
endif

