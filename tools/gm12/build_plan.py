"""Build classes/general-maths-12.json: Unit 3 lesson order (names only).
Sources: VCE Mathematics Study Design 2023-2027, Cambridge General Mathematics VCE Units 3&4
(2nd ed.) curriculum grid and sample planner. Run from the repo root."""
import json
A1=('U3 AoS1','Data analysis'); A2=('U3 AoS2','Recursion and financial modelling')
# (block, weekLabel, termLabel, aos, [(type, section, title), ...])
W=[
 ('su','Step-up week 1','Nov–Dec 2026',A1,[('lesson','1A–1B','Types of data; categorical data'),('lesson','1C–1E','Histograms, dot plots and stem plots; log scales')]),
 ('su','Step-up week 2','Nov–Dec 2026',A1,[('lesson','1F','Measures of centre and spread'),('lesson','1G','Five-number summary, boxplots and outliers'),('lesson','1H–1I','Normal distribution, z-scores; populations and samples')]),
 ('t1','Week 1','Term 1 · short week',A1,[('sac','1','Chapter 1 test (part 1)'),('sac','1','Chapter 1 test (part 2)')]),
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
FMT='About 20 min, individual, closed book (CAS allowed)'
SRC='Edrolo GM U3&4 2023 exercise questions (CFAT-only)'
DIR='1. Data Analysis\\CFATs\\Chapter 1\\'
CF={
 'gm12-u3-s3':[dict(id='CFAT 1.1.1',title='Types of data, displays, log scales',covers=['1A','1B','1C','1D','1E'],format=FMT,file=DIR+'CFAT 1.1.1 [1A–1E].docx',status='Written (10 Nov 2026)',
   plan='First 20 min of Step-up lesson 3 (1F). Covers everything from step-up week 1.',sources=[SRC+': 1A Q15, Q17 · 1B Q8, Q9 · 1C Q6, Q17 · 1D Q9, Q12, Q14'])],
 'gm12-u3-s4':[dict(id='CFAT 1.1.2',title='Describing numerical data: median, IQR, boxplots, SOCS',covers=['1F (median, IQR)','1G'],format=FMT,file=DIR+'CFAT 1.1.2 [1F, 1G].docx',status='Written (10 Nov 2026)',
   plan='Last 20 min of Step-up lesson 4 (1G), once 1G has been taught.',sources=[SRC+': 1E Q1, Q8, Q11, Q14, Q17, Q18 · 1F Q12, Q16, Q18, Q19'])],
 'gm12-u3-s5':[dict(id='CFAT 1.1.3',title='Mean and SD, the normal distribution, z-scores',covers=['1F (mean, SD)','1H','1I'],format=FMT,file=DIR+'CFAT 1.1.3 [1H, 1F, 1I].docx',status='Written (10 Nov 2026)',marks=16,
   plan='Last 20 min of Step-up lesson 5 (1H–1I), once 1H has been taught. Cambridge 1I not assessed. Q8a has a blank normal curve scaffold.',sources=[SRC+': 1G Q4 · 1H Q8, Q11, Q13 · 1I Q1, Q4, Q9, Q12, Q15'])],
}
for l in L:
  if l['id'] in CF: l['cfats']=CF[l['id']]
# Step-up lesson details. LOs: Cambridge learning intentions (verbatim). SC: Cambridge Chapter 1 skills checklist (verbatim).
# Study Design: VCE Mathematics Study Design 2023-2027, GM U3 AoS1 'Investigating data distributions' (verbatim).
# Vocab: terms from the Chapter 1 'Key ideas and chapter summary'; short definitions in our own words.
SDT=['types of data',
 'representation, display and description of the distributions of categorical variables: data tables, two-way frequency tables and their associated segmented bar charts',
 'representation, display and description of the distributions of numerical variables: dot plots, stem plots, histograms; the use of a logarithmic (base 10) scale to display data ranging over several orders of magnitude and their interpretation in terms of powers of ten',
 'use of the distribution(s) of one or more categorical or numerical variables to answer statistical questions',
 'summary of the distributions of numerical variables; the five-number summary and boxplots (including the use of the lower fence (Q1 – 1.5 × IQR) and upper fence (Q3 + 1.5 × IQR) to identify and display possible outliers); the sample mean and standard deviation and their use in comparing data distributions in terms of centre and spread',
 'the normal model for bell-shaped distributions and the use of the 68–95–99.7% rule to estimate percentages and to give meaning to the standard deviation; standardised values (z-scores) and their use in comparing data values across distributions']
LOS={'1A':['To be able to classify data as categorical or numerical.','To be able to further classify categorical data as nominal or ordinal.','To be able to further classify numerical data as discrete or continuous.'],
 '1B':['To be able to construct frequency and percentage frequency tables for categorical data.','To be able to construct bar charts and percentage bar charts from frequency tables.','To be able to interpret and describe frequency tables and bar charts.','To be able to answer statistical questions about a categorical variable.'],
 '1C':['To be able to construct frequency tables for discrete numerical data.','To be able to construct frequency tables for grouped numerical data (discrete and continuous).','To be able to construct a histogram from a frequency table for numerical data.','To be able to construct a histogram from numerical data using a CAS calculator.','To be able to describe the distribution of numerical data according to its key characteristics of shape, centre, spread and outliers.'],
 '1D':['To be able to construct a dot plot for numerical data.','To be able to construct a stem plot for numerical data.'],
 '1E':['To be able to revise the concept of log10 x.','To be able to investigate the effect of the logarithmic scale on the features of a distribution.'],
 '1F':['To be able to understand the mean and the median as measures of centre.','To be able to understand the range, interquartile range and standard deviation as measures of spread.'],
 '1G':['To be able to construct the boxplot for displaying the distribution of a numerical data.','To be able to define and identify outliers.','To be able to construct both simple boxplots and boxplots with outliers.','To be able to determine the features of a distribution from a boxplot.','To be able to use a CAS calculator to construct a boxplot.'],
 '1H':['To be able to introduce the normal model for bell-shaped distributions.','To be able to use the 68–95–99.7% rule to estimate percentages and give meaning to the standard deviation.','To be able to calculate standardised scores and use them to compare values across distributions.'],
 '1I':['No learning intentions found for 1I in the printed textbook (not assessed in the CFATs).']}
SC={'1A':['I can identify types of data.'],
 '1B':['I can construct a frequency table for categorical data.','I can construct a bar chart from a frequency table.','I can construct a percentage segmented bar chart from a frequency table.','I can describe the distribution of a categorical variable.'],
 '1C':['I can construct a frequency table for discrete numerical data.','I can construct a grouped frequency table.','I can construct a histogram from a grouped frequency table.','I can describe the features of a distribution from a histogram.'],
 '1D':['I can construct a dot plot.','I can construct a stem plot.'],
 '1E':['I can use a CAS calculator to find logs.','I can interpret a histogram with a log scale.'],
 '1F':['I can find the median value in a data set.','I can find the median value from a dot plot.','I can find the median value from a stem plot.','I can find the range from a stem plot.','I can find the IQR from a stem plot when n is even.','I can find the IQR from a stem plot when n is odd.','I can calculate the mean using the formula.','I can calculate the mean and standard deviation using the CAS calculator.'],
 '1G':['I can construct a boxplot from a five number summary.','I can construct a boxplot with outliers from data using the CAS calculator.','I can read values from a boxplot.','I estimate percentages from a boxplot.','I can use boxplots for describe a distribution without outliers.','I can use boxplots to describe a distribution with outliers.','I can use boxplots to answer statistical questions.'],
 '1H':['I can apply the 68-95-99.7% rule.','I can calculate standardised scores.','I can use standardised scores to make comparisons.','I can use standard scores to determine percentages.','I can convert standardised scores into actual scores.','I can solve for the values of the mean and standard deviation.'],
 '1I':[]}
V=dict(
 cat=['Categorical variable: describes a quality or category, not a quantity','Nominal: categories with no natural order (e.g. eye colour)','Ordinal: categories with a natural order (e.g. shirt size)','Numerical variable: values are quantities','Discrete: counted, whole-number values','Continuous: measured, any value in a range','Frequency table: lists each value and how often it occurs (count and %)','Bar chart: a bar for each category, bars separated by gaps','Segmented bar chart: one bar split into segments, one per category','Mode (modal category): the most common value or category'],
 num=['Histogram: columns showing the frequency of numerical data in class intervals; bars touch','Dot plot: one dot per data value above a number line','Stem plot: each value split into a stem (leading digits) and a leaf (last digit), with a key','Shape: symmetric, positively skewed or negatively skewed','Outlier: a value that stands out from the rest of the data','Log scale: an axis in powers of 10, for data spanning several orders of magnitude'],
 cen=['Summary statistics: numbers that describe features of a distribution, such as centre and spread','Mean (x̄): the sum of the values divided by n','Median (M): the middle value of the ordered data','Range: largest value minus smallest value','Quartiles (Q1, Q3): split the ordered data into four equal groups','Interquartile range (IQR): Q3 − Q1, the spread of the middle 50%','Standard deviation (s): spread of the data around the mean'],
 box=['Five-number summary: min, Q1, median, Q3, max','Boxplot: a display of the five-number summary, with outliers shown separately','Lower fence: Q1 − 1.5 × IQR','Upper fence: Q3 + 1.5 × IQR','Outlier: a value below the lower fence or above the upper fence'],
 nor=['Normal distribution: a bell-shaped model for symmetric data','68–95–99.7% rule: about 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean','Standardised score (z-score): how many standard deviations a value is above or below the mean','Population: every member of the group being studied','Sample: a subset of the population'])
DET={'gm12-u3-s1':(['1A','1B'],[0,1,3],V['cat']),'gm12-u3-s2':(['1C','1D','1E'],[2,3],V['num']),'gm12-u3-s3':(['1F'],[4],V['cen']),
 'gm12-u3-s4':(['1G'],[4,3],V['box']),'gm12-u3-s5':(['1H','1I'],[5],V['nor'])}
for l in L:
  if l['id'] in DET:
    subs,sd,voc=DET[l['id']]
    l['learningObjectives']=[dict(sub=x,items=LOS[x]) for x in subs]
    l['successCriteria']=[dict(sub=x,items=SC[x]) for x in subs if SC[x]]
    l['studyDesign']=[SDT[i] for i in sd]
    l['keyVocab']=voc
# We Do: Cambridge Examples (titles from the Chapter 1 skills checklist / example headings) paired with the
# Edrolo You Try map agreed with Rocco (Planning\Topics\1. Data Analysis\HANDOFF.md). Edrolo chapter letters differ from Cambridge.
EX={1:('1A','Types of data','Edrolo 1A Q11 a–e'),
 2:('1B','Constructing a frequency table for categorical data','Edrolo 1B WE1'),3:('1B','Constructing a bar chart from a frequency table','Edrolo 1B WE2'),
 4:('1B','Constructing a percentage segmented bar chart','Edrolo 1B WE3'),5:('1B','Describing the distribution of a categorical variable','Edrolo 1B WE4'),
 6:('1C','Constructing a frequency table for discrete numerical data',None),7:('1C','Constructing a grouped frequency table','Edrolo 1C WE4'),
 8:('1C','Constructing a histogram from a frequency table','Edrolo 1C WE5'),9:('1C','Describing the features of a distribution from a histogram',None),
 10:('1D','Constructing a dot plot','Edrolo 1C WE1'),11:('1D','Constructing a stem plot','Edrolo 1C WE2'),
 12:('1E','Using a CAS calculator to find logs','Edrolo 1D WE1'),13:('1E','Interpreting a histogram with a log scale','Edrolo 1D WE3'),
 14:('1F','Finding the median value in a data set','Edrolo 1E WE1'),15:('1F','Finding the median value from a dot plot','Edrolo 1F WE2'),
 16:('1F','Finding the median value from a stem plot','Edrolo 1F WE3'),17:('1F','Finding the range from a stem plot','Edrolo 1E WE2a'),
 18:('1F','Finding the IQR from an ordered stem plot when n is even','Edrolo 1E WE2b'),19:('1F','Finding the IQR from a stem plot when n is odd',None),
 20:('1F','Finding the median and quartiles from a histogram','Edrolo 1F WE1'),21:('1F','Calculating the mean using the formula','Edrolo 1G WE1'),
 22:('1G','Constructing a boxplot from a five-number summary','Edrolo 1E WE4'),23:('1G','Reading values from a boxplot','Edrolo 1E WE6'),
 24:('1G','Estimating percentages from a boxplot',None),25:('1G','Using a boxplot to describe a distribution without outliers','Edrolo 1F WE5'),
 26:('1G','Using a boxplot to describe a distribution with outliers',None),27:('1G','Using a boxplot to answer statistical questions',None),
 28:('1H','Applying the 68–95–99.7% rule','Edrolo 1H WE1'),29:('1H','Calculating standard scores','Edrolo 1I WE1'),
 30:('1H','Using standardised scores to make comparisons','Edrolo 1I WE3'),31:('1H','Using standardised scores to find percentages','Edrolo 1H WE2a'),
 32:('1H','Converting standardised scores into actual scores','Edrolo 1I WE2'),33:('1H','Finding the standard deviation given the mean and one percentage',None),
 34:('1H','Finding the mean and standard deviation','Edrolo 1H WE3a')}
WEDO={'gm12-u3-s1':range(1,6),'gm12-u3-s2':range(6,14),'gm12-u3-s3':range(14,22),'gm12-u3-s4':range(22,28),'gm12-u3-s5':range(28,35)}
for l in L:
  if l['id'] in WEDO:
    l['weDo']=[dict(n=n,sub=EX[n][0],title=EX[n][1],youTry=EX[n][2]) for n in WEDO[l['id']]]
    if l['id']=='gm12-u3-s5': l['weDoNote']='1I is online-only in Cambridge: no printed Examples.'
# CAS videos: links from 12MAG 2027\CAS Videos (Casio ClassPad and TI-nspire support-video lists for VCE GM 3&4).
def yt(t,u): return dict(title=t,url=u)
CP={'stat':yt('ClassPad Help 400 – Statistics: basic settings and actions','https://www.youtube.com/watch?v=Qqg8vWK3SE8'),
 'pie':yt('ClassPad Help 520 – Pie chart','https://www.youtube.com/watch?v=PKbqBLbW9DI'),
 'hl':yt('ClassPad Help 406 – Create a histogram from a list','https://www.youtube.com/watch?v=2YuJoKS4XvM'),
 'hf':yt('ClassPad Help 407 – Create a histogram from a frequency table','https://www.youtube.com/watch?v=E3JIz_SDywE'),
 'hc':yt('ClassPad Help 440 – Histogram class intervals','https://www.youtube.com/watch?v=nnJtqIB6yWM'),
 'sl':yt('ClassPad Help 401 – Statistical calcs from a list','https://www.youtube.com/watch?v=K93TBJP-uaA'),
 'sf':yt('ClassPad Help 402 – Statistical calcs from a frequency table','https://www.youtube.com/watch?v=GjbQKBD9f00'),
 'bl':yt('ClassPad Help 403 – Create a boxplot from a list','https://www.youtube.com/watch?v=HBS1g3cja2g'),
 'bf':yt('ClassPad Help 404 – Create a boxplot from a frequency table','https://www.youtube.com/watch?v=sw2xy8_x1k0'),
 'bm':yt('ClassPad Help 405 – Create multiple boxplots','https://www.youtube.com/watch?v=NCoE4Z-irZ0'),
 'calc':yt('ClassPad Help 007 – Simple calculations in Main','https://www.youtube.com/watch?v=Zb9V3RwXVLA'),
 'n80':yt('ClassPad Help 80 – Normal probability calculations','https://www.youtube.com/watch?v=OGBTcuB7S8E'),
 'n470':yt('ClassPad Help 470 – Normal probability calculations','https://www.youtube.com/watch?v=awgngSed02c'),
 'n81':yt('ClassPad Help 81 – Inverse normal probability calculations','https://www.youtube.com/watch?v=3VFcgs8Mp40')}
TI={'bar':yt('Bar & pie graphs | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=Wt0QZBrRzDA'),
 'lists':yt('Analysing data | Getting Started Series – Lists & Spreadsheets','https://www.youtube.com/watch?v=qDZRQeUvC0I'),
 'hist':yt('Creating histograms | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=YrluejAQRK4'),
 'dotbox':yt('Dot plots & box plots | Getting Started Series – Data & Statistics','https://www.youtube.com/watch?v=73Ymuvv-BU8'),
 'long':yt('Data analysis: box-plots, dot-plots and histograms (long walkthrough)','https://www.youtube.com/watch?v=wCb6z1IbVy8&t=965s'),
 'uni':yt('Data analysis – univariate data (long walkthrough)','https://www.youtube.com/watch?v=lqml9PBBhV0&t=630s'),
 'z':yt('Calculating and understanding z-scores with TI-nspire','https://www.youtube.com/watch?v=yrR9IALJD6g'),
 'calc':yt('Settings and calculations | Getting Started Series – Calculator','https://www.youtube.com/watch?v=35RcQzXqj6o')}
SK=lambda name,cp,ti:dict(skill=name,classpad=[CP[k] for k in cp],ti=[TI[k] for k in ti])
CASV={'gm12-u3-s1':[SK('Setting up the statistics app',['stat'],['lists'])],
 'gm12-u3-s2':[SK('Creating a histogram',['hl','hf'],['hist']),SK('Setting histogram class intervals',['hc'],[]),
   SK('Creating a dot plot',[],['dotbox']),SK('Finding logs (base 10)',['calc'],['calc']),SK('Full walkthrough: dot plots, boxplots and histograms',[],['long'])],
 'gm12-u3-s3':[SK('Calculating summary statistics (mean, median, standard deviation)',['sl','sf'],['lists','uni'])],
 'gm12-u3-s4':[SK('Creating a boxplot',['bl','bf'],['dotbox','long']),SK('Creating parallel boxplots',['bm'],[])],
 'gm12-u3-s5':[SK('Calculating z-scores',['calc'],['z']),SK('Normal probability calculations',['n80','n470','n81'],[])]}
for l in L:
  if l['id'] in CASV: l['cas']=CASV[l['id']]
ids={l['title']:l for l in L}
def when(t):l=ids[t];return dict(id=l['id'],week=l['week'],lesson=l['lesson'])
SD='VCE Mathematics Study Design 2023–2027'
d=dict(id='general-maths-12',name='Year 12 General Maths',unitLabel='Unit 3',
 scope='Unit 3 only · lesson order only (details to come) · step-up before summer, then Term 1 and Term 2 Weeks 1–11 · SAC sittings after school on Wednesdays',
 summary='Step-up 5 lessons · Term 1: 26 lessons · Term 2 Weeks 1–8: 24 lessons, Week 9 trial exams · Weeks 10–11 to be planned · 3 lessons a week (2 in Step-up week 1 and the Term 1 short week)',
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
