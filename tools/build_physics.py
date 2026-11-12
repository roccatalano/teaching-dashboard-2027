import json,re
raw=json.load(open('/tmp/build/raw.json'))
CAM={2:1,3:1,4:2,5:2,6:3,7:4,8:5,9:6,10:7,11:7,12:8,13:9,14:9}
AOS={ (1,1):("U1 AoS1","How are light and heat explained?",12),
      (1,2):("U1 AoS2","How is energy from the nucleus utilised?",12),
      (1,3):("U1 AoS3","How can electricity be used to transfer energy?",21),
      (2,1):("U2 AoS1","How is motion understood?",30)}
def lines(s): return [l.strip(' •\t') for l in s.split('\n') if l.strip(' •\t')]
def kk(s): return [l for l in lines(s) if not l.startswith('–') and len(l)>3][:8]
def parse_q(s):
  q={};cur=None;mode=None
  for l in lines(s):
    if l in('SB:','OA:'): mode=l[:2];continue
    if mode!='SB': continue
    m=re.match(r'^(\d+\.\d+)\s+(.*)',l)
    if m: cur=m.group(1);q.setdefault(cur,[]).append(m.group(2))
    elif cur: q[cur].append(l)
  return q
lessons=[]
def add(unit,aos,**k):
  lessons.append(dict(unit=unit,aos=aos,**k))
for (u,a),(code,title,budget) in AOS.items():
  rows=[r for r in raw if r['unit']==u and r['aos']==a]
  items=[];review=None;prior=None
  for r in rows:
    c=r['cells']
    sec=c[1]; 
    if not r['cells'][0]:
      if 'Review' in c[1]+c[2]: review=r
      else: prior=r
      continue
    secs=[l for l in lines(sec) if re.match(r'^\d+\.\d+',l)]
    q=parse_q(c[3]); sk=lines(c[4]); eb=lines(c[5]); k=kk(c[2])
    pas=[x for x in sk if x.startswith('PA')]; wss=[x for x in sk if x.startswith('WS')]
    vids=[x for x in eb if x.startswith('Video') or x.startswith('Interactive')]
    for i,s in enumerate(secs):
      num=s.split()[0]; ch=int(num.split('.')[0])
      exps=sorted({x for x in eb if re.match(r'EXP '+re.escape(num)+r'\.\d+$',x)})
      items.append(dict(type='lesson',section=num,title=s[len(num):].strip(),pweek=c[0],
        keyKnowledge=k,questions=q.get(num,[]),worksheets=wss if i==len(secs)-1 else [],
        experiments=exps,videos=vids if i==0 else [],cambridge=f"Cambridge Ch {CAM[ch]}",_pas=pas if i==len(secs)-1 else []))
  # prac lessons queue
  pracs=[]
  for idx,it in enumerate(items):
    for p in it.pop('_pas'): pracs.append((idx,p))
  tail=[dict(type='review',title=f'{code} review',questions=['AoS review questions'],worksheets=[x for x in lines(review['cells'][4]) if x.startswith('WS')] if review else []),
        dict(type='sac',title=f'{code} SAC',worksheets=[x for x in lines(review['cells'][4]) if 'EQ' in x] if review else [])]
  room=budget-len(items)-len(tail)
  ins={}
  for idx,p in pracs[:max(room,0)]: ins.setdefault(idx,[]).append(p)
  room-=min(len(pracs),max(room,0))
  seq=[]
  for idx,it in enumerate(items):
    seq.append(it)
    for p in ins.get(idx,[]):
      seq.append(dict(type='prac',title=re.sub(r'^PA \d+\s*','',p),section=it['section'],worksheets=[p],cambridge=it['cambridge']))
  # fill remaining with consolidation lessons spread evenly
  if room>0:
    step=max(1,len(seq)//(room+1)); pos=step
    for n in range(room):
      seq.insert(min(pos,len(seq)),dict(type='consolidation',title='Consolidation and practice questions'));pos+=step+1
  while len(seq)+len(tail)>budget:  # merge last two plain lessons sharing pweek
    for i in range(len(seq)-1,0,-1):
      x,y=seq[i-1],seq[i]
      if x['type']==y['type']=='lesson' and x['pweek']==y['pweek']:
        x['title']+=' + '+y['section']+' '+y['title']
        for f in('questions','worksheets','experiments','videos'): x[f]+=y[f]
        x['section']+=', '+y['section']; del seq[i]; break
    else: raise SystemExit(f'cannot fit {code}')
  for it in seq+tail: add(u,code,aosTitle=title,**it)
  if (u,a)==(1,3):
    for t in ['Buffer / SAC catch-up','Buffer / SAC catch-up','Unit 1 wrap-up']: add(1,'U1 buffer',aosTitle='Buffer week',type='buffer',title=t)
# Unit 2 AoS2/3/rev
opt=[r for r in raw if r['unit']==2 and r['aos']==2][0]['cells']
for t in ['Options launch: choose your question','Research: evaluating sources','Research and analysis','Research and analysis','Building your stance','Presentations']:
  add(2,'U2 AoS2',aosTitle='Options: how does physics inform contemporary issues?',type='options',title=t,keyKnowledge=kk(opt[2]),worksheets=lines(opt[5])[::2] if 'launch' in t else [])
inv=[r for r in raw if r['unit']==2 and r['aos']==3][0]['cells']
for t in ['Investigation intro: crumple zones and impulse','Designing the method + logbook','Risk assessment and pilot','Data collection','Data collection','Processing data and uncertainty','Analysis and evaluation','Poster preparation','Poster presentations (assessment)']:
  add(2,'U2 AoS3',aosTitle='How do physicists investigate questions?',type='sac' if t.startswith('Poster presentations') else 'investigation',title=t,keyKnowledge=kk(inv[1]) if 'intro' in t else [],worksheets=lines(inv[4])[:4] if 'intro' in t else [])
for t in ['Revision: Unit 1','Revision: Unit 2','Units 1 and 2 practice exam']:
  add(2,'U2 revision',aosTitle='Revision',type='review' if 'Revision' in t else 'sac',title=t,worksheets=['Units 1 and 2 practice exam'] if 'exam' in t else [])
# number + weeks
TASK={'lesson':['Slides ready','Questions set','Exit ticket'],'prac':['Book lab tech','Risk assessment','Print prac sheet'],'sac':['Task written','Printed','Marked'],'review':['Review set','Answers posted'],'consolidation':['Pick question set'],'investigation':['Prep materials'],'options':['Prep'],'buffer':[]}
for u in (1,2):
  L=[l for l in lessons if l['unit']==u]
  assert len(L)==48,(u,len(L))
  for i,l in enumerate(L):
    l['id']=f'p11-u{u}-l{i+1:02d}';l['lesson']=i+1;l['week']=i//3+1
    l['tasks']=[{'text':t,'done':False} for t in TASK[l['type']]]
    for f in('keyKnowledge','questions','worksheets','experiments','videos'): l.setdefault(f,[])
    l.setdefault('section','');l.setdefault('cambridge','');l['links']=[];l['notes']=''
    l.pop('pweek',None)
json.dump(dict(id='physics-11',name='Year 11 Physics',textbook='Heinemann Physics 11 5E',weeksPerUnit=16,lessonsPerWeek=3,lessons=lessons),open('/tmp/build/physics-11.json','w'),indent=1,ensure_ascii=False)
for l in lessons: print(l['unit'],l['week'],l['lesson'],l['aos'],l['type'],l['section'],l['title'][:60])
