from modules.large_language_model import llm_llama_index
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from modules.function import compare_strings



question_twenty_query = f"""

           
           From the below instructions first check which rule applies.
           
           Instructions:
           Don't assume anything. Just be precise and use the information given in the query.
           - If driver of automobile was impaired by alcohol or a drug or by a combination of alcohol and a drug the rule 20(1)(A) applies.
           - If the driver is charged with driving while his or her blood alcohol level or blood drug
             concentration level exceeded the limits permitted by law then rule 20(1)(B) applies.
           - If the driver is charged with an indictable offence related to the operation of the automobile the rule 20(1)(C)
           - If the driver, as a result of the incident, is asked to provide a breath sample or a sample of a bodily substance and he or she
             is charged with failing or refusing to provide the sample then rule 20(1)(D) applies.
           - if the driver, as a result of the incident, is asked to perform physical coordination tests or submit to an evaluation and
             he or she is charged with failing or refusing to comply with the demand then rule 20(1)(E) applies.
           - if, as a result of the incident, the driver is charged with exceeding the speed limit by 16 or more kilometres per hour then rule 20(1)(F) applies.
           - if the driver of automobile “A” involved in the incident is charged with a driving offence the rule 20(2)(A) applies.
           - if the driver of automobile “B” is wholly or partly at fault, as otherwise determined under these rules, for the incident the rule 20(2)(B) applies.
           
           Expalin in detail who is at fault.
           And also tell which rule applies at the end 
           """



def OOD(question):
   
    query = question + question_twenty_query
    path = "driver_charged_with_offence-drug/rule_20"
    question_twenty_response = llm_llama_index(path,query)
    return question_twenty_response
    
    