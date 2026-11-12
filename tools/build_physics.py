import json,re
raw=json.load(open('tools/raw.json'))
def lines(s): return [l.strip(' •\t') for l in s.split('\n') if l.strip(' •\t')]
exec("FIX="+open('tools/gen_head.py').read().split("FIX=",1)[1])
CI=json.load(open('tools/cambridge_index.json'))
MAP={'2.1':['1A'],'2.2':['1A'],'2.3':['1B'],'3.1':['1C'],'3.2':['1C'],'4.1':['2A'],'4.2':['2A'],'4.3':['2A'],'4.4':['2A','2B'],
'5.1':['2B'],'5.2':['2B'],'6.1':['3A'],'6.2':['3B'],'6.3':['3C','3D'],'6.4':['3E'],'7.1':['4A'],'7.2':['4B','4C'],
'8.1':['5A'],'8.2':['5A'],'8.3':['5B','5E'],'8.4':['6A'],'9.1':['5C','5D'],'9.2':['6B','5E'],'9.3':['6C'],
'10.1':['7A'],'10.2':['7A'],'10.3':['7A'],'11.1':['7A'],'11.2':['7A'],'11.3':['7B'],'11.4':['7C'],'11.5':['7C'],
'12.1':['8B'],'12.2':['8B'],'12.3':['8B'],'12.4':['8A'],'12.5':['8A'],'12.6':['8A'],'13.1':['9A'],'13.2':['9B','9C'],'13.3':['9B'],
'14.1':['8C'],'14.2':['8C'],'14.3':['8C']}
AOS={(1,1):("U1 AoS1","How are light and heat explained?",12,['1','2']),
     (1,2):("U1 AoS2","How is energy from the nucleus utilised?",12,['3','4']),
     (1,3):("U1 AoS3","How can electricity be used to transfer energy?",21,['5','6']),
     (2,1):("U2 AoS1","How is motion understood?",30,['7','8','9'])}
ORDER=['worksheet','questions','checkin','prac','slides','answers','extra']
def camb_for(codes,exclude_prac=False):
  res=[]
  for c in codes:
    for r in CI['sections'].get(c,[]):
      if exclude_prac and r['kind']=='prac': continue
      res.append(dict(r,section=c))
  res.sort(key=lambda r:(ORDER.index(r['kind']) if r['kind'] in ORDER else 9))
  return dict(sections=codes,resources=res)
def camb_chapters(chs,kinds):
  return [dict(r,section='Ch '+c) for c in chs for r in CI['chapters'].get(c,[]) if r['kind'] in kinds]
def plainq(q):
  out=[]
  for x in q:
    x=re.sub(r'^KQ\s*','Key questions ',x);x=re.sub(r'^KR\s*','Key questions ',x)
    x=re.sub(r'^CR\s*','Chapter review ',x);x=re.sub(r'^CS\s*','Case study questions ',x)
    out.append(x)
  return out
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
def add(unit,aos,**k): lessons.append(dict(unit=unit,aos=aos,**k))
for (u,a),(code,title,budget,chs) in AOS.items():
  rows=[r for r in raw if r['unit']==u and r['aos']==a]
  items=[]
  for r in rows:
    c=r['cells']
    if not c[0]: continue
    secs=[l for l in lines(c[1]) if re.match(r'^\d+\.\d+',l)]
    q=parse_q(c[3]); eb=lines(c[5]); k=kk(c[2])
    vids=[x for x in eb if x.startswith('Video') or x.startswith('Interactive')]
    for i,s in enumerate(secs):
      num=s.split()[0]
      exps=sorted({x for x in eb if re.match(r'EXP '+re.escape(num)+r'\.\d+$',x)})
      items.append(dict(type='lesson',section=num,title=s[len(num):].strip(),pweek=c[0],keyKnowledge=k,
        pearson=dict(reading=[f'Student book {num} {s[len(num):].strip()}'],questions=plainq(q.get(num,[])),
          experiments=[e.replace('EXP','Online experiment') for e in exps],videos=vids if i==0 else []),
        cambridge=camb_for(MAP[num],exclude_prac=True)))
  # Cambridge pracs become prac lessons after the last Pearson lesson that maps to their section
  pracs=[]
  for c in [x for ch in chs for x in sorted(CI['sections']) if x[0]==ch]:
    for r in CI['sections'][c]:
      if r['kind']=='prac':
        last=max(i for i,it in enumerate(items) if c in MAP[it['section']])
        pracs.append((last,c,r))
  tail=[dict(type='review',title=f'{code} review',keyKnowledge=[],
             pearson=dict(reading=['Area of study review (end of the AoS in the student book)'],questions=['AoS review questions'],experiments=[],videos=[]),
             cambridge=dict(sections=[],resources=camb_chapters(chs,['review','summary','checklist','links']))),
        dict(type='sac',title=f'{code} SAC',keyKnowledge=[],pearson=dict(reading=[],questions=[],experiments=[],videos=[]),
             cambridge=dict(sections=[],resources=camb_chapters(chs,['test','answers'])))]
  room=budget-len(items)-len(tail)
  use=pracs[:max(room,0)]; room-=len(use)
  ins={}
  for last,c,r in use: ins.setdefault(last,[]).append((c,r))
  seq=[]
  for i,it in enumerate(items):
    seq.append(it)
    for c,r in ins.get(i,[]):
      t=re.sub(r'^Practical \d[A-E]–\d\s*','',r['label'])
      seq.append(dict(type='prac',section=c,title=t,keyKnowledge=it['keyKnowledge'],pearson=dict(reading=[],questions=[],experiments=it['pearson']['experiments'],videos=[]),
        cambridge=dict(sections=[c],resources=[dict(r,section=c)])))
  # pracs that didn't get their own lesson stay visible on the Cambridge side of their lesson
  for last,c,r in pracs[len(use):]:
    items[last]['cambridge']['resources'].insert(0,dict(r,section=c))
  if room>0:
    gaps=[i+1 for i,x in enumerate(seq) if x['type']=='lesson']
    picks=[gaps[round((n+1)*len(gaps)/(room+1))-1] for n in range(room)]
    for p in sorted(picks,reverse=True):
      prev=seq[p-1]
      seq.insert(p,dict(type='consolidation',title='Consolidation: practice questions',section=prev.get('section',''),keyKnowledge=[],
        pearson=dict(reading=[],questions=['Chapter review questions for '+prev.get('section','')],experiments=[],videos=[]),
        cambridge=dict(sections=prev['cambridge']['sections'],resources=[x for x in prev['cambridge']['resources'] if x['kind'] in('checkin','questions','worksheet')])))
  while len(seq)+len(tail)>budget:
    for i in range(len(seq)-1,0,-1):
      x,y=seq[i-1],seq[i]
      if x['type']==y['type']=='lesson' and x['pweek']==y['pweek']:
        x['title']+=' + '+y['title']; x['section']+=', '+y['section']
        for f in('reading','questions','experiments','videos'): x['pearson'][f]+=y['pearson'][f]
        for r in y['cambridge']['resources']:
          if r not in x['cambridge']['resources']: x['cambridge']['resources'].append(r)
        x['cambridge']['sections']=sorted(set(x['cambridge']['sections']+y['cambridge']['sections']))
        del seq[i]; break
    else: raise SystemExit('cannot fit '+code)
  for it in seq+tail: it.pop('pweek',None); add(u,code,aosTitle=title,**it)
  if (u,a)==(1,3):
    for t in ['Buffer / SAC catch-up','Buffer / SAC catch-up','Unit 1 wrap-up']:
      add(1,'U1 buffer',aosTitle='Buffer week',type='buffer',title=t,keyKnowledge=[],pearson=dict(reading=[],questions=[],experiments=[],videos=[]),
          cambridge=dict(sections=[],resources=[dict(r,section='Unit 1') for r in CI['units'].get('1',[])]))
opt=[r for r in raw if r['unit']==2 and r['aos']==2][0]['cells']
optres=[dict(r,section='Options') for r in CI['options']]
for t in ['Options launch: choose your question','Research: evaluating sources','Research and analysis','Research and analysis','Building your stance','Presentations']:
  add(2,'U2 AoS2',aosTitle='Options: how does physics inform contemporary issues?',type='options',title=t,keyKnowledge=kk(opt[2]) if 'launch' in t else [],
      pearson=dict(reading=['Unit 2 Options (Pearson eBook)'] if 'launch' in t else [],questions=[],experiments=[],videos=[]),
      cambridge=dict(sections=[],resources=optres if 'launch' in t else []))
inv=[r for r in raw if r['unit']==2 and r['aos']==3][0]['cells']
pinv=[x.strip() for x in lines(inv[5])]
for t in ['Investigation intro: crumple zones and impulse','Designing the method and logbook','Risk assessment and pilot','Data collection','Data collection','Processing data and uncertainty','Analysis and evaluation','Poster preparation','Poster presentations (assessment)']:
  add(2,'U2 AoS3',aosTitle='How do physicists investigate questions?',type='sac' if t.startswith('Poster pres') else 'investigation',title=t,
      keyKnowledge=kk(inv[1]) if 'intro' in t else [],pearson=dict(reading=pinv if 'intro' in t else [],questions=[],experiments=[],videos=[]),
      cambridge=dict(sections=[],resources=[dict(r,section='8A') for r in CI['sections']['8A'] if r['kind']=='prac' and 'Egg' in r['label']] if 'intro' in t else []))
for t in ['Revision: Unit 1','Revision: Unit 2','Units 1 and 2 practice exam']:
  un='1' if 'Unit 1' in t else '2'
  add(2,'U2 revision',aosTitle='Revision',type='review' if t.startswith('Revision') else 'sac',title=t,keyKnowledge=[],
      pearson=dict(reading=['Units 1 and 2 practice exam (Pearson eBook)'] if 'exam' in t else [],questions=[],experiments=[],videos=[]),
      cambridge=dict(sections=[],resources=[dict(r,section='Course') for r in CI['course'] if r['kind']=='exam'] if 'exam' in t else [dict(r,section='Unit '+un) for r in CI['units'].get(un,[])]))
TASK={'lesson':['Slides ready','Questions set','Exit ticket'],'prac':['Book lab tech','Risk assessment','Print prac sheet'],'sac':['Task written','Printed','Marked'],
 'review':['Review set','Answers posted'],'consolidation':['Pick question set'],'investigation':['Prep materials'],'options':['Prep'],'buffer':[]}
for u in (1,2):
  L=[l for l in lessons if l['unit']==u]; assert len(L)==48,(u,len(L))
  for i,l in enumerate(L):
    l.update(id=f'p11-u{u}-l{i+1:02d}',lesson=i+1,week=i//3+1,tasks=[{'text':t,'done':False} for t in TASK[l['type']]],notes='')
    l.setdefault('section','')
json.dump(dict(id='physics-11',name='Year 11 Physics',textbook='Heinemann Physics 11 5E (student book only)',supplement='Cambridge VCE Physics Units 1&2 (offline teacher resources)',
  cambridgeRoot='Year 11 Physics/CambridgeGO Resources',weeksPerUnit=16,lessonsPerWeek=3,lessons=lessons),open('tools/physics-11.json','w'),indent=1,ensure_ascii=False)
for l in lessons: print(l['unit'],l['week'],l['lesson'],l['aos'],l['type'],l['section'],l['title'][:55],'| cam',len(l['cambridge']['resources']))
