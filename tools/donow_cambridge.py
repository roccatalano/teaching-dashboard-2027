import json,sys,re
d=json.load(open(sys.argv[1]));L=d['lessons']
Q=json.load(open('/tmp/pz/checkin_q.json'))
SET={'1A-1':'2.1','1A-2':'2.2','1B-1':'2.3','1B-2':'2.3','1C-1':'3.1','1C-2':'3.2','1C-3':'3.2','1C-4':'3.2','2A-1':'4.1','2A-2':'4.4','2A-3':'4.3',
 '2B-1':'5.1','2B-2':'5.2','3A-1':'6.1','3A-2':'6.1','3A-3':'6.1','3A-4':'7.1','3B-1':'6.2','3B-2':'6.2','3B-3':'6.2','3B-4':'6.2','3B-5':'6.2','3C-1':'6.3','3C-2':'6.3','3D-1':'6.3',
 '3E-1':'6.4','3E-2':'6.4','3E-3':'6.4','3E-4':'6.4','3E-5':'6.4','4A-1':'7.1','4A-2':'7.2','4A-3':'7.2','4B-1':'7.2','4B-2':'7.2','4C-1':'7.2',
 '5A-1':'8.1','5A-2':'8.2','5A-3':'8.2','5A-4':'8.2','5A-5':'8.2','5B-1':'8.2','5B-2':'8.2','5B-3':'8.2','5B-4':'8.3','5C-1':'8.4','5C-2':'9.1','5C-3':'9.1',
 '5D-1':'9.1','5D-2':'9.1','5E-1':'8.3','5E-2':'8.3','5E-3':'8.3','5E-4':'9.2','6A-1':'8.4','6A-2':'8.4','6A-3':'8.4','6A-4':'8.4','6B-1':'9.2','6B-2':'9.2','6B-3':'9.2','6C-1':'9.3','6C-2':'9.3'}
BAD=re.compile(r'Figure|Table|\[\]|Diagram|graph shows|following|this circuit|Redraw|Copy and complete|shown|Complete the|-----|above|below|Match the|In the bowling|Neatly draw|the slider|Using the decay|A₁|V₂|voltmeters V|ammeters A',re.I)
pool=[]
for k,qs in Q.items():
  for i,q in enumerate(qs,1):
    if not BAD.search(q) and len(q)<260: pool.append(dict(set=k,n=i,sec=SET[k],q=q))
used=set();taught=[]   # list of (lessonIndex, section)
def pick(secs):
  for s in secs:
    for c in pool:
      if c['sec']==s and (c['set'],c['n']) not in used:
        used.add((c['set'],c['n']));return c
  return None
fmt=lambda c:f"{c['q']}"
src=lambda c:f"Cambridge {c['set'].split('-')[0]} Check-in Set {c['set'].split('-')[1]}, Q{c['n']}"
for idx,l in enumerate(L):
  seq=l.get('sequence') or {}
  has=any(s['phase']=='Do-now' for s in seq.get('steps',[])) if seq else False
  if has and taught:
    secs=[s for _,s in taught]
    # last lesson: most recent section; last week: 3–6 lessons back; last term: oldest available
    last=[s for _,s in reversed(taught)]
    week=[s for i,s in reversed(taught) if idx-i>=3]
    term=[s for i,s in taught if idx-i>=8]
    out=[]
    a=pick(last[:1]) or pick(last[1:2]); 
    b=pick(week[:3]) or pick(last[1:]) 
    c=pick(term) or pick(week[3:]) or pick(last[2:])
    for when,cq,old in zip(['Last lesson','Last week','Last term'],[a,b,c],seq.get('doNow',[])+[None]*3):
      if cq: out.append(dict(when=when,q=fmt(cq),note=src(cq)))
      elif old: out.append(old)
    seq['doNow']=out
    for s in seq['steps']:
      if s['phase']=='Do-now': s['detail']='Three Cambridge check-in questions, done independently, then self-marked against your answers.' if all('Cambridge' in x.get('note','') for x in out) else 'Three do-now questions done independently, then self-marked.'; s['resource']='Cambridge check-in questions (Cambridge Resources > section folders)'
  if l['type']=='lesson': taught.append((idx,l['section']))
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
for l in L:
  dn=(l.get('sequence') or {}).get('doNow')
  if dn: print(l['lesson'],l['section'],'|',' || '.join(f"{x['when'][5:]}: {x.get('note','-')[10:]}" for x in dn))
print('used',len(used),'of',len(pool))
