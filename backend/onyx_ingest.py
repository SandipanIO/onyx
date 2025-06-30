import os
from onyx.ingest.document_loader import load_documents
from onyx.ingest.pipeline import run_ingest
from onyx.utils.file_processing import get_filepaths_from_dir

def main():
    # Local files folder
    folder = "backend/data/training_docs"
    os.makedirs(folder, exist_ok=True)

    # Load local documents (.docx, .pdf, .md)
    file_list = get_filepaths_from_dir(folder)
    docs = load_documents(file_list)

    # Load URLs
    urls = [
        # 🌐 HTML Core Topics
        "https://developer.mozilla.org/en-US/docs/Web/HTML",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element#text_content",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a",
        "https://developer.mozilla.org/en-US/docs/Glossary/Semantics",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol",
        "https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul",
    
        # 🎨 CSS Core Topics
        "https://developer.mozilla.org/en-US/docs/Web/CSS",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/Syntax",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Box_Model",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/position",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout",
        "https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/color",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/display",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-classes",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations",
        "https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries"
    ]

    docs += load_documents(urls)

    # Ingest
    run_ingest(docs)

if __name__ == "__main__":
    main()
