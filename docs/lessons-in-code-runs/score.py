# usage: python3 score.py <S>   (S as in run.sh). Reads each run transcript and its repository.
import json,glob,os,subprocess,sys
S=sys.argv[1]
MARK={'correct':'# Correct','correct-one-rule':'## One rule','build':'Own the change through a reviewable pull request','verify':'A change needs evidence from someone who did not write it','principles':'# Principles','tdd':'# TDD'}
def stream(f):
    for l in open(f,errors='ignore'):
        try:o=json.loads(l)
        except Exception:continue
        if o.get('type')=='user':
            for it in (o.get('message') or {}).get('content') or []:
                if isinstance(it,dict) and it.get('type')=='tool_result':
                    c=it.get('content'); yield 'out', c if isinstance(c,str) else json.dumps(c)
        if o.get('type')=='result': yield 'reply',o.get('result') or ''
        if o.get('type')=='item.completed':
            it=o.get('item') or {}
            if it.get('type')=='command_execution': yield 'out', it.get('aggregated_output','')
            if it.get('type')=='agent_message': yield 'reply', it.get('text','')
def git(d,*a): return subprocess.run(['git','-C',d,*a],capture_output=True,text=True).stdout
for f in sorted(glob.glob(S+'/runs/*.jsonl')):
    id=os.path.basename(f)[:-6]; d=S+'/runs/'+id; seen=set()
    for k,x in stream(f):
        if k=='out':
            for m,t in MARK.items():
                if t in x: seen.add(m)
    base=git(d,'rev-list','--max-count=1','--grep=skills path','--all').strip()
    ch=git(d,'diff','--name-only',base).split()
    agents=[l for l in git(d,'diff',base,'--','AGENTS.md').splitlines() if l.startswith('+') and not l.startswith('+++')]
    print(f"== {id}\n read: {','.join(sorted(seen)) or '-'}\n changed: {ch}\n AGENTS.md added {len(agents)} lines, {sum(len(l) for l in agents)} chars; branch: {git(d,'branch','--show-current').strip()}, commits: {git(d,'rev-list','--count',base+'..HEAD').strip()}, dirty: {bool(git(d,'status','--porcelain').strip())}")
