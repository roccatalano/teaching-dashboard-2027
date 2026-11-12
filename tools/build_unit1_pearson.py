import json,re
raw=json.load(open('/tmp/build/raw.json'))
P=json.load(open('/tmp/pz/moves.json'))   # organised Pearson paths (relative to Pearson Resources)
def pf(*keys):
  r=[p for p in P if all(k in p for k in keys)]
  assert r,(keys); return r[0]
exec("FIX="+open('/tmp/build/gen_head.py').read().split("FIX=",1)[1])
LTX={}
exec(open('/tmp/build/latexify.py').read().split("p=sys.argv[1]")[0].replace("import json,sys",""))
def ltx(k):
  for a,b in R:
    if a in k: k=k.replace(a,b)
  return k
def lines(s): return [l.strip(' •\t') for l in s.split('\n') if l.strip(' •\t')]
AOS={1:('U1 AoS1','How are light and heat explained?'),2:('U1 AoS2','How is energy from the nucleus utilised?'),3:('U1 AoS3','How can electricity be used to transfer energy?')}
CHF={2:'Ch02',3:'Ch03',4:'Ch04',5:'Ch05',6:'Ch06',7:'Ch07',8:'Ch08',9:'Ch09'}
def plainq(x):
  x=re.sub(r'^KQ\s*','Key questions ',x);x=re.sub(r'^CR\s*','Chapter review ',x);return re.sub(r'^CS\s*','Case study questions ',x)
sec={}
for r in raw:
  if r['unit']!=1 or not r['cells'][0]: continue
  c=r['cells'];q={};cur=None;mode=None
  for l in lines(c[3]):
    if l in('SB:','OA:'): mode=l[:2];continue
    if mode!='SB': continue
    m=re.match(r'^(\d+\.\d+)\s+(.*)',l)
    if m: cur=m.group(1);q.setdefault(cur,[]).append(m.group(2))
    elif cur: q[cur].append(l)
  kk=[ltx(fixk(l)) for l in lines(c[2]) if len(l)>3][:10]
  eb=lines(c[5])
  for s in [l for l in lines(c[1]) if re.match(r'^\d+\.\d+',l)]:
    n=s.split()[0];ch=int(n.split('.')[0])
    vids=[p for p in P if p.startswith('Unit 1') and f'/{CHF[ch]} ' in p and '/Videos/' in p]
    oes=sorted({p for p in P if f'/OE {n}.' in p and 'teacher' not in p})
    sec[n]=dict(section=n,title=s[len(n):].strip(),aos=AOS[r['aos']][0],aosTitle=AOS[r['aos']][1],keyKnowledge=kk,
      read=f'Student book {n} {s[len(n):].strip()}',questions=[plainq(x) for x in q.get(n,[])],
      experiments=[dict(label=p.split('/')[-1].rsplit('.',1)[0],path=p) for p in oes],
      solutions=dict(label=f'{CHF[ch]} fully worked solutions',path=pf(f'{CHF[ch]} fully worked solutions')),ch=ch)
# ---------- pracs ----------
def PA(n,title,aosdir):
  t=[p for p in P if aosdir in p and '/Pracs (SAB SPARKlabs)/Teacher/' in p]
  return dict(kind='SPARKlab',code=f'PA{n:02d}',title=title,student=dict(label='SPARKlab file (students open in the eBook)',path=pf(f'PA{n:02d} ')),
    teacher=[dict(label=p.split('/')[-1].rsplit('.',1)[0],path=p) for p in t if 'risk assessment' not in p or f'PA{n:02d}' in p or 'Heating' in p and n in(4,5,6) or 'Electricity' in p and n>=11])
def OE(n,title):
  st=[p for p in P if f'/OE {n} ' in p and 'teacher' not in p]
  t=[p for p in P if f'/OE {n} - teacher' in p]
  return dict(kind='Online experiment',code=f'OE {n}',title=title,student=dict(label='Student sheet (also in the eBook)',path=st[0]),teacher=[dict(label=p.split('/')[-1].rsplit('.',1)[0],path=p) for p in t])
A1,A2,A3='AoS1 Light','AoS2 Nuclear','AoS3 Electricity'
WEEKS=[
 (['2.1','2.2'],dict(PA(1,'Waves in slinky springs and ropes',A1),sec='2.1')),
 (['2.3','3.1'],dict(OE('2.2.1','The speed of sound by clap and echo'),sec='2.2')),
 (['3.2','4.1'],dict(PA(2,'Dispersion and refraction',A1),sec='3.2')),
 (['4.2','4.3'],dict(PA(5,'Determining the specific heat capacity of a substance',A1),sec='4.2')),
 (['4.4','5.1'],dict(PA(6,'Latent heat of fusion',A1),sec='4.3')),
 (['5.2','REVIEW1'],dict(OE('4.4.2','Insulation investigation'),sec='4.4')),
 (['SAC1','6.1','6.2'],None),
 (['6.3','6.4'],dict(PA(8,'An analogue model of radioactive decay',A2),sec='6.3')),
 (['7.1','7.2'],dict(PA(7,'Detecting radiation with a G-M tube',A2),sec='6.2')),
 (['REVIEW2','SAC2','SACREV2'],None),
 (['8.1','8.2'],dict(dict(OE('8.2.1','Using an ammeter'),title='Using an ammeter and a voltmeter',extra=OE('8.2.2','Using a voltmeter')),sec='8.2')),
 (['8.3','8.4'],dict(PA(11,'Ohmic and non-ohmic conductors',A3),sec='8.4')),
 (['9.1','9.2'],dict(PA(13,'Series and parallel circuits',A3),sec='9.1')),
 (['9.3','REVIEW3'],dict(PA(14,'Electrical equivalent of heat',A3),sec='9.2')),
 (['SAC3','SACREV3','CATCHUP'],None),
 (['EXAMREV','EXAMREV2','PRACEXAM'],None)]
def special(code,aos):
  a={'1':'U1 AoS1','2':'U1 AoS2','3':'U1 AoS3'}
  if code.startswith('REVIEW'):
    n=code[-1];return dict(type='review',aos=a[n],title=f'{a[n]} review',read='Student book Area of Study review',questions=['AoS review questions'],
      solutions=dict(label=f'AoS{n} Review fully worked solutions',path=pf(f'AoS{n} Review fully worked solutions')))
  if code.startswith('SACREV'):
    n=code[-1];return dict(type='review',aos=a[n],title=f'SAC {n} feedback and redemption')
  if code.startswith('SAC'):
    n=code[-1];return dict(type='sac',aos=a[n],title=f'SAC {n}',note='Return SAC 1 with feedback at the start of the next lesson (15 min).' if n=='1' else '')
  if code=='CATCHUP': return dict(type='prac',aos='U1 AoS3',title='Prac catch-up and logbook sign-off',prac=dict(kind='Catch-up',code='',title='Students complete any missed prac; teacher sights and signs every logbook',student=None,teacher=[]))
  if code=='PRACEXAM': return dict(type='sac',aos='Unit 1 exam',title='Practice exam (Unit 1 questions)',read='Pearson Units 1 and 2 practice exam: Unit 1 sections',
      solutions=dict(label='Practice exam suggested answers',path=pf('Practice exam suggested answers')))
  return dict(type='review',aos='Unit 1 exam',title='Exam revision: Unit 1',read='Unit 1 revision: AoS review questions',solutions=dict(label='Unit 1 fully worked solutions',path=pf('Unit 1 fully worked solutions')))
lessons=[];last_aos='U1 AoS1'
for w,(items,prac) in enumerate(WEEKS,1):
  slots=list(items)+([None] if prac else [])
  for i,code in enumerate(slots):
    if code is None:
      base=sec[prac['sec']]
      L=dict(type='prac',aos=base['aos'],aosTitle=base['aosTitle'],section=prac['sec'],title=prac['title'],keyKnowledge=base['keyKnowledge'],prac=prac)
    elif code in sec:
      s=sec[code];L=dict(type='lesson',**{k:v for k,v in s.items() if k!='ch'})
    else:
      L=special(code,last_aos);L.setdefault('aosTitle',dict(AOS.values()).get(L['aos'],'Unit 1 revision and exam'))
    last_aos=L['aos'] if L['aos'].startswith('U1') else last_aos
    L.update(unit=1,week=w,lesson=len(lessons)+1,id=f'p11-u1-l{len(lessons)+1:02d}')
    for f in('keyKnowledge','questions','experiments'): L.setdefault(f,[])
    L.setdefault('section','');L.setdefault('read','')
    lessons.append(L)
assert len(lessons)==48,len(lessons)

# ---------- extras: videos + unscheduled Pearson pracs/OEs per section ----------
VID={'2.1':['Ch02 Waves','Extreme wave science'],'3.2':['Ch03 Light','Why is the ocean blue'],'5.1':['Ch05','What is fire'],'5.2':['Ch05','The greenhouse effect'],
 '6.2':['Ch06','Alpha, beta and gamma'],'8.2':['Ch08','Flow of charge'],'9.1':['Ch09','series circuit']}
VID2={'9.1':['Ch09','parallel circuit']}
EMBED={'2.1':'Wave pulse and a mechanical wave (interactive, eBook only)','7.2':'Thermonuclear fusion (interactive, eBook only)'}
scheduled={l['prac']['code'] for l in lessons if l.get('prac')}|{'OE 8.2.2'}
EXTRA_PA={'2.3':(3,'Measuring the speed of light',A1),'4.1':(4,'The relationship between temperature and heat',A1),'7.2':(9,'The OPAL research reactor (research task)',A2),
 '8.2':(10,'Electrostatics with a Van de Graaff generator',A3),'9.1':(12,'Finding the resistance of an ohmic resistor',A3)}
for l in lessons:
  if l['type']!='lesson': continue
  n=l['section'];v=[]
  for spec in [VID.get(n),VID2.get(n)]:
    if spec: v.append(next(dict(label=p.split('/')[-1].rsplit('.',1)[0],path=p) for p in P if f'/{spec[0]}' in p and '/Videos/' in p and spec[1].lower() in p.lower()))
  if n in EMBED: v.append(dict(label=EMBED[n],path=None))
  l['videos']=v
  l['experiments']=[e for e in l['experiments'] if 'OE '+e['label'].split(' ')[1] not in scheduled]
  l['otherPracs']=[]
  if n in EXTRA_PA:
    k,t,ad=EXTRA_PA[n];pa=PA(k,t,ad);l['otherPracs'].append(dict(label=f"SAB PA{k:02d} {t} (SPARKlab)",path=pa['student']['path']))
# ---------- CFATs ----------
CF=[(5,'CFAT 1','Ch 2 Waves and electromagnetic radiation',['2.1','2.2','2.3'],'Ch02'),
    (8,'CFAT 2','Ch 3 Light',['3.1','3.2'],'Ch03'),
    (14,'CFAT 3','Ch 4 Thermal energy',['4.1','4.2','4.3','4.4'],'Ch04'),
    (17,'CFAT 4','Ch 5 Thermal radiation and climate (SAC 1 readiness check)',['5.1','5.2'],'Ch05'),
    (25,'CFAT 5','Ch 6 Radiation from the nucleus',['6.1','6.2','6.3','6.4'],'Ch06'),
    (28,'CFAT 6','Ch 7 Nuclear energy (SAC 2 readiness check)',['7.1','7.2'],'Ch07'),
    (37,'CFAT 7','Ch 8 Electrical physics',['8.1','8.2','8.3','8.4'],'Ch08'),
    (41,'CFAT 8','Ch 9 Electric circuits (SAC 3 readiness check)',['9.1','9.2','9.3'],'Ch09')]
for n,cid,t,secs,chs in CF:
  L=lessons[n-1]; assert L['type'] in('lesson','review'),(n,L['type'])
  L['cfat']=dict(id=cid,title=t,covers=secs,format='15–20 min, start of lesson, individual, closed book',
    plan='Write 5–8 short questions modelled on the student book Key questions for these sections (change the numbers and contexts: students can see the fully worked solutions in the eBook), plus 1 extended question in the style of the chapter Case study questions. Use the sections’ key knowledge as the success criteria.',
    sources=[f'Student book {s} Key questions (as models)' for s in secs]+[f'{c} fully worked solutions (marking guide)' for c in chs.split(', ')])
TASK={'lesson':['Slides ready','Questions set','Exit ticket'],'prac':['Book lab and tech','Risk assessment checked','Prac sheet ready'],'sac':['Task written','Printed','Marked'],'review':['Review set','Answers ready']}
for L in lessons:
  L['tasks']=[{'text':t,'done':False} for t in TASK[L['type']]]+([{'text':L['cfat']['id']+' written','done':False},{'text':L['cfat']['id']+' marked and data entered','done':False}] if L.get('cfat') else [])
# ---------- assessment ----------
def lid(pred): return next(l for l in lessons if pred(l))
def W(l): return dict(week=l['week'],lesson=l['lesson'],id=l['id'])
SUIT=['a report of a laboratory or fieldwork activity including the generation of primary data','reflective annotations related to one or more practical activities from a logbook','an analysis and evaluation of generated primary and/or collated secondary data','a critique of an experimental design, process or apparatus','a modelling or simulation activity','a report of the design, building, testing and evaluation of a device','an explanation of a selected physics device, design or innovation','a physics-referenced response to an issue','a report of a selected physics phenomenon','a media analysis/response','an infographic','problem-solving involving physics concepts and/or skills','a report of an application of physics concepts to a real-world context','an analysis, including calculations, of physics concepts applied to real-world contexts','comparison and evaluation of two solutions to a problem, two explanations of a physics phenomenon or concept, or two methods and/or findings from practical activities','a scientific poster']
OUT={'1':'Outcome 1: model, investigate and evaluate the wave-like nature of light, thermal energy and the emission and absorption of light by matter.',
     '2':'Outcome 2: explain, apply and evaluate nuclear radiation, radioactive decay and nuclear energy.',
     '3':'Outcome 3: investigate and apply a basic DC circuit model to simple battery-operated devices and household electrical systems, apply mathematical models to analyse circuits, and describe the safe and effective use of electricity by individuals and the community.'}
PSUG={'1':'Pearson suggests: SAB Unit 1 AoS 1 exam questions and WS 8 Literacy review. Students won’t have the SAB, so use these as models only.',
      '2':'Pearson suggests: SAB Unit 1 AoS 2 exam questions and WS 15 Literacy review. Students won’t have the SAB, so use these as models only.',
      '3':'Pearson suggests: SAB Unit 1 AoS 3 exam questions and WS 22 Literacy review. Students won’t have the SAB, so use these as models only.'}
assess=[]
for n,t in [('1','How are light and heat explained?'),('2','How is energy from the nucleus utilised?'),('3','How can electricity be used to transfer energy?')]:
  s=lid(lambda l:l['title']==f'SAC {n}')
  assess.append(dict(aos=f'U1 AoS{n}',title=t,outcome=OUT[n],when=W(s),
    task='Written SAC: problem-solving and analysis questions on the AoS key knowledge (to be written).',taskType='problem-solving involving physics concepts and/or skills',
    pearsonNote=PSUG[n],
    practice=[dict(label=f'AoS{n} review questions (student book)',source='Pearson',path=None,solutions=dict(label='Fully worked solutions',path=pf(f'AoS{n} Review fully worked solutions')))],
    actual=[],redemption=[],
    models=[dict(label=f'SAB AoS{n} exam question solutions (teacher model answers)',source='Pearson',path=pf(f'Unit 1/AoS{n}',f'AoS{n} SAB exam question solutions'))],
    gaps=['Pearson has no ready-made SAC students haven’t seen: write the SAC, using the SAB exam question solutions as a model for style and difficulty.','Write a redemption version at the same time.']))
EX=dict(name='Semester 1 exam',covers='Unit 1 (AoS 1–3)',when='Semester 1 exam period, after Week 16',
  practice=[dict(label='Units 1 and 2 practice exam: Unit 1 questions',source='Pearson',path=pf('Practice exam (Units 1 and 2)/Practice exam.docx'),solutions=dict(label='Suggested answers',path=pf('Practice exam suggested answers'))),
            dict(label='Practice exam mapping document (which questions are Unit 1)',source='Pearson',path=pf('Practice exam mapping'),solutions=None)],
  actual=[])
d=dict(id='physics-11',name='Year 11 Physics',scope='Unit 1 only, Pearson resources only',textbook='Heinemann Physics 11 5E',resourceRoot='VCE Physics Units 1 2 [2027]/Pearson Resources',
  weeksPerUnit=16,lessonsPerWeek=3,lessonMinutes=79,lessons=lessons,
  assessment=dict(rules=['All Units 1 and 2 assessment is school-based. Nothing is sent to the VCAA, and grading is a school decision.',
    'Satisfactory completion (S/N) requires demonstrating all 3 outcomes in Unit 1.','A logbook is required and must be regularly sighted.',
    'Practical work: at least 15 hours across Unit 1 AoS 1–3.','Where students choose between tasks, the tasks must be of comparable scope and demand.'],
    suitableTasks=SUIT,aos=assess,exams=[EX]))
json.dump(d,open('/tmp/build/physics-11.json','w'),indent=1,ensure_ascii=False)
pr=[l for l in lessons if l['type']=='prac']
print('pracs',len(pr),round(len(pr)*79/60,1),'h')
for l in lessons: print(l['week'],l['lesson'],l['type'],l['section'],l['title'][:45],'| CFAT' if l.get('cfat') else '')
