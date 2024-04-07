from dotenv import load_dotenv
import openai
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"]="OPENAI_API_KEY"


from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain 
from modules.large_language_model import llm_llama_index
from modules.same_dirction_and_lane import SDSL
from modules.same_direction_and_adjacent_lane import ADSL
from modules.opposite_direction import OD
from modules.parking_lot import PL
from modules.intersection import INTSC
from modules.offence_of_drugs import OOD
from modules.function import compare_strings





def VI_main(query, place_of_accident, number_of_vehicles):
    if number_of_vehicles=='two vehicles':
        number_of_vehicles=2
    else:
        number_of_vehicles=3

    if place_of_accident=='same direction and same lane':
        response = SDSL(number_of_vehicles,query)
        print(response)
        return response

    if place_of_accident=='same direction and adjacent lane':
        response = ADSL(number_of_vehicles,query)
        return response
    
    if place_of_accident=='opposite direction':
        response = OD(query)
        return response
    
    if place_of_accident=='parking lots/violate law':
        response = PL(query)
        return response
    
    if place_of_accident=='intersection':
        response = INTSC(query)
        return response
    
    if place_of_accident=='offence of drug':
        response = OOD(query)
        return response


# query = """
# I was driving north, the car in 
# front of me stopped, I stopped 
# as well, but the car behind me 
# could not stop in time and rear 
# ended me, I was not pushed 
# into the car in front
# """
# print(VI_main(query, "same direction and same lane","two vehicles"))

