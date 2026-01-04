#!/usr/bin/zsh
#sudo docker run sherlock/sherlock $1--nsfw
set -o pipefail
for url in "$@"; do
	echo "finding $url"
	sudo docker run sherlock/sherlock $url --nsfw
done
