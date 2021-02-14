#!/bin/bash
function biblt {
    STY=$1
    BST=$2
    OPT=$3
    EPS=$4
    MAC=$5
    if test "$EPS" == ""; then
#	echo "empty EPS: $EPS $BST"
	EPS=$BST
    fi
    echo "COMPILING $BST.bst WITH $STY.sty as $EPS"
    LATEXOPT="\def\litsty{$STY}\def\litbst{$BST}\def\litopt{$OPT}\input{litdok.tex}"
    if test $MAC; then
	LATEXOPT="\def\mycite{$MAC}$LATEXOPT"
    fi    
    latex -quiet -job-name lit-$EPS $LATEXOPT
    bibtex -quiet lit-$EPS
    latex -quiet -job-name lit-$EPS $LATEXOPT
    latex -quiet -job-name lit-$EPS $LATEXOPT
    dvips -q -E -o lit-$EPS.eps lit-$EPS.dvi
    epstopdf --outfile=lit-$EPS.pdf lit-$EPS.eps
#    start lit-$EPS.eps
}

if test "$1" != ""; then
    biblt $*
    exit
fi

biblt "" plain
biblt "" unsrt
biblt "" alpha
biblt "" abbrv
#biblt bibgerm gerplain
#biblt bibgerm gerunsrt
#biblt bibgerm geralpha
#biblt bibgerm gerabbrv
biblt "" plaindin
biblt "" unsrtdin
biblt "" alphadin
biblt "" abbrvdin
biblt natbib plainnat
biblt natbib plainnat "" "plainnatp" "\citep"
biblt natbib plainnat "numbers" "plainnatn"
biblt natbib plainnat "super" "plainnats"
biblt natbib unsrtnat
biblt natbib abbrvnat
biblt natbib dinat
biblt natbib dinat "" "dinatp" "\citep"
biblt cite alpha "" cite
#biblt overcite alpha "" overcite
#biblt overcite,bibgerm alpha "" bibgermovercite
biblt babelbib babplain
#biblt babelbib babplai3
biblt babelbib babunsrt
biblt babelbib babalpha
biblt babelbib bababbrv
biblt jurabib jurabib
#biblt jurabib jurabib "" "jurabib-foot" "\footcite"
biblt jurabib jurabib "" "jurabib-footfull" "\footfullcite"
biblt jurabib jureco
biblt jurabib jurunsrt
biblt jurabib jox
#biblt babelbib babamspl
#biblt babelbib bababbr3

latex -quiet litdokbu
bibtex -quiet bu1
bibtex -quiet bu2
latex -quiet litdokbu
latex -quiet litdokbu
dvips -q -E -o litdokbu.eps litdokbu.dvi
epstopdf --outfile=litdokbu.pdf litdokbu.eps
