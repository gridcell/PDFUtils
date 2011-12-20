# Copyright (c) 2011, CTQ Consultants Ltd, http://ctqconsultants.ca
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os, random, string, shutil
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

class PDFUtils(object):
	'''
		A few tools to help work with PDF documents.
	
	'''
	def __uniqueName(self):
		return''.join([random.choice(string.hexdigits) for i in range(10)])
	
	def pdfPageCount(self, pdf_doc):
		'''
			Wrapper to get page count from pdf document.
			
			pdf_doc: (string)
				Path to PDF document.
		'''
		pdf = PdfFileReader(file(pdf_doc, "rb"))
		page_count = pdf.numPages
		pdf.stream.close()
		return page_count
	
	def appendDocuments(self, pdf_docs, output_doc):
		'''
		Append PDF documents together.
		
		pdf_docs: (list)
			List of PDF document paths.
		
		output_doc: (string)
			Path to the outputed PDF document.
		'''
		try:
			outputWriter = PdfFileWriter()
			pdf_readers = []
			for doc in pdf_docs:
				# Need to add new PdfFileReader objects to 
				# list so stream can be closed after the loop.
				pdf_readers.append(PdfFileReader(file(doc , "rb")))
				for pg in pdf_readers[-1].pages:
					outputWriter.addPage(pg)
			# Output
			outputStream = file(output_doc, "wb")
			outputWriter.write(outputStream)
			outputStream.close()
			for pdf_reader in pdf_readers:
				pdf_reader.stream.close()
			return True
		except:
			return False

	def replicatePage(self, pdf_doc, count=1, pageNumber=1):
		'''
			Replicate a page in a document, appends replicated page to
			the end of the document.
			
			pdf_doc: (string)
				Path to PDF document.
			count: (integer)
				Number of times to replicate page. (default 1)
			pageNumber: (integer)
				Page number to replicate. (default 1)
		'''
		pdf_reader = PdfFileReader(file(pdf_doc, "rb"))
		page = pdf.getPage(pageNumber-1)
		pdf_dir = os.path.dirname(pdf_doc)
		unique_filename = self.__uniqueName()
		outputWriter = PdfFileWriter()
		# Copy oringal pages to new document.
		for pg in pdf_reader.pages:
			outputWriter.addPage(pg)
		
		# Added replicated pages.
		for n in range(count):
			outputWriter.addPage(page)
			
		# Output
		temp_file = os.path.join(pdf_dir, unique_filename+".pdf")
		outputStream = file(temp_file, "wb")
		outputWriter.write(outputStream)
		outputStream.close()
		pdf_reader.stream.close()
		
		shutil.move(temp_file, pdf_doc)
	
	def __applyCanvasOptions(self, canvas, opts):
		for opt in opts:
			if opt == 'fillColor':
				canvas.setFillColor(opts[opt])
			if opt == 'fontSize':
				canvas.setFontSize(opts[opt])
		return canvas
				
	def addPageNumbers(self, pdf_doc, x, y, template='Page %(page)s of %(count)s', canvas_opts=None):
		'''
		
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
				shutil.copy('c:/temp/doc.pdf','c:/temp/tt.pdf')
				pu.addPageNumbers('c:/temp/tt.pdf', 1.05*inch, 0.807*inch, canvas_opts=canvas_opts)
								
		'''
		# Create working directory
		dir_path = os.path.dirname(pdf_doc)
		tempdir_path = os.path.join(dir_path, self.__uniqueName())
		os.makedirs(tempdir_path)
		
		# Generate document for each numbered page
		pge_cnt = self.pdfPageCount(pdf_doc)
		template_data = {
			'page': None,
			'count': pge_cnt
		}
		numbered_pages = []
		for i in range(pge_cnt):
			doc = os.path.join(tempdir_path, '%s.pdf'%(i+1))
			numbered_pages.append(doc)
			c = canvas.Canvas(doc,pagesize=letter)
			if canvas_opts:
				self.__applyCanvasOptions(c,canvas_opts)
			template_data['page'] = i+1
			c.drawString(x, y, template % template_data)
			c.showPage()
			c.save()
			
		# Append all page pdf documents
		pg_num_doc = os.path.join(tempdir_path, '%s.pdf'%self.__uniqueName())
		self.appendDocuments(numbered_pages, pg_num_doc)
		
		# Overlay original pdf document with page number pdf document
		new_doc = os.path.join(tempdir_path, '%s.pdf'%self.__uniqueName())
		self.addPdfOverlay(pdf_doc, pg_num_doc, new_doc)
		
		# Cleanup the carnage
		shutil.move(new_doc, pdf_doc) # Replace original document with new one.
		shutil.rmtree(tempdir_path)
	
	def addPdfOverlay(self, pdf_doc, overlay_doc, output_doc, repeatOverlay=False):
		'''
			Essentially merging two PDF documents.
			
			pdf_doc: (string)
				Path to PDF document.
			overlay_doc: (string)
				Path to PDF overlay document to overlay pdf_doc.
			repeatOverlay: (boolean)
				If set to True, page 1 of the overlay document is repeated
				for each page of the pdf_doc. (default: False)
		'''
		pdf = PdfFileReader(file(pdf_doc, "rb"))
		pdf_overlay = PdfFileReader(file(overlay_doc, "rb"))
		page_cnt = pdf.numPages
		if repeatOverlay:
			overlay_pages = [pdf_overlay.getPage(0) for n in range(page_cnt)]
		else:
			overlay_pages = pdf_overlay.pages
		outputWriter = PdfFileWriter()
		for n in range(page_cnt):
			pg = pdf.getPage(n)
			pg.mergePage(overlay_pages[n])
			outputWriter.addPage(pg)
		
		# Output
		outputStream = file(output_doc, "wb")
		outputWriter.write(outputStream)
		
		# Close streams
		outputStream.close()
		pdf.stream.close()
		pdf_overlay.stream.close()
		
