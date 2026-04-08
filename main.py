from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
#from langchain_ollama import ChatOllama
load_dotenv()

def main():
    print("Hello from langchain-course!")
    information = """Elon Reeve Musk (* 28. června 1971 Pretorie) je podnikatel jihoafricko-kanadsko-britského původu.[2][3] Založil kosmickou společnost SpaceX a stál u vzniku automobilky Tesla, kterou začal jako CEO řídit. Společnost Twitter koupil za 44 miliard dolarů a sociální síť přejmenoval na X.[4] Založil také společnosti xAI, Starlink či Neuralink a v říjnu 2025 spustil internetovou encyklopedii generovanou umělou inteligencí Grokipedia, konkurenční projekt Wikipedie. V minulosti spoluvlastnil internetový platební systém PayPal a spoluzakládal společnost OpenAI."""

    summary_template = """
    given the following information {information}, please summarize the information about the person:
    1. A short summary
    2. Two interesting facts about the person
    """

    summary_prompt = PromptTemplate(input_variables=["information"], template=summary_template)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    #llm=ChatOllama(temperature=0,model="gemma3:270m")
    chain = summary_prompt | llm
    response = chain.invoke({"information": information})
    print(response.content)

if __name__ == "__main__":
    main()
