from text_processing import TextProcessing


def process_text(text):
    tp = TextProcessing(text)
    tp.comma_remover()
    tp.removes_special_characters()
    tp.removing_tabs()
    tp.converts_to_lowercase()
    tp.removing_stop_words()
    tp.finding_roots()
    return tp.processed_text
