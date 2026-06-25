import pandas as pd
import os
import json

# Ensure data directory exists
os.makedirs('data', exist_ok=True)

print("Generating Excel files...")

# 1. Practice Tasks (Mock Prompts)
tasks_data = [
    # ================= EMAILS =================
    {
        "task_type": "Email",
        "context": "You recently stayed at a hotel during a business trip, but several issues affected your stay.",
        "data": json.dumps({
            "bullets": [
                "Explain the purpose of your stay.",
                "Describe the problems you experienced.",
                "Request compensation or corrective action."
            ]
        })
    },
    {
        "task_type": "Email",
        "context": "You missed an important meeting due to unforeseen circumstances and need to inform your manager.",
        "data": json.dumps({
            "bullets": [
                "Explain why you missed the meeting.",
                "Apologize for the inconvenience.",
                "Suggest how you will catch up on missed work."
            ]
        })
    },
    {
        "task_type": "Email",
        "context": "You want to request a change in your work schedule due to family responsibilities.",
        "data": json.dumps({
            "bullets": [
                "Explain your current situation.",
                "Describe why the change is necessary.",
                "Suggest a possible schedule arrangement."
            ]
        })
    },
    {
        "task_type": "Email",
        "context": "You received a damaged item from an online store and want to contact customer service.",
        "data": json.dumps({
            "bullets": [
                "Describe what you ordered and when.",
                "Explain the damage.",
                "Request a replacement or refund."
            ]
        })
    },
    {
        "task_type": "Email",
        "context": "You want to invite a colleague to a professional networking event.",
        "data": json.dumps({
            "bullets": [
                "Describe the event.",
                "Explain why you think they should attend.",
                "Provide details and ask for confirmation."
            ]
        })
    },

    # ================= SURVEYS =================
    {
        "task_type": "Survey",
        "context": "Your company is deciding between increasing remote work or returning to full office work.",
        "data": json.dumps({
            "option_a": "Increase remote work flexibility.",
            "option_b": "Return to full-time office work."
        })
    },
    {
        "task_type": "Survey",
        "context": "The city is deciding how to reduce traffic congestion.",
        "data": json.dumps({
            "option_a": "Invest in better public transportation.",
            "option_b": "Build more roads and highways."
        })
    },
    {
        "task_type": "Survey",
        "context": "A university is deciding whether to increase tuition fees or reduce student services.",
        "data": json.dumps({
            "option_a": "Increase tuition fees.",
            "option_b": "Reduce student services."
        })
    },
    {
        "task_type": "Survey",
        "context": "A company is choosing between investing in employee training or new technology.",
        "data": json.dumps({
            "option_a": "Invest in employee training.",
            "option_b": "Invest in new technology."
        })
    },
    {
        "task_type": "Survey",
        "context": "The government is deciding how to reduce environmental pollution.",
        "data": json.dumps({
            "option_a": "Increase taxes on polluting companies.",
            "option_b": "Offer incentives for green technology."
        })
    }
]

tasks_data.extend([
    # --- Formal Emails ---
    {
        "task_type": "Email",
        "context": "You recently took your 2019 Ford Escape to a local mechanic in Truro for a wheel bearing replacement, but the issue was not resolved.",
        "data": json.dumps({
            "bullets": [
                "Explain when you brought the car in and the service you paid for.",
                "Describe the ongoing noise or issue you are experiencing.",
                "Request a free follow-up inspection to fix the problem."
            ]
        })
    },
    {
        "task_type": "Email",
        "context": "You are organizing a professional development workshop on Python automation for your team and need to request a budget from your manager.",
        "data": json.dumps({
            "bullets": [
                "Outline the purpose and benefits of the workshop.",
                "Provide a breakdown of the estimated costs.",
                "Ask for their approval to proceed."
            ]
        })
    },
    # --- Informal Emails ---
    {
        "task_type": "Email",
        "context": "You are organizing a study session with a classmate and want to suggest ordering dinner from Greco Pizza.",
        "data": json.dumps({
            "bullets": [
                "Suggest a time and place for the study session.",
                "Ask what kind of food they would like and suggest Greco Pizza.",
                "Offer to place the order and pick it up."
            ]
        })
    },
    # --- Surveys ---
    {
        "task_type": "Survey",
        "context": "Your local community center is deciding on a new adult recreation program.",
        "data": json.dumps({
            "option_a": "Offer a traditional martial arts class focusing on Hung Ga Kung Fu.",
            "option_b": "Offer a professional networking and technology skills bootcamp."
        })
    },
    {
        "task_type": "Survey",
        "context": "The city council is debating how to handle a recent increase in residential noise complaints.",
        "data": json.dumps({
            "option_a": "Implement stricter bylaws and heavy fines for noise violations.",
            "option_b": "Fund a community mediation program to help neighbors resolve disputes."
        })
    }
])

pd.DataFrame(tasks_data).replace({'’': "'", '‘': "'"}, regex=True).to_excel('data/practice_tasks.xlsx', index=False)


# 2. Vocabulary Data
vocab_data = [
    {"word": "Advantageous", "category": "General", "difficulty": 8, "definition": "Providing an advantage; favorable.", "synonym_1": "Beneficial", "synonym_2": "Favorable", "example_sentence": "Working remotely is highly advantageous for work-life balance.", "celpip_usefulness_score": 10},
    {"word": "Detrimental", "category": "General", "difficulty": 9, "definition": "Tending to cause harm.", "synonym_1": "Harmful", "synonym_2": "Damaging", "example_sentence": "Lack of investment in public transport is detrimental to the city's growth.", "celpip_usefulness_score": 10},
    {"word": "Consequently", "category": "Connector", "difficulty": 7, "definition": "As a result.", "synonym_1": "Therefore", "synonym_2": "Thus", "example_sentence": "The train was delayed; consequently, I missed the meeting.", "celpip_usefulness_score": 12},
    {"word": "Indispensable", "category": "Work", "difficulty": 10, "definition": "Absolutely necessary.", "synonym_1": "Essential", "synonym_2": "Crucial", "example_sentence": "Good communication skills are indispensable in the modern workplace.", "celpip_usefulness_score": 9},
    {"word": "Mitigate", "category": "Problem Solving", "difficulty": 11, "definition": "Make less severe, serious, or painful.", "synonym_1": "Alleviate", "synonym_2": "Reduce", "example_sentence": "We must take immediate action to mitigate the risks.", "celpip_usefulness_score": 9}
]
vocab_data.extend([
    {"word": "Moreover", "category": "Connector", "difficulty": 7, "definition": "In addition to what has been stated.", "synonym_1": "Furthermore", "synonym_2": "Additionally", "example_sentence": "Moreover, the policy will reduce long-term costs.", "celpip_usefulness_score": 10},

    {"word": "Nevertheless", "category": "Connector", "difficulty": 9, "definition": "In spite of that.", "synonym_1": "However", "synonym_2": "Nonetheless", "example_sentence": "The task is difficult; nevertheless, it is achievable.", "celpip_usefulness_score": 10},

    {"word": "Substantial", "category": "General", "difficulty": 8, "definition": "Of considerable importance or size.", "synonym_1": "Significant", "synonym_2": "Considerable", "example_sentence": "There was a substantial improvement in performance.", "celpip_usefulness_score": 9},

    {"word": "Implement", "category": "Work", "difficulty": 8, "definition": "Put a plan into action.", "synonym_1": "Execute", "synonym_2": "Apply", "example_sentence": "We will implement the new system next month.", "celpip_usefulness_score": 10},

    {"word": "Inadequate", "category": "Problem Solving", "difficulty": 8, "definition": "Not enough or insufficient.", "synonym_1": "Insufficient", "synonym_2": "Deficient", "example_sentence": "The current facilities are inadequate for growing demand.", "celpip_usefulness_score": 9}
])
vocab_data.extend([
    {"word": "Unprecedented", "category": "General", "difficulty": 10, "definition": "Never done or known before.", "synonyms": "Unparalleled, Extraordinary", "example_sentence": "The city is experiencing an unprecedented level of population growth.", "celpip_usefulness_score": 9},
    {"word": "Lucrative", "category": "Work", "difficulty": 9, "definition": "Producing a great deal of profit.", "synonyms": "Profitable, Rewarding", "example_sentence": "Learning data engineering can lead to a highly lucrative career.", "celpip_usefulness_score": 8},
    {"word": "Streamline", "category": "Work", "difficulty": 8, "definition": "Make an organization or system more efficient.", "synonyms": "Optimize, Simplify", "example_sentence": "We need to streamline our data pipelines to reduce processing time.", "celpip_usefulness_score": 10},
    {"word": "On the contrary", "category": "Connector", "difficulty": 7, "definition": "Used to intensify a denial of what has just been implied.", "synonyms": "Conversely, Oppositely", "example_sentence": "I am not opposed to the new software; on the contrary, I fully support it.", "celpip_usefulness_score": 11},
    {"word": "Alleviate", "category": "Problem Solving", "difficulty": 10, "definition": "Make a problem less severe.", "synonyms": "Relieve, Ease", "example_sentence": "The new transit route will alleviate traffic on the main highway.", "celpip_usefulness_score": 10}
])
pd.DataFrame(vocab_data).replace({'’': "'", '‘': "'"}, regex=True).to_excel('data/vocabulary.xlsx', index=False)


# 3. Phrase Bank Data (For Typing Challenge)
phrase_data = [
    {"phrase": "I am writing to express my profound dissatisfaction regarding...", "category": "Complaint Email", "difficulty": 8},
    {"phrase": "Furthermore, it is crucial to consider the long-term impact of this decision.", "category": "Survey Body", "difficulty": 9},
    {"phrase": "One of the primary advantages of this approach is that it significantly improves efficiency.", "category": "Survey Argument", "difficulty": 10},
    {"phrase": "I kindly request that you address this matter at your earliest convenience.", "category": "Email Conclusion", "difficulty": 8},
    {"phrase": "Although Option A has its merits, I strongly believe that Option B is the superior choice.", "category": "Survey Intro", "difficulty": 11},
    {"phrase": "Consequently, allocating funds to public transport would mitigate traffic congestion.", "category": "Survey Body", "difficulty": 12}
]
phrase_data.extend([
    {"phrase": "I am writing to bring to your attention an issue that requires immediate action.", "category": "Complaint Email", "difficulty": 9},
    {"phrase": "I would greatly appreciate your assistance in resolving this matter.", "category": "Email Request", "difficulty": 8},
    {"phrase": "While I understand the constraints, I believe an alternative solution could be considered.", "category": "Negotiation", "difficulty": 10},
    {"phrase": "From my perspective, the most effective option would be...", "category": "Survey Argument", "difficulty": 8},
    {"phrase": "I regret to inform you that I will be unable to attend due to unforeseen circumstances.", "category": "Formal Email", "difficulty": 9},
    {"phrase": "This decision will have a significant impact on both employees and stakeholders.", "category": "Survey Body", "difficulty": 10},
    {"phrase": "It is worth noting that this approach offers both short-term and long-term benefits.", "category": "Survey Body", "difficulty": 9}
])
phrase_data.extend([
    # Formal
    {"phrase": "I would be incredibly grateful if we could resolve this matter swiftly.", "category": "Formal Email", "difficulty": 8},
    {"phrase": "To put it simply, the benefits of the first option far outweigh the drawbacks.", "category": "Survey Argument", "difficulty": 9},
    {"phrase": "Thank you in advance for your time and consideration.", "category": "Formal Conclusion", "difficulty": 6},
    
    # Informal
    {"phrase": "Let me know if you’re down to grab a slice later!", "category": "Informal Conclusion", "difficulty": 5},
    {"phrase": "I was wondering if you’d be up for helping me out with something.", "category": "Informal Request", "difficulty": 6},
    {"phrase": "It totally slipped my mind!", "category": "Informal Apology", "difficulty": 7}
])
pd.DataFrame(phrase_data).replace({'’': "'", '‘': "'"}, regex=True).to_excel('data/phrase_bank.xlsx', index=False)


# 4. Band 12 Examples
band12_data = [
    {
        "task_type": "Email", 
        "topic": "Restaurant Complaint", 
        "prompt": "You recently ate at a restaurant. The service and food were terrible.", 
        "response": "Dear Restaurant Manager,\n\nI am writing to express my profound disappointment regarding my recent dining experience at your establishment on Friday evening. My family and I visited your restaurant to celebrate my wife's birthday; however, the evening fell significantly short of our expectations.\n\nFirstly, despite having a reservation, we were forced to wait for over 45 minutes for a table. Furthermore, when our meals finally arrived, they were lukewarm and completely lacked the quality we have come to expect from your kitchen. To make matters worse, our server was remarkably inattentive and dismissive when we politely raised these concerns.\n\nConsequently, our special celebration was largely ruined. Given the premium prices your establishment charges, this level of service is entirely unacceptable.\n\nI kindly request a full refund for our meal or, at the very least, a voucher for a future visit to demonstrate your commitment to customer satisfaction. I look forward to your prompt response regarding how you intend to rectify this situation.\n\nSincerely,\nJohn Smith"
    },
    {
        "task_type": "Survey", 
        "topic": "City Budget", 
        "prompt": "City surplus: Park vs Public Transport", 
        "response": "While investing in green spaces is undoubtedly beneficial for community well-being, I firmly believe that upgrading the city's public transportation system should be the absolute priority for the budget surplus.\n\nThe primary reason for my stance is the immediate and widespread economic impact. Currently, our transit system is heavily congested and notoriously unreliable. By directing funds toward purchasing modern buses and expanding train routes, the city can drastically reduce commute times. Consequently, this will enhance productivity for thousands of daily commuters who rely on these services to reach their workplaces.\n\nFurthermore, improving public transit is an indispensable step toward environmental sustainability. If the city provides a more efficient and comfortable transit alternative, a substantial number of residents will be incentivized to leave their personal vehicles at home. Over time, this shift will mitigate traffic congestion and significantly lower our city's carbon footprint.\n\nAlthough building more parks is an attractive option, it simply does not address the pressing logistical and environmental challenges our rapidly growing population faces. Therefore, allocating the surplus to transportation infrastructure is the most pragmatic and advantageous decision."
    },
    {
    "task_type": "Email",
    "topic": "Missed Appointment Apology",
    "prompt": "You missed an appointment with a service provider and need to explain.",
    "response": "Dear Sir/Madam,\n\nI am writing to sincerely apologize for missing my scheduled appointment on Tuesday afternoon. Unfortunately, due to an unexpected medical situation, I was unable to attend as planned.\n\nI fully understand that my absence may have caused inconvenience, and I deeply regret any disruption this may have caused to your schedule. I take full responsibility for not informing you in advance.\n\nI would greatly appreciate the opportunity to reschedule the appointment at your earliest convenience. Please let me know a suitable time, and I will ensure that I make the necessary arrangements to attend without fail.\n\nThank you for your understanding.\n\nSincerely,\nJohn Smith"
    },
    {
    "task_type": "Survey",
    "topic": "Education Funding",
    "prompt": "Increase funding for sports vs academic programs",
    "response": "While sports programs play an important role in student development, I strongly believe that increasing funding for academic programs should be the priority.\n\nAcademic excellence forms the foundation of future career success, and many schools currently lack adequate resources such as updated textbooks, technology, and qualified teaching staff. By investing in these areas, students will be better prepared for higher education and the workforce.\n\nMoreover, improving academic infrastructure benefits all students, whereas sports programs tend to serve a smaller group. Although physical activity is important, it should not come at the expense of core educational needs.\n\nTherefore, allocating additional funding to academic programs is the most practical and impactful decision."
    }
]
band12_data.extend([
    {
        "task_type": "Email", 
        "topic": "Mechanic Complaint (Formal)", 
        "prompt": "You recently took your car to a mechanic for a repair, but the issue was not resolved.", 
        "response": "Dear Service Manager,\n\nI am writing to express my concern regarding the recent service performed on my 2019 Ford Escape at your garage last Tuesday. I brought the vehicle in to have the front wheel bearings replaced, as there was a distinct grinding noise while driving at highway speeds.\n\nWhile the customer service I received at the front desk was excellent, I noticed immediately upon driving home that the exact same grinding noise is still present. It appears the underlying issue was not correctly diagnosed or resolved, despite my paying the full invoice for the bearing replacement.\n\nSince I rely heavily on my vehicle for my daily commute, I am quite worried about the safety of driving it in its current condition. I kindly request that you arrange a free follow-up inspection this week to properly identify and rectify the source of the noise.\n\nI look forward to hearing from you soon to schedule an appointment.\n\nSincerely,\nJohn Smith"
    },
    {
        "task_type": "Survey", 
        "topic": "Community Center Programs", 
        "prompt": "Community Center: Martial Arts vs Coding Bootcamp", 
        "response": "While a technology bootcamp offers valuable career skills, I strongly support introducing a Hung Ga Kung Fu class at the community center, as it provides unique physical and mental health benefits that are currently lacking in our local programming.\n\nFirst and foremost, martial arts training promotes an active lifestyle. Many adults in our community work sedentary office jobs, and a dynamic physical activity like Kung Fu is an excellent way to improve cardiovascular health, flexibility, and overall fitness. Furthermore, the discipline required to master the forms, such as the Tiger and Crane movements, fosters mental resilience and stress relief, which is incredibly beneficial after a long workday.\n\nConversely, while coding skills are undeniably lucrative, they require participants to spend even more time sitting in front of screens. Additionally, there are already countless online resources and formal educational institutions in our area that provide excellent tech training, making it redundant for the community center to allocate funds toward it.\n\nTherefore, offering a martial arts program is the most advantageous choice for promoting the holistic well-being of our residents."
    }
])
pd.DataFrame(band12_data).replace({'’': "'", '‘': "'"}, regex=True).to_excel('data/band12_examples.xlsx', index=False)

print("✅ Excel files successfully generated in the /data/ folder!")