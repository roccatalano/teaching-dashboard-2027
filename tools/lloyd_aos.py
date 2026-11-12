import json,sys
fs=set(json.load(open('/tmp/build/lloyd_all.json')))
SEQ={
'U1 AoS1':['Introduction to the course','1A–C Waves, wave fundamentals, everyday electromagnetism','Prac 1C.1 Seeing the colours of the Sun’s rays','1D–E Refraction/reflection, white light and optical phenomena','Chapter 1 review (WS01)','2A Temperature fundamentals','2B How thermal energy moves','2C How heat affects temperature','Chapter 2 review (WS02)','Prac 2A How thermometers work','3A Thermal radiation','3B Global warming and climate change','Chapter 3 review (WS03)','SAC revision','SAC','SAC review + redemption','Prac 3B Presenting renewable energy sources'],
'U1 AoS2':['4A Nuclear stability and the fundamental forces','4B Nuclear half-life','4C Types of nuclear radiation','4D Radiation and the human body','Prac 4B Modelling radioactive decay','5A Nuclear energy','5B Fission','Chapters 4–5 review (WS01, WS02)','SAC revision (practice SAC)','SAC','SAC review + redemption'],
'U1 AoS3':['6A Fundamentals of electricity','Prac 6A Measuring electrical quantities','6B Resistance and Ohm’s law','6C Series circuits','6D Parallel circuits','6E Combination circuits','Chapter 6 review (WS01, WS02)','Prac 6E Equivalent resistance in combination circuits','7A Applications of electric circuits','7B–C Household electricity and electrical safety','Prac 7B Modelling household electrical circuits','Chapter 7 review (WS03)','SAC revision','SAC (+ prac version)','SAC review','Exam revision (Unit 1 exam)'],
'U2 AoS1':['8A Describing motion','8B Graphing motion','8C Constant acceleration equations (SUVAT)','Chapter 8 review (WS01, WS02)','9A–B Forces, momentum and impulse','Prac 9A Newton’s laws and a balloon rocket','9C Force vectors in two dimensions','9D Inclined planes and connected bodies','9E Torque','9F Equilibrium','Chapter 9 review (WS03, WS04)','10A Conservation of energy and kinetic energy','10B Work and gravitational potential energy','10B Power and energy efficiency','10C Springs','10D Vehicle safety case study','Chapter 10 review (WS05, WS06)','Prac 10C Energy transformations of a spring-mass system','SAC revision (practice SAC)','SAC']}
d=json.load(open(sys.argv[1]));L=d['lessons']
ov={}
for a,seq in SEQ.items():
  u=a[1]; n=a[-1]
  items={}
  def addk(k,label,path,**x):
    items.setdefault(k,[]);
    if not any(i['path']==path for i in items[k]): items[k].append(dict(label=label,path=path,**x))
  addk('slides',f'{a} slide deck (PowerPoint)',f'Unit {u}/Teaching materials/Physics_U{u}_AoS{n}.pptx')
  addk('slides',f'{a} notes (Obsidian zip)',f'Unit {u}/Teaching materials/Physics_U{u}_AoS{n}.zip')
  for l in L:
    if l['aos']!=a: continue
    for r in l['lloyd']:
      k={'prac':'pracs','worksheet':'worksheets','sac':'sacs','exam':'exams','notes':'slides'}.get(r['kind'])
      if k: addk(k,r['label'],r['path'],**{x:r[x] for x in('teacher','solutions') if r.get(x)})
  if a=='U1 AoS3':
    for l in L:
      for r in l['lloyd']:
        if r['kind']=='exam' and r['path'].startswith('Unit 1'): addk('exams',r['label'],r['path'],solutions=r.get('solutions'))
  ov[a]=dict(plan=f'U{u} Plan (Google Doc, VCE Physics folder)',sequence=seq,lessonCount=len(seq),resources=items)
d['lloydOverview']=ov
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
for a,o in ov.items(): print(a,{k:len(v) for k,v in o['resources'].items()})
