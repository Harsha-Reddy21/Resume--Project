from client import client

def extract_keywords(job_description):
    """
    Extract key skills and requirements from job description
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                        {
                            "role": "system", 
                            "content": "You are an expert in extracting key skills and keywords from job descriptions."
                        },
                        {
                            "role": "user", 
                            "content": f"Extract the most important technical skills, soft skills, and key requirements from this job description. Provide a comma-separated list of keywords:\n{job_description}"
                        }
                    ],
            model="llama3-70b-8192",  # You can change the model as needed
            max_tokens=1000,
            temperature=0.7
        )
        keywords=chat_completion.choices[0].message.content.strip()
        return keywords
    except Exception as e:
        print(f"Error extracting keywords: {e}")
        return []
