#/bin/bash
if [$1 == ""]; then
	echo "Usage: ./update.sh [commit-msg]"
else
	git add .
	git commit -m "$1"
	git push
fi