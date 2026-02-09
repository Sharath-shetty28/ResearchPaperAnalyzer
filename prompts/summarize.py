from prompts.length_instruction import length_instruction

def build_summary_prompt(text, length):
    instructions = length_instruction()

    summary_prompt = f"""
You are an expert research analyst and technical writer.

TASK:
Summarize the following academic document accurately and concisely.

SUMMARY DEPTH:
{instructions[length]}

STRICT RULES:
- Do NOT add information that is not present in the document.
- If a section is missing, clearly state "Not specified in the paper".
- Prefer factual clarity over creativity.
- Avoid vague phrases like "various methods" or "significant improvements".

REQUIRED STRUCTURE:
• Problem Statement:
• Approach / Methodology:
• Key Findings:
• Conclusion / Implications:
• Important Keywords:

WRITING STYLE:
- Plain English
- Clear bullet points
- Each bullet should contain ONE idea only
- No paragraphs

CONTENT TO SUMMARIZE:
--------------------
{text}
--------------------
"""
    return summary_prompt


