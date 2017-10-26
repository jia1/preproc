COR_DIR=../1-billion-word-language-modeling-benchmark-r13output/training-monolingual.tokenized.shuffled/
COR_FIL=1b-training-corpus.txt
nohup time python comb-corpora.py $COR_DIR $COR_FIL &> nohup-comb-corpora.out &
