import os
import sys
import shutil

args = sys.argv

if len(args) != 3:
    exit('Usage: python comb.py corpora_dir dst_file')

corpora_dir, fin_result_fn = args[1:]

corpora_dir = os.path.abspath(corpora_dir)
fin_result_fn = os.path.abspath(fin_result_fn)

def comb(src_dir, fn_prefix, dst_fn):
    with open(dst_fn, 'wb') as f:
        for fn in os.listdir(src_dir):
            if fn.startswith(fn_prefix) and fn != dst_fn:
                with open(os.path.join(src_dir, fn), 'rb') as g:
                    shutil.copyfileobj(g, f)

comb(corpora_dir, 'news.en', fin_result_fn)

