from fastapi import HTTPException
import json
from io import BytesIO
import re
import pdfplumber

# <----- MAIN Function ----->
def extractor(file, type: str, category: str):
    match category:
        case "judgement":
            return judgement_extractor(file)
        
        case "order":
            return order_extractor(file)
        
        case "act":
            return act_extractor(file)

        case _:
            raise HTTPException(detail="Unsupported file format!!!", status_code=400)

# <----- ORDER EXTRACTOR ----->
def cleanup_order_text(text: str):
    outcomes = re.split("=.+=", text)
    main_content = outcomes[-1]
    metadatas = "\n".join(outcomes[:-1])
    response = "# SEPERATOR #".join([metadatas, main_content])
    return response

def order_extractor(file):
    file_bytes = file.file.read()
    with pdfplumber.open(BytesIO(file_bytes)) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""

    cleaned_text = cleanup_order_text(text)
    return cleaned_text

# <----- JUDGEMENT EXTRACTOR ----->
def judgement_extractor(file):
    file_bytes = file.file.read()
    content = json.loads(file_bytes)

    max_chunk_size = 2000
    output = []

    temp_text = ""
    header
    data = content.get("JudgementText", {}).get("Paragraphs", [])

    for para in data:
        subparagraphs = para.get("SubParagraphs", [])
        for i, sub in enumerate(subparagraphs):
            text = sub.get("Text", "")
            # add indentation for subpoints
            if sub.get("IsSub"):
                text = "\t" + text

            # if adding this sub/sub-sub paragraph exceeds max_chunk_size, flush current
            if len(temp_text) + len(text) > max_chunk_size:
                if temp_text:
                    output.append(temp_text.strip())
                    output.append("# SEPERATOR #")
                temp_text = text  # start new chunk with current subparagraph
            else:
                temp_text += text

    # flush leftover text
    if temp_text:
        output.append(temp_text.strip())

    return "\n".join(output)

# def judgement_extractor(file):
#     file_bytes = file.file.read()
#     content = json.loads(file_bytes)

#     chunk_size = 2000
#     max_chunk_size = 2500
#     output = []

#     temp_text = ""
#     data = content.get("JudgementText", {}).get("Paragraphs", [])

#     for para in data:
#         for sub in para.get("SubParagraphs", []):
#             text = sub.get("Text", "")
#             temp_text += text

#             # keep cutting chunks while temp_text is too long
#             while len(temp_text) >= chunk_size:
#                 # cut at max_chunk_size if possible
#                 cut_point = min(len(temp_text), max_chunk_size)
#                 chunk = temp_text[:cut_point]
#                 output.append(chunk.strip())
#                 output.append("# SEPERATOR #")
#                 temp_text = temp_text[cut_point:]

#     # flush leftover text
#     if temp_text:
#         output.append(temp_text.strip())

#     return "\n".join(output)

    
    # for para in data:
    #     subparagraphs = para.get("SubParagraphs", [])
    #     for i, sub in enumerate(subparagraphs):
    #         if not sub.get("IsSub"):
    #             output.append(f"{sub['Text']}")
    #         else:
    #             # Begin subpoints list if the previous item was not a subpoint
    #             if i > 0 and not subparagraphs[i - 1].get("IsSub"):
    #                 pass
    #             output.append(f"\t{sub['Text']}")
                
        # output.append("") # Add newline between main paragraphs

    # return "\n".join(output)

# <----- ACT EXTRACTOR ----->
def cleanup_act_text(text: str):
    text = re.sub("<Section>", "", text)
    text = re.sub("</Section>", "", text)
    text = re.sub("<SubSection>", "\n\t", text, count=100)
    text = re.sub("</SubSection>", "", text, count=100)
    text = re.sub("<FNR>", "", text, count=100)
    text = re.sub("</FNR>", "", text, count=100)
    text = re.sub("<FN>", "", text, count=100)
    text = re.sub("</FN>", "", text, count=100)
    text = re.sub("<FT>", "", text, count=100)
    text = re.sub("</FT>", "", text, count=100)

    return text

def act_extractor(file):
    data = json.loads(file)
    text = data.get("text", "No content")
    splitted_text = cleanup_act_text(text)
    return splitted_text