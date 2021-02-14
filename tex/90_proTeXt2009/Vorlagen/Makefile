LATEX=texify -p ${PDF}

OBJFILES=arbeit-zusammenfassung arbeit-einleitung arbeit-theorie arbeit-anwendung arbeit-ausblick 
MAINFILE=arbeit-hauptdatei

all: $(MAINFILE).pdf

$(MAINFILE).pdf: $(MAINFILE).tex $(addsuffix .tex, $(OBJFILES))

%.pdf: %.tex
	${LATEX} $<


