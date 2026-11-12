import json,sys
d=json.load(open(sys.argv[1]));L={l['id']:l for l in d['lessons']}
SEQ={
'p11-u1-l01':dict(length=79,
 goals=['Distinguish between transverse and longitudinal waves','Distinguish between mechanical and electromagnetic waves','Identify amplitude, wavelength, period and frequency on a wave diagram'],
 vocab=['transverse','longitudinal','mechanical wave','electromagnetic wave','medium','amplitude','wavelength','period','frequency','compression','rarefaction'],
 doNow=[dict(when='Last lesson',note='First lesson of the year, so this draws on Year 10 science',q='Name the unit of energy, and give one example of energy being transferred from one place to another.'),
        dict(when='Last week',note='Year 10 science',q='Sound travels as a wave. Can sound travel through outer space? Why or why not?'),
        dict(when='Last term',note='Year 9/10 science',q='Give two examples of things that are waves and one thing that moves but is not a wave.')],
 steps=[
  dict(min=8,phase='Do-now',title='Retrieval practice',detail='Students answer the three do-now questions independently as they arrive, then self-mark as you reveal answers.'),
  dict(min=7,phase='Course intro',title='Week 1 housekeeping',detail='Logbook expectations, where resources live, how CFATs and SACs work this semester. Keep it brief.'),
  dict(min=2,phase='Learning goals',title='Share the goals',detail='Read the “I can” statements together; students write them at the top of the page.'),
  dict(min=7,phase='APK',title='What does a wave carry?',detail='Prerequisite: energy transfer, and the idea of a medium (particles). Quick think-pair-share: “A stadium Mexican wave moves around the ground, but does anyone actually move around the stadium?” Draw out that the wave transfers energy but not matter, and that the people are the medium.'),
  dict(min=20,phase='New knowledge',title='Transverse vs longitudinal; mechanical vs EM',detail='Slinky demo (Mr Lloyd prac 1A): flick sideways for transverse, push-pull for longitudinal. Students sketch both and label particle motion vs energy direction. Then mechanical (needs a medium) vs EM (no medium, all travel at $c$ in a vacuum). Finish with a displacement–distance graph labelling amplitude and wavelength, and a displacement–time graph labelling period; define $f = \\frac{1}{T}$.',resource='Mr Lloyd prac 1A Modelling mechanical waves; Mr Lloyd U1 AoS1 slides; Pearson SB 2.1'),
  dict(min=8,phase='Guided practice',title='We do',detail='Label a wave diagram together: amplitude 3 cm, wavelength 40 cm. One wave passes a point every 0.5 s. What are the period and frequency?'),
  dict(min=19,phase='Apply',title='Independent practice',detail='Pearson 2.1 Key questions 1–9. Early finishers: Cambridge 1A Check-in Set 1.',resource='Pearson SB 2.1 KQ 1–9; Cambridge 1A Check-in Set 1'),
  dict(min=8,phase='Exit ticket',title='Goals revisited',detail='Two quick sketches: a transverse wave with amplitude and wavelength labelled, and a longitudinal wave with a compression and rarefaction labelled. Students rate confidence red/amber/green on each goal.')]),
'p11-u1-l02':dict(length=79,
 goals=['Use the wave equation $v = f\\lambda$ to calculate speed, frequency or wavelength','Use $T = \\frac{1}{f}$ to convert between period and frequency','Explain that wave speed is set by the medium and frequency by the source'],
 vocab=['wave equation','wave speed','period','frequency','hertz (Hz)','medium','source'],
 doNow=[dict(when='Last lesson',q='Sketch a transverse wave and label the amplitude and the wavelength.'),
        dict(when='Last week',note='Lesson 1, since it is still Week 1',q='What is the difference between a mechanical wave and an electromagnetic wave?'),
        dict(when='Last term',note='Year 10 science',q='A car travels 100 m in 5 s. What is its average speed?')],
 steps=[
  dict(min=8,phase='Do-now',title='Retrieval practice',detail='Three do-now questions done independently, then self-marked.'),
  dict(min=2,phase='Learning goals',title='Share the goals',detail='Read the “I can” statements together.'),
  dict(min=7,phase='APK',title='Speed and rearranging formulas',detail='Prerequisites for $v = f\\lambda$: speed as $v = \\frac{d}{t}$, and rearranging a formula. Mini whiteboards: “Rearrange $v = \\frac{d}{t}$ for $t$, then for $d$. Convert 2.5 km to m, and 300 ms to s.” Check who struggles with rearranging before you teach.'),
  dict(min=18,phase='New knowledge',title='The wave equation, and what sets wave speed',detail='Derive $v = \\frac{\\lambda}{T} = f\\lambda$ from distance over time for one wavelength. Two worked examples: find $v$, then rearrange to find $\\lambda$; stress units. Then a thought experiment: a wave passes from deep to shallow water. Frequency stays the same (set by the source); speed changes (set by the medium), so wavelength must change.',resource='Mr Lloyd U1 AoS1 slides; Pearson SB 2.2'),
  dict(min=10,phase='Guided practice',title='We do',detail='Mr Lloyd’s problem as a guided example: a wave has $f = 250$ Hz and $\\lambda = 1.2$ m. Find its speed, then its period. Then students try one in pairs: a sound wave in air ($v = 340$ m s$^{-1}$) has $f = 680$ Hz. Find $\\lambda$.'),
  dict(min=26,phase='Apply',title='Independent practice',detail='Pearson 2.2 Key questions 1–7, then Cambridge Worksheet 1A–1. Optional hands-on extension: Mr Lloyd prac 1B.1 Modelling tsunami waves.',resource='Pearson SB 2.2 KQ 1–7; Cambridge Worksheet 1A–1; Cambridge 1A Check-in Set 2; Mr Lloyd prac 1B.1'),
  dict(min=8,phase='Exit ticket',title='Goals revisited',detail='“A radio station broadcasts at 100 MHz. Find the wavelength.” ($c = 3.0 \\times 10^8$ m s$^{-1}$.) Red/amber/green on each goal.')]),
'p11-u1-l03':dict(length=79,
 goals=['Order the regions of the EM spectrum by wavelength, frequency and energy','Describe the Sun’s radiation as mainly UV, visible and infrared','Compare the uses of different regions of the EM spectrum in society'],
 vocab=['electromagnetic spectrum','radio','microwave','infrared','visible','ultraviolet','X-ray','gamma','speed of light, $c$'],
 doNow=[dict(when='Last lesson',q='A wave has $f = 50$ Hz and $\\lambda = 4$ m. Calculate its speed.'),
        dict(when='Last week',note='Lesson 1, since it is still Week 1',q='Is light a transverse or longitudinal wave? Is it mechanical or electromagnetic?'),
        dict(when='Last term',note='Year 9/10 science',q='Name two types of radiation that can be harmful to people, and one way to protect against them.')],
 steps=[
  dict(min=8,phase='Do-now',title='Retrieval practice',detail='Three do-now questions done independently, then self-marked.'),
  dict(min=2,phase='Learning goals',title='Share the goals',detail='Read the “I can” statements together.'),
  dict(min=7,phase='APK',title='Scientific notation and big and small numbers',detail='Prerequisites: scientific notation and SI prefixes (nm, MHz, GHz). Mini whiteboards: “Write 500 nm in metres. Write 2.4 GHz in hertz. Which is bigger, $10^{-7}$ or $10^{-9}$?” Also ask: “What everyday things use ‘radiation’?” to surface the misconception that all radiation is dangerous.'),
  dict(min=18,phase='New knowledge',title='The EM spectrum',detail='Build the spectrum on the board from radio to gamma, with wavelength and frequency arrows in opposite directions; energy increases with frequency. All travel at $c$ in a vacuum. The Sun emits mainly UV, visible and IR. Worked example: “Light has $\\lambda = 500$ nm. Find its frequency.”',resource='Pearson SB 2.3; Cambridge Figure slides 1B; Mr Lloyd U1 AoS1 slides'),
  dict(min=18,phase='Guided practice',title='Jigsaw: uses of EM radiation',detail='Each group takes one region and finds two uses and one hazard, then reports back in 1 minute. Use Mr Lloyd prac 1C.2 Using the electromagnetic spectrum as the task sheet. Build a class summary table as groups report.',resource='Mr Lloyd prac 1C.2'),
  dict(min=18,phase='Apply',title='Independent practice',detail='Pearson 2.3 Key questions 1–8. Early finishers: Cambridge 1B Check-in Set 1.',resource='Pearson SB 2.3 KQ 1–8; Cambridge Worksheet 1B–1; Cambridge 1B Check-in Set 1'),
  dict(min=8,phase='Exit ticket',title='Goals revisited',detail='“Order these by increasing frequency: infrared, ultraviolet, visible, radio.” (Mr Lloyd’s do-now.) Plus one use each of microwaves and X-rays. Red/amber/green on each goal.')])}
for k,v in SEQ.items():
  assert sum(s['min'] for s in v['steps'])==79,(k,sum(s['min'] for s in v['steps']))
  L[k]['sequence']=v
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print('ok')
