from prompts.length_instruction import length_instruction

def build_initial_summary_prompt(text_chunk, length):
    instructions = length_instruction()

    return f"""
You are an expert research analyst and technical writer.

TASK:
Create an INITIAL summary of an academic document based ONLY on the section provided.

SUMMARY DEPTH:
{instructions[length]}

STRICT RULES:
- Do NOT add information not present in the text.
- If a section is missing, write "Not specified in the paper".
- Prefer factual clarity over creativity.
- Avoid vague phrases.

REQUIRED STRUCTURE:
• Problem Statement:
• Approach / Methodology:
• Key Findings:
• Conclusion / Implications:
• Important Keywords:

WRITING STYLE:
- Plain English
- Clear bullet points
- One idea per bullet
- No paragraphs

CONTENT:
--------------------
{text_chunk}
--------------------
"""


def build_refine_summary_prompt(existing_summary, new_chunk, length):
    instructions = length_instruction()

    return f"""
You are an expert research analyst refining an existing summary.

TASK:
Improve and refine the existing summary using ONLY the new section provided.

SUMMARY DEPTH:
{instructions[length]}

EXISTING SUMMARY:
--------------------
{existing_summary}
--------------------

NEW CONTENT:
--------------------
{new_chunk}
--------------------

STRICT RULES:
- Do NOT remove correct existing information.
- Add new points ONLY if supported by the new content.
- If a required section is still missing, keep "Not specified in the paper".
- Maintain the required structure exactly.
- No paragraphs, bullet points only.

REQUIRED STRUCTURE:
• Problem Statement:
• Approach / Methodology:
• Key Findings:
• Conclusion / Implications:
• Important Keywords:
"""
