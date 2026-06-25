import pandas as pd
import os
import json
from app.extensions import db
from app.models import VocabularyWord, Connector, Band12Example, Phrase, PracticeTask

def load_excel_to_db(app):
    data_dir = os.path.join(app.root_path, '..', 'data')
    
    with app.app_context():
        # 1. Load Vocabulary
        vocab_path = os.path.join(data_dir, 'vocabulary.xlsx')
        if os.path.exists(vocab_path):
            try:
                df = pd.read_excel(vocab_path)
                db.session.query(VocabularyWord).delete()
                for _, row in df.iterrows():
                    db.session.add(VocabularyWord(
                        word=row.get('word'),
                        category=row.get('category'),
                        difficulty=row.get('difficulty'),
                        definition=row.get('definition'),
                        synonyms=f"{row.get('synonym_1', '')}, {row.get('synonym_2', '')}",
                        example_sentence=row.get('example_sentence'),
                        celpip_usefulness_score=row.get('celpip_usefulness_score')
                    ))
                db.session.commit()
                print("✅ Vocabulary imported.")
            except Exception as e:
                print(f"Error importing vocabulary: {e}")

        # 2. Load Phrase Bank
        phrase_path = os.path.join(data_dir, 'phrase_bank.xlsx')
        if os.path.exists(phrase_path):
            try:
                df = pd.read_excel(phrase_path)
                db.session.query(Phrase).delete()
                for _, row in df.iterrows():
                    db.session.add(Phrase(
                        phrase=row.get('phrase'), category=row.get('category'), difficulty=row.get('difficulty')
                    ))
                db.session.commit()
                print("✅ Phrase Bank imported.")
            except Exception as e:
                print(f"Error importing phrases: {e}")

        # 3. Load Band 12 Examples
        band12_path = os.path.join(data_dir, 'band12_examples.xlsx')
        if os.path.exists(band12_path):
            try:
                df = pd.read_excel(band12_path)
                db.session.query(Band12Example).delete()
                for _, row in df.iterrows():
                    db.session.add(Band12Example(
                        task_type=row.get('task_type'), topic=row.get('topic'),
                        prompt=row.get('prompt'), response=row.get('response')
                    ))
                db.session.commit()
                print("✅ Band 12 Examples imported.")
            except Exception as e:
                print(f"Error importing Band 12: {e}")

        # 4. Load Practice Prompts (Mock Tasks)
        tasks_path = os.path.join(data_dir, 'practice_tasks.xlsx')
        if os.path.exists(tasks_path):
            try:
                df = pd.read_excel(tasks_path)
                db.session.query(PracticeTask).delete()
                for _, row in df.iterrows():
                    db.session.add(PracticeTask(
                        task_type=row.get('task_type'), context=row.get('context'), data=row.get('data') 
                    ))
                db.session.commit()
                print("✅ Practice Tasks imported.")
            except Exception as e:
                print(f"Error importing tasks: {e}")