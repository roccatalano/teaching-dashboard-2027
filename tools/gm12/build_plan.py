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
 ('t1','Week 9','Term 1',A1,[('review','6','Review: regression, transformations and time series'),('sac','SAC 1','Application task (Data analysis)'),('review','SAC 1','SAC 1 feedback')]),
 ('t2','Week 1','Term 2',A2,[('lesson','7A','Sequences and recurrence relations'),('lesson','7B, 7D','Linear and geometric growth and decay'),('lesson','7C, 7E','Explicit rules for linear and geometric growth and decay')]),
 ('t2','Week 2','Term 2',A2,[('lesson','7F','Interest rates over different periods; effective interest rates'),('review','7','Chapter 7 review'),('lesson','8A','Compound interest investments with regular additions')]),
 ('t2','Week 3','Term 2',A2,[('lesson','8B','Reducing balance loans and annuities'),('lesson','8C','Amortisation tables'),('lesson','8D','Analysing financial situations with amortisation tables')]),
 ('t2','Week 4','Term 2',A2,[('lesson','8E','Finance solver: balance and final payment'),('lesson','8F','Finance solver: interest rate, time and payment'),('lesson','8G','Harder financial problems')]),
 ('t2','Week 5','Term 2',A2,[('lesson','8H','Interest-only loans'),('lesson','8I','Perpetuities'),('review','8','Chapter 8 review')]),
 ('t2','Week 6','Term 2',A2,[('review','9','Review: recursion and financial modelling'),('review','SAC 2','Practice SAC'),('sac','SAC 2','Modelling or problem-solving task 1 (Recursion and financial modelling)')]),
 ('t2','Week 7','Term 2',A2,[('review','SAC 2','SAC 2 feedback'),('review','Exam','Unit 3 mock exam revision'),('review','Exam','Unit 3 mock exam revision')]),
 ('t2','Week 8','Term 2',A2,[('review','Exam','Unit 3 mock exam revision'),('review','Exam','Unit 3 mock exam revision'),('review','Exam','Unit 3 mock exam revision')]),
 ('t2','Week 9','Term 2',A2,[('sac','Exam','Unit 3 mock exams')]),
]
TASKS={'lesson':['Slides ready','Guided sheet ready','Exit ticket'],'review':['Review set ready'],'sac':['Task ready','Marking scheme ready']}
L=[];n=0;s=0
for wi,(blk,wl,tl,(aos,at),ls) in enumerate(W,1):
  for typ,sec,title in ls:
    if blk=='su': s+=1;num=f'S{s}'
    else: n+=1;num=n
    L.append(dict(type=typ,section=sec,title=title,aos=aos,aosTitle=at,unit=3,week=wi,weekLabel=wl,termLabel=tl,lesson=num,
      id=f'gm12-u3-{num if blk=="su" else "l%02d"%num}'.lower(),keyKnowledge=[],questions=[],tasks=[dict(text=t,done=False) for t in TASKS[typ]]))
ids={l['title']:l for l in L}
def when(t):l=ids[t];return dict(id=l['id'],week=l['week'],lesson=l['lesson'])
SD='VCE Mathematics Study Design 2023–2027'
d=dict(id='general-maths-12',name='Year 12 General Maths',unitLabel='Unit 3',
 scope='Unit 3 only · lesson order only (details to come) · step-up before summer, then Term 1 and Term 2 Weeks 1–9',
 summary='Step-up 5 lessons · Term 1: 26 lessons · Term 2 Weeks 1–9: 25 lessons · 3 lessons a week (2 in the Term 1 short week)',
 textbook='Cambridge Senior Mathematics General Mathematics VCE Units 3&4 (2nd ed.)',
 lessonsPerWeek=3,lessonMinutes=None,lessons=L,
 assessment=dict(rulesTitle=SD,
  rules=['Unit 3 School-assessed Coursework contributes 24 per cent to the study score (60 marks).',
   'Application task (Data analysis): 4–6 hours over 1–2 weeks. Outcome 1: 10, Outcome 2: 20, Outcome 3: 10 marks.',
   'Modelling or problem-solving task 1 (Recursion and financial modelling): 2–3 hours over 1 week. Outcome 1: 5, Outcome 2: 10, Outcome 3: 5 marks.',
   'Examinations 1 and 2 each contribute 30 per cent.'],
  suitableTasks=['Application task: a guided investigation of a given data set with several variables, with three components of increasing complexity: data plots (including smoothed plots for time series); summary statistics (including seasonal indices); modelling linear associations or trends (including data transformation).'],
  aos=[dict(aos='SAC 1',title='Application task: Data analysis',when=when('Application task (Data analysis)'),outcome='Outcomes 1–3 (40 of 60 marks)',task='Guided investigation of a given multivariate data set.',taskType='Application task, 4–6 hours over 1–2 weeks',gaps=['Timing: currently one lesson. The Study Design requires 4–6 hours over 1–2 weeks.'],practice=[],actual=[],redemption=[],models=[]),
       dict(aos='SAC 2',title='Modelling or problem-solving task 1: Recursion and financial modelling',when=when('Modelling or problem-solving task 1 (Recursion and financial modelling)'),outcome='Outcomes 1–3 (20 of 60 marks)',task='Modelling or problem-solving task on recursion and financial modelling.',taskType='Modelling or problem-solving task, 2–3 hours over 1 week',gaps=['Timing: currently one lesson. The Study Design requires 2–3 hours over 1 week.'],practice=[],actual=[],redemption=[],models=[])],
  exams=[dict(name='Unit 3 mock exams',covers='Unit 3: Data analysis; Recursion and financial modelling',when='Term 2 Week 9',practice=[],actual=[])]))
json.dump(d,open('classes/general-maths-12.json','w'),ensure_ascii=False,indent=1)
print(len(L),'entries')
