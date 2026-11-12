import json,sys
d=json.load(open(sys.argv[1]));L=d['lessons']
CI=json.load(open('/tmp/build/cambridge_index.json'))
GROUPS=[(['2','3'],'Waves, light and refraction'),(['4','5'],'Thermal energy and radiation'),(['6'],'Radiation from the nucleus'),(['7'],'Nuclear energy'),
(['8'],'Charge, current, energy and resistance'),(['9'],'Circuits, household electricity and safety'),(['10','11'],'Vectors and kinematics'),
(['12'],'Newton’s laws and momentum'),(['13'],'Work, energy and power'),(['14'],'Torque and equilibrium')]
for l in L: l.pop('cfat',None)
def chs(l): return {x.split('.')[0] for x in l.get('section','').split(', ') if '.' in x}
for n,(pch,name) in enumerate(GROUPS,1):
  idx=[i for i,l in enumerate(L) if l['type'] in('lesson','consolidation','prac') and chs(l)&set(pch)]
  last=max(idx); t=last+1
  if t>=len(L) or L[t]['type'] in('review','sac') or L[t]['unit']!=L[last]['unit'] or 'cfat' in L[t]: t=last
  secs=sorted({s for i in idx for s in L[i]['cambridge']['sections']})
  src=[]
  for s_ in secs: src+=[dict(r,section=s_) for r in CI['sections'].get(s_,[]) if r['kind'] in('checkin','questions')]
  for c in sorted({s_[0] for s_ in secs}): src+=[dict(r,section='Ch '+c) for r in CI['chapters'].get(c,[]) if r['kind'] in('test','checklist')]
  L[t]['cfat']=dict(id=f'CFAT {n}',title=name,coversPearson=', '.join('Ch '+c for c in pch),covers=secs,
    format='15–20 min, start of lesson, individual, closed book',
    plan='Pick 5–8 questions from the Cambridge check-in sets (recall plus at least one multi-step calculation) and 1 extended question from the chapter test. Use the chapter checklist as the success criteria.',
    sources=src)
  L[t]['tasks']=L[t]['tasks']+[{'text':f'CFAT {n} written','done':False},{'text':f'CFAT {n} marked and data entered','done':False}]
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
for l in L:
  if 'cfat' in l: print(l['unit'],'wk',l['week'],'L',l['lesson'],l['title'][:35],'|',l['cfat']['id'],l['cfat']['covers'],len(l['cfat']['sources']))
