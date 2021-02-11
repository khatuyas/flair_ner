import re

import ner_flair_model as NER_MODEL

Idea_Text="Subhendu lives in Kolkata"

PUNCTUATIONS='''%!()-[]{;:}'"<>/¬†?@#$%^&*_~'''
#paragraph=clean_content(Idea_Text)
paragraph = Idea_Text
for punc in PUNCTUATIONS:
    paragraph = paragraph.replace(punc,' ')


paragraph = paragraph.replace('\n', ' ')
paragraph = paragraph.replace('\r', ' ')

paragraph = re.sub(r'^https?:\/\/.*[\r\n]*', '', paragraph, flags=re.MULTILINE)
print (paragraph)
ner_dict=NER_MODEL.extract_named_entity(paragraph.strip())
print (ner_dict)

