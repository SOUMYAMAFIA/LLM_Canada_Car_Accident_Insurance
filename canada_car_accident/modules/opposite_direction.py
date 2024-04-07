from modules.large_language_model import llm_llama_index
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from modules.function import compare_strings


question_twelve_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Dont explain all the rules. Pick one who is best suited and then explain about that rule and query
           Don't assume anything. Just be precise and use the information given in the query.
           - If both automobiles are not changeing lanes and both automobiles are on or over the centre lane when the incident (a “sideswipe”) occurs, the rule 12(2) applies.
           - If the loation of automobiles cannot be determined then rule 12(3) applies.
           - If one automobile is on or over the centre line of the road and other vehicle is on the road (not on the center line of road) then rule 12(4) applies.
           - If automobile “B” turns left into the path of automobile “A” then rule 12(5) applies.
           - If automobile “B” is leaving a parking place or is entering the road from a private road or driveway, and 
             if automobile “A” is overtaking to pass another automobile when the incident occurs then rule 12(6) applies.

           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """

def OD(question):
    query = question + question_twelve_query
    path = "opposite_direction/rule_12"
    question_twelve_response = llm_llama_index(path,query)
    return question_twelve_response