#!/bin/bash

# 警告：这是一个临时的脚本，仅用于内部使用和提供给实习生学习
#       这个脚本的正确性依赖于 members.md 的格式。

die () {
	echo "$*"
	exit 3
}

LIST='members.md'
[ -f "$LIST" ] || LIST='../members.md'
[ -f "$LIST" ] || die "No members.md found"

[ -d 'pubkeys' ] || mkdir pubkeys || die "pubkeys/ creation failed"

cat "$LIST" | grep '|' | tail -n +3 | cut -f6 -d'|' | \
while read s; do
	echo "====$s===="
	curl https://github.com/${s}.keys > pubkeys/pubkeys.${s}
done

echo "Have a nice day."
