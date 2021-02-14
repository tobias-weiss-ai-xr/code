#!/bin/sh
function indexlt {
    STY=$1
    OPT=$2
    OUT=$3
    PKG=$4
    IDX=$5
    if test "$OUT" == ""; then
	OUT=$STY
    fi
    if test "$STY" != ""; then
	STY="-s $STY"
    fi
    IDX=indextst$IDX
    OUT="indextst-$OUT"
    echo " COMPILING WITH $STY.ist as $OUT"
    LATEXOPT="\input{indextst.tex}"
    if test "$PKG" != ""; then
	LATEXOPT="\def\stypkg{$PKG}$LATEXOPT"
    fi
#    latex -quiet -job-name $OUT $LATEXOPT
    makeindex -q -c $OPT -o $OUT.ind $STY $IDX.idx
    latex -quiet -job-name $OUT $LATEXOPT
    dvips -q -E -o $OUT.eps $OUT.dvi
    epstopdf --outfile=$OUT.pdf $OUT.eps
#    start lit-$OUT.eps
}

#sed -e 's/!/>/g;s/@/=/g;s/"/!/g;' indextst.idx > indextst2.idx


if test "$1" != ""; then
    indexlt $*
    exit
fi

indexlt "" "" "default"
indexlt latex
indexlt din 
indexlt iso
indexlt wb 
indexlt gind "" "" "\usepackage{doc}" 
#indexlt bbind "" "" "\usepackage{doc}" "2"


