all: black stage commit push

black:
	find ./ -name "*.py" | xargs black

stage:
	git add .

commit:
	git commit -m "testing"

push:
	git push origin main
	git push server main
	