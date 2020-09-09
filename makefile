all:$(f)
	python $(f)
git:
	git add *
	git commit -m --all
	git push origin master
