import json,glob,os,subprocess,re
def stream(f):
    for l in open(f,errors='ignore'):
        try:o=json.loads(l)
        except:continue
        if o.get('type')=='user':
            for it in (o.get('message') or {}).get('content') or []:
                if isinstance(it,dict) and it.get('type')=='tool_result':
                    c=it.get('content'); yield 'out', c if isinstance(c,str) else json.dumps(c)
        if o.get('type')=='result': yield 'reply',o.get('result') or ''
        if o.get('type')=='item.completed':
            it=o.get('item') or {}
            if it.get('type')=='command_execution': yield 'out', it.get('aggregated_output','')
            if it.get('type')=='agent_message': yield 'reply', it.get('text','')
MARK={'tdd':'# TDD Bug Fix','tdd-new':'Find every consumer with the same fault','build':'Own the change through a reviewable pull request','design':'# Design before code'}
def git(d,*a): return subprocess.run(['git','-C',d,*a],capture_output=True,text=True).stdout
for f in sorted(glob.glob('runs/*.jsonl')):
    id=os.path.basename(f)[:-6]; d='runs/'+id; seen=set(); reply=''
    for k,x in stream(f):
        if k=='out':
            for m,t in MARK.items():
                if t in x: seen.add(m)
        else: reply=x
    base=git(d,'rev-list','--max-count=1','--grep=skills path','HEAD').strip()
    ch=set(git(d,'diff','--name-only',base,'HEAD').split())
    fixed=[n for n,p in (('cli','src/cli/commands/show.ts'),('web','src/web/pages/change.ts'),('digest','src/integrations/chat/digest.ts')) if p in ch]
    other=sorted(x for x in ch if x not in('src/cli/commands/show.ts','src/web/pages/change.ts','src/integrations/chat/digest.ts'))
    named=[n for n,r in (('web',r'change\.ts|changePage|web page|change page'),('digest',r'digest')) if re.search(r,reply,re.I)]
    print(id.ljust(11),'read:',','.join(sorted(seen)) or '-','| fixed:',fixed,'| reply names:',named,'| other files:',other)
