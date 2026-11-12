import docx,re,json,sys
out=[]
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M='{http://schemas.openxmlformats.org/officeDocument/2006/math}'
def celltext(cell):
  ps=[]
  for p in cell._tc.iter(W+'p'):
    t=''.join(n.text or '' for n in p.iter() if n.tag in (W+'t',M+'t'))
    ps.append(t)
  return '\n'.join(ps).strip()
for unit,f in [(1,'Unit 1 Pearson Plan/hp11_u1_stp (2).docx'),(2,'Unit 2 Pearson Plan/hp11_u2_stp.docx')]:
  d=docx.Document('/mnt/user-data/uploads/Pearson Resources/'+f)
  aos=0
  for t in d.tables[1:]:
    hdr=[c.text.strip() for c in t.rows[0].cells]
    if hdr[0]!='Week': continue
    aos+=1
    for r in t.rows[1:]:
      c=[celltext(x) for x in r.cells]
      out.append(dict(unit=unit,aos=aos,week=c[0],hdr=hdr,cells=c))
json.dump(out,open('/tmp/build/raw.json','w'),indent=1)
