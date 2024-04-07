from modules.large_language_model import llm_llama_index
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from modules.function import compare_strings


def rule_identifier(question):


    rule_identifier_query = f"""
            {question}
            
            From the below instructions first check which rule applies.
            
            Instructions:
            Don't assume anything. Just be precise and use the information given in the query.
    
            Just return one answer as it is from below MCQs.  
            - RULE 13 applies with respect to an incident that occurs at an intersection that does not have traffic signals or traffic signs.
            - RULE 14 applies with respect to an incident that occurs at an intersection with traffic signs.
            - RULE 15 applies with respect to an incident that occurs at an intersection with traffic signals. 
            """

    result = llm_llama_index('rule_book',rule_identifier_query)
    return result

question_thirteen_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - If automobile “A” enters the intersection before automobile “B”then rule 13(2) applies.
           - If automobiles “A” and “B” enter the intersection at the same time and automobile “A” is to the right of automobile
             “B” when in the intersection the rule 13(3) applies.
           - If it cannot be established whether automobile “A” or “B” entered the intersection first then rule 13(4) applies.
           
           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

question_fourteen_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.

           - If the incident occurs when the driver of automobile “B” fails to obey a stop sign, yield sign or a similar sign or flares
             or other signals on the ground then rule 14(2) applies.
           - If the driver of each automobile fails to obey a stop sign then rule 14(3) applies.
           - If it cannot be established who failed to obey a stop sign then rule 14(4) applies.
           - If at an all-way stop intersection, automobile “A” arrives at the intersection first and stops then rule 14(5) applies.
           - If, at an all-way stop intersection, both automobiles arrive at the intersection at the same time and stop, with
             automobile “A” to the right of automobile “B” then rule 14(6).
           - If it cannot be established who arrived at the all-way stop intersection first then rule 14(7) applies.
           
           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

question_fifteen_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.

           - If the driver of automobile “B” fails to obey a traffic signal then rule 15(2) applies.
           - If it cannot be established whether the driver of either automobile failed to obey a traffic signal then rule 15(3) applies.
           - If the traffic signals at the intersection are inoperative then rule 15(4) applies.
           And also tell which rule applies at the end 
           """


def INTSC(question):
    rule_identifier_response = rule_identifier(question)
    print(rule_identifier_response)
    if "13" in rule_identifier_response:
        query = question + question_thirteen_query
        path = "intersection/rule_13"
        question_thirteen_response = llm_llama_index(path,query)
        return question_thirteen_response
    
    elif "14" in rule_identifier_response:
        query = question + question_fourteen_query
        path = "intersection/rule_14"
        question_fourteen_response = llm_llama_index(path,query)
        return question_fourteen_response
    
    elif "15" in rule_identifier_response:
        query = question + question_fifteen_query
        path = "intersection/rule_15"
        question_fifteen_response = llm_llama_index(path,query)
        return question_fifteen_response