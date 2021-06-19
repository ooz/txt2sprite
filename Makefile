test:
	@echo '1. Image to text:'
	pipenv run python . -i stdin.png > test/regression.txt
	@echo '2. Text to image:'
	pipenv run python . < example.txt
	@echo '... should not produce a changed file,'
	@echo 'otherwise there is a regression!'
	git status

.PHONY: test
