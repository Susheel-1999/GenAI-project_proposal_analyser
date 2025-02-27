from docling.document_converter import DocumentConverter, PdfFormatOption
# from docling.datamodel.pipeline_options import (PdfPipelineOptions, TesseractCliOcrOptions)
from docling.datamodel.base_models import InputFormat

# # to use the tesseract ocr
# pipeline_options = PdfPipelineOptions(ocr_options=TesseractCliOcrOptions(force_full_page_ocr=True), 
#                                       do_ocr=True, 
#                                       do_table_structure=True)
# pipeline_options.table_structure_options.do_cell_matching = True


converter = DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption()})  

def read_document(source: str) -> str:
    result = converter.convert(source)
    result = result.document.export_to_markdown()
    return result