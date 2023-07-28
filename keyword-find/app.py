import requests
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def get_website_keywords(url):
    # Send a GET request to the website
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text content from the website
    text = soup.get_text()
    
    # Tokenize the text into words
    words = word_tokenize(text)
    
    # Remove stopwords (common words with little significance)
    stopwords_set = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words if word.isalpha() and word.lower() not in stopwords_set]
    
    # Count the frequency of each word
    word_freq = {}
    for word in filtered_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Sort the words based on frequency (optional)
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Return the sorted words or perform additional processing as needed
    return sorted_words

# Example usage:
website_url = "https://www.spyfu.com/"
keywords = get_website_keywords(website_url)
print(keywords)
