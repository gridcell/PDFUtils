This simple library was basically created so I could add Page X of Y to pdf
documents that were generated using ReportLab.


Requirements
------------

ReportLab:
http://pypi.python.org/pypi/reportlab

PyPDF:
http://pypi.python.org/pypi/pyPdf
         

Features
--------
* Add Page X of Y to PDF documents.
* Append PDF documents together.
* Overlay/Merge two PDF documents.


Using
-----

Example::

	from reportlab.lib.units import inch
	pu = PDFUtils()
	canvas_opts = {
		'fillColor': '#5C9CCC',
		'fontSize': 9
	}
	pu.addPageNumbers('c:/temp/doc.pdf', 1.05*inch, 0.807*inch, canvas_opts=canvas_opts)

Documentation
-------------

PDFUtils Class::

   A few tools to help work with PDF documents.
   
   Methods defined here:
   
   addPageNumbers(self, pdf_doc, x, y, template='Page %(page)s of %(count)s', canvas_opts=None)
       Add page numbers to a PDF document.
       
       pdf_doc: (string)
               Path to PDF document.
       x: (integer)
               X coordinate to place text (in pixels).
       y: (integer)
                Y coordinate to place text (in pixels).
       template: (string)
               Template to use for page numbers. Uses string formating
                         with the following options (default: Page %(page)s of %(count)s):
                       page:
                               Current page.
                       count:
                               Page count for the PDF document.
       canvas_opts: (dict)
               Options to apply to the canvas. (default: None)
               NOTE: Only fillColor and fontSize are currently implemented.
               Example: canvas_opts = {'fillColor': '#5C9CCC','fontSize': 9}
               
       Example:
               from reportlab.lib.units import inch
               pu = PDFUtils()
               canvas_opts = {
                       'fillColor': '#5C9CCC',
                       'fontSize': 9
               }
               pu.addPageNumbers('c:/temp/doc.pdf', 1.05*inch, 0.807*inch, canvas_opts=canvas_opts)
   
   addPdfOverlay(self, pdf_doc, overlay_doc, output_doc, repeatOverlay=False)
       Essentially merging two PDF documents.
       
       pdf_doc: (string)
               Path to PDF document.
       overlay_doc: (string)
               Path to PDF overlay document to overlay pdf_doc.
       repeatOverlay: (boolean)
               If set to True, page 1 of the overlay document is repeated
               for each page of the pdf_doc. (default: False)
   
   appendDocuments(self, pdf_docs, output_doc)
       Append PDF documents together.
       
       pdf_docs: (list)
               List of PDF document paths.
       
       output_doc: (string)
               Path to the outputed PDF document.
   
   pdfPageCount(self, pdf_doc)
       Wrapper to get page count from pdf document.
       
       pdf_doc: (string)
               Path to PDF document.
   
   replicatePage(self, pdf_doc, count=1, pageNumber=1)
       Replicate a page in a document, appends replicated page to
       the end of the document.
       
       pdf_doc: (string)
               Path to PDF document.
       count: (integer)
               Number of times to replicate page. (default 1)
       pageNumber: (integer)
               Page number to replicate. (default 1)
   




License
--------
                    
Copyright (c) 2011, CTQ Consultants 
All rights reserved. 

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met: 

* Redistributions of source code must retain the above copyright notice, 
  this list of conditions and the following disclaimer. 
* Redistributions in binary form must reproduce the above copyright 
  notice, this list of conditions and the following disclaimer in the 
  documentation and/or other materials provided with the distribution. 
* Neither the name of CTQ Consultants nor the names of its contributors 
  may be used to endorse or promote products derived from this software 
  without specific prior written permission. 

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
POSSIBILITY OF SUCH DAMAGE. 








































