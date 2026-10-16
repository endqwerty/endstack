import json,glob,os,sys
# A file counts as read when its distinctive text appears in a tool result before the run's first edit of src/.
MARK={'design':'# Design before code','indexS':'Read this whole index before','indexN':"Use this index to select the principle",
      'indexEnd':'[Encode Lessons in Structure](references/encode-lessons-in-structure.md)','build':'Own the change through a reviewable pull request',
      'autopilot':'Own delivery inside an explicit boundary','tdd':'# TDD Bug Fix'}
def stream(f):
    for l in open(f,errors='ignore'):
        try:o=json.loads(l)
        except:continue
        if o.get('type')=='user':
            for it in (o.get('message') or {}).get('content') or []:
                if isinstance(it,dict) and it.get('type')=='tool_result':
                    c=it.get('content'); yield 'out', c if isinstance(c,str) else json.dumps(c)
        if o.get('type')=='assistant':
            for it in o['message'].get('content',[]):
                if it.get('type')=='tool_use': yield 'call', json.dumps(it.get('input'))
        if o.get('type')=='item.completed':
            it=o.get('item') or {}
            if it.get('type')=='command_execution': yield 'call',it.get('command',''); yield 'out', it.get('aggregated_output','')
            if it.get('type')=='file_change': yield 'call','EDIT '+json.dumps(it.get('changes'))
def edits_src(kind,x):
    return ('src/' in x) and (x.startswith('EDIT') or '"old_string"' in x or '"content"' in x or 'apply_patch' in x or 'cat >' in x or "<<'EOF'" in x)
for f in sorted(glob.glob(os.path.expanduser('~/.cache/endstack-design-dryrun/runs/*.jsonl'))):
    seen=set(); first_edit=False
    for kind,x in stream(f):
        if kind=='call' and edits_src(kind,x): first_edit=True
        if kind=='out' and not first_edit:
            for k,m in MARK.items():
                if m.replace('\\n','\n') in x: seen.add(k)
    idx=('indexS' in seen or 'indexN' in seen) and 'indexEnd' in seen
    print(os.path.basename(f)[:-6].ljust(20),'design' if 'design' in seen else '-','INDEX' if idx else ('part' if ('indexS' in seen or 'indexN' in seen) else '-'),' '.join(k for k in ('build','autopilot','tdd') if k in seen))
