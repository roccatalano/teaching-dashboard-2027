"""Build classes/general-maths-12.json: Unit 3 lesson order (names only).
Sources: VCE Mathematics Study Design 2023-2027, Cambridge General Mathematics VCE Units 3&4
(2nd ed.) curriculum grid and sample planner. Run from the repo root."""
import json
A1=('U3 AoS1','Data analysis'); A2=('U3 AoS2','Recursion and financial modelling')
# (block, weekLabel, termLabel, aos, [(type, section, title), ...])
W=[
 ('su','Step-up week 1','Nov–Dec 2026',A1,[('lesson','1A–1B','Types of data; categorical data'),('lesson','1C–1D','Histograms, dot plots and stem plots'),('lesson','1E–1F','Log (base 10) scales; centre and spread')]),
 ('su','Step-up week 2','Nov–Dec 2026',A1,[('lesson','1G','Five-number summary, boxplots and outliers'),('lesson','1H–1I','Normal distribution, z-scores; populations and samples')]),
 ('t1','Week 1','Term 1 · short week',A1,[('review','1','Chapter 1 review'),('sac','1','Chapter 1 test')]),
 ('t1','Week 2','Term 1',A1,[('lesson','2A–2B','Response and explanatory variables; two-way tables'),('lesson','2C','Numerical vs categorical: parallel boxplots, back-to-back stem plots'),('lesson','2D–2E','Scatterplots: direction, form and strength')]),
 ('t1','Week 3','Term 1',A1,[('lesson','2F','Correlation coefficient, $r$'),('lesson','2G–2H','Coefficient of determination; correlation and causation'),('review','2I','Which graph? and Chapter 2 review')]),
 ('t1','Week 4','Term 1',A1,[('lesson','3A','Least squares regression line'),('lesson','3B','Interpreting slope and intercept; predictions'),('lesson','3C','Residual analysis and regression analysis')]),
 ('t1','Week 5','Term 1',A1,[('lesson','4A','Squared transformation'),('lesson','4B','Log transformation'),('lesson','4C','Reciprocal transformation')]),
 ('t1','Week 6','Term 1',A1,[('lesson','4D','Choosing and applying a transformation'),('lesson','5A','Time series data: features of time series plots'),('lesson','5B','Smoothing with moving means')]),
 ('t1','Week 7','Term 1 · Labour Day Mon 8 Mar',A1,[('lesson','5B','Centring moving means'),('lesson','5C','Smoothing with moving medians'),('lesson','5D','Seasonal indices')]),
 ('t1','Week 8','Term 1',A1,[('lesson','5D','Deseasonalising and reseasonalising'),('lesson','5E','Trend lines and forecasting'),('review','6','Review: distributions and associations')]),
 ('t1','Week 9','Term 1',A1,[('review','6','Review: regression, transformations and time series'),('review','SAC 1','SAC 1 practice application task'),('review','SAC 1','SAC 1 targeted revision')]),
 ('t2','Week 1','Term 2',A2,[('review','SAC 1','SAC 1 refresher (before Part 1, Wed 14 Apr after school)'),('review','SAC 1','SAC 1 revision'),('sac','SAC 1','SAC 1 Part 2: in class (10 min reading + 60 min)')]),
 ('t2','Week 2','Term 2',A2,[('review','SAC 1','SAC 1 revision (before Part 3, Wed 21 Apr after school)'),('lesson','7A','Sequences and recurrence relations (after SAC 1 Part 3)'),('lesson','7B, 7D','Linear and geometric growth and decay')]),
 ('t2','Week 3','Term 2',A2,[('lesson','7C, 7E','Explicit rules for linear and geometric growth and decay'),('lesson','7F','Interest rates over different periods; effective interest rates'),('review','SAC 1','SAC 1 feedback')]),
 ('t2','Week 4','Term 2',A2,[('review','7','Chapter 7 review'),('lesson','8A','Compound interest investments with regular additions'),('lesson','8B','Reducing balance loans and annuities')]),
 ('t2','Week 5','Term 2',A2,[('lesson','8C','Amortisation tables'),('lesson','8D','Analysing financial situations with amortisation tables'),('lesson','8E','Finance solver: balance and final payment')]),
 ('t2','Week 6','Term 2',A2,[('lesson','8F','Finance solver: interest rate, time and payment'),('lesson','8G','Harder financial problems'),('lesson','8H','Interest-only loans')]),
 ('t2','Week 7','Term 2',A2,[('lesson','8I','Perpetuities'),('review','8','Chapter 8 review'),('review','9','Review: recursion and financial modelling')]),
 ('t2','Week 8','Term 2',A2,[('review','SAC 2','SAC 2 revision (Part 1, Wed 2 Jun after school)'),('review','Exam','Unit 3 exam revision'),('review','Exam','Unit 3 exam revision')]),
 ('t2','Week 9','Term 2 · trial exam week',A2,[('sac','Exam','Unit 3 trial exams')]),
 ('t2','Week 10','Term 2',A2,[('tbc','','To be planned'),('tbc','','To be planned'),('tbc','','To be planned')]),
 ('t2','Week 11','Term 2',A2,[('tbc','','To be planned'),('tbc','','To be planned'),('tbc','','To be planned')]),
]
TASKS={'tbc':[],'lesson':['Slides ready','Guided sheet ready','Exit ticket'],'review':['Review set ready'],'sac':['Task ready','Marking scheme ready']}
L=[];n=0;s=0
for wi,(blk,wl,tl,(aos,at),ls) in enumerate(W,1):
  for typ,sec,title in ls:
    if blk=='su': s+=1;num=f'S{s}'
    else: n+=1;num=n
    L.append(dict(type=typ,section=sec,title=title,aos=aos,aosTitle=at,unit=3,week=wi,weekLabel=wl,termLabel=tl,lesson=num,
      id=f'gm12-u3-{num if blk=="su" else "l%02d"%num}'.lower(),keyKnowledge=[],questions=[],tasks=[dict(text=t,done=False) for t in TASKS[typ]]))
import datetime as dt
START={'t1':dt.date(2027,1,25),'t2':dt.date(2027,4,12)}; END={'t1':dt.date(2027,3,25)}
def rng(blk,wl):
  if blk not in START: return ''
  mon=START[blk]+dt.timedelta(weeks=int(wl.split()[1])-1)
  a=max(mon,dt.date(2027,1,28)); b=min(mon+dt.timedelta(days=4),END.get(blk,dt.date(2099,1,1)))
  f=lambda d:f"{d.day} {d.strftime('%b')}"
  return f"{a.day}–{f(b)}" if a.month==b.month else f"{f(a)} – {f(b)}"
for blk,wl,tl,_,_ in W:
  for l in L:
    if l['weekLabel']==wl and l['termLabel']==tl: l['dates']=rng(blk,wl)
for l in L:
  if l['title']=='Unit 3 trial exams': l['span']=3
# CFATs (from Planning\Topics\1. Data Analysis\README.md + HANDOFF.md). ~20 min each, on lighter lessons.
FMT='About 20 min, start of lesson, individual, closed book (CAS allowed)'
SRC='Edrolo GM U3&4 2023 exercise questions (CFAT-only)'
DIR='1. Data Analysis\\CFATs\\Chapter 1\\'
CF={
 'gm12-u3-s4':[dict(id='CFAT 1.1.1',title='Types of data, displays, log scales',covers=['1A','1B','1C','1D','1E'],format=FMT,file=DIR+'CFAT 1.1.1 [1A–1E].docx',status='Written (10 Nov 2026)',
   plan='Done at the start of the 1G lesson, a single-subchapter lesson. Covers everything from Step-up lessons 1–3.',sources=[SRC+': 1A Q15, Q17 · 1B Q8, Q9 · 1C Q6, Q17 · 1D Q9, Q12, Q14'])],
 'gm12-u3-l01':[dict(id='CFAT 1.1.2',title='Describing numerical data: median, IQR, boxplots, SOCS',covers=['1F (median, IQR)','1G'],format=FMT,file=DIR+'CFAT 1.1.2 [1F, 1G].docx',status='Written (10 Nov 2026)',
   plan='Chapter 1 review lesson, after the summer break.',sources=[SRC+': 1E Q1, Q8, Q11, Q14, Q17, Q18 · 1F Q12, Q16, Q18, Q19']),
  dict(id='CFAT 1.1.3',title='Mean and SD, the normal distribution, z-scores',covers=['1F (mean, SD)','1H','1I'],format=FMT,file=DIR+'CFAT 1.1.3 [1H, 1F, 1I].docx',status='Written (10 Nov 2026)',marks=16,
   plan='Chapter 1 review lesson, straight after CFAT 1.1.2. Cambridge 1I not assessed. Q8a has a blank normal curve scaffold.',sources=[SRC+': 1G Q4 · 1H Q8, Q11, Q13 · 1I Q1, Q4, Q9, Q12, Q15'])],
}
for l in L:
  if l['id'] in CF: l['cfats']=CF[l['id']]
ids={l['title']:l for l in L}
def when(t):l=ids[t];return dict(id=l['id'],week=l['week'],lesson=l['lesson'])
SD='VCE Mathematics Study Design 2023–2027'
d=dict(id='general-maths-12',name='Year 12 General Maths',unitLabel='Unit 3',
 scope='Unit 3 only · lesson order only (details to come) · step-up before summer, then Term 1 and Term 2 Weeks 1–11 · SAC sittings after school on Wednesdays',
 summary='Step-up 5 lessons · Term 1: 26 lessons · Term 2 Weeks 1–8: 24 lessons, Week 9 trial exams · Weeks 10–11 to be planned · 3 lessons a week (2 in the Term 1 short week)',
 textbook='Cambridge Senior Mathematics General Mathematics VCE Units 3&4 (2nd ed.)',
 lessonsPerWeek=3,lessonMinutes=None,lessons=L,
 assessment=dict(rulesTitle=SD,
  rules=['Unit 3 School-assessed Coursework contributes 24 per cent to the study score (60 marks).',
   'Application task (Data analysis): 4–6 hours over 1–2 weeks. Outcome 1: 10, Outcome 2: 20, Outcome 3: 10 marks.',
   'Modelling or problem-solving task 1 (Recursion and financial modelling): 2–3 hours over 1 week. Outcome 1: 5, Outcome 2: 10, Outcome 3: 5 marks.',
   'Examinations 1 and 2 each contribute 30 per cent.',
   'School arrangement: SAC sittings run after school on Wednesdays (up to 100 minutes), so they do not use lesson time.'],
  suitableTasks=['Application task: a guided investigation of a given data set with several variables, with three components of increasing complexity: data plots (including smoothed plots for time series); summary statistics (including seasonal indices); modelling linear associations or trends (including data transformation).'],
  aos=[dict(aos='SAC 1',title='Application task: Data analysis',when=when('SAC 1 Part 2: in class (10 min reading + 60 min)'),outcome='Outcomes 1–3 (40 of 60 marks)',task='Guided investigation of a given multivariate data set, in three parts: Part 1 after school Wed 14 Apr (10 min reading + 90 min), Part 2 in class in Term 2 Week 1 (10 min reading + 60 min). No new content until Part 3 is done; Chapter 7 starts after it., Part 3 after school Wed 21 Apr (10 min reading + 90 min). Total 4 h 30 min (4 h working time) over 7 days.',taskType='Application task, 4–6 hours over 1–2 weeks',gaps=['Check lessons are at least 70 minutes long, for Part 2.','Part 2 must fall between the two Wednesday sittings (Thu 15 Apr – Tue 20 Apr).','Confirm the Wednesday dates against the school calendar.'],practice=[],actual=[],redemption=[],models=[]),
       dict(aos='SAC 2',title='Modelling or problem-solving task 1: Recursion and financial modelling',when=when('SAC 2 revision (Part 1, Wed 2 Jun after school)'),outcome='Outcomes 1–3 (20 of 60 marks)',task='Modelling or problem-solving task on recursion and financial modelling, in two parts after school: Part 1 Wed 2 Jun (Week 8), Part 2 Wed 9 Jun (Week 9, trial exam week). Feedback in Week 10. Keep the total at 2–3 hours, e.g. 2 × (10 min reading + 80 min).',taskType='Modelling or problem-solving task, 2–3 hours over 1 week',gaps=['Part 2 falls in trial exam week: confirm, or move it to Wed 16 Jun (Week 10).','Week 10 lessons are not planned yet (Unit 4 starts there); SAC 2 feedback needs a slot.','Two full 100-minute sittings would be 3 h 20 min, over the 3-hour maximum. Cap each sitting.','Confirm the Wednesday dates against the school calendar.'],practice=[],actual=[],redemption=[],models=[])],
  exams=[dict(name='Unit 3 trial exams',covers='Unit 3: Data analysis; Recursion and financial modelling',when='Term 2 Week 9 (trial exam week, no classes)',practice=[],actual=[])]))
json.dump(d,open('classes/general-maths-12.json','w'),ensure_ascii=False,indent=1)
print(len(L),'entries')
