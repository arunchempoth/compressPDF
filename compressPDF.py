from __future__ import print_function
import os
import subprocess

PDF_LOCATION=""

for root, dirs, files in os.walk(PDF_LOCATION):
	print(root)
	for file in files:
    		if file.endswith(".pdf"):
      			filename = os.path.join(root, file)
      			arg1= '-sOutputFile=' +"v"+ file
      			p = subprocess.Popen(['/usr/local/bin/gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4', '-dPDFSETTINGS=/default', '-dNOPAUSE', '-dBATCH',  '-dQUIET', str(arg1), filename], stdout=subprocess.PIPE)
      			print (p.communicate())
