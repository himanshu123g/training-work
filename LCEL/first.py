# # ############ All 3 chains run in parallel!
# parallel_chain = RunnableParallel(
#     pros    = pros_chain,
#     cons    = cons_chain,
#     summary = summary_chain
# )

# import time
# start = time.time()
# result = parallel_chain.invoke({"technology": "artificial intelligence"})
# elapsed = time.time() - start

# print(f"Completed in {elapsed:.1f}s (all 3 ran simultaneously!)")
# print("\n📋 Summary:", result["summary"])
# print("\n✅ Pros:\n", result["pros"])
# print("\n❌ Cons:\n", result["cons"])




# # ── Context-Aware Chain ─────────────────────────────────────────────
# # Simulates RAG: retrieve context → answer based on it

# # Fake retriever (in real RAG, this fetches from vector DB)
def fake_retriever(query: str) -> str:
    context_db = {
        "virat kohli": "Virat Kohli is an Indian cricketer, former captain of the Indian national team, and one of the greatest batsmen in the history of cricket.He is playing as a actor in a new movie called Long 18 years",
        "java": "Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. It emphasizes code readability and supports multiple programming paradigms.",
        "python":   "Java is a class-based, object-oriented language designed to have as few implementation dependencies as possible. Created by James Gosling at Sun Microsystems in 1995.",
        "default": "No specific context available. Please answer from general knowledge."
    }
    query_lower = query.lower()
    for key in context_db:
        if key in query_lower:
            return context_db[key]
    return context_db["default"]

retriever = RunnableLambda(fake_retriever)

rag_prompt = ChatPromptTemplate.from_template(
    """Use only the following context to answer the question.
    Context: {context}
    Question: {question}
    Answer:"""
)

rag_chain = (
    RunnablePassthrough.assign(
        context=RunnableLambda(lambda x: fake_retriever(x["question"]))
    )
    | rag_prompt
    | chat
    | StrOutputParser()
)

# result = rag_chain.invoke({"question": "Who created java and when?"})
result = rag_chain.invoke({"question": "Who is Virat Kohli and what is his new movie name?"})
print("RAG Answer:", result)