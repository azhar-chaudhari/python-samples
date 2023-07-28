import PyPDF2
import nltk
from nltk.tokenize import sent_tokenize
from transformers import BertTokenizer, BertForQuestionAnswering
import torch
nltk.download('punkt')

def read_pdf_text(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = ""
    for page_num in range(len(pdf_reader.pages)):
        pdf_page = pdf_reader.pages[page_num]
        pdf_text += pdf_page.extract_text()
    pdf_file.close()
    return pdf_text

def preprocess_text(text):
    # Tokenize text into sentences
    sentences = sent_tokenize(text)
    return sentences

def answer_question(question, context, model, tokenizer):
    inputs = tokenizer.encode_plus(question, context, return_tensors="pt", add_special_tokens=True)
    input_ids = inputs["input_ids"].tolist()[0]

    # Get the model's answer
    with torch.no_grad():
        outputs = model(**inputs)
        answer_start = torch.argmax(outputs.start_logits)
        answer_end = torch.argmax(outputs.end_logits) + 1

    answer = tokenizer.decode(input_ids[answer_start:answer_end], skip_special_tokens=True)
    return answer

def main():
    # Load pre-trained BERT model and tokenizer
    model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
    model = BertForQuestionAnswering.from_pretrained(model_name)
    tokenizer = BertTokenizer.from_pretrained(model_name)

    # Replace 'your_pdf_file.pdf' with the path to your PDF file
    pdf_text = read_pdf_text('story.pdf')

    # Preprocess text into sentences
    sentences = preprocess_text(pdf_text)

    # Example questions
    questions = ["What is the name of doctor?",
                 "Who is the author of the document?",
                 "Where was the first trip?",
                 "What is the name of queen?"]

    for question in questions:
        print(f"Question: {question}")
        for sentence in sentences:
            answer = answer_question(question, sentence, model, tokenizer)
            if answer.strip():
                print(f"Answer: {answer}")
                break

if __name__ == "__main__":
    main()
