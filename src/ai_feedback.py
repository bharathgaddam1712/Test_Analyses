import google.generativeai as genai
from config import config

def generate_feedback(student_name, test_info, subjects, chapters, llm_context):
    try:
        genai.configure(api_key=config.GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        
        prompt = f"""
        You are a friendly, expert tutor who speaks directly to the student, like a supportive mentor. Given the following student data:
        {llm_context}

        Generate a structured response for {student_name}'s performance with the following sections, using clear delimiters:
        - [SUGGESTIONS]
          - Provide 4-5 actionable, detailed suggestions for improvement, each tailored to the student's performance.
          - Each suggestion should have a main title followed by a colon, and 3-4 sub-bullets starting with an asterisk (*).
          - Use a warm, conversational tone, as if talking directly to the student (e.g., "Hey {student_name}, let's try this!").
          - Cover diverse strategies (e.g., time management, concept review, practice techniques, mindset tips).
          - Example:
            1. Boost Your Time Management: * Practice with a timer: Set a timer to mimic exam pressure. * Focus on quick wins: Tackle easier questions first. * Review slow topics: Check what’s holding you up in Physics. * Stay calm: Take a deep breath if you feel rushed.
            2. Dive Into Weak Areas: * Revisit Electrochemistry: Brush up on the Nernst equation. * Solve varied problems: Try different question types. * Use visual aids: Watch tutorials for tough concepts. * Ask for help: Reach out if you’re stuck!
        - [CLOSING]
          - Write a personalized, motivational closing message (3-5 sentences).
          - Make it warm, encouraging, and conversational, like a mentor cheering the student on.
          - Example: Hey {student_name}, you’re putting in awesome effort, and that’s half the battle won! Keep tackling those tough spots, and you’ll see huge progress. I’m rooting for you—let’s keep the momentum going!

        Tone: Warm, conversational, and encouraging, like a supportive tutor talking to the student.
        Use [SUGGESTIONS] and [CLOSING] as delimiters to separate sections.
        Do not include intro, performance breakdown, or insights sections.
        """
        
        response = model.generate_content(prompt)
        response_text = response.text

        # Parse response into structured dictionary
        feedback = {'suggestions': [], 'closing': ''}

        # Split response by delimiters
        sections = response_text.split('[SUGGESTIONS]')
        if len(sections) > 1:
            suggestion_section = sections[1].split('[CLOSING]')[0].strip()
            closing_section = sections[1].split('[CLOSING]')[1].strip() if '[CLOSING]' in sections[1] else ''

            # Extract suggestions
            lines = suggestion_section.split('\n')
            current_suggestion = None
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                if line.startswith(tuple(f"{i}." for i in range(1, 10))):
                    if current_suggestion:
                        feedback['suggestions'].append(current_suggestion)
                    current_suggestion = line
                elif line.startswith('*') and current_suggestion:
                    current_suggestion += ' ' + line
            if current_suggestion:
                feedback['suggestions'].append(current_suggestion)

            # Extract closing
            feedback['closing'] = closing_section.strip()

        return feedback

    except Exception as e:
        return {'suggestions': [f"Error generating feedback: {str(e)}"], 'closing': ''}