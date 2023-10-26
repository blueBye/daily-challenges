from math import ceil
import re


def extract_paper(paper_file_path: str, font_size: int) -> dict:
    sections = {
        "title": [], 
        "abstract": [], 
        "keywords": [],
        "introduction": [], 
        "body": [], 
        "conclusion": [], 
        "references": [],
    }
    current_section = "title"
    words_count = 0

    with open(paper_file_path, 'r') as f:
        for line in f.readlines():
            if line.strip().lower() in sections.keys():
                current_section = line.strip().lower()
            elif line.strip():
                words_count += len(line.strip().split())
                sections[current_section].append(line)

    sections['title'] = ''.join(sections['title'])
    sections['abstract'] = ''.join(sections['abstract'])
    sections['keywords'] = [i.strip() for i in sections['keywords'][0].split(',')]
    sections['introduction'] = ''.join(sections['introduction'])
    sections['body'] = ''.join(sections['body'])
    sections['conclusion'] = ''.join(sections['conclusion'])
    sections['references'] = [re.sub('^\[\d+\]', '', i).strip() for i in sections['references']]
    
    # validate abstract
    if len(sections['abstract'].split()) > 150:
        raise Exception("The abstract section can't be more than 150 words")

    # validate keywords
    if len(sections['keywords']) > 5:
        raise Exception("You can't put more than 5 keywords")
    
    if sorted(sections['keywords']) != sections['keywords']:
        raise Exception("Keywords are not sorted")
    
    # validate length
    pages_count = words_count / 512 * font_size / 16 
    if pages_count > 9:
        raise Exception("The whole paper can't be more than 9 pages")

    return(
        {
            **sections,
            'words_count': words_count,
            'pages_count': ceil(pages_count),
        }
    )

