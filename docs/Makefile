SPHINXOPTS =
SPHINXBUILD = sphinx-build
SOURCEDIR = source
BUILDDIR = build

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo $(CWD)
	@if [ "$@" = "html" ]; then rm build/html/.buildinfo build/html/objects.inv; fi