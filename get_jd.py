from client import client
import requests
from bs4 import BeautifulSoup

def extract_job_description(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text()
        truncated_text = page_text[:4000]

        prompt = f"""
        You are an expert job description extractor. 
        Carefully analyze the following webpage text and extract the most relevant job description.
        
        Guidelines:
        - Focus on key job responsibilities
        - Identify required skills and qualifications
        - Provide a clear, concise summary
        - Remove any irrelevant website navigation or header/footer text
        
        Webpage Text:
        {truncated_text}
        
        Extracted Job Description:
        """

        
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional job description extraction assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-70b-8192",  
            max_tokens=1000,
            temperature=0.7
        )
        
        job_description = chat_completion.choices[0].message.content.strip()
        
        
        return job_description
    
    except requests.RequestException as e:
        print(f"Network error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None