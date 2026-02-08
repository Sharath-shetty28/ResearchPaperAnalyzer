from core.chunking import chunk_text ,summarize_chunk
from prompts.combine_summaries import combine_summaries

def summarize_pdf_detail(text, summary_length):
    chunks = chunk_text(text)

    chunk_summaries = []
    for chunk in chunks:
        summary = summarize_chunk(chunk, summary_length)
        chunk_summaries.append(summary)

    final_summary = combine_summaries(chunk_summaries)
    return final_summary