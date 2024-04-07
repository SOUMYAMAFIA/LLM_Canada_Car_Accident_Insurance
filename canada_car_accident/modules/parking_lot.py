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

            - if vehicle is backing out, u-turn or leaves door open during accident then rule 19 applies  
            - If vehicle failed to obey law (like police direction, enter sign, passing sign or prohinited turn sign) then rule 18 applies.
            - if vehicle is parked then rule 17 applies
            - if vehicle is leaving feeder lane or leaving parking space then rule 16 applies.
              
            """

    result = llm_llama_index('automobiles_in_parking_lots/',rule_identifier_query)
    return result
    # return result, rules_query

def check_for_rule(number,input_string):
    return number in input_string




question_seventeen_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - If automobile is parked then rule 17(1) applies.
           - If automobile is illegaly parked then rule 17(2) applies.

           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

question_sixteen_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - If automobile is leaving the feeder lane then rule 16(3) applies
           - If automobile is leaving the parking sapce then rule 16(4) applies

           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

question_eighteen_query = """
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - if driver failed to obey police officer's direction then rule 18(a) applies.
           - if driver failed to obey do not enter sign then rule 18(b) applies.
           - if driver failed to obey prohibited passing sign then rule 18(c) applies.
           - if driver failed to obey prohibited turn sign then rule 18(d) applies
           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
"""

question_ninghteen_query = """
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - If automobile is backing up/out rule 19(a) applies
           - If automobile is making uturn rule 19(b) 
           - If driver or passenger leaves the door open then rule 19(c) applies

           Explain in detail who is at fault.
           And also tell which rule applies at the end 
"""



    


def PL(question):
    response = rule_identifier(question)
    print(response)
    if check_for_rule("16",response):
        query = question + question_sixteen_query
        path =  "automobiles_in_parking_lots/rule_16/"
        nighteen_result = llm_llama_index(path,query)
        return nighteen_result
    
    if check_for_rule("17",response):
        query = question + question_seventeen_query
        path =  "automobiles_in_parking_lots/rule_17/"
        nighteen_result = llm_llama_index(path,query)
        return nighteen_result
    
    if check_for_rule("18",response):
        query = question + question_eighteen_query
        path =  "automobiles_in_parking_lots/rule_18/"
        nighteen_result = llm_llama_index(path,query)
        return nighteen_result
    
    if check_for_rule("19",response):
        query = question + question_ninghteen_query
        path =  "automobiles_in_parking_lots/rule_19/"
        nighteen_result = llm_llama_index(path,query)
        return nighteen_result
        







    