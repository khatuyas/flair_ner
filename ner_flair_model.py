'''
This code is used to extract named entity using flair-ner model
'''

# Import required packages
from flair.data import Sentence
from flair.models import SequenceTagger

import re

# load the NER tagger
# tagger = SequenceTagger.load('ner-ontonotes')
tagger = SequenceTagger.load("en2-ner-ontonotes-v0.3.pt")


def extract_named_entity(Idea_Text):
    # Pre-process the text
    text_input = Idea_Text
    # text_input=clean_content(Idea_Text)
    ### Preporocess Input Text 1. remove Non-english characters
    text_input = text_input.encode("ascii", errors="ignore").decode()
    sentence = Sentence(text_input)

    # load the NER tagger
    tagger.predict(sentence)

    # iterate over entities and print
    dict_ner = {}
    list_entity = ['PERSON', 'NORP', 'FAC', 'ORG', 'GPE', 'LOC', 'PRODUCT', 'EVENT', 'WORK_OF_ART', 'LAW', 'LANGUAGE',
                   'DATE', 'TIME', 'PERCENT', 'MONEY', 'QUANTITY', 'ORDINAL', 'CARDINAL']

    '''
    for entity in sentence.get_spans('ner'):
        named_entity=str(entity).strip().split('-')[0]
        dict_ner[entity]=[]
    '''

    for entity in list_entity:
        dict_ner[entity] = []

    list_ner_entity = []
    dict_ner_entitiy = {}
    for entity in sentence.get_spans('ner'):
        # print (entity)
        temp_dict_ner = {}
        named_entity = str(entity).strip().split('-')[0]
        entity_value = str(entity).strip().split(':')[1]

        if entity_value:
            entity_value = re.sub(r'\..*', '', entity_value)
            temp_dict_ner['Name'] = entity_value.strip().replace('"', '')
            temp_dict_ner['Type'] = named_entity
            list_ner_entity.append(temp_dict_ner)

        '''
        try:
            dict_ner[named_entity].append(entity_value)
        except:
            dict_ner[named_entity]=[]
            dict_ner[named_entity].append(entity_value)
        '''

    # print (list_ner_entity)
    dict_ner_entitiy['Entities'] = list_ner_entity
    return dict_ner_entitiy
