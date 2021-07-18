.PHONY: deploy
deploy:
	@zip -r todo.zip *
	@echo '#!/usr/local/bin/python3' | cat - todo.zip > todo
	@rm todo.zip
	@chmod +x todo
	@mv todo /Users/bradley/bin
