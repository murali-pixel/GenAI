from flask import Flask, request, jsonify
import openai
import requests

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'
# Placeholder list of documents
documents = [
    {
        'title': 'Document 1',
        'content': 'This is the content of Document 1.'
    },
    {
        'title': 'Document 2',
        'content': 'This is the content of Document 2.'
    },
    {
        'title': 'Document 3',
        'content': 'He I am Murali Krishna'
    }
]

def search_documents(query):
    # Perform the document search based on the query
    results = []
    for document in documents:
        if query.lower() in document['content'].lower():
            results.append(document)

    return results

# GenAI interaction function
def generate_response(query):
    # Generate a response using GenAI
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.6
    )

    return response.choices[0].text.strip()

# API endpoint for search and chat
@app.route('/api/search-and-chat', methods=['POST'])
def search_and_chat():
    data = request.json
    query = data['query']
    context = data['context']

    # Perform document search
    documents = search_documents(query)

    # Generate response using GenAI
    response = generate_response(context)

    # Return the response
    return jsonify({
        'documents': documents,
        'response': response
    })

if __name__ == '__main__':
    app.run()
