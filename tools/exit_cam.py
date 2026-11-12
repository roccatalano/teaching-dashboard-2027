import json,sys,re
d=json.load(open(sys.argv[1]));L=d['lessons']
SQ=json.load(open('/tmp/pz/section_q.json'))
MAP={'2.1':['1A'],'2.2':['1A'],'2.3':['1B'],'3.1':['1C'],'3.2':['1C'],'4.1':['2A'],'4.2':['2A'],'4.3':['2A'],'4.4':['2A'],'5.1':['2B'],'5.2':['2B'],
 '6.1':['3A'],'6.2':['3B'],'6.3':['3C','3D'],'6.4':['3E'],'7.1':['4A'],'7.2':['4B','4C'],'5.1':r'blackbody|black-body|Wien|peak|temperature curve','5.2':r'greenhouse|climate|albedo|global|atmosphere','7.1':r'mass|energy|E = mc|binding|defect',
 '8.1':['5A'],'8.2':['5A','5B'],'8.3':['5B','5E'],'8.4':['6A','5C'],
 '9.1':['5C','5D'],'9.2':['6B','5E'],'9.3':['6C']}
KEY={'2.1':r'transverse|longitudinal|mechanical|energy|medium','2.2':r'frequency|wavelength|period|speed|amplitude|Calculate',
 '3.1':r'Snell|refractive index|reflect|refract(?!.*dispers)','3.2':r'dispers|critical|total internal|rainbow|mirage|polari|fibre|prism|colour',
 '4.1':r'kelvin|Celsius|temperature|thermometer|kinetic','4.2':r'specific heat|heat capacity|raise the temperature|warm','4.3':r'latent|melt|boil|evapor|steam|ice|condens','4.4':r'conduct|convect|radiat|insulat',
 '5.1':r'blackbody|black-body|Wien|peak|temperature curve','5.2':r'greenhouse|climate|albedo|global|atmosphere','7.1':r'mass|energy|E = mc|binding|defect',
 '8.1':r'charge|electron|coulomb|proton|repel|attract','8.2':r'current|ammeter|potential difference|voltmeter|volt|coulomb','8.3':r'energy|power|joule|watt|kWh|E =|P =',
 '8.4':r'resist|ohm|diode|LED|thermistor|LDR|I–V|non-ohmic','9.1':r'series|parallel|equivalent','9.2':r'household|kWh|cost|power|parallel','9.3':r'fuse|circuit breaker|RCD|earth|shock'}
BAD=re.compile(r'Figure|Table|\[|Diagram|graph|shown|below|above|following information|Questions? \d+ and|arrows|this circuit|sketch|Sketch|draw|Draw|Copy|Question \d|Questions \d',re.I)
CALC=re.compile(r'^(Calculate|Find|Determine|How much|How many|What is the (speed|frequency|wavelength|energy|current|power|resistance|half-life|activity))',re.I)
pool=[]
for k,qs in SQ.items():
  for i,q in enumerate(qs,1):
    q=re.sub(r'\s*(Short answer questions|Multiple-choice questions).*$','',q).strip()
    if q and not BAD.search(q) and len(q)<420: pool.append(dict(c=k,n=i,q=q,calc=bool(CALC.search(q)),mc=bool(re.search(r'\bA\. .* B\. ',q) or re.search(r' A [a-z].* B [a-z]',q))))
used=set()
def choose(sec):
  cands=[p for p in pool if p['c'] in MAP[sec] and (p['c'],p['n']) not in used]
  if sec in KEY: 
    k=[p for p in cands if re.search(KEY[sec],p['q'],re.I) and not (sec=='3.1' and re.search('dispers|critical',p['q'],re.I))]
    cands=k or cands
  out=[]
  for pref in (lambda p:p['calc'],lambda p:not p['calc'] and not p['mc'],lambda p:True):
    for p in cands:
      if len(out)<2 and pref(p) and p not in out: out.append(p)
  for p in out: used.add((p['c'],p['n']))
  return out
OV={'2.1':['1A1','1A2'],'3.1':['1C3','1C5'],'3.2':['1C9','1C6'],'4.2':['2A11','2A9'],'4.3':['2A8','2A7'],'4.4':['2A5','2A10'],'5.1':['2B2','2B3'],'5.2':['2B5','2B6'],'9.1':['5D7','5D3']}
for v in OV.values():
  for c in v: used.add((c[:2],int(c[2:])))
n=0
for l in L:
  if l['type']!='lesson' or not l.get('sequence'): continue
  qs=[dict(c=c[:2],n=int(c[2:]),q=SQ[c[:2]][int(c[2:])-1]) for c in OV[l['section']]] if l['section'] in OV else choose(l['section'])
  if not qs: continue
  l['sequence']['exitQs']=[dict(q=p['q'],note=f"Cambridge {p['c']} Section questions, Q{p['n']}") for p in qs]
  for s in l['sequence']['steps']:
    if s['phase']=='Exit ticket':
      s['detail']='Two Cambridge section questions on today’s content (below), done individually and handed in. Then red/amber/green on each goal.'
      s.pop('resource',None)
  n+=1
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print('lessons',n,'questions used',len(used))
for l in L:
  e=(l.get('sequence') or {}).get('exitQs')
  if e: print(l['lesson'],l['section'],'|',' || '.join(x['note'][10:]+': '+x['q'][:70] for x in e))
