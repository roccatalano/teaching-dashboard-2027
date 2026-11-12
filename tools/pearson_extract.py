import docx,re,json,sys
out=[]
for unit,f in [(1,'Unit 1 Pearson Plan/hp11_u1_stp (2).docx'),(2,'Unit 2 Pearson Plan/hp11_u2_stp.docx')]:
  d=docx.Document('/mnt/user-data/uploads/Pearson Resources/'+f)
  aos=0
  for t in d.tables[1:]:
    hdr=[c.text.strip() for c in t.rows[0].cells]
    if hdr[0]!='Week': continue
    aos+=1
    for r in t.rows[1:]:
      c=[x.text.strip() for x in r.cells]
      out.append(dict(unit=unit,aos=aos,week=c[0],hdr=hdr,cells=c))
json.dump(out,open('/tmp/build/raw.json','w'),indent=1)
for o in out:
  c=o['cells'];print(o['unit'],o['aos'],repr(c[0]),'|',c[1].replace('\n',' / ')[:150] if o['hdr'][1].startswith('Hein') else c[3].replace('\n',' / ')[:150])
