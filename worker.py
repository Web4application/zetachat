import re
import requests
from bs4 import BeautifulSoup

def clean_string(text):
    """
    This function takes in a string and performs a series of text cleaning operations.

    Args:
        text (str): The text to be cleaned. This is expected to be a string.

    Returns:
        cleaned_text (str): The cleaned text after all the cleaning operations have been performed.
    """
    # Replacement of newline characters
    text = text.replace("\n", " ")

    # Stripping and reducing multiple spaces to single
    cleaned_text = re.sub(r"\s+", " ", text.strip())

    # Removing backslashes
    cleaned_text = cleaned_text.replace("\\", "")

    # Replacing hash characters
    cleaned_text = cleaned_text.replace("#", " ")

    # Eliminating consecutive non-alphanumeric characters
    cleaned_text = re.sub(r"([^\w\s])\1*", r"\1", cleaned_text)

    return cleaned_text

def load_data_from_url(url):
    """Load data from a web page."""
    response = requests.get(url)
    data = response.content
    soup = BeautifulSoup(data, "html.parser")

    tags_to_exclude = ["nav", "aside", "form", "header", "noscript", "svg", "canvas", "footer", "script", "style"]
    for tag in soup(tags_to_exclude):
        tag.decompose()

    ids_to_exclude = ["sidebar", "main-navigation", "menu-main-menu"]
    for id in ids_to_exclude:
        tags = soup.find_all(id=id)
        for tag in tags:
            tag.decompose()

    classes_to_exclude = ["elementor-location-header", "navbar-header", "nav", "header-sidebar-wrapper", "blog-sidebar-wrapper", "related-posts"]
    for class_name in classes_to_exclude:
        tags = soup.find_all(class_=class_name)
        for tag in tags:
            tag.decompose()

    content = soup.get_text()
    content = clean_string(content)

    return content

def search_from_google(keyword):
    url = "https://google.serper.dev/search"
    payload = json.dumps({"q": keyword})
    headers = {'X-API-KEY': 'SERP_KEY', 'Content-Type': 'application/json'}

    response = requests.request("POST", url, headers=headers, data=payload)
    results = response.json()['organic']
    urls = [result['link'] for result in results]
    return urls

def generate_data_file(name):
    urls = search_from_google(name)
    data = ""
    for url in urls:
        data += load_data_from_url(url)
        data += '\n'
    with open('data.txt', 'w') as fp:
        fp.write(data)
    return data

def generate_prompt_file(context):
    prompt_to_generate_system = f'''
    Context
    ---
    {context}
    ---
    '''
    with open('system.txt', 'w') as fp:
        fp.write(prompt_to_generate_system)
    with open("user.txt", "w") as fp:
        fp.write(f'''
        Context
        ---
        {context}
        ---
        Use previous information as context to answer the following user question.
        Aim to keep responses super concise and meaningful and try to express emotions.
        ALWAYS ask clarification questions when:
        - the user's question isn't clear
        - it seems unfinished
        - it seems totally irrelevant
        Remember to prefix your reply.
        ---
        ''')

# Example usage
generate_data_file("tim cook")
generate_prompt_file("tim cook")
