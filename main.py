import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def initialize_advisor():
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.1-flash-lite-preview",
        temperature=0.5,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    template = ("Você é um assistente que recomenda tecnologias de programação com base no interesse do usuário.\n""Usuário: {interesse}\n" "Recomende uma tecnologia apropriada para o usuário aprender em seguida e explique brevemente o porquê.")
    
    prompt = PromptTemplate(
        input_variables=["interesse"],
        template=template
    )

    chain = prompt | llm
    
    # Exemplo 1:

    pergunta1 = "quero melhorar minhas habilidades em desenvolvimento web frontend" 
    resposta1 = chain.invoke({"interesse": pergunta1}) 
    print("Pergunta:", pergunta1) 
    print("Resposta do agente:", resposta1.content)
    
    # Exemplo 2:
    pergunta2 = "interesso em análise de dados, qual tecnologia devo aprender?" 
    resposta2 = chain.invoke({"interesse": pergunta2}) 
    print("\nPergunta:", pergunta2)
    print("Resposta do agente:", resposta2.content)

if __name__ == "__main__":
    initialize_advisor()