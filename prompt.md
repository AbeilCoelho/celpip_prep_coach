# CELPIP Writing Coach - Full Project Specification

## Project Vision

Build a full-featured Python Flask web application called **CELPIP Writing Coach** designed to help students achieve CELPIP Writing scores of 10–12.

The application should not only simulate the CELPIP Writing test but actively teach users how to write like a high-scoring candidate through:

* Writing simulations
* Vocabulary training
* Connector mastery
* Sentence complexity training
* Typing speed improvement
* Personalized feedback
* Spaced repetition
* Gamification

The application should feel like a combination of:

* Duolingo
* Grammarly
* CELPIP Test Simulator
* Anki
* TypingClub

The ultimate goal is measurable score improvement, not passive learning.

---

# Core Learning Philosophy

The application should focus on the factors that most impact CELPIP Writing scores:

1. Task Fulfillment
2. Organization
3. Connector Variety
4. Advanced Vocabulary
5. Sentence Complexity
6. Typing Speed
7. Error Reduction

Every feature should support at least one of these goals.

---

# Technology Stack

## Backend

* Python 3.12+
* Flask
* Flask-Login
* SQLAlchemy
* Flask-WTF
* SQLite (development)
* PostgreSQL (production)

## Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript
* Jinja2

## Optional Integrations

* HTMX
* Chart.js
* Quill Editor
* LanguageTool
* OpenAI API

---

# User Interface Requirements

Create a modern, professional and responsive interface.

Requirements:

* Clean academic appearance
* Dark mode
* Light mode
* Mobile responsive
* Statistics cards
* Progress widgets
* Achievement badges
* Animations
* Gamification elements

The interface should resemble modern educational platforms.

---

# Development Phases

## Phase 1 - Foundation

Build:

* Authentication
* User profiles
* Dashboard
* SQLite models
* Excel import engine
* Progress tracking

## Phase 2 - Writing Simulator

Build:

* Task 1 Email Practice
* Task 2 Survey Practice
* Timers
* Word counters
* Auto-save
* Spell checking

## Phase 3 - Scoring Engine

Build:

* CELPIP-style scoring
* Feedback generation
* Statistics

## Phase 4 - Learning Modules

Build:

* Vocabulary Trainer
* Connector Trainer
* Sentence Complexity Trainer
* Phrase Bank
* Band 12 Library

## Phase 5 - Gamification

Build:

* Streaks
* Badges
* Leaderboards (optional)
* Typing challenges
* Vocabulary games

## Phase 6 - AI Features

Build:

* Writing assistant
* Vocabulary suggestions
* Adaptive learning
* AI-generated practice tasks

---

# Dashboard

Display:

* Estimated CELPIP Writing Level
* Daily Streak
* Vocabulary Mastery
* Connector Mastery
* Practice Sessions Completed
* Average Writing Score
* Weakness Analysis
* Recent Activity

---

# Writing Simulator

The simulator should closely mimic the real CELPIP environment.

---

## Task 1 - Email Writing

Generate unlimited scenarios:

Examples:

* Complaint email
* Workplace request
* Landlord issue
* Customer service issue
* School inquiry
* Thank-you email
* Invitation response

Features:

* 27-minute timer
* Word counter
* Auto-save
* Spell checker
* Formal/informal indicator
* Bullet points displayed exactly like CELPIP

After submission evaluate:

* Content
* Task Fulfillment
* Vocabulary
* Grammar
* Sentence Structure
* Organization
* Tone

Provide:

* Estimated CELPIP score
* Detailed breakdown
* Suggestions
* Improved sentence examples

---

## Task 2 - Survey Response

Generate survey questions similar to CELPIP.

Example:

Would you rather:

A) Work from home

OR

B) Work in an office

Features:

* 26-minute timer
* Word counter
* Auto-save
* Spell checker

Evaluate:

* Argument strength
* Supporting details
* Organization
* Vocabulary sophistication
* Grammar quality
* Coherence

Provide:

* Estimated score
* Suggestions
* Improved examples

---

# CELPIP Blueprint Builder

Before every writing task the user should create a quick outline.

## Email Blueprint

Fields:

* Purpose
* Bullet Point 1
* Bullet Point 2
* Bullet Point 3
* Closing

## Survey Blueprint

Fields:

* Selected Option
* Reason 1
* Example 1
* Reason 2
* Example 2
* Conclusion

Store blueprint and compare it against final submission.

This trains planning skills used by high-scoring candidates.

---

# Gold Standard Structure Training

Teach reusable high-scoring structures.

---

## Email Structures

### Introduction

* I am writing to...
* I would like to...
* I am contacting you regarding...

### Body

* Firstly,
* Furthermore,
* In addition,
* Moreover,
* Another important point is...

### Conclusion

* Thank you for your consideration.
* I look forward to hearing from you.
* Please do not hesitate to contact me.

---

## Survey Structures

### Introduction

* I strongly believe...
* In my opinion...
* Given the choice...

### Body

* The primary reason is...
* Another significant advantage is...
* Furthermore...
* In addition...

### Complex Sentences

* Although...
* Even though...
* While...
* Since...
* Because...
* Therefore...
* Consequently...
* Not only... but also...

---

# Advanced Vocabulary Training

Categories:

* Work
* Education
* Technology
* Travel
* Housing
* Community
* Environment
* Healthcare

Each word contains:

* Definition
* Synonyms
* Example sentence
* CELPIP usefulness score
* Difficulty level

Examples:

* beneficial
* advantageous
* consequently
* furthermore
* substantial
* efficient
* flexible
* reliable
* indispensable

---

# Vocabulary Memorization Games

## Spelling Challenge

Spell advanced words.

Features:

* Hints
* Difficulty levels
* Timer
* Audio pronunciation

---

## Missing Letters

Example:

a _ v a n t a g e o u s

---

## Connector Match

Match:

* Furthermore → Addition
* Consequently → Result
* However → Contrast

---

## Sentence Builder

Build complex sentences from provided words.

---

## Vocabulary Sprint

60-second challenge.

Type as many advanced words as possible.

---

## Connector Race

Select the correct connector under time pressure.

---

# Vocabulary-in-Context Training

The goal is to teach vocabulary usage rather than memorization.

---

## Fill in the Blank

Example:

Working remotely is ______ because it allows employees greater flexibility.

Options:

* advantageous
* dangerous
* expensive
* irrelevant

---

## Context Selection

Choose the best word for a situation.

---

## Connector Selection

Choose the best connector for a paragraph.

---

## Sentence Completion

Complete Band 12 sentences.

---

## Vocabulary Replacement

Replace weak vocabulary.

Examples:

* good → beneficial
* bad → detrimental
* important → significant
* big → substantial

---

## Context-Based Writing

Generate mini-writing tasks using target vocabulary.

Use spaced repetition for difficult words.

---

# Sentence Complexity Trainer

Train users to transform simple writing into Band 10–12 writing.

---

## Transform Simple Sentences

Input:

I like working from home.

Output:

I prefer working from home because it provides greater flexibility and significantly reduces commuting time.

---

## Combine Sentences

Input:

The office is far away.

I still work there.

Output:

Although the office is far away, I still choose to work there.

---

## Pattern Practice

Train:

* Although
* Even though
* While
* Since
* Because
* Therefore
* Consequently
* Not only... but also

---

## Complexity Scoring

Calculate:

* Average sentence length
* Subordinate clauses
* Connector usage
* Variety

Generate:

Sentence Complexity Score

---

# Band 12 Example Library

One of the most important modules.

Purpose:

Allow users to study high-scoring responses and understand why they work.

---

## Features

* Filter by topic
* Filter by task type
* Search examples
* Highlight advanced vocabulary
* Highlight connectors
* Highlight sentence structures
* Display estimated score

---

## Read Mode

Read complete answer.

---

## Analyze Mode

Click phrases to reveal:

* Why they are effective
* Vocabulary level
* Connector category
* Complexity level

---

## Shadow Writing Mode

Hide sections and ask user to complete them.

---

## Reconstruction Mode

Shuffle paragraphs and reconstruct the response.

---

## Comparison Mode

Compare user answer against Band 12 answer.

Show:

* Missing vocabulary
* Missing connectors
* Structural differences

---

# Personal Phrase Bank

Allow users to save favorite CELPIP phrases.

Examples:

* I am writing to express my concern regarding...
* The primary reason for my preference is...
* Thank you for your time and consideration.

Store:

* Phrase
* Category
* Difficulty
* Notes

---

## Favorite Phrases

Categories:

* Email Introduction
* Email Body
* Email Conclusion
* Survey Introduction
* Survey Arguments
* Survey Conclusion

---

## Typing Challenge

Turn saved phrases into typing drills.

Track:

* Accuracy
* WPM
* Best Time
* Personal Records

---

## Rapid Recall Mode

Show phrase briefly.

Hide phrase.

User must retype from memory.

---

## Daily Phrase Drill

Generate practice sessions automatically.

Use mastery tracking.

---

# Error Notebook

Store every mistake detected during writing.

Track:

* Grammar mistakes
* Spelling mistakes
* Connector misuse
* Weak vocabulary
* Repeated vocabulary
* Sentence structure issues

Store:

* Date
* Original text
* Corrected text
* Severity
* Repetition count

---

## Common Mistakes Dashboard

Display:

* Most frequent mistakes
* Improvement trends

---

## Smart Review

Generate exercises based on previous mistakes.

---

## Error Mastery

Mistakes disappear after repeated successful correction.

---

## Spaced Repetition

Review schedule:

* 1 day
* 3 days
* 7 days
* 14 days
* 30 days

---

# Connector Heatmap

Analyze connector usage.

Track:

* Connector frequency
* Connector diversity
* Connector categories used
* Missing categories

Visualize:

* Heatmaps
* Charts
* Trends

Examples:

Overused:

* because
* also

Underused:

* nevertheless
* consequently
* furthermore

Generate:

Connector Diversity Score

Provide replacement suggestions automatically.

---

# Smart Writing Assistant

Optional module.

Real-time assistance.

Features:

* Grammar correction
* Spelling correction
* Connector suggestions
* Vocabulary upgrades
* Sentence variety suggestions

Allow users to enable or disable assistance.

---

# Word Forecast System

Optional AI-powered autocomplete.

Examples:

User types:

"I think"

Suggestions:

* I strongly believe
* In my opinion
* From my perspective
* I am convinced that

Suggest:

* Better vocabulary
* Formal alternatives
* Stronger connectors
* Advanced sentence starters

---

# Adaptive Learning Engine

Identify weaknesses automatically.

Examples:

If grammar is weak:

* Assign grammar exercises

If connectors are weak:

* Increase connector drills

If vocabulary is weak:

* Increase vocabulary exercises

Generate personalized learning plans.

---

# Practice Scheduler

Daily study planner.

Example:

15 min Vocabulary

15 min Connectors

30 min Writing Task

10 min Review

Track completion.

---

# Achievement System

Badges:

* 7 Day Streak
* 30 Day Streak
* Vocabulary Master
* Connector Expert
* Email Specialist
* Survey Specialist
* CELPIP Ready

---

# Performance Analytics

Calculate:

* Estimated CELPIP Writing Score
* Vocabulary Mastery %
* Connector Diversity Score
* Sentence Complexity Score
* Typing Speed
* Error Rate
* Band 12 Readiness Score

Generate personalized recommendations.

---

# Writing Analytics Engine

Calculate:

## Vocabulary Score

Based on:

* Unique words
* Advanced words
* Repetition rate

## Connector Score

Based on:

* Variety
* Frequency
* Category coverage

## Complexity Score

Based on:

* Subordinate clauses
* Sentence variety
* Complex structures

## Task Fulfillment Score

Based on:

* Required points addressed
* Word count
* Organization

Combine these metrics into an estimated CELPIP score.

---

# Excel-Driven Content Management

IMPORTANT:

Educational content must never be hardcoded.

Excel files are the source of truth.

SQLite acts only as the runtime database.

On startup:

1. Validate spreadsheets
2. Import data
3. Log errors
4. Continue operation using SQLite

Support:

* Full refresh
* Incremental updates
* Duplicate detection
* Validation
* Error reporting

---

# Excel Files

## vocabulary.xlsx

Columns:

* id
* word
* category
* difficulty
* definition
* synonym_1
* synonym_2
* synonym_3
* example_sentence
* celpip_usefulness_score

---

## connectors.xlsx

Columns:

* id
* connector
* category
* meaning
* example
* difficulty

Categories:

* Addition
* Contrast
* Cause
* Effect
* Sequence
* Conclusion

---

## phrase_bank.xlsx

Columns:

* id
* phrase
* category
* task_type
* difficulty
* example

---

## band12_examples.xlsx

Columns:

* id
* task_type
* topic
* prompt
* response
* score
* notes
* highlighted_connectors
* highlighted_vocabulary

---

## sentence_patterns.xlsx

Columns:

* id
* pattern
* complexity_level
* explanation
* example

---

# Database Schema

Users

PracticeSessions

WritingSubmissions

VocabularyWords

VocabularyProgress

ConnectorProgress

PhraseBankProgress

Mistakes

Achievements

DailyGoals

Statistics

Band12Examples

SentencePatterns

Blueprints

---

# Deliverables

Generate:

* Flask project structure
* SQLAlchemy models
* Routes
* Services layer
* Import engine
* Templates
* CSS
* JavaScript
* Authentication
* Admin dashboard
* Unit tests
* Docker support
* README

Follow Flask best practices.

Use a modular architecture.

The code should be production-ready, maintainable, scalable, and easy to extend.
