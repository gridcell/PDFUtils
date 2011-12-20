A few tools to help work with PDF documents.


Requirements:
=============

ReportLab:
http://pypi.python.org/pypi/reportlab

PyPDF:
http://pypi.python.org/pypi/pyPdf
         


Example:
=======

	from reportlab.lib.units import inch
	pu = PDFUtils()
	canvas_opts = {
		'fillColor': '#5C9CCC',
		'fontSize': 9
	}
	shutil.copy('c:/temp/doc.pdf','c:/temp/tt.pdf')
	pu.addPageNumbers('c:/temp/tt.pdf', 1.05*inch, 0.807*inch, canvas_opts=canvas_opts)




License:
=======
                    
Copyright (c) 2011, CTQ Consultants Ltd, http://ctqconsultants.ca
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
   * Redistributions of source code must retain the above copyright
	 notice, this list of conditions and the following disclaimer.
   * Redistributions in binary form must reproduce the above copyright
	 notice, this list of conditions and the following disclaimer in the
	 documentation and/or other materials provided with the distribution.
   * Neither the name of the <organization> nor the
	 names of its contributors may be used to endorse or promote products
	 derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.








































