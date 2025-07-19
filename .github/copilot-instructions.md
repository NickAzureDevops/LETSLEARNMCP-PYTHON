This project is Python 3.12+ and uses modern Python features including dataclasses and asyncio.

Make sure all code generated is inside of the PythonStudyBuddy project, which may be a subfolder inside of the main folder.

It is on GitHub at https://github.com/YOUR_USERNAME/YOUR_REPO_NAME

## Project Context
This is an interactive console application that helps developers learn Python concepts at beginner, intermediate, and expert levels through personalized study sessions.

## Python Coding Standards
- Use snake_case for function names, method names, and variables
- Use PascalCase for class names
- Use descriptive names that clearly indicate purpose
- Add docstrings for public functions and classes
- Use type hints for function parameters and return values
- Prefer f-strings for string formatting
- Use async/await for asynchronous operations
- Follow the repository pattern for data access
- Use proper exception handling with try-except blocks
- Use dataclasses for data models
- Use pathlib for file operations
- Follow PEP 8 style guidelines

## Naming Conventions
- Classes: `StudySession`, `LearningConcept`, `ProgressTracker`
- Functions: `get_concepts_by_level()`, `start_study_session()`, `generate_challenge()`
- Properties: `name`, `level`, `difficulty`, `mastery_score`
- Variables: `current_concept`, `study_progress`, `user_response`
- Constants: `BEGINNER_LEVEL`, `INTERMEDIATE_LEVEL`, `EXPERT_LEVEL`

## Architecture
- Interactive console application with study session management
- Helper classes for learning concept management
- Dataclass models for learning data representation
- Progress tracking and gamification elements
- Separation of concerns between UI and learning logic