#!/usr/bin/env python3
"""
修复 Obsidian 风格的 Wiki 链接的确定性问题：
- 指向文件夹的链接 -> 指向该文件夹下的 README.md / index.md / 00_index.md / foldername.md（优先顺序）
- 指向不存在的目标但在仓库中唯一匹配的 basename -> 替换为相对路径链接

运行后会在仓库根目录生成 `link_fix_report.json`，并在 `.link_fix_backups/` 中保存被修改文件的备份。
"""
import os
import re
import json
from pathlib import Path

ROOT = Path(r"c:\Users\CaoXv\Documents\obsidian_files\XuCao")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")

INDEX_CANDIDATES = ["README.md", "index.md", "00_index.md"]

def find_md_files(root: Path):
    return [p for p in root.rglob('*.md') if p.is_file()]

def build_maps(md_files):
    by_rel = {str(p.relative_to(ROOT)).replace('\\','/'): p for p in md_files}
    by_name = {}
    for p in md_files:
        name = p.stem
        by_name.setdefault(name, []).append(p)
    return by_rel, by_name

def choose_index_in_dir(d: Path):
    for name in INDEX_CANDIDATES:
        cand = d / name
        if cand.is_file():
            return cand
    # try foldername.md
    cand = d / (d.name + '.md')
    if cand.is_file():
        return cand
    return None

def rel_link(from_path: Path, to_path: Path):
    rel = os.path.relpath(to_path.with_suffix(''), start=from_path.parent)
    return rel.replace('\\','/')

def process_file(path: Path, by_rel, by_name):
    text = path.read_text(encoding='utf-8')
    changed = False
    fixes = []
    def repl(m):
        nonlocal changed
        raw = m.group(1).strip()
        target_part = raw.split('|',1)[0].split('#',1)[0].strip()
        anchor = ''
        if '#' in raw:
            anchor = '#' + raw.split('#',1)[1]
        alias = None
        if '|' in raw:
            alias = raw.split('|',1)[1]

        # If target looks like a path (contains / or startswith . or ..)
        if '/' in target_part or target_part.startswith('.'):
            # normalize relative candidate
            candidate = target_part
            if not candidate.lower().endswith('.md'):
                candidate_md = candidate + '.md'
            else:
                candidate_md = candidate
            resolved = (path.parent / candidate_md).resolve()
            # if points to directory
            dir_try = (path.parent / target_part).resolve()
            if dir_try.exists() and dir_try.is_dir():
                idx = choose_index_in_dir(dir_try)
                if idx:
                    new_link = rel_link(path, idx) + anchor
                    changed = True
                    fixes.append((target_part, str(idx)))
                    if alias:
                        return f'[[{new_link}|{alias}]]'
                    else:
                        return f'[[{new_link}]]'
            # if file exists as resolved
            if resolved.exists() and resolved.is_file():
                new_link = rel_link(path, resolved) + anchor
                changed = True
                fixes.append((target_part, str(resolved)))
                if alias:
                    return f'[[{new_link}|{alias}]]'
                else:
                    return f'[[{new_link}]]'
            # else leave unchanged
            return m.group(0)

        # target is simple name
        # exact relative at repo root?
        cand_rel = target_part + '.md'
        if cand_rel in by_rel:
            return m.group(0)
        # unique match by name anywhere
        found = by_name.get(target_part, [])
        if len(found) == 1:
            target_file = found[0]
            new_link = rel_link(path, target_file) + anchor
            changed = True
            fixes.append((target_part, str(target_file)))
            if alias:
                return f'[[{new_link}|{alias}]]'
            else:
                return f'[[{new_link}]]'
        # maybe points to a directory at repo root
        dir_try = (ROOT / target_part)
        if dir_try.exists() and dir_try.is_dir():
            idx = choose_index_in_dir(dir_try)
            if idx:
                new_link = rel_link(path, idx) + anchor
                changed = True
                fixes.append((target_part, str(idx)))
                if alias:
                    return f'[[{new_link}|{alias}]]'
                else:
                    return f'[[{new_link}]]'
        return m.group(0)

    new_text = WIKILINK_RE.sub(repl, text)
    return changed, new_text, fixes

def main():
    md_files = find_md_files(ROOT)
    by_rel, by_name = build_maps(md_files)
    report = {'scanned_files': len(md_files), 'modified_files': [], 'fixes_total': 0, 'skipped_ambiguous': 0}
    backup_root = ROOT / '.link_fix_backups'
    backup_root.mkdir(parents=True, exist_ok=True)
    for p in md_files:
        changed, new_text, fixes = process_file(p, by_rel, by_name)
        if changed:
            relp = str(p.relative_to(ROOT)).replace('\\','/')
            bpath = backup_root / (relp.replace('/','__') + '.bak')
            bpath.parent.mkdir(parents=True, exist_ok=True)
            bpath.write_text(p.read_text(encoding='utf-8'), encoding='utf-8')
            p.write_text(new_text, encoding='utf-8')
            report['modified_files'].append({'file': relp, 'fixes': fixes})
            report['fixes_total'] += len(fixes)

    report_path = ROOT / 'link_fix_report.json'
    report['modified_count'] = len(report['modified_files'])
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Done. Report:', report_path)

if __name__ == '__main__':
    main()
