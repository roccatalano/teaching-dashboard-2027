import json,sys
d=json.load(open(sys.argv[1]));L=d['lessons']
fs=set(json.load(open('/tmp/build/lloyd_all.json')));CI=json.load(open('/tmp/build/cambridge_index.json'))
def F(p,label,src='Mr Lloyd',sol=None,soll='Solutions'):
  assert p in fs or src!='Mr Lloyd',p
  if sol: assert sol in fs or src!='Mr Lloyd',sol
  return dict(label=label,path=p,source=src,solutions=dict(label=soll,path=sol) if sol else None)
def C(ch,kind):
  return [dict(label=r['label'],path=r['path'],source='Cambridge',solutions=None) for r in CI['chapters'].get(ch,[]) if r['kind']==kind]
def when(aos,pred):
  l=next((l for l in L if l['aos']==aos and pred(l)),None)
  return dict(unit=l['unit'],week=l['week'],lesson=l['lesson'],id=l['id']) if l else None
U1='Unit 1/SACs/Physics_';U2='Unit 2/SACs/Physics_'
def camtests(chs): 
  out=[]
  for c in chs: 
    t=C(c,'test');a=C(c,'answers')
    for x in t: x['solutions']=dict(label='Suggested responses',path=a[0]['path']) if a else None;x['label']+=' (Cambridge)'
    out+=t
  return out
SUIT=['a report of a laboratory or fieldwork activity including the generation of primary data','reflective annotations related to one or more practical activities from a logbook','an analysis and evaluation of generated primary and/or collated secondary data','a critique of an experimental design, process or apparatus','a modelling or simulation activity','a report of the design, building, testing and evaluation of a device','an explanation of a selected physics device, design or innovation','a physics-referenced response to an issue','a report of a selected physics phenomenon','a media analysis/response','an infographic','problem-solving involving physics concepts and/or skills','a report of an application of physics concepts to a real-world context','an analysis, including calculations, of physics concepts applied to real-world contexts','comparison and evaluation of two solutions to a problem, two explanations of a physics phenomenon or concept, or two methods and/or findings from practical activities','a scientific poster']
A=[]
A.append(dict(aos='U1 AoS1',title='How are light and heat explained?',outcome='Outcome 1: model, investigate and evaluate the wave-like nature of light, thermal energy and the emission and absorption of light by matter.',
  task='Written SAC (problem-solving and analysis) on waves, light, thermal energy and thermal radiation.',taskType='problem-solving involving physics concepts and/or skills',when=when('U1 AoS1',lambda l:l['type']=='sac'),
  practice=camtests(['1','2']),actual=[F(U1+'U1_AoS1_2026_SAC.pdf','SAC (2026)',sol=U1+'U1_AoS1_2026_SAC_solutions.pdf')],
  redemption=[F(U1+'U1_AoS1_2026_SAC_redemption.pdf','Redemption SAC',sol=U1+'U1_AoS1_2026_SAC_redemption_solutions.pdf')],
  gaps=['No Mr Lloyd practice SAC: the Cambridge Chapter 1 and 2 tests stand in.']))
A.append(dict(aos='U1 AoS2',title='How is energy from the nucleus utilised?',outcome='Outcome 2: explain, apply and evaluate nuclear radiation, radioactive decay and nuclear energy.',
  task='Written SAC (problem-solving and analysis) on nuclear stability, decay, half-life, dose and nuclear energy.',taskType='problem-solving involving physics concepts and/or skills',when=when('U1 AoS2',lambda l:l['type']=='sac'),
  practice=[F(U1+'U1_AoS2_2026_SAC_practice.pdf','Practice SAC',sol=U1+'U1_AoS2_2026_SAC_practice_solutions.pdf')]+camtests(['3','4']),
  actual=[F(U1+'U1_AoS2_2026_SAC.pdf','SAC (2026)',sol=U1+'U1_AoS2_2026_SAC_solutions.pdf')],
  redemption=[F(U1+'U1_AoS2_2026_SAC_redemption.pdf','Redemption SAC',sol=U1+'U1_AoS2_2026_SAC_redemption_solutions.pdf')],gaps=[]))
A.append(dict(aos='U1 AoS3',title='How can electricity be used to transfer energy?',outcome='Outcome 3: investigate and apply a basic DC circuit model to simple battery-operated devices and household electrical systems, apply mathematical models to analyse circuits, and describe the safe and effective use of electricity by individuals and the community.',
  task='SAC in two parts: a practical component (circuit investigation) and a written problem-solving test.',taskType='a report of a laboratory activity + problem-solving',when=when('U1 AoS3',lambda l:l['type']=='sac'),
  practice=camtests(['5','6']),
  actual=[F(U1+'U1_AoS3_2026_SAC (1).pdf','SAC (2026) written',sol=U1+'U1_AoS3_2026_SAC_solutions (1).pdf'),F(U1+'U1_AoS3_2026_SAC_prac.pdf','SAC prac component'),F('Unit 1/SACs/Physics_U1_AoS3_SAC_merged (1).docx','SAC editable Word version')],
  redemption=[],gaps=['No practice SAC from Mr Lloyd: the Cambridge Chapter 5 and 6 tests stand in.','No redemption task: one needs writing (or reuse a Cambridge chapter test).','No solutions for the prac component.']))
A.append(dict(aos='U2 AoS1',title='How is motion understood?',outcome='Outcome 1: investigate, analyse, mathematically model and apply force, energy and motion.',
  task='Written SAC (problem-solving and analysis) on kinematics, forces, momentum, energy and equilibrium. The study design also requires a motion case study (e.g. vehicle safety).',taskType='problem-solving involving physics concepts and/or skills',when=when('U2 AoS1',lambda l:l['type']=='sac'),
  practice=[F(U2+'U2_AoS1_2026_SAC_practice.pdf','Practice SAC',sol=U2+'U2_AoS1_2026_SAC_practice_solutions.pdf')]+camtests(['7','8','9']),
  actual=[F(U2+'U2_AoS1_2026_SAC.pdf','SAC (2026)',sol=U2+'U2_AoS1_2026_SAC_solutions.pdf')],
  redemption=[F(U2+'U2_AoS1_2026_SAC_redemption.pdf','Redemption SAC',sol=U2+'U2_AoS1_2026_SAC_redemption_solutions.pdf')],gaps=[]))
optb=[dict(label=r['label'],path=r['path'],source='Cambridge',solutions=None) for r in CI['options'] if r['label'].endswith('.pdf') or 'editable' not in r['label'] and 'Answers' not in r['label']]
A.append(dict(aos='U2 AoS2',title='Options: how does physics inform contemporary issues and applications in society?',outcome='Outcome 2: investigate and apply physics knowledge to develop and communicate an informed response to a contemporary societal issue or application related to a selected option.',
  task='Infographic: students research one option and present a physics-informed stance or solution.',taskType='an infographic',when=when('U2 AoS2',lambda l:l['title']=='Presentations'),
  practice=[],actual=[F(U2+'U2_AoS2_2026_SAC.pdf','Infographic SAC (2026)')],redemption=[],
  gaps=['No marking rubric or exemplar found in Mr Lloyd’s folder.','No redemption task (for an infographic, usually a resubmission).','Cambridge Options booklets are the research base for students.']))
A.append(dict(aos='U2 AoS3',title='How do physicists investigate questions?',outcome='Outcome 3: draw an evidence-based conclusion from primary data generated from a student-adapted or student-designed scientific investigation related to a selected physics question.',
  task='Scientific poster reporting a student-designed or adapted investigation, supported by the logbook. Minimum 7 hours of class time.',taskType='a report of a practical investigation (scientific poster)',when=when('U2 AoS3',lambda l:l['type']=='sac'),
  practice=[F('Unit 2/Formative assessments/Physics_U2_AoS3_ws01_scientific_investigation_and_data.pdf','Worksheet: scientific investigation and data',sol='Unit 2/Formative assessments/Physics_U2_AoS3_ws01_scientific_investigation_and_data_solutions.pdf'),
            F('Unit 2/Prac materials/9C_critiquing_an_experimental_report_student_version.docx','Prac: critiquing an experimental report',sol='Unit 2/Prac materials/9C_critiquing_an_experimental_report_teacher_version.docx',soll='Teacher version'),
            F('Unit 2/Prac materials/9D2_presenting_results_in_a_scientific_poster_student_version.docx','Prac: presenting results in a scientific poster',sol='Unit 2/Prac materials/9D2_presenting_results_in_a_scientific_poster_teacher_version.docx',soll='Teacher version')],
  actual=[F(U2+'U2_AoS3_2025_SAC_with_cover.pdf','Poster SAC (2025)'),F('Other/Physics_U2-4_poster_SAC.pdf','Poster SAC guide'),F('Other/Logbook_style_guide.pdf','Logbook style guide')],
  redemption=[],gaps=['Pearson has a ready-made crumple zones investigation with poster template, logbook template, rubric and student checklist (Pearson eBook teacher resources).','No redemption task: posters are usually resubmitted after feedback.']))
EX=[dict(name='Semester 1 exam',covers='Unit 1 (AoS 1–3)',when='Semester 1 exam period (after Week 16)',
  practice=[F('Unit 1/Exams/Physics_unit1_exam.pdf','Unit 1 exam (older)',sol='Unit 1/Exams/Physics_unit1_exam_answers.pdf'),
            dict(label='Unit 1 revision exercise (textbook revision chapter)',path='CambridgeGO Resources/Textbook/Physics12_Ch06B_Revision.pdf',source='Cambridge',solutions=dict(label='Suggested responses',path=CI['units']['1'][0]['path']))],
  actual=[F('Unit 1/Exams/Physics_U1_Exam_2026.pdf','Unit 1 exam (2026)',sol='Unit 1/Exams/Physics_U1_Exam_solutions_2026.pdf')]),
 dict(name='Semester 2 exam',covers='Unit 2 (Mr Lloyd’s exams are Unit 2 only; Pearson and Cambridge practice papers cover Units 1 and 2)',when='Semester 2 exam period (after Week 16)',
  practice=[F('Unit 2/Exams/Physics_U2_Exam_2026_practice.pdf','Unit 2 practice exam (2026)',sol='Unit 2/Exams/Physics_U2_Exam_2026_practice_solutions.pdf'),
            F('Unit 2/Exams/Physics_U2_exam.pdf','Unit 2 exam (older)',sol='Unit 2/Exams/Physics_U2_Exam_solutions.pdf'),
            dict(label='Units 1 and 2 Exam Generator practice paper',path=[r for r in CI['course'] if r['kind']=='exam'][0]['path'],source='Cambridge',solutions=dict(label='Answers',path=[r for r in CI['course'] if r['kind']=='exam'][2]['path'])),
            dict(label='Unit 2 revision exercise (textbook revision chapter)',path='CambridgeGO Resources/Textbook/Physics12_Ch10_Revision.pdf',source='Cambridge',solutions=dict(label='Suggested responses',path=CI['units']['2'][0]['path'])),
            dict(label='Units 1 and 2 practice exam',path='Pearson eBook teacher resources',source='Pearson',solutions=dict(label='Suggested answers',path='Pearson eBook teacher resources'))],
  actual=[F('Unit 2/Exams/Physics_U2_Exam_2026.pdf','Unit 2 exam (2026)',sol='Unit 2/Exams/Physics_U2_Exam_2026_solutions.pdf')])]
d['assessment']=dict(rules=['All Units 1 and 2 assessment is school-based. Nothing is sent to the VCAA, and grading is a school decision.',
 'Satisfactory completion (S/N) requires demonstrating all 3 outcomes in each unit.','A logbook is required in both units and must be regularly sighted.',
 'Practical hours: at least 15 h in Unit 1; at least 10 h across Unit 2 AoS 1–2, plus at least 7 h for the AoS 3 investigation.',
 'Where students choose between tasks, the tasks must be of comparable scope and demand.'],suitableTasks=SUIT,aos=A,exams=EX)
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print([ (a['aos'],a['when']) for a in A])
