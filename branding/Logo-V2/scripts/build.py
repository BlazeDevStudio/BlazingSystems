#!/usr/bin/env python3
"""Build reusable PNG, PDF and ZIP brand kit from committed SVGs; no original PSD is fabricated."""
from pathlib import Path
import io, zipfile
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import cairosvg
base=Path(__file__).resolve().parents[1]
out=base/"dist";out.mkdir(exist_ok=True)
for file in [*(base/"assets/vector").glob("*.svg"),*(base/"mockups").glob("*.svg"),*(base/"preview").glob("*.svg")]:
    sizes=(128,256,512,1024) if file.name in ("icon-traced.svg","app-icon.svg") else (1024,)
    for width in sizes:
        cairosvg.svg2png(url=str(file),write_to=str(out/(file.stem+"-"+str(width)+".png")),output_width=width)
pdf=out/"Logo-V2-Brand-Guidelines.pdf";c=canvas.Canvas(str(pdf),pagesize=(595,842));c.setTitle("Blaze Systems Logo V2 Brand Guidelines")
c.setFillColor(HexColor("#001A3D"));c.rect(0,615,595,227,stroke=0,fill=1)
c.setFillColor(HexColor("#7DD3FF"));c.setFont("Helvetica-Bold",14);c.drawString(44,785,"BLAZE SYSTEMS / BRAND IDENTITY")
c.setFillColor(HexColor("#FFFFFF"));c.setFont("Helvetica-Bold",40);c.drawString(44,698,"LOGO V2")
c.setFont("Helvetica",12);c.drawString(44,656,"PEOPLE / TECHNOLOGY / PROGRESS")
c.setFillColor(HexColor("#001A3D"));c.setFont("Helvetica-Bold",18);c.drawString(44,557,"Brand palette")
colors=[("#0066FF","Blaze Blue"),("#00B0FF","Electric Blue"),("#001A3D","Deep Blue"),("#7DD3FF","Light Blue")]
for i,(hex,label) in enumerate(colors):
 x=44+i*132;c.setFillColor(HexColor(hex));c.roundRect(x,445,110,82,10,stroke=0,fill=1);c.setFillColor(HexColor("#001A3D"));c.setFont("Helvetica",9);c.drawString(x,428,label);c.drawString(x,414,hex)
c.setFont("Helvetica-Bold",18);c.drawString(44,345,"Identity and implementation")
lines=["B: stylized blue ribbon/flame symbol; two-part BLAZE / SYSTEMS lockup.","Type: Montserrat, bold/extra bold with spaced uppercase SYSTEMS.","Usage: preserve ratio; suggested 25% icon-width clear space.","Suggested sizes: icon 32 CSS px; horizontal lockup 180 CSS px.","For accessible interfaces use alternative text: Blaze Systems.","Important: SVG is an approximate trace of an approved flattened reference.","Not an original AI, PSD, EPS, or trademark-clearance certificate.","See docs/BRAND_GUIDELINES.md for complete rules and provenance."]
c.setFont("Helvetica",10)
for i,line in enumerate(lines): c.drawString(44,312-i*27,line)
c.setFillColor(HexColor("#446480"));c.setFont("Helvetica",9);c.drawString(44,60,"Blaze Systems / Logo V2 / 2026-10-20")
c.save()
kit=out/"Blaze-Systems-Logo-V2-Kit.zip"
with zipfile.ZipFile(kit,"w",compression=zipfile.ZIP_DEFLATED) as z:
 for p in base.rglob("*"):
  if not p.is_file() or p==kit:continue
  z.write(p,arcname="Logo V2/"+str(p.relative_to(base)))
print("Generated",kit)
