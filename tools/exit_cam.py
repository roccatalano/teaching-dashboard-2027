# Exit tickets: one Cambridge question per learning goal (goal order matches sequence.goals).
# Usage: python exit_cam.py classes/physics-11.json   (pool: tools/cambridge_exit_pool.json)
import json,sys,re,os
d=json.load(open(sys.argv[1]))
P=json.load(open(os.path.join(os.path.dirname(__file__),'cambridge_exit_pool.json')))
FIG=' [figure in Cambridge doc]'
OWN={
 'pol':"Unpolarised light passes through a polarising filter, then through a second filter that is slowly rotated through 90°. Describe what happens to the brightness of the light coming through, and explain why this is evidence that light is a transverse wave.",
 'chg':"Two small spheres are held 10 cm apart. Sphere A has a charge of +2 nC and sphere B has a charge of –3 nC.\na Do the spheres attract or repel? Explain.\nb Sphere B is replaced by a sphere with a charge of +3 nC. What changes, and why?",
}
TXT={  # trimmed versions where the original refers to a picture or asks for a drawing
 '2A10':"Suggest why people sometimes prefer mittens to gloves in cold weather.",
 '5D7':"Lamps of resistance 300 Ω, 400 Ω and 600 Ω are connected in parallel to a 12 V battery.\na What is the total resistance in the circuit?\nb What is the current in each lamp?",
}
# section -> one ref per goal. 'own:x' = written question; '*' = needs the Cambridge figure (slides)
MAP={
 '2.1':['1A1','Ch1-18','Ch1-4'], '2.2':['1A3*','1A7','Ch1-23'], '2.3':['1B5','Ch1-3','Ch1-27'],
 '3.1':['1C2','1C4*','1C5'], '3.2':['1C9','Ch1-11','own:pol'],
 '4.1':['Ch2-2','Ch2-3','2A1'], '4.2':['2A11','2A7','2A6'], '4.3':['Ch2-7','2A8','2A3'], '4.4':['2A4','2A5','2A10'],
 '5.1':['2B3','2B5','2B4'], '5.2':['2B6','Ch2-13','Ch2-20'],
 '6.1':['3A1','3A6','3A10'], '6.2':['3B4','3B6','3B2'], '6.3':['3C2','3C1','3D2'], '6.4':['3E9','3E11','3E12'],
 '7.2':['4A7','4B7','4C9'],
 '8.1':['own:chg','Ch5-4','5A10'], '8.2':['5A11','5B6','5D2'], '8.3':['5E8','6B1','6B3'],
 '8.4':['5C1','Ch5-9','6A7'], '9.1':['5D7','5D8','5D3'], '9.2':['6B4','6B6','6B8'], '9.3':['6C9','6C11','6C2'],
}
def clean(q):
  q=re.sub(r'\n?\s*(Short[- ]answer questions|Multiple-choice questions|Use c = .*)\s*$','',q.strip())
  q=re.sub(r'\[[^\]]*\]','',q); q=re.sub(r'\s*\(\d+ marks?\)','',q)
  return '\n'.join(l.strip() for l in q.splitlines() if l.strip())
def item(ref,g):
  if ref.startswith('own:'): return dict(q=OWN[ref[4:]],note=f'Goal {g} · own question (no Cambridge match)')
  fig=ref.endswith('*'); ref=ref.rstrip('*')
  if ref.startswith('Ch'):
    c,n=ref.split('-'); q=P[c][n]; src=f'Cambridge {c[2:] and "Ch"+c[2:]} Review questions, Q{n}'
  else:
    c,n=ref[:2],ref[2:]; q=P[c][n]; src=f'Cambridge {c} Section questions, Q{n}'
  q=TXT.get(ref) or clean(q)
  if fig: src+=FIG
  return dict(q=q,note=f'Goal {g} · {src}')
n=0
for l in d['lessons']:
  s=l.get('sequence')
  if l['type']!='lesson' or not s or l['section'] not in MAP: continue
  refs=MAP[l['section']]; assert len(refs)==len(s['goals']),l['id']
  s['exitQs']=[item(r,i+1) for i,r in enumerate(refs)]
  for st in s['steps']:
    if st['phase']=='Exit ticket':
      st['detail']='One question per learning goal (below), done individually and handed in. Then red/amber/green on each goal.'
      st.pop('resource',None)
  n+=1
json.dump(d,open(sys.argv[1],'w'),indent=1,ensure_ascii=False)
print('lessons',n)
