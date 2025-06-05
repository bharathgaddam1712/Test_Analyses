import json
import pandas as pd
from collections import defaultdict
from config import config
import os

def parse_syllabus(syllabus_html):
    chapters = {}
    current_subject = ""
    for line in syllabus_html.split("\n"):
        if "<h2>" in line:
            current_subject = line.replace("<h2>", "").replace("</h2>", "").strip()
            chapters[current_subject] = []
        if "<li>" in line:
            chapter = line.replace("<li>", "").replace("</li>", "").strip()
            chapters[current_subject].append(chapter)
    return chapters

def process_single_json(file_path, student_name="Student"):
    # Load JSON data with UTF-8 encoding
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error loading JSON file: {str(e)}")
    except UnicodeDecodeError as e:
        print(f"Warning: Unicode decode error ({str(e)}), attempting to read with errors='replace'")
        with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
            data = json.load(f)
    
    # Check if data is a list and take the first entry if so
    if isinstance(data, list):
        if not data:
            raise ValueError("JSON file contains an empty list")
        print("Warning: JSON file is a list; processing the first entry")
        data = data[0]
    elif not isinstance(data, dict):
        raise TypeError(f"Expected JSON to be a dictionary, got {type(data)}")
    
    # Validate required keys
    required_keys = ["test", "subjects", "sections"]
    for key in required_keys:
        if key not in data:
            raise KeyError(f"JSON data missing required key: '{key}'")
    
    # Test-level stats
    test_info = {
        "totalTime": data["test"]["totalTime"],
        "totalQuestions": data["test"]["totalQuestions"],
        "totalMarks": data["test"]["totalMarks"],
        "totalTimeTaken": data.get("totalTimeTaken", 0),
        "totalMarkScored": data.get("totalMarkScored", 0),
        "totalAttempted": data.get("totalAttempted", 0),
        "totalCorrect": data.get("totalCorrect", 0),
        "accuracy": round(data.get("accuracy", 0), 2)
    }
    
    # Parse syllabus to map subjects to chapters
    syllabus = parse_syllabus(data["test"]["syllabus"])
    
    # Subject-wise stats
    subjects = {}
    for subj in data["subjects"]:
        if "subjectId" not in subj or "$oid" not in subj["subjectId"]:
            raise KeyError("Subject data missing 'subjectId' or '$oid'")
        subj_name = config.SUBJECT_MAP.get(str(subj["subjectId"]["$oid"]), "Unknown")
        subjects[subj_name] = {
            "time": subj["totalTimeTaken"],
            "marks": subj["totalMarkScored"],
            "attempted": subj["totalAttempted"],
            "correct": subj["totalCorrect"],
            "accuracy": round(subj["accuracy"], 2),
            "avg_time_per_question": round(subj["totalTimeTaken"] / subj["totalAttempted"], 1) if subj["totalAttempted"] > 0 else 0
        }
    
    # Chapter-wise stats
    chapters = defaultdict(lambda: {"attempted": 0, "correct": 0, "time": 0, "difficulty": defaultdict(int), "concepts": set(), "subject": ""})
    if not data["sections"]:
        print("Warning: No sections found in JSON; chapter-wise stats will be empty")
    for section in data["sections"]:
        if "sectionId" not in section or "title" not in section["sectionId"]:
            raise KeyError("Section missing 'sectionId' or 'title'")
        section_subject = ""
        section_title_lower = section["sectionId"]["title"].lower()
        if "mathematics" in section_title_lower or "maths" in section_title_lower:
            section_subject = "Maths"
        elif "physics" in section_title_lower:
            section_subject = "Physics"
        elif "chemistry" in section_title_lower:
            section_subject = "Chemistry"
        
        if "questions" not in section:
            raise KeyError(f"Section '{section['sectionId']['title']}' missing 'questions'")
        for q in section["questions"]:
            if "status" not in q:
                print(f"Warning: Question in section '{section['sectionId']['title']}' missing 'status'; skipping")
                continue
            if q["status"] in ["answered", "markedReview"]:
                if "questionId" not in q or "chapters" not in q["questionId"] or not q["questionId"]["chapters"]:
                    raise KeyError("Question missing 'questionId' or 'chapters'")
                chapter = q["questionId"]["chapters"][0]["title"]
                chapters[chapter]["attempted"] += 1
                try:
                    is_correct = any(opt.get("isCorrect", False) for opt in q["markedOptions"]) or q["inputValue"].get("isCorrect", False)
                except Exception as e:
                    print(f"Warning: Issue processing question in {chapter} (section: {section['sectionId']['title']}): {str(e)}")
                    print(f"Question data: {q}")
                    is_correct = False
                if is_correct:
                    chapters[chapter]["correct"] += 1
                chapters[chapter]["time"] += q.get("timeTaken", 0)  # Default to 0 if missing
                chapters[chapter]["difficulty"][q["questionId"].get("level", "unknown")] += 1
                for concept in q["questionId"].get("concepts", []):
                    chapters[chapter]["concepts"].add(concept.get("title", "unknown"))
                chapters[chapter]["subject"] = section_subject
    
    for chapter, stats in chapters.items():
        stats["accuracy"] = round((stats["correct"] / stats["attempted"] * 100), 2) if stats["attempted"] > 0 else 0
        stats["avg_time"] = round(stats["time"] / stats["attempted"], 1) if stats["attempted"] > 0 else 0
        stats["concepts"] = list(stats["concepts"])
    
    # Prepare LLM context
    llm_context = []
    llm_context.append(f"Student: {student_name}")
    llm_context.append(f"Test: QPT 1, 11 May 2025, Total Time: {test_info['totalTime']} min, Total Questions: {test_info['totalQuestions']}, Total Marks: {test_info['totalMarks']}")
    llm_context.append(f"Overall: Time Taken: {test_info['totalTimeTaken']} sec, Marks Scored: {test_info['totalMarkScored']}, Attempted: {test_info['totalAttempted']}, Correct: {test_info['totalCorrect']}, Accuracy: {test_info['accuracy']}%")
    llm_context.append("Subjects:")
    for subj, data in subjects.items():
        llm_context.append(f"  - {subj}: Time: {data['time']} sec, Marks: {data['marks']}, Attempted: {data['attempted']}, Correct: {data['correct']}, Accuracy: {data['accuracy']}%, Avg Time per Question: {data['avg_time_per_question']} sec")
    llm_context.append("Chapters:")
    for chap, stats in chapters.items():
        difficulty_str = ', '.join([f"{k} ({v})" for k, v in stats['difficulty'].items()])
        concepts_str = ', '.join(stats['concepts'])
        llm_context.append(f"    - {chap} ({stats['subject']}): Attempted: {stats['attempted']}, Correct: {stats['correct']}, Accuracy: {stats['accuracy']}%, Avg Time: {stats['avg_time']} sec, Difficulty: {difficulty_str}, Concepts: {concepts_str}")
    
    llm_context = "\n".join(llm_context)
    
    return test_info, syllabus, subjects, dict(chapters), llm_context

def compute_accuracy_over_time(file_path):
    # Load JSON data
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Error loading JSON file: {str(e)}")
    
    if isinstance(data, list):
        if not data:
            raise ValueError("JSON file contains an empty list")
        print("Warning: JSON file is a list; processing the first entry")
        data = data[0]
    elif not isinstance(data, dict):
        raise TypeError(f"Expected JSON to be a dictionary, got {type(data)}")
    
    # Validate required keys
    if "sections" not in data:
        raise KeyError("JSON data missing 'sections' key")
    
    # Initialize tracking for each subject with independent time
    subjects_data = {
        "Maths": {"times": [], "cumulative_correct": 0, "cumulative_attempted": 0, "accuracies": []},
        "Physics": {"times": [], "cumulative_correct": 0, "cumulative_attempted": 0, "accuracies": []},
        "Chemistry": {"times": [], "cumulative_correct": 0, "cumulative_attempted": 0, "accuracies": []}
    }
    
    # Track cumulative time for each subject independently
    subject_times = {"Maths": 0, "Physics": 0, "Chemistry": 0}
    
    # Process questions in order
    if not data["sections"]:
        print("Warning: No sections found in JSON; returning empty accuracy data")
        return {subj: pd.DataFrame({"time": [], "accuracy": []}) for subj in subjects_data}
    
    for section in data["sections"]:
        if "sectionId" not in section or "title" not in section["sectionId"]:
            raise KeyError("Section missing 'sectionId' or 'title'")
        section_subject = ""
        section_title_lower = section["sectionId"]["title"].lower()
        if "mathematics" in section_title_lower or "maths" in section_title_lower:
            section_subject = "Maths"
        elif "physics" in section_title_lower:
            section_subject = "Physics"
        elif "chemistry" in section_title_lower:
            section_subject = "Chemistry"
        
        if not section_subject:
            print(f"Warning: Could not determine subject for section '{section['sectionId']['title']}'; skipping")
            continue
        
        if "questions" not in section:
            raise KeyError(f"Section '{section['sectionId']['title']}' missing 'questions'")
        if not section["questions"]:
            print(f"Warning: Section '{section['sectionId']['title']}' has no questions; skipping")
            continue
        
        for q in section["questions"]:
            if "status" not in q:
                print(f"Warning: Question in section '{section['sectionId']['title']}' missing 'status'; skipping")
                continue
            if q["status"] in ["answered", "markedReview"]:
                if "timeTaken" not in q:
                    raise KeyError(f"Question in section '{section['sectionId']['title']}' missing 'timeTaken'")
                # Update subject-specific time and accuracy
                subject_times[section_subject] += q["timeTaken"]
                subj_data = subjects_data[section_subject]
                subj_data["times"].append(subject_times[section_subject])
                subj_data["cumulative_attempted"] += 1
                try:
                    if "markedOptions" not in q or "inputValue" not in q:
                        raise KeyError("Question missing 'markedOptions' or 'inputValue'")
                    is_correct = any(opt.get("isCorrect", False) for opt in q["markedOptions"]) or q["inputValue"].get("isCorrect", False)
                except Exception as e:
                    print(f"Warning: Issue determining correctness for question in section '{section['sectionId']['title']}': {str(e)}")
                    print(f"Question data: {q}")
                    is_correct = False
                if is_correct:
                    subj_data["cumulative_correct"] += 1
                accuracy = (subj_data["cumulative_correct"] / subj_data["cumulative_attempted"] * 100) if subj_data["cumulative_attempted"] > 0 else 0
                subj_data["accuracies"].append(round(accuracy, 2))
    
    # Convert to DataFrames
    result = {}
    for subj, data in subjects_data.items():
        if data["times"]:
            result[subj] = pd.DataFrame({"time": data["times"], "accuracy": data["accuracies"]})
        else:
            print(f"Info: No data points for subject '{subj}'; including empty DataFrame")
            result[subj] = pd.DataFrame({"time": [], "accuracy": []})
    
    return result