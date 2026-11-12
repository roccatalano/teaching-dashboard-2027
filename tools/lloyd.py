import json,re,sys
fs=json.load(open('/tmp/build/lloyd_all.json'))
d=json.load(open(sys.argv[1])); L=d['lessons']
def les(**k): return [l for l in L if all(l.get(a)==b for a,b in k.items())]
def by_sec(s): return [l for l in L if l['type']=='lesson' and s in l['section'].split(', ')]
for l in L: l['lloyd']=[]
def put(targets,kind,label,path,**extra):
  for t in targets: t['lloyd'].append(dict(kind=kind,label=label,path=path,**extra))
PRAC={'1A':'2.1','1B.1':'2.2','1B.2':'2.1','1C.1':'2.3','1C.2':'2.3','1D':'3.1','1E':'3.2','2A':'4.1','2B':'4.2','2C':'4.3','3A':'5.1','3B':'5.2',
'4A':'6.1','4B':'6.3','4C':'6.2','4D':'6.4','5A':'7.2','5B':'7.2','6A':'8.2','6B':'8.4','6C':'9.1','6D':'9.1','6E':'9.1','7A':'8.4','7B':'9.2',
'8A':'11.1','8B':'11.3','8C':'11.4','9A':'12.3','9B':'12.6','9C':'INV:intro','9D.1':'12.2','9D2':'INV:Poster preparation','9E':'14.1','9F':'14.3','10A':'13.2','10B':'13.2','10C':'13.2'}
for f in fs:
  m=re.match(r'Unit [12]/Prac materials/([\d.A-Z]+)_(.*)_student_version\.docx$',f)
  if not m: continue
  code,name=m.groups(); tgt=PRAC[code]
  label=name.replace('_',' ').capitalize()
  if tgt.startswith('INV:'): T=[l for l in L if l['aos']=='U2 AoS3' and tgt[4:] in l['title']][:1]
  else: T=by_sec(tgt)
  assert T,(code,tgt)
  put(T,'prac',label,f,teacher=f.replace('_student_version','_teacher_version'))
WS={'U1_AoS1_ws01':'3.2','U1_AoS1_ws02':'4.4','U1_AoS1_ws03':'5.1','U1_AoS2_ws01':'6.3','U1_AoS2_ws02':'7.2','U1_AoS3_ws01':'8.4','U1_AoS3_ws02':'9.1','U1_AoS3_ws03':'9.3',
'U2_AoS1_ws01':'11.3','U2_AoS1_ws02':'11.5','U2_AoS1_ws03':'14.3','U2_AoS1_ws04':'12.3','U2_AoS1_ws05':'13.3','U2_AoS1_ws06':'13.2','U2_AoS3_ws01':'INV:Processing'}
for f in fs:
  m=re.match(r'Unit [12]/Formative assessments/Physics_(U\d_AoS\d_ws\d\d)_(.*)\.pdf$',f)
  if not m or m.group(2).endswith('solutions'): continue
  tgt=WS[m.group(1)]; label='Worksheet: '+m.group(2).replace('_',' ').replace('earths',"Earth's").replace('ohms',"Ohm's").replace('newtons',"Newton's")
  T=[l for l in L if l['aos']=='U2 AoS3' and 'Processing' in l['title']] if tgt.startswith('INV') else by_sec(tgt)
  sol=f[:-4]+'_solutions.pdf'
  put(T,'worksheet',label,f,solutions=sol if sol in fs else None)
  # also on the AoS review lesson
  aos=T[0]['aos']; put([l for l in L if l['aos']==aos and l['type']=='review'],'worksheet',label,f,solutions=sol if sol in fs else None)
# slides: AoS deck on every lesson in that AoS
SL={'U1 AoS1':'Unit 1/Teaching materials/Physics_U1_AoS1.pptx','U1 AoS2':'Unit 1/Teaching materials/Physics_U1_AoS2.pptx','U1 AoS3':'Unit 1/Teaching materials/Physics_U1_AoS3.pptx',
    'U2 AoS1':'Unit 2/Teaching materials/Physics_U2_AoS1.pptx','U2 AoS2':'Unit 2/Teaching materials/Physics_U2_AoS2.pptx','U2 AoS3':'Unit 2/Teaching materials/Physics_U2_AoS3.pptx'}
for a,p in SL.items(): put([l for l in L if l['aos']==a],'slides',a+' slide deck',p)
put([l for l in L if l['aos']=='U2 AoS1'],'notes','Notes: How is motion understood (PDF)','Unit 2/Teaching materials/Area of Study 1 - How is motion understood.pdf')
# SACs and exams: curated, one version each with its solutions
U1='Unit 1/SACs/Physics_';U2='Unit 2/SACs/Physics_'
def sac(aos,sel,label,f,sol=None):
  T=[l for l in L if l['aos']==aos and sel(l)]
  assert f in fs,f; assert sol is None or sol in fs,sol
  put(T,'sac',label,f,solutions=sol)
isSac=lambda l:l['type']=='sac'; isRev=lambda l:l['type']=='review' and 'SAC review' not in l['title']
for a,p in [('U1 AoS1',U1+'U1_AoS1_2026_SAC'),('U1 AoS2',U1+'U1_AoS2_2026_SAC'),('U2 AoS1',U2+'U2_AoS1_2026_SAC')]:
  sac(a,isSac,'SAC',p+'.pdf',p+'_solutions.pdf')
  red=(lambda l:'SAC review' in l['title']) if any(l['aos']==a and 'SAC review' in l['title'] for l in L) else isSac
  sac(a,red,'Redemption SAC',p+'_redemption.pdf',p+'_redemption_solutions.pdf')
for a,p in [('U1 AoS2',U1+'U1_AoS2_2026_SAC'),('U2 AoS1',U2+'U2_AoS1_2026_SAC')]:
  sac(a,isRev,'Practice SAC',p+'_practice.pdf',p+'_practice_solutions.pdf')
sac('U1 AoS3',isSac,'SAC',U1+'U1_AoS3_2026_SAC (1).pdf',U1+'U1_AoS3_2026_SAC_solutions (1).pdf')
sac('U1 AoS3',isSac,'SAC prac component',U1+'U1_AoS3_2026_SAC_prac.pdf')
sac('U1 AoS3',isSac,'SAC (editable Word)','Unit 1/SACs/Physics_U1_AoS3_SAC_merged (1).docx')
sac('U2 AoS2',lambda l:l['title']=='Presentations','SAC',U2+'U2_AoS2_2026_SAC.pdf')
sac('U2 AoS3',isSac,'SAC (2025 poster)',U2+'U2_AoS3_2025_SAC_with_cover.pdf')
def exam(titles,label,f,sol=None):
  assert f in fs,f; assert sol is None or sol in fs,sol
  put([l for l in L if l['title'] in titles],'exam',label,f,solutions=sol)
exam(('Unit 1 wrap-up and exam revision','Exam revision: Unit 1','Revision: Unit 1'),'Unit 1 exam (2026)','Unit 1/Exams/Physics_U1_Exam_2026.pdf','Unit 1/Exams/Physics_U1_Exam_solutions_2026.pdf')
exam(('Unit 1 wrap-up and exam revision','Exam revision: Unit 1','Revision: Unit 1'),'Unit 1 exam (older)','Unit 1/Exams/Physics_unit1_exam.pdf','Unit 1/Exams/Physics_unit1_exam_answers.pdf')
exam(('Revision: Unit 2',),'Unit 2 practice exam (2026)','Unit 2/Exams/Physics_U2_Exam_2026_practice.pdf','Unit 2/Exams/Physics_U2_Exam_2026_practice_solutions.pdf')
exam(('Units 1 and 2 practice exam',),'Unit 2 exam (2026)','Unit 2/Exams/Physics_U2_Exam_2026.pdf','Unit 2/Exams/Physics_U2_Exam_2026_solutions.pdf')
exam(('Revision: Unit 2',),'Unit 2 exam (older)','Unit 2/Exams/Physics_U2_exam.pdf','Unit 2/Exams/Physics_U2_Exam_solutions.pdf')
put([l for l in L if l['unit']==1 and l['lesson']==1],'plan','Mr Lloyd Unit 1 plan (Google Doc)','U1 Plan.gdoc')
put([l for l in L if l['unit']==2 and l['lesson']==1],'plan','Mr Lloyd Unit 2 plan (Google Doc)','U2 Plan.gdoc')
d['lloydRoot']='VCE Physics (shared drive)'
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print(sum(1 for l in L if any(r['kind'] not in('slides','notes') for r in l['lloyd'])),'lessons with specific Lloyd items')
