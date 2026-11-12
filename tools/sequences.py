import json,sys
d=json.load(open(sys.argv[1]));L={l['id']:l for l in d['lessons']}
SEQ={
'p11-u1-l01':dict(length=60,
 goals=['Distinguish between transverse and longitudinal waves','Distinguish between mechanical and electromagnetic waves','Identify amplitude, wavelength, period and frequency on a wave diagram'],
 vocab=['transverse','longitudinal','mechanical wave','electromagnetic wave','medium','amplitude','wavelength','period','frequency','compression','rarefaction'],
 steps=[
  dict(min=5,phase='Do-now',title='What is a wave?',detail='On the board: “Write down 3 things that are waves and 1 thing that moves but is not a wave.” Share a few; aim to reach “a wave transfers energy, not matter”.'),
  dict(min=5,phase='Course intro',title='Week 1 housekeeping',detail='Logbook expectations, where resources live, how CFATs and SACs work this semester. Keep it short; full intro can go in a homeroom slot.'),
  dict(min=15,phase='New knowledge',title='Transverse vs longitudinal',detail='Demo with a slinky (or Mr Lloyd prac 1A): flick sideways for transverse, push-pull for longitudinal. Students sketch both and label particle motion vs energy direction. Introduce mechanical (needs a medium) vs EM (no medium, all travel at c in a vacuum).',resource='Mr Lloyd prac 1A Modelling mechanical waves; Mr Lloyd U1 AoS1 slides'),
  dict(min=10,phase='New knowledge',title='Parts of a wave',detail='Worked example on a displacement–distance graph: label amplitude, wavelength. Then a displacement–time graph: label period. Define $f = \\frac{1}{T}$.',resource='Pearson SB 2.1 diagrams'),
  dict(min=17,phase='Apply',title='Practice',detail='Pearson 2.1 Key questions 1–9. Early finishers: Cambridge 1A Check-in Set 1.',resource='Pearson SB 2.1 KQ 1–9; Cambridge 1A Check-in Set 1'),
  dict(min=8,phase='Exit ticket',title='Goal revisited',detail='Two quick sketches: a transverse wave with amplitude and wavelength labelled, and a longitudinal wave with a compression and rarefaction labelled. Students rate confidence red/amber/green on the goals.')]),
'p11-u1-l02':dict(length=60,
 goals=['Use the wave equation $v = f\\lambda$ to calculate speed, frequency or wavelength','Use $T = \\frac{1}{f}$ to convert between period and frequency','Explain that wave speed is set by the medium and frequency by the source'],
 vocab=['wave equation','wave speed','period','frequency','hertz (Hz)','medium','source'],
 steps=[
  dict(min=6,phase='Do-now',title='Retrieval from Lesson 1',detail='“Sketch a transverse wave and label the amplitude and wavelength. What is the difference between a mechanical and an EM wave?”'),
  dict(min=12,phase='New knowledge',title='The wave equation',detail='Derive $v = \\frac{\\lambda}{T} = f\\lambda$ from distance over time for one wavelength. Two worked examples: find $v$, then rearrange to find $\\lambda$. Stress units (Hz, m, m s$^{-1}$).',resource='Mr Lloyd U1 AoS1 slides; Pearson SB 2.2'),
  dict(min=8,phase='New knowledge',title='What sets the speed?',detail='Thought experiment: a wave passes from deep to shallow water. Frequency stays the same (set by the source); speed changes (set by the medium), so wavelength must change. Quick class discussion.'),
  dict(min=8,phase='Guided practice',title='We do',detail='Mr Lloyd’s do-now problem as a guided example: a wave has $f = 250$ Hz and $\\lambda = 1.2$ m. Find its speed, then its period.'),
  dict(min=18,phase='Apply',title='Practice',detail='Pearson 2.2 Key questions 1–7. Extension: Mr Lloyd prac 1B.1 Modelling tsunami waves (or save it for a later lesson).',resource='Pearson SB 2.2 KQ 1–7; Cambridge 1A Check-in Set 2; Cambridge Worksheet 1A–1'),
  dict(min=8,phase='Exit ticket',title='Goal revisited',detail='“A radio station broadcasts at 100 MHz. Find the wavelength.” ($c = 3.0 \\times 10^8$ m s$^{-1}$.) Red/amber/green on the goals.')]),
'p11-u1-l03':dict(length=60,
 goals=['Order the regions of the EM spectrum by wavelength, frequency and energy','Describe the Sun’s radiation as mainly UV, visible and infrared','Compare the uses of different regions of the EM spectrum in society'],
 vocab=['electromagnetic spectrum','radio','microwave','infrared','visible','ultraviolet','X-ray','gamma','speed of light, $c$'],
 steps=[
  dict(min=6,phase='Do-now',title='Wave equation check',detail='“Light has $\\lambda = 500$ nm. Find its frequency.” Reviews $v = f\\lambda$ with $c$.'),
  dict(min=14,phase='New knowledge',title='The EM spectrum',detail='Build the spectrum on the board from radio to gamma, with wavelength and frequency arrows in opposite directions. Mnemonic optional. All travel at $c$ in a vacuum. Note the Sun emits mainly UV, visible and IR.',resource='Pearson SB 2.3; Cambridge Figure slides 1B; Mr Lloyd U1 AoS1 slides'),
  dict(min=15,phase='Apply',title='Uses of EM radiation',detail='Jigsaw: each group takes one region and finds two uses and one hazard, then reports back in 1 minute. Mr Lloyd prac 1C.2 Using the electromagnetic spectrum works as the task sheet.',resource='Mr Lloyd prac 1C.2'),
  dict(min=17,phase='Apply',title='Practice',detail='Pearson 2.3 Key questions 1–8. Early finishers: Cambridge 1B Check-in Set 1.',resource='Pearson SB 2.3 KQ 1–8; Cambridge Worksheet 1B–1'),
  dict(min=8,phase='Exit ticket',title='Goal revisited',detail='“Order these by increasing frequency: infrared, ultraviolet, visible, radio.” (Mr Lloyd’s do-now.) Plus one use each of microwaves and X-rays. Red/amber/green on the goals.')])}
for k,v in SEQ.items(): L[k]['sequence']=v
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print('ok',[ (k,sum(s['min'] for s in v['steps'])) for k,v in SEQ.items()])
