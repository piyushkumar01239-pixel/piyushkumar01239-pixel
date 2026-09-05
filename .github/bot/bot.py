#!/usr/bin/env python3
"""
GitHub Profile Bot for Piyush Kumar
Answers questions about profile, projects, skills, and achievements
"""

import os
import json
import requests

# Configuration
REPO_NAME = os.environ.get('GITHUB_REPOSITORY', 'piyushkumar01239-pixel/piyushkumar01239-pixel')
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_API_URL = 'https://api.github.com'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# ================================================
# YOUR PROFILE DATA - UPDATE THIS SECTION
# ================================================

PROFILE_DATA = {
    "name": "Piyush Kumar",
    "title": "Computer Science Student",
    "username": "piyushkumar01239-pixel",
    "email": "piyushkumar01239@gmail.com",
    "linkedin": "piyush-kumar-0a5412328",
    "leetcode": "piyush_1_1_1_",
    "tryhackme": "piyushkumar357",
    
    "about": """Passionate Computer Science student with a deep interest in software engineering, 
Android development, AI, and cybersecurity.""",
    
    "skills": {
        "core_cs": ["Data Structures & Algorithms", "Object-Oriented Programming", 
                    "Operating Systems", "Computer Networks", "Database Management Systems",
                    "Computer Architecture", "Software Engineering"],
        "programming": ["Java", "Python", "C", "C++", "JavaScript"],
        "development": ["Android", "React", "Flask", "Git", "GitHub"],
        "cybersecurity": ["Networking", "Linux", "Nmap", "Wireshark", 
                          "Vulnerability Assessment", "Web Security", "Ethical Hacking"]
    },
    
    "projects": [
        {
            "name": "AI-Code-Review",
            "description": "CodeGuard — AI-Powered Security Code Review. Find security vulnerabilities in your code instantly.",
            "tech": ["Python", "Flask", "AI"],
            "url": "https://github.com/piyushkumar01239-pixel/AI-code-Review"
        },
        {
            "name": "WomenSafety-App",
            "description": "Women Safety SOS Alert System. Native Android app that protects women in emergencies.",
            "tech": ["Java", "SQLite", "Google Maps API", "Android Studio"],
            "url": "https://github.com/piyushkumar01239-pixel/WomenSafety-App"
        },
        {
            "name": "Personal-AI-Assistant",
            "description": "Personal AI Assistant. Voice-controlled AI that performs system-level tasks.",
            "tech": ["Python", "speech_recognition", "pyttsx3"],
            "url": "https://github.com/piyushkumar01239-pixel/Personal-AI-Assistant"
        },
        {
            "name": "DevSecOps Lab",
            "description": "DevSecOps Lab. Cybersecurity project testing environment.",
            "tech": ["DevSecOps", "Security Testing"],
            "url": "https://github.com/piyushkumar01239-pixel/devsecops-lab"
        }
    ],
    
    "achievements": {
        "coding": ["129th Rank — CodeQuezt #31 Coding Challenge", 
                   "159th Rank — Crack Government Exam – Bank PO #7"],
        "hackathons": ["Top 5% — AINCAT 2025", 
                       "2-Month Cybersecurity Internship — Jyesta EdTech × E-Cell IIT Roorkee"],
        "certifications": ["Python for Data Analytics — Coursera", 
                           "IBM Cybersecurity Careers Badge"],
        "community": ["Cyber Lock Club Member — Cybersecurity workshops & activities"]
    },
    
    "learning_journey": [
        "Computer Networks",
        "Linux Fundamentals",
        "Cybersecurity Basics",
        "Python for Security",
        "Android Development",
        "Web Security",
        "DevSecOps",
        "AI & Machine Learning"
    ]
}

# ================================================
# RESPONSE GENERATORS
# ================================================

def generate_response(question):
    """Generate response based on question"""
    question_lower = question.lower()
    
    # Greeting
    if any(word in question_lower for word in ['hi', 'hello', 'hey', 'greetings']):
        return f"""👋 Hello! I'm Piyush Kumar's profile bot!

{PROFILE_DATA['about']}

Feel free to ask me about:
• 📚 My skills and technologies
• 🚀 My projects
• 🏆 My achievements
• 📊 My GitHub stats
• 🎯 What I'm learning

What would you like to know?"""

    # About Me
    if any(word in question_lower for word in ['who', 'about', 'introduce', 'yourself', 'tell me about']):
        return f"""👤 **About Piyush Kumar**

{PROFILE_DATA['about']}

**Current Focus:** AI-Code-Review — AI-Powered Security Code Review
**Learning:** Web Security, DevSecOps, Advanced Python

**Contact:**
• 📧 Email: {PROFILE_DATA['email']}
• 🔗 LinkedIn: {PROFILE_DATA['linkedin']}
• 💻 LeetCode: {PROFILE_DATA['leetcode']}
• 🛡️ TryHackMe: {PROFILE_DATA['tryhackme']}"""

    # Skills
    if any(word in question_lower for word in ['skill', 'tech', 'technology', 'know', 'languages']):
        response = "🛠️ **Skills & Technologies**\n\n"
        
        response += "**📚 Core CS:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['skills']['core_cs']) + "\n\n"
        
        response += "**💻 Programming:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['skills']['programming']) + "\n\n"
        
        response += "**🛠️ Development:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['skills']['development']) + "\n\n"
        
        response += "**🔐 Cybersecurity:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['skills']['cybersecurity'])
        
        return response

    # Projects
    if any(word in question_lower for word in ['project', 'work', 'built', 'create', 'make', 'develop']):
        response = "🚀 **Featured Projects**\n\n"
        for project in PROFILE_DATA['projects']:
            response += f"**{project['name']}**\n"
            response += f"• {project['description']}\n"
            response += f"• Tech: " + ", ".join(project['tech']) + "\n"
            response += f"• 🔗 {project['url']}\n\n"
        return response

    # Achievements
    if any(word in question_lower for word in ['achievement', 'award', 'rank', 'prize', 'certification']):
        response = "🏆 **Achievements**\n\n"
        
        response += "**🏅 Coding:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['achievements']['coding']) + "\n\n"
        
        response += "**🚀 Hackathons:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['achievements']['hackathons']) + "\n\n"
        
        response += "**📜 Certifications:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['achievements']['certifications']) + "\n\n"
        
        response += "**🛡️ Community:**\n"
        response += "• " + "\n• ".join(PROFILE_DATA['achievements']['community'])
        
        return response

    # Learning Journey
    if any(word in question_lower for word in ['learn', 'learning', 'study', 'studying', 'journey']):
        response = "📚 **Learning Journey**\n\n"
        for i, topic in enumerate(PROFILE_DATA['learning_journey'], 1):
            response += f"{i}. {topic}\n"
        return response

    # Default response
    return f"""🤖 **I can answer questions about:**

📚 **Skills & Technologies** - Ask about programming languages, CS topics
🚀 **Projects** - Ask about my featured projects
🏆 **Achievements** - Ask about awards, rankings, certifications
📊 **GitHub Stats** - Ask about contributions, stars, followers
🎯 **Learning Journey** - Ask about what I'm currently learning

**Example questions:**
• "Tell me about yourself"
• "What projects have you built?"
• "What skills do you have?"
• "What are your achievements?"
• "What are you learning?"

💡 Quick Links:
• 📧 Email: {PROFILE_DATA['email']}
• 🔗 LinkedIn: https://linkedin.com/in/{PROFILE_DATA['linkedin']}
• 💻 LeetCode: https://leetcode.com/{PROFILE_DATA['leetcode']}
• 🛡️ TryHackMe: https://tryhackme.com/p/{PROFILE_DATA['tryhackme']}"""

# ================================================
# MAIN BOT LOGIC
# ================================================

def get_issue_question():
    """Get the question from the issue"""
    event_path = os.environ.get('GITHUB_EVENT_PATH')
    if event_path and os.path.exists(event_path):
        with open(event_path, 'r') as f:
            event = json.load(f)
        
        # Check if it's an issue
        if 'issue' in event:
            title = event['issue'].get('title', '')
            body = event['issue'].get('body', '')
            question = f"{title} {body}"
            return question, event['issue']['number']
    
    return None, None

def post_response(response, issue_number):
    """Post response back to GitHub"""
    try:
        url = f"{GITHUB_API_URL}/repos/{REPO_NAME}/issues/{issue_number}/comments"
        data = {"body": response}
        requests.post(url, headers=HEADERS, json=data)
        print(f"✅ Response posted to issue #{issue_number}")
    except Exception as e:
        print(f"❌ Error posting response: {e}")

def main():
    """Main bot function"""
    print("🤖 Bot Starting...")
    
    question, issue_number = get_issue_question()
    
    if not question:
        print("No question found. Bot sleeping...")
        return
    
    print(f"📝 Question: {question[:100]}...")
    
    # Generate response
    response = generate_response(question)
    
    # Post response
    post_response(response, issue_number)

if __name__ == "__main__":
    main()
