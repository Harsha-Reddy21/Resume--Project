
import json
from client import client
def get_content(keywords):

    chat_completion = client.chat.completions.create(
        messages=[
                    {
                        "role": "system", 
                        "content": """
                        You are an expert resume optimizer and ATS specialist. 
                        Rewrite resume content to maximize ATS compatibility 
                        .You have to give two projects that enhaces the ats score. The ats score should exceed 90 percent.
                        You have to give the project name, tools used and description in brief. And those projects should related to machine learning.
                        You just have to return projects only no other results.
                        The output should be like this line by line:
                        Project Name: 
                        Description:
                        Tools Used
                        """
                    },
                    {
                        "role": "user", 
                        "content": f"""
                        Optimize this resume for an ATS system based on these keywords: {keywords}. 
                        You have to give two projects that enhaces the ats score. The ats score should exceed 90 percent.
                        You have to give the project name, tools used and description in brief. And those projects related to machine learning.
                        You just have to return projects only no other results.
                        The output should be like this line by line:
                        Project Name: 
                        Description:
                        Tools Used
                        
                        Job Description Keywords: {', '.join(keywords)}
                        
                        Requirements:
                        1. Align experiences with job description
                        2. Use exact keywords from job description
                        3. Quantify achievements
                        4. Ensure 90%+ ATS compatibility
                        5. Maintain professional tone
                        """
                    }
                ],
        model="llama3-70b-8192",  # You can change the model as needed
        max_tokens=1000,
        temperature=0.7
    )
    keywords=chat_completion.choices[0].message.content.strip()
    return keywords

