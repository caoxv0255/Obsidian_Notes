import os
BASE = r'C:\Users\CaoXv\Documents\obsidian_files\XuCao'

def tree(path, prefix='', max_depth=5, depth=0):
    if depth > max_depth or not os.path.isdir(path):
        return
    try:
        entries = sorted(os.listdir(path))
    except:
        return
    for i, e in enumerate(entries):
        full = os.path.join(path, e)
        is_last = i == len(entries)-1
        connector = '\\- ' if is_last else '|- '
        if os.path.isdir(full):
            try:
                sub = os.listdir(full)
            except:
                sub = []
            md_count = sum(1 for x in sub if x.endswith('.md'))
            has_files = any(not os.path.isdir(os.path.join(full, x)) for x in sub)
            tag = ' [F]' if has_files else ''
            print(f'{prefix}{connector}{e}/ ({md_count}md{tag})')
            tree(full, prefix+('   ' if is_last else '|  '), max_depth, depth+1)
        else:
            print(f'{prefix}{connector}{e}')

for d in ['MY_Learning', '按学科笔记']:
    print(f'\n=== {d} ===')
    tree(os.path.join(BASE, d), max_depth=5)
