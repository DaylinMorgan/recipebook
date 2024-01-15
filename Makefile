serve: ## start dev build of site
	HUGO_MODULE_REPLACEMENTS="github.com/daylinmorgan/simple-recipe -> simple-recipe" \
		hugo serve --buildDrafts --buildFuture --logLevel info

dev-build: ## build with local theme
	HUGO_MODULE_REPLACEMENTS="github.com/daylinmorgan/simple-recipe -> simple-recipe" \
		hugo

-include .task.cfg.mk .task.mk
$(if $(filter help,$(MAKECMDGOALS)),$(if $(wildcard .task.mk),,.task.mk: ; curl -fsSL https://raw.githubusercontent.com/daylinmorgan/task.mk/v23.1.1/task.mk -o .task.mk))
