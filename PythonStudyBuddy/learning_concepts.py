"""
Learning Concepts Module for Python Study Buddy

This module contains dataclass models for representing learning concepts,
challenges, and educational content at different skill levels.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Literal
from enum import Enum


class SkillLevel(Enum):
    """Enumeration for different skill levels."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    EXPERT = "expert"


class ConceptCategory(Enum):
    """Categories of Python concepts."""
    BASICS = "basics"
    DATA_STRUCTURES = "data_structures"
    CONTROL_FLOW = "control_flow"
    FUNCTIONS = "functions"
    OOP = "object_oriented_programming"
    MODULES = "modules"
    FILE_IO = "file_io"
    ERROR_HANDLING = "error_handling"
    ADVANCED = "advanced_topics"
    TESTING = "testing"
    ASYNC = "asynchronous_programming"


class ChallengeType(Enum):
    """Types of coding challenges."""
    MULTIPLE_CHOICE = "multiple_choice"
    CODE_COMPLETION = "code_completion"
    DEBUG_CODE = "debug_code"
    WRITE_FUNCTION = "write_function"
    EXPLAIN_CODE = "explain_code"


@dataclass
class CodeExample:
    """Represents a code example with explanation."""
    code: str
    explanation: str
    output: Optional[str] = None
    is_runnable: bool = True


@dataclass
class Challenge:
    """Represents a coding challenge for learning."""
    id: str
    title: str
    description: str
    challenge_type: ChallengeType
    difficulty: int  # 1-10 scale
    expected_answer: str
    hints: List[str] = field(default_factory=list)
    code_template: Optional[str] = None
    test_cases: List[Dict[str, str]] = field(default_factory=list)
    points: int = 10
    time_limit_minutes: Optional[int] = None


@dataclass
class LearningConcept:
    """Represents a single learning concept with educational content."""
    id: str
    name: str
    category: ConceptCategory
    skill_level: SkillLevel
    description: str
    learning_objectives: List[str]
    explanation: str
    code_examples: List[CodeExample] = field(default_factory=list)
    challenges: List[Challenge] = field(default_factory=list)
    prerequisites: List[str] = field(default_factory=list)
    next_concepts: List[str] = field(default_factory=list)
    estimated_duration_minutes: int = 30
    keywords: List[str] = field(default_factory=list)
    resources: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """Validate the learning concept after initialization."""
        if not self.name.strip():
            raise ValueError("Learning concept name cannot be empty")
        if not self.description.strip():
            raise ValueError("Learning concept description cannot be empty")
        if self.estimated_duration_minutes <= 0:
            raise ValueError("Estimated duration must be positive")


@dataclass
class ConceptProgress:
    """Tracks user progress on a specific concept."""
    concept_id: str
    is_completed: bool = False
    is_started: bool = False
    completed_challenges: List[str] = field(default_factory=list)
    score: int = 0
    time_spent_minutes: int = 0
    last_accessed: Optional[str] = None  # ISO format timestamp
    mastery_level: float = 0.0  # 0.0 to 1.0


@dataclass
class LearningPath:
    """Represents a structured learning path for a skill level."""
    id: str
    name: str
    skill_level: SkillLevel
    description: str
    concept_ids: List[str]
    estimated_total_hours: int
    prerequisites: List[str] = field(default_factory=list)
    
    def get_next_concept(self, completed_concepts: List[str]) -> Optional[str]:
        """Get the next concept to study based on completed concepts."""
        for concept_id in self.concept_ids:
            if concept_id not in completed_concepts:
                return concept_id
        return None
    
    def get_progress_percentage(self, completed_concepts: List[str]) -> float:
        """Calculate progress percentage for this learning path."""
        if not self.concept_ids:
            return 0.0
        completed_count = sum(1 for concept_id in self.concept_ids 
                            if concept_id in completed_concepts)
        return (completed_count / len(self.concept_ids)) * 100


class ConceptRepository:
    """Repository for managing learning concepts and paths."""
    
    def __init__(self):
        self.concepts: Dict[str, LearningConcept] = {}
        self.learning_paths: Dict[str, LearningPath] = {}
    
    def add_concept(self, concept: LearningConcept) -> None:
        """Add a learning concept to the repository."""
        self.concepts[concept.id] = concept
    
    def get_concept(self, concept_id: str) -> Optional[LearningConcept]:
        """Get a learning concept by ID."""
        return self.concepts.get(concept_id)
    
    def get_concepts_by_level(self, skill_level: SkillLevel) -> List[LearningConcept]:
        """Get all concepts for a specific skill level."""
        return [concept for concept in self.concepts.values() 
                if concept.skill_level == skill_level]
    
    def get_concepts_by_category(self, category: ConceptCategory, 
                               skill_level: Optional[SkillLevel] = None) -> List[LearningConcept]:
        """Get concepts by category, optionally filtered by skill level."""
        concepts = [concept for concept in self.concepts.values() 
                   if concept.category == category]
        if skill_level:
            concepts = [concept for concept in concepts 
                       if concept.skill_level == skill_level]
        return concepts
    
    def add_learning_path(self, learning_path: LearningPath) -> None:
        """Add a learning path to the repository."""
        self.learning_paths[learning_path.id] = learning_path
    
    def get_learning_path(self, path_id: str) -> Optional[LearningPath]:
        """Get a learning path by ID."""
        return self.learning_paths.get(path_id)
    
    def get_learning_paths_by_level(self, skill_level: SkillLevel) -> List[LearningPath]:
        """Get all learning paths for a specific skill level."""
        return [path for path in self.learning_paths.values() 
                if path.skill_level == skill_level]
    
    def search_concepts(self, query: str) -> List[LearningConcept]:
        """Search concepts by name, description, or keywords."""
        query_lower = query.lower()
        results = []
        
        for concept in self.concepts.values():
            if (query_lower in concept.name.lower() or 
                query_lower in concept.description.lower() or 
                any(query_lower in keyword.lower() for keyword in concept.keywords)):
                results.append(concept)
        
        return results


def create_sample_concepts() -> ConceptRepository:
    """Create sample learning concepts for demonstration."""
    repo = ConceptRepository()
    
    # Beginner concept example
    variables_concept = LearningConcept(
        id="python_variables_beginner",
        name="Variables and Data Types",
        category=ConceptCategory.BASICS,
        skill_level=SkillLevel.BEGINNER,
        description="Learn about Python variables and basic data types",
        learning_objectives=[
            "Understand what variables are and how to create them",
            "Learn about basic data types: int, float, str, bool",
            "Practice variable assignment and naming conventions"
        ],
        explanation="""
        Variables in Python are containers for storing data values. Python has no command 
        for declaring a variable - you create one by assigning a value to it.
        
        Python supports several basic data types:
        - int: Integer numbers (e.g., 42, -10)
        - float: Decimal numbers (e.g., 3.14, -2.5)
        - str: Text strings (e.g., "Hello", 'Python')
        - bool: Boolean values (True or False)
        """,
        code_examples=[
            CodeExample(
                code='name = "Alice"\nage = 25\nheight = 5.6\nis_student = True',
                explanation="Creating variables of different data types",
                output="Variables created successfully"
            )
        ],
        challenges=[
            Challenge(
                id="variables_challenge_1",
                title="Create Your Profile",
                description="Create variables for your name, age, and favorite number",
                challenge_type=ChallengeType.WRITE_FUNCTION,
                difficulty=2,
                expected_answer='name = "Your Name"\nage = 25\nfavorite_number = 7',
                hints=["Use quotes for strings", "Numbers don't need quotes"],
                points=15
            )
        ],
        keywords=["variables", "data types", "assignment", "int", "float", "str", "bool"],
        estimated_duration_minutes=45
    )
    
    repo.add_concept(variables_concept)
    
    # Create a beginner learning path
    beginner_path = LearningPath(
        id="python_beginner_path",
        name="Python Fundamentals",
        skill_level=SkillLevel.BEGINNER,
        description="Complete introduction to Python programming",
        concept_ids=["python_variables_beginner"],
        estimated_total_hours=20
    )
    
    repo.add_learning_path(beginner_path)
    
    return repo


if __name__ == "__main__":
    # Example usage
    repo = create_sample_concepts()
    concepts = repo.get_concepts_by_level(SkillLevel.BEGINNER)
    print(f"Found {len(concepts)} beginner concepts")
    
    for concept in concepts:
        print(f"- {concept.name}: {concept.description}")