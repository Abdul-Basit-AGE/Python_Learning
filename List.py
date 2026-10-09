chunks = ["RAG architecture", "AI", "Vector DB", "LLM", "Prompt Engineering"]
chunks.append("Fast API")
chunks[0] = 'Python Basics'
selected_chunk = chunks[1:4]
filtered_chunks = [chunk for chunk in chunks if len(chunk) >= 3]
print("chunks:", chunks)
print("selected_chunk:", selected_chunk)
print("filtered_chunks:", filtered_chunks)
