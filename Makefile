DEV_FLAGS = -e development \
	--config config.yml,config.toml,config.dev.toml \
	--buildDrafts --buildFuture --logLevel info

build: ## build site
	hugo -e production --minify --gc --cleanDestinationDir --logLevel info

dev: ## build dev site
	hugo $(DEV_FLAGS) --gc --cleanDestinationDir

serve: ## serve dev site
	hugo server $(DEV_FLAGS) --disableFastRender

-include .task.mk
$(if $(filter help,$(MAKECMDGOALS)),$(if $(wildcard .task.mk),,.task.mk: ; curl -fsSL https://raw.githubusercontent.com/daylinmorgan/task.mk/v23.1.2/task.mk -o .task.mk))
