test:
	pipenv run python . -i stdin.png > test/regression.txt
	@echo '... should not produce a changed file, or there is a regression!'
	git status

.PHONY: test
