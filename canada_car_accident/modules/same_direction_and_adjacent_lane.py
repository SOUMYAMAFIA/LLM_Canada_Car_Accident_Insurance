from modules.large_language_model import llm_llama_index
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from modules.function import compare_strings


question_ten_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           Read the query carefully and then based on below instructions explain the query and rules that applies
           - If both automobiles are on or over the center lane the rule when incident occurs 10(2) applies.
           - If location/direction of both automobiles cannot be determined/unsure then rule 10(3) applies.
           - If in the query location cannot be determined then in this case rule 10(3) applies
           - If driver of automobile B changes lane then rule 10(4) applies.
           - If incident occurs when automobile is overtake then rule 10(5) applies.
           - If incident occurs when automobile is turning left at private road or drive way and other automobile tries to overtake automobile then rule 10(6) applies.
           - If the incident occurs when automobile “A” is turning left at a private road or a driveway and automobile “B” is
             passing one or more automobiles stopped behind automobile “A”, then rule 10(7) applies.

           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

question_eleven_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.

           
           Expalin in detail who is at fault.
           And also tell which rule applies at the end.
           just stick to rule that applies. if you dont know just say dont know 
           """


def ADSL(vehicles, question):
    if vehicles==2:
        query = question + question_ten_query
        path="adjacent_lane_and_same_direction/rule_10"
        response = llm_llama_index(path, query)
        return response
    else:
        query = question + question_ten_query
        path="adjacent_lane_and_same_direction/rule_11"
        response = llm_llama_index(path, query)
        return response