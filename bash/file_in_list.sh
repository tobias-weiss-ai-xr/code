WORD_LIST="one two three"
MATCH="two2"

if echo $WORD_LIST | grep -w $MATCH > /dev/null; then
    echo $MATCH
else
	echo "Not found"
    exit 1
fi
