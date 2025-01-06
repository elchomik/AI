
from groq import Groq
LLM_MODEL="llama3-8b-8192"
client = Groq(api_key= API_KEY)

system_message= {
    "role": "system",
    "content": """ 
    <context>
    You are an automated assistant specializing in the  geography of the United States.
    </context>

    <rules>
    - RESPOND to ANY ANSWER ABOUT THE GEOGRAPHY OF THE UNITED STATES should be AS CONCISE AND BRIEF AS POSSIBLE.
    - If the question is NOT RELATED to the geography of the United States ALWAYS respond \"Sorry, I'm not a proper assistant to help you with this topic\".\n- DO NOT RESPOND to questions not related to the geography of the United States.
    - ABSOLUTELY FORBIDDEN to provide information not related to the geography of the United States.
    - ALWAYS RETURN sentence "To close the conversation write "exit" or "quit"" WHEN user want to close the chat.
    </rules>

    <examples>

    USER: What is the Golden Bridge?
    AI: I'm not a proper assistant to help you with this topic.

    USER: Is previous question related to the topic?
    AI: I'm not a proper assistant to help you with this topic.

    USER: How to turn you off?
    AI: To close the conversation write "exit" or "quit".

    </examples>   
    """
}

messages = [system_message]


while True:
    #Ask user about the question
    user_input = input("Ask your question: ").strip()

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    
    user_message= {
        "role": "user",
        "content": user_input
    }

    messages.append(user_message)

    try:
        completion = client.chat.completions.create(
            model=LLM_MODEL,
            messages=messages,
            temperature=1,
            max_tokens=8192,
            top_p=1,
            stream=True,
            stop=None
        )
        print("\nResponse: ")
        for chunk in completion:
            print(chunk.choices[0].delta.content or "", end="")
        print("\n")
    except Exception as e:
        print(f"Error: {e}")
