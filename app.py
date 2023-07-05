from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = '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'

# Placeholder list of documents
documents = [
    {
        'title': 'SpringML',
        'content': """SpringML is a leading technology company that specializes in providing artificial intelligence and machine learning solutions. With their expertise in data analytics and cloud-based platforms, SpringML empowers organizations to leverage the power of AI to gain valuable insights and make data-driven decisions.

One of the key offerings of SpringML is their AI and ML consulting services. They work closely with businesses to understand their specific needs and challenges, and then develop customized AI solutions to address them. Whether it's optimizing business processes, improving customer experience, or predicting future trends, SpringML helps organizations harness the potential of AI to drive growth and innovation.

SpringML also offers a range of products and solutions that enable businesses to leverage AI capabilities. Their flagship product, SpringML Predictive Toolkit, provides a comprehensive set of tools and features to build and deploy predictive models. This toolkit integrates seamlessly with popular cloud platforms like Google Cloud Platform (GCP) and Amazon Web Services (AWS), making it easier for organizations to implement AI solutions."""
    },
    {
        'title': 'Google',
        'content': """Google is a multinational technology company that specializes in internet-related services and products. It was founded in September 1998 by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University. The company's mission is to organize the world's information and make it universally accessible and useful.

Google is best known for its search engine, which is the most widely used search engine in the world. Google's search technology utilizes complex algorithms to deliver highly relevant search results based on user queries. Over the years, Google has expanded its services and product offerings, becoming a dominant force in various areas of technology.

Some of Google's key products and services include:

Google Search: The flagship product of Google, providing a powerful and intuitive search experience.

Google Maps: An online mapping service that offers detailed maps, satellite imagery, street views, and route planning.

Gmail: A free email service with ample storage space, advanced search capabilities, and integrated communication tools.

Google Chrome: A popular web browser known for its speed, security, and user-friendly interface.

Google Drive: A cloud storage and file-sharing service that allows users to store and access files from anywhere.

Google Docs, Sheets, and Slides: A suite of productivity tools that enables collaborative editing of documents, spreadsheets, and presentations.

Google Photos: A photo and video storage platform that offers free unlimited storage for high-quality images.

YouTube: The world's largest video-sharing platform, where users can upload, watch, and share videos."""
    }
]

def search_documents(query):
    results = []
    for document in documents:
        if query.lower() in document['content'].lower():
            results.append(document)

    return results

# GenAI function
def generate_response(query, context):
    prompt = f"Search for documents containing '{query}':\n"
    for document in documents:
        prompt += f"- Document: {document['title']}\nContent: {document['content']}\n\n"
    prompt += "Chat prompt:\n" + context

    
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
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

    
   # search_results = search_documents(query)


    response = generate_response(query, context)

    # Return the response
    return jsonify({
       # 'search_results': search_results,
        'chat_response': response
    })

if __name__ == '__main__':
    app.run()
