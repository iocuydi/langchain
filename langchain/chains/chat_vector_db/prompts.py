# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

_template = """Given the following conversation history and a new question, rephrase the new question to be a standalone question.
If the follow up question is about a completely different topic and has nothing to do with the conversation, then the standalone question should just be the new question.

Chat History:
{chat_history}

New Question:
Human: {question}

(Remember that while the follow up question may be directly related to the chat history, it could also be a new question about a whole different topic.)

Standalone question:"""
CONDENSE_QUESTION_PROMPT = PromptTemplate.from_template(_template)

prompt_template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
Helpful Answer:"""
QA_PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)
