from modules.large_language_model import llm_llama_index
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from modules.function import compare_strings

def rule_identifier(question):

    rules_query = ["- vehicle hit from behind/rear",
            "- enter",
            "- exit"
            ] 

    rule_identifier_query = f"""
            {question}
            
            From the below instructions first check which rule applies.
            
            Instructions:
            Don't assume anything. Just be precise and use the information given in the query.
    
            Just return one answer as it is from below MCQs.  
            - vehicle hit from behind/rear
            - enter
            - exit
            """

    result = llm_llama_index('rule_book',rule_identifier_query)
    return result, rules_query

question_seven_query = f"""

           
           From the below instructions first check which rule applies.
           Before answwering. make sure who is vehicle A and vehicle B. In both of these cases, Vehicle existing is Vehicle AB and other vehicle is vehicle A.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - If parking place is mentioned then rule 7(2) applies.
           - Other than that rule 7(3)applies
           - Before answwering. make sure who is vehicle A and vehicle B. In both of these cases, Vehicle existing is Vehicle AB and other vehicle is vehicle A.
           
           
           while answering and talking about vehicles mentione that w=vehicle on road or vehilce exiting.  

           breakdown the problems. And and based on rules you select tell that who is at fault. 
           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

question_6_8_query_chooser = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.

           
           Just return one answer as it is from below MCQs.  
           - If entrance lane/entry lane, link lane then rule 8
           - else rule_6

"""

question_six_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - If car hits from behind then rule 6(2) applies
           - If parking place is mentioned then rule 6(3) applies.
           - Other than that rule 6(4)applies

           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

question_eight_query = """
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.

           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
"""

question_nine_query = """
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - Rule 9(3) applies when all vehicles are in motion at the time of the accident, including vehicles in stop-and-go traffic or those that are slowing down.
            If any two vehicles stopped then Ruke 9(3) is not applicable
           - Rule 9(4) is relevant under the following conditions:
                If Vehicle C was moving while other vehicles were stopped.
                If both Vehicles B and C were initially moving, then stopped, and subsequently, a third vehicle failed to stop in time, causing an accident.
                If all cars were in motion and two stoppedd and the third car could not stop in time and rear ended into vehicles

           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
"""



    


def SDSL(vehicles, question):
    if vehicles==2:
        rule_identifier_result,rules_query = rule_identifier(question)

        # for rule_query in rules_query:

        #     similarity = compare_strings(rule_identifier_result, rule_query)
        #     if similarity>80.0:
        #         break

        if rule_identifier_result == 'exit':
            query = question + question_seven_query
            path = 'same_lane_and_same_direction/rule_7'
            seven_result = llm_llama_index(path, query)
            return seven_result
        else:
            query_chooser = question + question_6_8_query_chooser
            path = "same_lane_and_same_direction/rule_6_8"
            question_6_8_query_choosen = llm_llama_index(path, query_chooser)

            if question_6_8_query_choosen=='rule_6':
                query_choosen = question + question_six_query
                path = 'same_lane_and_same_direction/rule_6_8/rule_6'
                question_six_result = llm_llama_index(path, query_choosen)
                return question_six_result
            else:
                query_choosen = question + question_eight_query
                path = 'same_lane_and_same_direction/rule_6_8/rule_8'
                question_eight_result = llm_llama_index(path, query_choosen)
                return question_eight_result
    else:
        query = question + question_nine_query
        path = 'same_lane_and_same_direction/rule_9'
        seven_result = llm_llama_index(path, query)
        print(seven_result)
        return seven_result
        







    