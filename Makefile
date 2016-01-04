# Idea from: 
#* http://stackoverflow.com/questions/637227/makefile-for-multi-file-latex-document
#* http://stackoverflow.com/questions/4058840/makefile-that-distincts-between-windows-and-unix-like-systems

.PHONY: all clean
CLASSES = 00 1A 1B 1C 1D 2A 2B 2C 2D 3A 3B 3C 3D 4A 4B 4C 4D 4E 4F 4G 4H 5A 5B 5C 5D 5E 5F 5G 6 all
MAIN = CourseraMOOC

ifdef SystemRoot
	RM = -del /Q/F
	SUBDIR = classes\\
else
	RM = -rm -f
	SUBDIR = classes/
endif

.DEFAULT_GOAL := all
all: clean
	$(foreach FILE, $(CLASSES), $(MAKE) $(FILE);)

$(CLASSES): %:
    # Runs PDF latex on the main file, sending in jobname that is used in 
    # $(MAIN).tex to \input{} the correct class file
	pdflatex --shell-escape --jobname=$(SUBDIR)CourseraMOOC-class-$* $(MAIN).tex;
	mv $(SUBDIR)CourseraMOOC-class-$*.pdf $(SUBDIR)$*.pdf
	open $(SUBDIR)$*.pdf
	#open $(SUBDIR)2014-TrojanUV-$*.pdf

clean:  
    # Windows requires one wildcard entry per line, unfortunately
	$(RM) *.log
	$(RM) *.aux
	$(RM) *.out
	$(RM) *.idx
	$(RM) *.lof
	$(RM) *.lot
	$(RM) *.nav
	$(RM) *.toc
	$(RM) *.ilg
	$(RM) *.ind
	$(RM) *.glo
	$(RM) *.gls
	$(RM) *.snm
	$(RM) *.vrb
	$(RM) $(SUBDIR)*.log
	$(RM) $(SUBDIR)*.aux
	$(RM) $(SUBDIR)*.out
	$(RM) $(SUBDIR)*.idx
	$(RM) $(SUBDIR)*.lof
	$(RM) $(SUBDIR)*.lot
	$(RM) $(SUBDIR)*.nav
	$(RM) $(SUBDIR)*.toc
	$(RM) $(SUBDIR)*.ilg
	$(RM) $(SUBDIR)*.ind
	$(RM) $(SUBDIR)*.glo
	$(RM) $(SUBDIR)*.gls
	$(RM) $(SUBDIR)*.snm
	$(RM) $(SUBDIR)*.vrb
