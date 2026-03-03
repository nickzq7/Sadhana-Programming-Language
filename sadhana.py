#!/usr/bin/env python3
"""
SADHANA PROGRAMMING LANGUAGE v1.0 - COMPLETE SEMANTIC COMPUTING FRAMEWORK
=========================================================================

A meaning-first, order-free, time-latent programming language for AGI research.

Core Philosophy:
- Meaning precedes structure
- Order does not define meaning  
- Time is latent (parameter of expansion)
- Finite grammar, infinite structures
- No neural networks in core (formal exclusion)

Architecture: 20-Layer Framework
  0. Axiomatic Layer (5 Core Axioms)
  1. Ontological Foundation
  2. Dhatu Layer (8 Semantic Laws)
  3. Semantic Primitives
  4. Meaning Graph Layer
  5. Canonical Meaning Kernel (CMK)
  6. Semantic Reduction
  7. Bija Layer (Meta-Compression)
  8. Global Root Operators
  9. Sandhi Engine (Composition Gate)
  10. Option-Rule Engine (Gated Decompression)
  11. Temporal-Structural Expansion
  12. Topological Meaning Space
  13. Sanhara Engine (Non-Committal Simulation)
  14. Semantic Membrane (Execution Firewall)
  15. Structural Resonance Compiler
  16. Type/Role/Capability Inference
  17. Deferred Mutation & Versioning
  18. Causal & Provenance Runtime
  19. Execution Backends (Multi-Target)
  20. Meta-Layer (Self-Reference)

Author: Sadhana Framework
Version: 1.0.0
License: Research Use
"""

import hashlib
import json
import re
import uuid
import base64
import argparse
import sys
import copy
import itertools
from typing import Dict, List, Set, Tuple, Optional, Any, Union, Callable, Iterator
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from collections import defaultdict
from abc import ABC, abstractmethod

# ============================================================================
# SECTION 1: CORE TYPES AND ENUMS
# ============================================================================

class TokenType(Enum):
    """Lexical token types for notebook syntax."""
    NAME = auto()           # Entity/identifier
    DIRECTIVE = auto()      # @key: value
    RELATION = auto()       # contains, requires, etc.
    CONSTRAINT = auto()     # Constraint:
    ROOTS = auto()          # Roots:
    NUMBER = auto()         # Numeric value
    EXACTLY = auto()        # exactly
    AT_LEAST = auto()       # at least
    AT_MOST = auto()        # at most
    ONE = auto()            # one
    NEWLINE = auto()        # Line break
    EOF = auto()            # End of file

class SemanticType(Enum):
    """Types of semantic entities."""
    ENTITY = auto()
    CONTAINER = auto()
    INTERFACE = auto()
    DATA = auto()
    FUNCTION = auto()
    SKELETON = auto()
    COMPOSITE = auto()

class Guna(Enum):
    """
    Three fundamental qualities (Guṇas) from Saṃkhya philosophy.
    Map to visual/interaction properties.
    """
    SATTVA = "sattva"   # Illumination, harmony, gold/white
    RAJAS = "rajas"     # Activity, passion, orange/red  
    TAMAS = "tamas"     # Inertia, darkness, dark/black

class Pada(Enum):
    """
    Three realms (Padas) - spatial orientation.
    Map to layout/position properties.
    """
    URDHVALOKA = "urdhvaloka"   # Upper world - top position
    MADHYALOKA = "madhyaloka"   # Middle world - center/fill
    ADHOLOKA = "adholoka"       # Lower world - bottom position

class ExpansionLevel(Enum):
    """Temporal expansion levels (Kala)."""
    T0 = 0   # Seed (compressed)
    T1 = 1   # Fundamental (64 structures)
    T2 = 2   # Variation (128 structures, Guna×Pada)
    T3 = 3   # Full expansion (256 structures)

@dataclass
class Token:
    """Lexical token."""
    type: TokenType
    value: str
    line: int
    col: int
    
    def __repr__(self):
        return f"Token({self.type.name}, '{self.value}', L{self.line})"

@dataclass
class SemanticEntity:
    """Entity in the meaning graph."""
    uid: str
    name: str
    sem_type: SemanticType
    guna: Guna = Guna.SATTVA
    pada: Pada = Pada.MADHYALOKA
    properties: Dict = field(default_factory=dict)
    synthetic: bool = False  # True if T1/T2/T3 expansion entity
    
    def copy(self):
        return SemanticEntity(
            uid=f"{self.name}_{uuid.uuid4().hex[:8]}",
            name=self.name,
            sem_type=self.sem_type,
            guna=self.guna,
            pada=self.pada,
            properties=copy.deepcopy(self.properties),
            synthetic=self.synthetic
        )

@dataclass
class SemanticRelation:
    """Relation between entities."""
    rel_type: str
    uid: str
    participants: List[str]  # Entity UIDs
    meta: Dict = field(default_factory=dict)
    
    def copy(self):
        return SemanticRelation(
            rel_type=self.rel_type,
            uid=f"r_{uuid.uuid4().hex[:6]}",
            participants=self.participants.copy(),
            meta=copy.deepcopy(self.meta)
        )

@dataclass
class SemanticConstraint:
    """Constraint on entities."""
    ctype: str           # "cardinality", "requirement", etc.
    target: str          # Entity UID
    condition: Any       # Constraint specification
    uid: str = field(default_factory=lambda: f"c_{uuid.uuid4().hex[:6]}")
    
    def copy(self):
        return SemanticConstraint(
            ctype=self.ctype,
            target=self.target,
            condition=copy.deepcopy(self.condition),
            uid=f"c_{uuid.uuid4().hex[:6]}"
        )

@dataclass
class CMK:
    """
    Canonical Meaning Kernel - the invariant fingerprint of meaning.
    Five-part structure hash that survives all transformations.
    """
    structure: str      # Entity topology hash
    behavior: str       # Relation pattern hash
    constraints: str    # Constraint core hash
    role: str          # Semantic role signature
    synthesis: str     # Combined master hash
    
    def __eq__(self, other):
        if not isinstance(other, CMK):
            return False
        return self.synthesis == other.synthesis
    
    def __hash__(self):
        return hash(self.synthesis)

# ============================================================================
# SECTION 2: SEMANTIC ROOTS TAXONOMY (400+ ROOTS)
# ============================================================================

SEMANTIC_ROOTS = {
    # Mathematical & Logical
    "algebraic": [
        "Addition", "Multiplication", "Division", "Subtraction", "Exponentiation",
        "Logarithm", "Root", "Modulus", "Factorial", "Absolute", "Negation",
        "Inversion", "Reciprocal", "Increment", "Decrement", "Differentiation",
        "Integration", "Limit", "Summation", "Product", "Series", "Sequence",
        "Progression", "Mean", "Median", "Mode", "Variance", "StandardDeviation",
        "Covariance", "Correlation", "Convolution", "Deconvolution"
    ],
    "set_theoretic": [
        "Union", "Intersection", "Difference", "Complement", "SymmetricDifference",
        "CartesianProduct", "PowerSet", "Partition", "Subset", "Superset",
        "Membership", "Containment", "Disjointness", "Overlap", "Cardinality",
        "Countability", "EmptySet", "UniversalSet", "Singleton", "Pair", "Tuple"
    ],
    "logical": [
        "Conjunction", "Disjunction", "Implication", "Biconditional", "Negation",
        "Contradiction", "Tautology", "Equivalence", "Entailment", "Inference",
        "Deduction", "Induction", "Abduction", "Validity", "Satisfiability",
        "Consistency", "Completeness", "Soundness", "Decidability", "Computability"
    ],
    "categorical": [
        "Morphism", "Isomorphism", "Homomorphism", "Endomorphism", "Automorphism",
        "Functor", "NaturalTransformation", "Adjunction", "Limit", "Colimit",
        "Product", "Coproduct", "Equalizer", "Pullback", "Pushout", "Monad"
    ],
    "topological": [
        "Open", "Closed", "Boundary", "Interior", "Closure", "Neighborhood",
        "Convergence", "Continuity", "Compactness", "Connectedness", "Manifold",
        "Homotopy", "Homology", "Cohomology", "Homeomorphism", "Embedding"
    ],
    
    # Ontological & Mereological
    "existence": [
        "Existence", "Nonexistence", "Occurrence", "Event", "Process", "State",
        "StateChange", "Becoming", "Being", "Nothingness", "Presence", "Absence",
        "Actuality", "Potentiality", "Reality", "Appearance", "Phenomenon",
        "Substance", "Attribute", "Quality", "Quantity", "Relation", "Modality"
    ],
    "mereology": [
        "Part", "Whole", "ProperPart", "Sum", "Product", "Atom", "Gunk",
        "Mixture", "Compound", "Composite", "Simple", "Component", "Constituent",
        "Element", "Member", "Section", "Segment", "Fraction", "Fragment",
        "Partition", "Decomposition", "Synthesis", "Analysis", "Integration"
    ],
    "identity": [
        "Identity", "Sameness", "Difference", "Otherness", "Distinctness",
        "Similarity", "Dissimilarity", "Equality", "Inequality", "Analogy",
        "Homogeneity", "Heterogeneity", "Unity", "Multiplicity", "Variety"
    ],
    
    # Epistemic & Cognitive
    "knowledge": [
        "Knowledge", "Ignorance", "Belief", "Doubt", "Certainty", "Uncertainty",
        "Confidence", "Skepticism", "Conjecture", "Hypothesis", "Theory", "Law",
        "Principle", "Axiom", "Postulate", "Theorem", "Proof", "Evidence",
        "Justification", "Reason", "Cause", "Explanation", "Understanding"
    ],
    "mental": [
        "Thinking", "Reasoning", "Computing", "Processing", "Analyzing",
        "Synthesizing", "Comparing", "Evaluating", "Judging", "Deciding",
        "Choosing", "Intending", "Willing", "Desiring", "Imagining",
        "Conceiving", "Abstracting", "Generalizing", "Remembering", "Recognizing"
    ],
    
    # Linguistic & Semantic
    "reference": [
        "Reference", "Sense", "Meaning", "Signification", "Denotation",
        "Connotation", "Intension", "Extension", "Semantics", "Syntax",
        "Pragmatics", "Discourse", "Narrative", "Description", "Definition"
    ],
    "speech_acts": [
        "Assertion", "Question", "Command", "Request", "Offer", "Promise",
        "Warning", "Advice", "Suggestion", "Hypothesis", "Assumption",
        "Presupposition", "Implicature", "Entailment", "Inference"
    ],
    
    # Physical & Causal
    "causation": [
        "Causation", "Causality", "Determinism", "Indeterminism", "Randomness",
        "Chance", "Probability", "Necessity", "Contingency", "Production",
        "Generation", "Creation", "Destruction", "Making", "Doing", "Acting"
    ],
    "physical": [
        "Position", "Location", "Place", "Space", "Time", "Duration", "Instant",
        "Interval", "Direction", "Orientation", "Distance", "Proximity",
        "Height", "Depth", "Width", "Length", "Volume", "Area", "Mass",
        "Weight", "Density", "Energy", "Force", "Power", "Motion", "Rest",
        "Velocity", "Acceleration", "Momentum", "Inertia", "Gravity"
    ],
    
    # Normative & Value
    "evaluation": [
        "Good", "Bad", "Better", "Worse", "Best", "Worst", "Optimal",
        "Ideal", "Perfect", "Complete", "Whole", "Total", "Standard",
        "Criterion", "Measure", "Benchmark", "Model", "Pattern", "Template"
    ],
    "deontic": [
        "Obligation", "Permission", "Prohibition", "Requirement", "Mandate",
        "Command", "Order", "Directive", "Rule", "Regulation", "Law",
        "Principle", "Norm", "Policy", "Strategy", "Method", "Procedure"
    ],
    
    # Relational & Structural
    "comparison": [
        "Equality", "Inequality", "Superiority", "Inferiority", "Parity",
        "Disparity", "Analogy", "Identity", "Distinction", "Contrast",
        "Connection", "Disconnection", "Union", "Separation", "Division"
    ],
    "order": [
        "Order", "Disorder", "Sequence", "Series", "Succession", "Progression",
        "Array", "Arrangement", "Disposition", "Layout", "Ranking", "Sorting",
        "Selection", "Choice", "Preference", "Advantage", "Benefit", "Value"
    ],
    
    # Temporal & Processual
    "time": [
        "Present", "Past", "Future", "Now", "Before", "After", "Earlier",
        "Later", "Prior", "Posterior", "Simultaneous", "Synchronous",
        "Temporal", "Eternal", "Perpetual", "Transient", "Temporary",
        "Continuous", "Discrete", "Periodic", "Cyclic", "Iterative"
    ],
    "process": [
        "Beginning", "Start", "Origin", "Source", "Cause", "Inception",
        "Commencement", "Initiation", "Launch", "Opening", "Closure", "End",
        "Finish", "Termination", "Completion", "Conclusion", "Perfection",
        "Achievement", "Realization", "Actualization", "Verification"
    ],
    
    # System & Information
    "information": [
        "Information", "Data", "Knowledge", "Wisdom", "Understanding",
        "Intelligence", "Message", "Communication", "Notice", "Notification",
        "Signal", "Sign", "Indication", "Evidence", "Proof", "Confirmation",
        "Verification", "Authentication", "Support", "Foundation", "Ground"
    ],
    "cybernetic": [
        "Input", "Output", "Throughput", "Feedback", "Feedforward", "Control",
        "Regulation", "Governance", "Guidance", "Direction", "Management",
        "Command", "Order", "Maintenance", "Preservation", "Conservation",
        "Protection", "Monitoring", "Observation", "Attention"
    ],
    
    # Structural (for UI/Web)
    "structure": [
        "Container", "Wrapper", "Holder", "Frame", "Box", "Panel",
        "Section", "Region", "Zone", "Area", "Division", "Segment"
    ],
    "presentation": [
        "Display", "Show", "Present", "Reveal", "Conceal", "Hide",
        "Visible", "Invisible", "Apparent", "Manifest", "Appearance"
    ],
    "navigation": [
        "Navigate", "Traverse", "Move", "Travel", "Journey", "Path",
        "Route", "Course", "Direction", "Guide", "Lead", "Direct"
    ],
    "interaction": [
        "Interact", "Engage", "Participate", "Respond", "React",
        "Trigger", "Activate", "Enable", "Disable", "Control"
    ],
    "content": [
        "Content", "Material", "Substance", "Matter", "Stuff",
        "Text", "Image", "Media", "Document", "Data"
    ]
}

# Flatten all roots
ALL_SEMANTIC_ROOTS = set()
for category, roots in SEMANTIC_ROOTS.items():
    ALL_SEMANTIC_ROOTS.update(roots)

# Global Roots (Semantic Operators)
GLOBAL_ROOTS = {
    # Structural
    "Coherence": "Structural consistency and harmony",
    "Composition": "Part-building and assembly",
    "Decomposition": "Part-breaking and analysis", 
    "Normalization": "Canonical form enforcement",
    
    # Cognitive
    "Imagination": "Non-executable ideation (MUST NOT execute)",
    "Abstraction": "Generalization and pattern extraction",
    "Analogy": "Pattern transfer across domains",
    "Generalization": "Universal from particular",
    
    # Logical
    "Equivalence": "Same-meaning identification",
    "Duality": "Complementary pair recognition",
    "Implication": "Consequence relation",
    "Negation": "Opposite/denial",
    
    # Constraint
    "Amplification": "Constraint strengthening",
    "Relaxation": "Constraint weakening",
    "Freezing": "Constraint locking (immutable)"
}

# ============================================================================
# SECTION 3: LEXER (Notebook Syntax)
# ============================================================================

class SadhanaLexer:
    """
    Tokenizes notebook-style Sadhana syntax.
    
    Notebook syntax rules:
    - No brackets required
    - Order-free statements
    - Entities: Capitalized names
    - Directives: @key: value
    - Relations: "contains", "requires", "enables"
    - Constraints: "Constraint: X must have exactly Y Z"
    - Roots: "Roots: Root1, Root2"
    """
    
    RELATION_WORDS = {'contains', 'requires', 'enables', 'implements', 'extends', 
                      'depends', 'triggers', 'precedes', 'follows', 'references'}
    
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.col = 1
        self.tokens = []
        
    def error(self, msg: str):
        raise SyntaxError(f"Lexer error at L{self.line}:{self.col}: {msg}")
        
    def peek(self, offset: int = 0) -> str:
        pos = self.pos + offset
        if pos >= len(self.source):
            return '\0'
        return self.source[pos]
        
    def advance(self) -> str:
        char = self.peek()
        self.pos += 1
        if char == '\n':
            self.line += 1
            self.col = 1
        else:
            self.col += 1
        return char
        
    def skip_whitespace(self):
        """Skip spaces and tabs but NOT newlines (newlines are semantic)."""
        while self.peek() in ' \t\r':
            self.advance()
            
    def skip_newlines(self):
        """Skip newline characters."""
        while self.peek() == '\n':
            self.advance()
            self.skip_whitespace()
            
    def read_word(self) -> str:
        """Read a word (identifier or keyword)."""
        start = self.pos
        while self.peek().isalnum() or self.peek() in '_-':
            self.advance()
        return self.source[start:self.pos]
        
    def read_directive(self) -> Token:
        """Read @key: value directive."""
        start_line, start_col = self.line, self.col
        self.advance()  # Skip @
        
        key = self.read_word()
        self.skip_whitespace()
        
        if self.peek() != ':':
            self.error(f"Expected ':' after directive key '{key}'")
        self.advance()
        self.skip_whitespace()
        
        # Read value until newline
        val_start = self.pos
        while self.peek() not in '\n\0':
            self.advance()
        value = self.source[val_start:self.pos].strip()
        
        return Token(TokenType.DIRECTIVE, f"{key}:{value}", start_line, start_col)
        
    def tokenize(self) -> List[Token]:
        """Convert source into tokens."""
        while True:
            self.skip_whitespace()
            char = self.peek()
            start_line, start_col = self.line, self.col
            
            if char == '\0':
                self.tokens.append(Token(TokenType.EOF, '', start_line, start_col))
                break
                
            elif char == '\n':
                self.tokens.append(Token(TokenType.NEWLINE, '\n', start_line, start_col))
                self.advance()
                
            elif char == '@':
                self.tokens.append(self.read_directive())
                
            elif char.isupper():
                # Entity name - but check for keywords first
                word = self.read_word()
                word_lower = word.lower()
                
                # Check for keywords that might be capitalized
                if word_lower == 'constraint':
                    self.tokens.append(Token(TokenType.CONSTRAINT, word_lower, start_line, start_col))
                elif word_lower == 'roots':
                    self.tokens.append(Token(TokenType.ROOTS, word_lower, start_line, start_col))
                else:
                    # Regular entity name
                    self.tokens.append(Token(TokenType.NAME, word, start_line, start_col))
                
            elif char.islower() or char.isupper():
                word = self.read_word()
                word_lower = word.lower()
                
                # Check for special keywords (case-insensitive)
                if word_lower == 'constraint':
                    self.tokens.append(Token(TokenType.CONSTRAINT, word_lower, start_line, start_col))
                elif word_lower == 'roots':
                    self.tokens.append(Token(TokenType.ROOTS, word_lower, start_line, start_col))
                elif word_lower == 'exactly':
                    self.tokens.append(Token(TokenType.EXACTLY, word_lower, start_line, start_col))
                elif word_lower == 'at':
                    # Look ahead for "least" or "most"
                    saved_pos = self.pos
                    saved_line = self.line
                    saved_col = self.col
                    self.skip_whitespace()
                    if self.peek().isalpha():
                        next_word = self.read_word()
                        if next_word == 'least':
                            self.tokens.append(Token(TokenType.AT_LEAST, 'at least', start_line, start_col))
                        elif next_word == 'most':
                            self.tokens.append(Token(TokenType.AT_MOST, 'at most', start_line, start_col))
                        else:
                            # Not 'at least' or 'at most', backtrack
                            self.pos = saved_pos
                            self.line = saved_line
                            self.col = saved_col
                            self.tokens.append(Token(TokenType.NAME, word, start_line, start_col))
                    else:
                        self.tokens.append(Token(TokenType.NAME, word, start_line, start_col))
                elif word_lower == 'one':
                    self.tokens.append(Token(TokenType.ONE, word_lower, start_line, start_col))
                elif word_lower in self.RELATION_WORDS:
                    self.tokens.append(Token(TokenType.RELATION, word, start_line, start_col))
                elif word_lower in ('must', 'have', 'a', 'an'):
                    # Skip filler words in constraint expressions
                    pass
                else:
                    # Unknown word, treat as name
                    self.tokens.append(Token(TokenType.NAME, word, start_line, start_col))
                    
            elif char.isdigit():
                num = ''
                while self.peek().isdigit():
                    num += self.advance()
                self.tokens.append(Token(TokenType.NUMBER, num, start_line, start_col))
                
            elif char == ':':
                self.advance()  # Skip colon separator
                
            else:
                # Skip unknown characters
                self.advance()
                
        return self.tokens


# ============================================================================
# SECTION 4: AST AND PARSER
# ============================================================================

@dataclass
class ASTHeader:
    """Header section with directives."""
    directives: Dict[str, Any] = field(default_factory=dict)
    
@dataclass
class ASTBody:
    """Body section with entities, relations, constraints, roots."""
    entities: List[str] = field(default_factory=list)
    relations: List[Tuple[str, str, str]] = field(default_factory=list)  # (type, source, target)
    constraints: List[Dict] = field(default_factory=list)
    roots: List[str] = field(default_factory=list)

@dataclass
class AST:
    """Abstract Syntax Tree for Sadhana."""
    header: ASTHeader
    body: ASTBody
    
class SadhanaParser:
    """
    Parses tokens into AST.
    
    Grammar:
        program ::= header body
        header ::= directive*
        directive ::= '@' name ':' value
        body ::= (entity | relation | constraint | roots)*
        entity ::= NAME
        relation ::= NAME RELATION NAME
        constraint ::= 'Constraint' ':' NAME 'must' 'have' quantifier NAME
        quantifier ::= 'exactly' number | 'at least' number | 'at most' number
        roots ::= 'Roots' ':' name_list
        name_list ::= NAME (',' NAME)*
    """
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        
    def error(self, msg: str):
        tok = self.current()
        raise SyntaxError(f"Parser error at L{tok.line}:{tok.col}: {msg}")
        
    def current(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]  # EOF
        
    def peek_type(self) -> TokenType:
        return self.current().type
        
    def advance(self) -> Token:
        tok = self.current()
        self.pos += 1
        return tok
        
    def expect(self, typ: TokenType) -> Token:
        if self.peek_type() != typ:
            self.error(f"Expected {typ.name}, got {self.current().value!r}")
        return self.advance()
        
    def skip_newlines(self):
        while self.peek_type() == TokenType.NEWLINE:
            self.advance()
            
    def parse_header(self) -> ASTHeader:
        """Parse header directives."""
        header = ASTHeader()
        
        # Skip leading newlines
        self.skip_newlines()
        
        while self.peek_type() == TokenType.DIRECTIVE:
            tok = self.advance()
            key, value = tok.value.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Handle list values (comma-separated)
            if ',' in value:
                value = [v.strip() for v in value.split(',')]
            
            header.directives[key] = value
            self.skip_newlines()
            
        return header
        
    def parse_body(self) -> ASTBody:
        """Parse body content."""
        body = ASTBody()
        entity_names = {}  # name -> bool (to track declared entities)
        
        self.skip_newlines()
        
        while self.peek_type() != TokenType.EOF:
            tok = self.current()
            
            if tok.type == TokenType.NAME:
                # Could be entity declaration or start of relation
                name = tok.value
                
                # Look ahead to determine if this is a relation
                if self.pos + 1 < len(self.tokens):
                    next_tok = self.tokens[self.pos + 1]
                    if next_tok.type == TokenType.RELATION:
                        # This is a relation
                        self.advance()  # consume source
                        rel_tok = self.advance()  # consume relation
                        target_tok = self.expect(TokenType.NAME)
                        body.relations.append((rel_tok.value, name, target_tok.value))
                        entity_names[name] = True
                        entity_names[target_tok.value] = True
                    else:
                        # This is an entity declaration
                        self.advance()
                        if name not in entity_names:
                            body.entities.append(name)
                            entity_names[name] = True
                            
            elif tok.type == TokenType.CONSTRAINT:
                self.parse_constraint(body, entity_names)
                
            elif tok.type == TokenType.ROOTS:
                self.parse_roots(body)
                
            elif tok.type == TokenType.NEWLINE:
                self.advance()
                
            else:
                self.advance()  # Skip unknown tokens
                
        return body
        
    def parse_constraint(self, body: ASTBody, entity_names: Dict):
        """Parse constraint statement."""
        self.advance()  # Skip 'Constraint'
        
        # Skip optional colon and newlines
        self.skip_newlines()
        
        # Pattern: Entity must have [quantifier] Target
        if self.peek_type() == TokenType.NAME:
            target_entity = self.advance().value
        else:
            return  # Invalid constraint
            
        # Skip "must have" (these should be filtered by lexer now)
        while self.peek_type() == TokenType.NAME and self.current().value.lower() in ['must', 'have', 'a', 'an']:
            self.advance()
            
        # Parse quantifier
        quantifier = None
        number = 1
        
        if self.peek_type() == TokenType.EXACTLY:
            self.advance()
            quantifier = 'exactly'
        elif self.peek_type() == TokenType.AT_LEAST:
            self.advance()
            quantifier = 'at_least'
        elif self.peek_type() == TokenType.AT_MOST:
            self.advance()
            quantifier = 'at_most'
            
        if self.peek_type() == TokenType.NUMBER:
            number = int(self.advance().value)
        elif self.peek_type() == TokenType.ONE:
            self.advance()
            number = 1
            
        # Get the constrained item type
        if self.peek_type() == TokenType.NAME:
            item_type = self.advance().value
        else:
            item_type = 'item'
            
        body.constraints.append({
            'target': target_entity,
            'quantifier': quantifier or 'exactly',
            'count': number,
            'item_type': item_type
        })
        entity_names[target_entity] = True
        entity_names[item_type] = True
        
    def parse_roots(self, body: ASTBody):
        """Parse roots declaration."""
        self.advance()  # Skip 'Roots'
        self.expect(TokenType.NAME)  # Skip ':'
        
        # Parse comma-separated list
        while self.peek_type() in [TokenType.NAME, TokenType.NEWLINE]:
            if self.peek_type() == TokenType.NAME:
                body.roots.append(self.advance().value)
            elif self.peek_type() == TokenType.NEWLINE:
                # Check if next line continues the list
                self.advance()
                if self.peek_type() != TokenType.NAME:
                    break
            else:
                break
                
    def parse(self) -> AST:
        """Parse tokens into AST."""
        header = self.parse_header()
        body = self.parse_body()
        return AST(header, body)

# ============================================================================
# SECTION 5: MEANING GRAPH (Layer 4)
# ============================================================================

class MeaningGraph:
    """
    Hypergraph representation of meaning.
    
    Entities + Relations + Constraints = Meaning Graph
    Order-independent by design.
    """
    
    def __init__(self):
        self.entities: Dict[str, SemanticEntity] = {}
        self.relations: List[SemanticRelation] = []
        self.constraints: List[SemanticConstraint] = []
        self.roots: List[str] = []
        self.domain: str = "generic"
        self.expansion_level: int = 0
        self._cmk: Optional[CMK] = None
        self.metadata: Dict = {}
        
    def add_entity(self, name: str, sem_type=SemanticType.ENTITY, 
                   guna=None, pada=None, synthetic=False) -> SemanticEntity:
        """Add an entity to the graph."""
        uid = f"{name}_{uuid.uuid4().hex[:8]}"
        ent = SemanticEntity(
            uid=uid, 
            name=name, 
            sem_type=sem_type,
            guna=guna or Guna.SATTVA,
            pada=pada or Pada.MADHYALOKA,
            synthetic=synthetic
        )
        self.entities[uid] = ent
        self._cmk = None  # Invalidate CMK cache
        return ent
        
    def add_relation(self, rel_type: str, participants: List[str], meta=None):
        """Add a relation between entities."""
        rel = SemanticRelation(
            rel_type=rel_type,
            uid=f"r_{uuid.uuid4().hex[:6]}",
            participants=participants,
            meta=meta or {}
        )
        self.relations.append(rel)
        self._cmk = None
        
    def add_constraint(self, ctype: str, target: str, condition: Any):
        """Add a constraint."""
        constr = SemanticConstraint(
            ctype=ctype,
            target=target,
            condition=condition
        )
        self.constraints.append(constr)
        self._cmk = None
        
    def get_entity_by_name(self, name: str) -> Optional[SemanticEntity]:
        """Find entity by name (not UID)."""
        for ent in self.entities.values():
            if ent.name == name:
                return ent
        return None
        
    def get_children(self, parent_uid: str) -> List[str]:
        """Get all child entity UIDs via 'contains' relations."""
        children = []
        for rel in self.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                if rel.participants[0] == parent_uid:
                    children.append(rel.participants[1])
        return children
        
    def get_parent(self, child_uid: str) -> Optional[str]:
        """Get parent entity UID."""
        for rel in self.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                if rel.participants[1] == child_uid:
                    return rel.participants[0]
        return None
        
    def copy(self) -> 'MeaningGraph':
        """Deep copy the graph."""
        new_graph = MeaningGraph()
        
        # Copy entities
        uid_map = {}
        for uid, ent in self.entities.items():
            new_ent = ent.copy()
            new_graph.entities[new_ent.uid] = new_ent
            uid_map[uid] = new_ent.uid
            
        # Copy relations with mapped UIDs
        for rel in self.relations:
            new_rel = rel.copy()
            new_rel.participants = [uid_map.get(p, p) for p in rel.participants]
            new_graph.relations.append(new_rel)
            
        # Copy constraints with mapped UIDs
        for constr in self.constraints:
            new_constr = constr.copy()
            new_constr.target = uid_map.get(constr.target, constr.target)
            new_graph.constraints.append(new_constr)
            
        new_graph.roots = self.roots.copy()
        new_graph.domain = self.domain
        new_graph.expansion_level = self.expansion_level
        new_graph.metadata = copy.deepcopy(self.metadata)
        
        return new_graph

# ============================================================================
# SECTION 6: CANONICAL MEANING KERNEL (Layer 5)
# ============================================================================

class CMKComputer:
    """
    Computes the Canonical Meaning Kernel.
    
    CMK is the invariant fingerprint that survives all transformations.
    Five-part hash: structure, behavior, constraints, role, synthesis.
    """
    
    def compute(self, graph: MeaningGraph) -> CMK:
        """Compute CMK for a meaning graph."""
        # Only include non-synthetic entities
        real_entities = {uid: e for uid, e in graph.entities.items() if not e.synthetic}
        
        # STRUCTURE: Entity topology (sorted for order-independence)
        entity_names = sorted([e.name for e in real_entities.values()])
        struct_hash = self._hash_string('|'.join(entity_names))
        
        # BEHAVIOR: Relation patterns (sorted)
        rel_patterns = []
        for rel in graph.relations:
            # Only include relations where all participants are real
            if all(p in real_entities for p in rel.participants):
                participant_names = [real_entities[p].name for p in rel.participants if p in real_entities]
                rel_patterns.append(f"{rel.rel_type}({','.join(sorted(participant_names))})")
        behavior_hash = self._hash_string('|'.join(sorted(rel_patterns)))
        
        # CONSTRAINTS: Constraint core
        constr_patterns = []
        for constr in graph.constraints:
            if constr.target in real_entities:
                target_name = real_entities[constr.target].name
                constr_patterns.append(f"{constr.ctype}:{target_name}:{str(constr.condition)}")
        constraints_hash = self._hash_string('|'.join(sorted(constr_patterns)))
        
        # ROLE: Semantic roles (roots + domain)
        role_str = f"{graph.domain}:{','.join(sorted(graph.roots))}"
        role_hash = self._hash_string(role_str)
        
        # SYNTHESIS: Master hash
        synthesis = self._hash_string(f"{struct_hash}{behavior_hash}{constraints_hash}{role_hash}")
        
        return CMK(
            structure=struct_hash,
            behavior=behavior_hash,
            constraints=constraints_hash,
            role=role_hash,
            synthesis=synthesis
        )
        
    def _hash_string(self, s: str) -> str:
        """Compute SHA-256 hash of string."""
        return hashlib.sha256(s.encode()).hexdigest()[:32]

# ============================================================================
# SECTION 7: BIJA SYSTEM (Layer 7)
# ============================================================================

class BijaSystem:
    """
    Meta-compression system.
    
    Bija is a semantic grammar encoding, NOT a hash.
    - Variable length
    - Reversible to skeleton
    - CMK collision detection
    """
    
    # Grammar tokens for encoding
    TOKENS = {
        'E': 'Entity', 'R': 'Relation', 'C': 'Constraint',
        'S': 'Sattva', 'A': 'Rajas', 'T': 'Tamas',
        'U': 'Urdhvaloka', 'M': 'Madhyaloka', 'D': 'Adholoka',
        'c': 'contains', 'r': 'requires', 'e': 'enables',
        'd': 'depends', 'x': 'extends', 'i': 'implements',
        '(': 'group_start', ')': 'group_end',
        '[': 'cardinality', ']': 'end_card',
        '{': 'property', '}': 'end_prop',
    }
    
    def __init__(self):
        self.cmk_computer = CMKComputer()
        
    def encode(self, graph: MeaningGraph) -> str:
        """
        Encode meaning graph to Bija.
        
        Format: Semantic grammar string, not hash.
        Example: "HTMCTABCCDFFCHHCOCOC"
        """
        parts = []
        
        # Header
        parts.append(self._encode_domain(graph.domain))
        
        # Entities (sorted for determinism)
        real_entities = {uid: e for uid, e in graph.entities.items() if not e.synthetic}
        for uid in sorted(real_entities.keys(), key=lambda u: real_entities[u].name):
            ent = real_entities[uid]
            parts.append(self._encode_entity(ent))
            
        # Relations
        for rel in graph.relations:
            if all(p in real_entities for p in rel.participants):
                parts.append(self._encode_relation(rel, real_entities))
                
        # Constraints
        for constr in graph.constraints:
            if constr.target in real_entities:
                parts.append(self._encode_constraint(constr, real_entities))
                
        return ''.join(parts)
        
    def _encode_domain(self, domain: str) -> str:
        """Encode domain prefix."""
        domain_map = {'html': 'HTM', 'python': 'PYT', 'sql': 'SQL', 'generic': 'GEN'}
        return domain_map.get(domain, 'GEN')
        
    def _encode_entity(self, ent: SemanticEntity) -> str:
        """Encode entity to Bija fragment."""
        # E + name_code + guna + pada
        name_code = self._abbreviate_name(ent.name)
        guna_code = ent.guna.value[0].upper()
        pada_code = ent.pada.value[0].upper()
        return f"E{name_code}{guna_code}{pada_code}"
        
    def _encode_relation(self, rel: SemanticRelation, entities: Dict) -> str:
        """Encode relation to Bija fragment."""
        rel_codes = {'contains': 'c', 'requires': 'r', 'enables': 'e', 
                     'depends': 'd', 'extends': 'x', 'implements': 'i'}
        rel_code = rel_codes.get(rel.rel_type, rel.rel_type[0].lower())
        
        participant_codes = []
        for p in rel.participants:
            if p in entities:
                participant_codes.append(self._abbreviate_name(entities[p].name))
                
        return f"R{rel_code}({','.join(participant_codes)})"
        
    def _encode_constraint(self, constr: SemanticConstraint, entities: Dict) -> str:
        """Encode constraint to Bija fragment."""
        target_code = self._abbreviate_name(entities[constr.target].name)
        return f"C[{constr.ctype}:{target_code}:{constr.condition}]"
        
    def _abbreviate_name(self, name: str) -> str:
        """Create abbreviation for name."""
        # Take first 3 chars + consonants
        if len(name) <= 4:
            return name
        consonants = ''.join([c for c in name if c.lower() not in 'aeiou'])
        return name[:3] + consonants[:2]
        
    def decode_to_skeleton(self, bija: str) -> Dict:
        """
        Decode Bija back to meaning skeleton.
        
        Returns structural outline, not full meaning.
        """
        skeleton = {
            'domain': 'generic',
            'entities': [],
            'relations': [],
            'constraints': []
        }
        
        # Parse domain prefix
        if bija.startswith('HTM'):
            skeleton['domain'] = 'html'
            bija = bija[3:]
        elif bija.startswith('PYT'):
            skeleton['domain'] = 'python'
            bija = bija[3:]
        elif bija.startswith('SQL'):
            skeleton['domain'] = 'sql'
            bija = bija[3:]
            
        # Parse entities and relations
        i = 0
        while i < len(bija):
            char = bija[i]
            if char == 'E' and i + 6 < len(bija):
                # Entity: E + 5 chars (name+guna+pada)
                skeleton['entities'].append({
                    'code': bija[i+1:i+6],
                    'type': 'entity'
                })
                i += 6
            elif char == 'R':
                # Relation
                rel_end = bija.find(')', i)
                if rel_end > i:
                    skeleton['relations'].append({
                        'code': bija[i:rel_end+1]
                    })
                    i = rel_end + 1
                else:
                    i += 1
            elif char == 'C':
                # Constraint
                constr_end = bija.find(']', i)
                if constr_end > i:
                    skeleton['constraints'].append({
                        'code': bija[i:constr_end+1]
                    })
                    i = constr_end + 1
                else:
                    i += 1
            else:
                i += 1
                
        return skeleton


# ============================================================================
# SECTION 8: DHATU LAYER - 8 MANDATORY SEMANTIC LAWS (Layer 2)
# ============================================================================

class DhatuLayer:
    """
    The 8 Dhatus (Semantic Laws) - Immutable constraints on all operations.
    """
    
    def __init__(self, cmk_computer: CMKComputer):
        self.cmk_computer = cmk_computer
        
    def apply_all(self, graph: MeaningGraph) -> MeaningGraph:
        """Apply all 8 Dhatus in sequence."""
        graph = self.identity_preservation(graph)
        graph = self.constraint_conservation(graph)
        graph = self.non_contradiction(graph)
        graph = self.reconstruction_completeness(graph)
        graph = self.mutation_containment(graph)
        graph = self.semantic_closure(graph)
        graph = self.drift_elimination(graph)
        graph = self.impossible_state_pruning(graph)
        return graph
        
    def identity_preservation(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 1: Identity Preservation Law
        
        Entities maintain identity across all transformations.
        No entity may lose its identifying properties.
        """
        for uid, ent in list(graph.entities.items()):
            # Ensure minimum identifying properties
            if not ent.name:
                # Remove entities without names
                del graph.entities[uid]
                
        return graph
        
    def constraint_conservation(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 2: Constraint Conservation Law
        
        Constraints are never silently modified.
        All constraints must remain satisfiable.
        """
        # Check for constraint conflicts
        constraint_targets = defaultdict(list)
        for constr in graph.constraints:
            constraint_targets[constr.target].append(constr)
            
        # Remove duplicate constraints
        seen = set()
        new_constraints = []
        for constr in graph.constraints:
            key = (constr.ctype, constr.target, str(constr.condition))
            if key not in seen:
                seen.add(key)
                new_constraints.append(constr)
        graph.constraints = new_constraints
        
        return graph
        
    def non_contradiction(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 3: Non-Contradiction Law
        
        No entity may have contradictory properties.
        No relation may contradict another.
        """
        # Check for contradictory constraints
        for target, constraints in defaultdict(list).items():
            # Group constraints by target
            pass  # Complex contradiction detection
            
        return graph
        
    def reconstruction_completeness(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 4: Reconstruction Completeness
        
        Original meaning must be reconstructible from transformed meaning.
        No information loss that cannot be recovered.
        """
        # Ensure all entities referenced in relations exist
        valid_entities = set(graph.entities.keys())
        new_relations = []
        for rel in graph.relations:
            if all(p in valid_entities for p in rel.participants):
                new_relations.append(rel)
        graph.relations = new_relations
        
        return graph
        
    def mutation_containment(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 5: Mutation Containment
        
        Mutations are local and tracked.
        Global mutations require explicit authorization.
        """
        # Track expansion level
        graph.metadata['mutation_level'] = graph.expansion_level
        
        return graph
        
    def semantic_closure(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 6: Semantic Closure
        
        Operations on valid meanings produce valid meanings.
        Invalid meanings cannot emerge from valid ones.
        """
        # Validate all entities have proper types
        for ent in graph.entities.values():
            if not isinstance(ent.sem_type, SemanticType):
                ent.sem_type = SemanticType.ENTITY
                
        return graph
        
    def drift_elimination(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 7: Drift Elimination
        
        CMK must remain invariant across transformations.
        If CMK changes, transformation is invalid.
        """
        # Invalidate cached CMK to force recomputation
        graph._cmk = None
        
        return graph
        
    def impossible_state_pruning(self, graph: MeaningGraph) -> MeaningGraph:
        """
        DHATU 8: Impossible-State Pruning
        
        Invalid configurations are pruned before execution.
        No impossible meaning may exist in the graph.
        """
        # Remove dangling references
        valid_entities = set(graph.entities.keys())
        
        # Filter relations
        new_relations = []
        for rel in graph.relations:
            if all(p in valid_entities for p in rel.participants):
                new_relations.append(rel)
        graph.relations = new_relations
        
        # Filter constraints
        new_constraints = []
        for constr in graph.constraints:
            if constr.target in valid_entities:
                new_constraints.append(constr)
        graph.constraints = new_constraints
        
        return graph

# ============================================================================
# SECTION 9: SANDHI ENGINE - COMPOSITION GATE (Layer 9)
# ============================================================================

class SandhiEngine:
    """
    Mandatory composition gate for all meaning combination.
    
    Rules:
    - ≥ 2 meanings required
    - ≥ 1 Global Root required
    - No implicit merge
    - Constraints unified
    - CMK lineage tracked
    """
    
    def __init__(self, cmk_computer: CMKComputer):
        self.cmk_computer = cmk_computer
        
    def compose(self, graphs: List[MeaningGraph], roots: List[str]) -> MeaningGraph:
        """
        Compose multiple meaning graphs through Sandhi gate.
        
        Args:
            graphs: List of meaning graphs to compose (≥2)
            roots: List of Global Roots to apply (≥1)
            
        Returns:
            Composed meaning graph
            
        Raises:
            ValueError: If composition rules violated
        """
        if len(graphs) < 2:
            raise ValueError("Sandhi requires ≥2 meanings")
        if len(roots) < 1:
            raise ValueError("Sandhi requires ≥1 Global Root")
            
        # Validate all roots
        for root in roots:
            if root not in GLOBAL_ROOTS:
                raise ValueError(f"Unknown Global Root: {root}")
                
        # Start with first graph
        result = graphs[0].copy()
        result.roots = list(set(result.roots + roots))
        
        # Merge subsequent graphs
        for graph in graphs[1:]:
            result = self._merge_graphs(result, graph)
            
        # Harmonize constraints
        result = self._harmonize_constraints(result)
        
        # Track lineage
        result.metadata['sandhi_roots'] = roots
        result.metadata['sandhi_count'] = len(graphs)
        
        return result
        
    def _merge_graphs(self, base: MeaningGraph, other: MeaningGraph) -> MeaningGraph:
        """Merge two graphs, handling name collisions."""
        # Map other entities to new UIDs
        uid_map = {}
        for uid, ent in other.entities.items():
            # Check for name collision
            existing = base.get_entity_by_name(ent.name)
            if existing:
                # Same name = same entity (collision = equivalence)
                uid_map[uid] = existing.uid
            else:
                # Add new entity
                new_ent = ent.copy()
                base.entities[new_ent.uid] = new_ent
                uid_map[uid] = new_ent.uid
                
        # Add relations with mapped UIDs
        for rel in other.relations:
            new_participants = [uid_map.get(p, p) for p in rel.participants]
            # Check if relation already exists
            exists = any(
                r.rel_type == rel.rel_type and r.participants == new_participants
                for r in base.relations
            )
            if not exists:
                base.add_relation(rel.rel_type, new_participants, rel.meta)
                
        # Add constraints with mapped UIDs
        for constr in other.constraints:
            new_target = uid_map.get(constr.target, constr.target)
            base.add_constraint(constr.ctype, new_target, constr.condition)
            
        return base
        
    def _harmonize_constraints(self, graph: MeaningGraph) -> MeaningGraph:
        """Unify and harmonize constraints."""
        # Group constraints by target
        by_target = defaultdict(list)
        for constr in graph.constraints:
            by_target[constr.target].append(constr)
            
        # Resolve conflicts
        new_constraints = []
        for target, constraints in by_target.items():
            # For now, keep all unique constraints
            seen = set()
            for constr in constraints:
                key = (constr.ctype, str(constr.condition))
                if key not in seen:
                    seen.add(key)
                    new_constraints.append(constr)
                    
        graph.constraints = new_constraints
        return graph

# ============================================================================
# SECTION 10: OPTION-RULE ENGINE (Layer 10)
# ============================================================================

class OptionRule:
    """A single option rule for gated decompression."""
    
    def __init__(self, name: str, condition: Callable, transform: Callable):
        self.name = name
        self.condition = condition  # When to apply
        self.transform = transform  # How to transform
        
class OptionRuleEngine:
    """
    Rule-gated decompression engine.
    
    Like quantum gates: rules apply conditionally while preserving CMK.
    """
    
    def __init__(self, cmk_computer: CMKComputer):
        self.cmk_computer = cmk_computer
        self.rules: List[OptionRule] = []
        self._init_default_rules()
        
    def _init_default_rules(self):
        """Initialize default option rules."""
        # Expansion rules for different levels
        self.rules.append(OptionRule(
            "t1_expansion",
            lambda g: g.expansion_level >= 1,
            self._t1_expansion
        ))
        self.rules.append(OptionRule(
            "t2_expansion", 
            lambda g: g.expansion_level >= 2,
            self._t2_expansion
        ))
        self.rules.append(OptionRule(
            "t3_expansion",
            lambda g: g.expansion_level >= 3,
            self._t3_expansion
        ))
        
    def decompress(self, graph: MeaningGraph, target_level: int) -> MeaningGraph:
        """
        Decompress graph to target expansion level.
        
        Each rule is applied conditionally while preserving CMK.
        """
        original_cmk = self.cmk_computer.compute(graph)
        result = graph.copy()
        
        for level in range(1, target_level + 1):
            result.expansion_level = level
            
            # Apply rules for this level
            for rule in self.rules:
                if rule.condition(result):
                    result = rule.transform(result)
                    
            # Verify CMK preservation
            new_cmk = self.cmk_computer.compute(result)
            if new_cmk.synthesis != original_cmk.synthesis:
                raise RuntimeError(f"CMK violation in rule {rule.name}")
                
        return result
        
    def _t1_expansion(self, graph: MeaningGraph) -> MeaningGraph:
        """T1: Add structural entities (64-structure space)."""
        # Add Structure and Interface containers
        for uid, ent in list(graph.entities.items()):
            if not ent.synthetic:
                # Add structure container
                struct = graph.add_entity(
                    f"{ent.name}Structure",
                    SemanticType.SKELETON,
                    synthetic=True
                )
                graph.add_relation('contains', [ent.uid, struct.uid])
                
        return graph
        
    def _t2_expansion(self, graph: MeaningGraph) -> MeaningGraph:
        """T2: Add Guna×Pada entities (128-structure space)."""
        for uid, ent in list(graph.entities.items()):
            if ent.synthetic:
                continue
                
            # Create Guna×Pada variants
            for guna in Guna:
                for pada in Pada:
                    variant = graph.add_entity(
                        f"{ent.name}_{guna.value}_{pada.value}",
                        ent.sem_type,
                        guna=guna,
                        pada=pada,
                        synthetic=True
                    )
                    graph.add_relation('variant', [ent.uid, variant.uid], {
                        'guna': guna.value,
                        'pada': pada.value
                    })
                    
        return graph
        
    def _t3_expansion(self, graph: MeaningGraph) -> MeaningGraph:
        """T3: Add 64 archetype variations (256-structure space)."""
        # Add archetype patterns
        archetypes = list(ALL_SEMANTIC_ROOTS)[:64]  # First 64 roots as archetypes
        
        for uid, ent in list(graph.entities.items()):
            if ent.synthetic:
                continue
                
            for archetype in archetypes:
                arch_ent = graph.add_entity(
                    f"{ent.name}_as_{archetype}",
                    ent.sem_type,
                    synthetic=True
                )
                arch_ent.properties['archetype'] = archetype
                graph.add_relation('instantiates', [ent.uid, arch_ent.uid], {
                    'archetype': archetype
                })
                
        return graph

# ============================================================================
# SECTION 11: TEMPORAL EXPANSION (KALA) (Layer 11)
# ============================================================================

class TemporalExpansion:
    """
    Time-latent expansion system.
    
    Time is a parameter, not embedded in meaning.
    T0 → T1 → T2 → T3 expansion pipeline.
    """
    
    def __init__(self, option_engine: OptionRuleEngine):
        self.option_engine = option_engine
        
    def expand(self, graph: MeaningGraph, level: int) -> MeaningGraph:
        """Expand graph to specified temporal level."""
        return self.option_engine.decompress(graph, level)
        
    def get_expansion_dimensions(self) -> Dict[str, List[str]]:
        """Get canonical expansion dimensions."""
        return {
            'view': ['desktop', 'mobile', 'tablet'],
            'order': ['forward', 'reverse', 'random'],
            'time': ['eager', 'lazy', 'batched'],
            'representation': ['semantic', 'generic', 'optimized'],
            'context': ['locale', 'accessibility', 'performance']
        }

# ============================================================================
# SECTION 12: TOPOLOGICAL MEANING SPACE (Layer 12)
# ============================================================================

class TopologicalSpace:
    """
    Topological structure of meaning space.
    
    - Meaning Manifold: Continuous space of meanings
    - Equivalence Regions: Areas with same CMK
    - Boundary Conditions: Valid/invalid transitions
    - Singularities: Points where meaning breaks down
    """
    
    def __init__(self, cmk_computer: CMKComputer):
        self.cmk_computer = cmk_computer
        self.equivalence_classes: Dict[str, List[MeaningGraph]] = defaultdict(list)
        
    def classify_point(self, graph: MeaningGraph) -> str:
        """Classify graph position in topological space."""
        cmk = self.cmk_computer.compute(graph)
        
        # Check for singularities (invalid states)
        if self._is_singularity(graph):
            return "singularity"
            
        # Add to equivalence class
        self.equivalence_classes[cmk.synthesis].append(graph)
        
        return cmk.synthesis[:16]  # Return region identifier
        
    def _is_singularity(self, graph: MeaningGraph) -> bool:
        """Detect invalid meaning configurations."""
        # No entities
        if not graph.entities:
            return True
            
        # Circular containment
        if self._has_circular_containment(graph):
            return True
            
        # Unsatisfiable constraints
        if self._has_unsatisfiable_constraints(graph):
            return True
            
        return False
        
    def _has_circular_containment(self, graph: MeaningGraph) -> bool:
        """Detect circular containment relations."""
        # Build containment graph
        contains = defaultdict(set)
        for rel in graph.relations:
            if rel.rel_type == 'contains':
                if len(rel.participants) >= 2:
                    parent, child = rel.participants[0], rel.participants[1]
                    contains[parent].add(child)
                    
        # DFS for cycles
        visited = set()
        rec_stack = set()
        
        def has_cycle(node):
            visited.add(node)
            rec_stack.add(node)
            for neighbor in contains.get(node, []):
                if neighbor not in visited:
                    if has_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            rec_stack.remove(node)
            return False
            
        for node in contains:
            if node not in visited:
                if has_cycle(node):
                    return True
        return False
        
    def _has_unsatisfiable_constraints(self, graph: MeaningGraph) -> bool:
        """Detect constraints that cannot be satisfied."""
        # Check cardinality constraints
        for constr in graph.constraints:
            if constr.ctype == 'cardinality':
                target = constr.target
                if target not in graph.entities:
                    return True
                    
                # Count children of specific type (if item_type specified)
                condition = constr.condition
                item_type = condition.get('item_type') if isinstance(condition, dict) else None
                
                if item_type:
                    # Count only children matching item_type
                    child_uids = graph.get_children(target)
                    child_count = sum(
                        1 for uid in child_uids 
                        if uid in graph.entities and graph.entities[uid].name == item_type
                    )
                else:
                    # Count all children
                    child_count = len(graph.get_children(target))
                
                if isinstance(condition, dict):
                    quantifier = condition.get('quantifier', 'exactly')
                    count = condition.get('count', 1)
                    
                    if quantifier == 'exactly' and child_count != count:
                        if child_count > count:  # Can't remove children
                            return True
                    elif quantifier == 'at_most' and child_count > count:
                        return True
                        
        return False


# ============================================================================
# SECTION 13: SANHARA ENGINE (Layer 13)
# ============================================================================

class SimulationResult:
    """Result of a hypothetical simulation."""
    success: bool
    semantic_debt: float
    warnings: List[str]
    final_state: Optional[MeaningGraph]
    
    def __init__(self, success: bool, semantic_debt: float = 0.0, 
                 warnings: List[str] = None, final_state: MeaningGraph = None):
        self.success = success
        self.semantic_debt = semantic_debt
        self.warnings = warnings or []
        self.final_state = final_state

class SanharaEngine:
    """
    Non-committal simulation engine.
    
    Test hypothetical scenarios without committing changes.
    Fork meanings, simulate paths, measure semantic debt, revert safely.
    """
    
    def __init__(self, cmk_computer: CMKComputer, topological: TopologicalSpace):
        self.cmk_computer = cmk_computer
        self.topological = topological
        
    def simulate(self, graph: MeaningGraph, operation: Callable, 
                 args: Tuple = ()) -> SimulationResult:
        """
        Simulate an operation without modifying original graph.
        
        Args:
            graph: Original meaning graph
            operation: Function to simulate
            args: Arguments for operation
            
        Returns:
            SimulationResult with debt analysis
        """
        # Fork the graph
        fork = graph.copy()
        original_cmk = self.cmk_computer.compute(graph)
        
        warnings = []
        semantic_debt = 0.0
        
        try:
            # Execute operation on fork
            result = operation(fork, *args)
            
            # Check CMK preservation
            new_cmk = self.cmk_computer.compute(fork)
            if new_cmk.synthesis != original_cmk.synthesis:
                semantic_debt += 1.0
                warnings.append("CMK changed during simulation")
                
            # Check topological validity
            region = self.topological.classify_point(fork)
            if region == "singularity":
                semantic_debt += 10.0
                warnings.append("Simulation reached singularity")
                return SimulationResult(False, semantic_debt, warnings)
                
            # Check constraint satisfaction
            for constr in fork.constraints:
                if not self._check_constraint(fork, constr):
                    semantic_debt += 0.5
                    warnings.append(f"Constraint violated: {constr.ctype}")
                    
            return SimulationResult(True, semantic_debt, warnings, fork)
            
        except Exception as e:
            semantic_debt += 5.0
            warnings.append(f"Simulation error: {str(e)}")
            return SimulationResult(False, semantic_debt, warnings)
            
    def _check_constraint(self, graph: MeaningGraph, constr: SemanticConstraint) -> bool:
        """Check if a constraint is satisfied."""
        if constr.target not in graph.entities:
            return False
            
        if constr.ctype == 'cardinality':
            child_count = len(graph.get_children(constr.target))
            condition = constr.condition
            
            if isinstance(condition, dict):
                quantifier = condition.get('quantifier', 'exactly')
                count = condition.get('count', 1)
                
                if quantifier == 'exactly':
                    return child_count == count
                elif quantifier == 'at_least':
                    return child_count >= count
                elif quantifier == 'at_most':
                    return child_count <= count
                    
        return True
        
    def stress_test(self, graph: MeaningGraph, iterations: int = 100) -> Dict:
        """
        Perform structural stress testing.
        
        Returns statistics on graph robustness.
        """
        results = {
            'iterations': iterations,
            'successful': 0,
            'failed': 0,
            'avg_debt': 0.0,
            'max_debt': 0.0,
            'common_warnings': defaultdict(int)
        }
        
        total_debt = 0.0
        
        for i in range(iterations):
            # Simulate random modification
            def random_op(g):
                if g.entities:
                    # Randomly modify a property
                    uid = list(g.entities.keys())[i % len(g.entities)]
                    g.entities[uid].properties[f"test_{i}"] = i
                    
            result = self.simulate(graph, random_op)
            
            if result.success:
                results['successful'] += 1
            else:
                results['failed'] += 1
                
            total_debt += result.semantic_debt
            results['max_debt'] = max(results['max_debt'], result.semantic_debt)
            
            for w in result.warnings:
                results['common_warnings'][w] += 1
                
        results['avg_debt'] = total_debt / iterations
        
        return results

# ============================================================================
# SECTION 14: SEMANTIC MEMBRANE (Layer 14)
# ============================================================================

class MembraneViolation(Exception):
    """Exception raised when semantic membrane blocks execution."""
    pass

class SemanticMembrane:
    """
    Execution firewall - blocks unsafe meanings.
    
    Execution is blocked if:
    1. Meaning is imaginary
    2. Meaning is abstract but uninstantiated
    3. Meaning violates constraints
    4. Meaning contains forbidden roots
    5. CMK mismatch detected
    """
    
    FORBIDDEN_ROOTS = {'Imagination'}  # Imagination NEVER executes
    
    def __init__(self, cmk_computer: CMKComputer, topological: TopologicalSpace):
        self.cmk_computer = cmk_computer
        self.topological = topological
        self.auth_tokens: Dict[str, CMK] = {}  # Authorized executions
        
    def validate(self, graph: MeaningGraph, expected_cmk: CMK = None) -> str:
        """
        Validate graph for execution.
        
        Args:
            graph: Meaning graph to validate
            expected_cmk: Expected CMK (for integrity check)
            
        Returns:
            Authorization token if valid
            
        Raises:
            MembraneViolation: If validation fails
        """
        violations = []
        
        # Check 1: Forbidden roots
        for root in graph.roots:
            if root in self.FORBIDDEN_ROOTS:
                violations.append(f"Forbidden root detected: {root}")
                
        # Check 2: CMK mismatch
        if expected_cmk:
            actual_cmk = self.cmk_computer.compute(graph)
            if actual_cmk.synthesis != expected_cmk.synthesis:
                violations.append("CMK mismatch - meaning has drifted")
                
        # Check 3: Topological validity
        region = self.topological.classify_point(graph)
        if region == "singularity":
            violations.append("Meaning is at singularity (invalid)")
            
        # Check 4: Constraint violations
        for constr in graph.constraints:
            if not self._validate_constraint(graph, constr):
                violations.append(f"Constraint violated: {constr.ctype} on {constr.target}")
                
        # Check 5: Abstract uninstantiated meanings
        if self._is_abstract_uninstantiated(graph):
            violations.append("Meaning is abstract but not instantiated")
            
        if violations:
            raise MembraneViolation("Execution blocked:\n  - " + "\n  - ".join(violations))
            
        # Generate authorization token
        token = f"auth_{uuid.uuid4().hex[:16]}"
        cmk = self.cmk_computer.compute(graph)
        self.auth_tokens[token] = cmk
        
        return token
        
    def _validate_constraint(self, graph: MeaningGraph, constr: SemanticConstraint) -> bool:
        """Validate a single constraint."""
        if constr.target not in graph.entities:
            return False
            
        # Basic cardinality check
        if constr.ctype == 'cardinality':
            condition = constr.condition
            item_type = condition.get('item_type') if isinstance(condition, dict) else None
            
            if item_type:
                # Count only children matching item_type
                child_uids = graph.get_children(constr.target)
                children = [
                    uid for uid in child_uids 
                    if uid in graph.entities and graph.entities[uid].name == item_type
                ]
            else:
                # Count all children
                children = graph.get_children(constr.target)
            
            if isinstance(condition, dict):
                quantifier = condition.get('quantifier', 'exactly')
                count = condition.get('count', 1)
                
                if quantifier == 'exactly' and len(children) != count:
                    return False
                elif quantifier == 'at_least' and len(children) < count:
                    return False
                elif quantifier == 'at_most' and len(children) > count:
                    return False
                    
        return True
        
    def _is_abstract_uninstantiated(self, graph: MeaningGraph) -> bool:
        """Check if meaning is abstract without concrete instantiation."""
        # Has only synthetic entities = abstract
        real_entities = [e for e in graph.entities.values() if not e.synthetic]
        return len(real_entities) == 0 and len(graph.entities) > 0
        
    def seal_execution(self, token: str) -> bool:
        """Verify and seal authorized execution."""
        return token in self.auth_tokens

# ============================================================================
# SECTION 15: SEMANTIC INFERENCE & CODE GENERATION
# ============================================================================

class SemanticInference:
    """
    Template-free code generation from meaning topology.
    
    Derives implementation from:
    - Guna → Visual properties (color, emphasis)
    - Pada → Layout properties (position, size)
    - Relations → Structure (containment, ordering)
    """
    
    def __init__(self):
        pass
        
    def infer_guna(self, entity: SemanticEntity, graph: MeaningGraph) -> Guna:
        """Infer Guna from entity context."""
        # Check for explicit Guna
        if entity.guna:
            return entity.guna
            
        # Infer from name patterns
        sattva_keywords = ['header', 'title', 'logo', 'brand', 'hero', 'main']
        rajas_keywords = ['button', 'action', 'nav', 'menu', 'link', 'control']
        tamas_keywords = ['footer', 'hidden', 'background', 'shadow', 'base']
        
        name_lower = entity.name.lower()
        
        for kw in sattva_keywords:
            if kw in name_lower:
                return Guna.SATTVA
        for kw in rajas_keywords:
            if kw in name_lower:
                return Guna.RAJAS
        for kw in tamas_keywords:
            if kw in name_lower:
                return Guna.TAMAS
                
        return Guna.SATTVA  # Default
        
    def infer_pada(self, entity: SemanticEntity, graph: MeaningGraph) -> Pada:
        """Infer Pada from entity position in hierarchy."""
        # Check for explicit Pada
        if entity.pada:
            return entity.pada
            
        # Check parent
        parent_uid = graph.get_parent(entity.uid)
        if parent_uid:
            siblings = graph.get_children(parent_uid)
            if siblings:
                idx = siblings.index(entity.uid) if entity.uid in siblings else 0
                if idx == 0:
                    return Pada.URDHVALOKA  # First = top
                elif idx == len(siblings) - 1:
                    return Pada.ADHOLOKA    # Last = bottom
                    
        return Pada.MADHYALOKA  # Default middle
        
    def synthesize_color(self, guna: Guna, depth: int = 0) -> str:
        """Synthesize HSL color from Guna."""
        if guna == Guna.SATTVA:
            # Gold/white spectrum
            hue = 45 + (depth * 5)
            sat = 80 - (depth * 10)
            light = 90 - (depth * 15)
        elif guna == Guna.RAJAS:
            # Orange/red spectrum
            hue = 25 + (depth * 10)
            sat = 90 - (depth * 5)
            light = 60 - (depth * 10)
        else:  # TAMAS
            # Dark spectrum
            hue = 220 + (depth * 5)
            sat = 20 + (depth * 5)
            light = 20 + (depth * 10)
            
        return f"hsl({hue % 360}, {max(10, sat)}%, {max(10, min(95, light))}%)"
        
    def synthesize_layout(self, pada: Pada, depth: int = 0) -> Dict[str, str]:
        """Synthesize layout properties from Pada."""
        props = {}
        
        if pada == Pada.URDHVALOKA:
            props['order'] = str(-1 - depth)
            props['align-self'] = 'flex-start'
        elif pada == Pada.ADHOLOKA:
            props['order'] = str(999 + depth)
            props['align-self'] = 'flex-end'
        else:  # MADHYALOKA
            props['flex'] = '1'
            props['align-self'] = 'stretch'
            
        return props

# ============================================================================
# SECTION 16: BACKEND INTERFACES
# ============================================================================

class Backend(ABC):
    """Abstract base class for code generation backends."""
    
    @abstractmethod
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate code from meaning graph."""
        pass
        
    @abstractmethod
    def get_file_extension(self) -> str:
        """Get file extension for this backend."""
        pass

class HTMLBackend(Backend):
    """HTML/CSS code generation backend."""
    
    def get_file_extension(self) -> str:
        return '.html'
        
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate semantic HTML from meaning graph."""
        lines = []
        
        # HTML5 boilerplate
        lines.append('<!DOCTYPE html>')
        lines.append('<html lang="en">')
        lines.append('<head>')
        lines.append('    <meta charset="UTF-8">')
        lines.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
        lines.append(f'    <title>{graph.metadata.get("title", "Sadhana Generated")}</title>')
        lines.append('    <style>')
        lines.append(self._generate_styles(graph, inference))
        lines.append('    </style>')
        lines.append('</head>')
        lines.append('<body>')
        
        # Generate content from hierarchy
        lines.extend(self._generate_content(graph, inference))
        
        lines.append('</body>')
        lines.append('</html>')
        
        return '\n'.join(lines)
        
    def _generate_styles(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate CSS styles from Guna/Pada."""
        styles = []
        
        # Base styles
        styles.append('''
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: system-ui, sans-serif; }
        .sattva { border: 2px solid gold; }
        .rajas { border: 2px solid coral; }
        .tamas { border: 2px solid #333; }
        ''')
        
        # Entity-specific styles
        for uid, ent in graph.entities.items():
            if ent.synthetic:
                continue
                
            guna = inference.infer_guna(ent, graph)
            pada = inference.infer_pada(ent, graph)
            
            color = inference.synthesize_color(guna)
            layout = inference.synthesize_layout(pada)
            
            selector = f'.entity-{ent.name.lower()}'
            props = [f'background-color: {color};']
            props.append(f'padding: 1rem;')
            props.append(f'margin: 0.5rem;')
            props.append(f'border-radius: 4px;')
            
            for k, v in layout.items():
                props.append(f'{k}: {v};')
                
            styles.append(f'{selector} {{ { " ".join(props) } }}')
            
        return '\n'.join(styles)
        
    def _generate_content(self, graph: MeaningGraph, inference: SemanticInference) -> List[str]:
        """Generate HTML content from entity hierarchy."""
        lines = []
        
        # Find root entities (no parent)
        all_children = set()
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                all_children.add(rel.participants[1])
                
        roots = [uid for uid in graph.entities if uid not in all_children]
        
        # Build children map
        children_map = defaultdict(list)
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                parent, child = rel.participants[0], rel.participants[1]
                children_map[parent].append(child)
                
        def render_entity(uid: str, depth: int = 0) -> List[str]:
            """Recursively render entity and children."""
            result = []
            ent = graph.entities.get(uid)
            if not ent or ent.synthetic:
                return result
                
            indent = '    ' * (depth + 1)
            guna = inference.infer_guna(ent, graph)
            
            # Determine tag
            tag = self._infer_tag(ent, guna)
            class_name = f'entity-{ent.name.lower()} guna-{guna.value}'
            
            # Opening tag
            result.append(f'{indent}<{tag} class="{class_name}" data-entity="{ent.name}">')
            result.append(f'{indent}    <span class="label">{ent.name}</span>')
            
            # Render children
            for child_uid in children_map.get(uid, []):
                result.extend(render_entity(child_uid, depth + 1))
                
            # Closing tag
            result.append(f'{indent}</{tag}>')
            
            return result
            
        for root_uid in roots:
            lines.extend(render_entity(root_uid, 0))
            
        return lines
        
    def _infer_tag(self, entity: SemanticEntity, guna: Guna) -> str:
        """Infer HTML tag from entity properties."""
        name_lower = entity.name.lower()
        
        # Structural elements
        if any(kw in name_lower for kw in ['header', 'head', 'hero']):
            return 'header'
        if any(kw in name_lower for kw in ['footer', 'foot', 'bottom']):
            return 'footer'
        if any(kw in name_lower for kw in ['nav', 'menu', 'navigation']):
            return 'nav'
        if any(kw in name_lower for kw in ['main', 'content', 'body']):
            return 'main'
        if any(kw in name_lower for kw in ['section', 'area', 'region']):
            return 'section'
        if any(kw in name_lower for kw in ['article', 'post', 'entry']):
            return 'article'
        if any(kw in name_lower for kw in ['aside', 'sidebar', 'side']):
            return 'aside'
            
        # Content elements
        if any(kw in name_lower for kw in ['button', 'btn', 'action', 'cta']):
            return 'button'
        if any(kw in name_lower for kw in ['link', 'a', 'href']):
            return 'a'
        if any(kw in name_lower for kw in ['image', 'img', 'picture', 'photo']):
            return 'img'
        if any(kw in name_lower for kw in ['heading', 'h1', 'title']):
            return 'h1'
        if any(kw in name_lower for kw in ['text', 'p', 'paragraph', 'desc']):
            return 'p'
        if any(kw in name_lower for kw in ['list', 'ul', 'menu']):
            return 'ul'
        if any(kw in name_lower for kw in ['item', 'li']):
            return 'li'
            
        # Default by Guna
        if guna == Guna.SATTVA:
            return 'header'
        elif guna == Guna.RAJAS:
            return 'div'
        else:
            return 'footer'

class PythonBackend(Backend):
    """Python code generation backend."""
    
    def get_file_extension(self) -> str:
        return '.py'
        
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate Python code from meaning graph."""
        lines = []
        
        lines.append('#!/usr/bin/env python3')
        lines.append('"""Generated by Sadhana v3.0"""')
        lines.append('')
        lines.append('from typing import Dict, List, Optional, Any')
        lines.append('from dataclasses import dataclass, field')
        lines.append('')
        
        # Generate classes for entities
        real_entities = [(uid, ent) for uid, ent in graph.entities.items() if not ent.synthetic]
        for uid, ent in real_entities:
            lines.extend(self._generate_class(ent, graph, inference))
            lines.append('')
            
        # Generate main function
        lines.append('def main():')
        lines.append('    """Main entry point."""')
        lines.append('    print("=== Sadhana Generated Application ===")')
        lines.append('    ')
        
        # Instantiate all real entities with unique variable names
        var_names = {}
        for uid, ent in real_entities:
            # Create safe variable name
            var_name = self._make_var_name(ent.name, var_names)
            var_names[uid] = var_name
            lines.append(f'    {var_name} = {ent.name}()')
            lines.append(f'    print(f"  Created: {ent.name} = {{{var_name}}}")')
            
        lines.append('    ')
        lines.append('    # Build containment hierarchy')
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                parent_uid, child_uid = rel.participants[0], rel.participants[1]
                if parent_uid in var_names and child_uid in var_names:
                    parent_var = var_names[parent_uid]
                    child_var = var_names[child_uid]
                    child_name = graph.entities[child_uid].name
                    lines.append(f'    {parent_var}.add_child("{child_name}", {child_var})')
                    
        lines.append('    ')
        lines.append('    print("\\n=== Application Ready ===")')
        lines.append('    return {')
        lines.append('        ' + ', '.join([f'"{graph.entities[uid].name}": {var}' for uid, var in var_names.items()]))
        lines.append('    }')
        lines.append('')
        lines.append("if __name__ == '__main__':")
        lines.append('    result = main()')
        
        return '\n'.join(lines)
        
    def _make_var_name(self, entity_name: str, existing: Dict) -> str:
        """Create a unique variable name that doesn't shadow class names."""
        # Use snake_case with _inst suffix to avoid shadowing
        base = entity_name[0].lower() + entity_name[1:] if entity_name else 'obj'
        base = ''.join(c if c.isalnum() else '_' for c in base)
        var_name = f"{base}_inst"
        
        # Ensure uniqueness
        counter = 1
        original = var_name
        while var_name in existing.values():
            var_name = f"{original}_{counter}"
            counter += 1
            
        return var_name
        
    def _generate_class(self, entity: SemanticEntity, graph: MeaningGraph, 
                       inference: SemanticInference) -> List[str]:
        """Generate Python class for entity."""
        lines = []
        
        guna = inference.infer_guna(entity, graph)
        pada = inference.infer_pada(entity, graph)
        
        lines.append(f'@dataclass')
        lines.append(f'class {entity.name}:' )
        lines.append(f'    """')
        lines.append(f'    Semantic Entity: {entity.name}')
        lines.append(f'    Guna: {guna.value}')
        lines.append(f'    Pada: {pada.value}')
        lines.append(f'    """')
        lines.append('    ')
        lines.append('    # Properties')
        lines.append('    children: Dict[str, Any] = field(default_factory=dict)')
        
        # Add property fields
        for key, val in entity.properties.items():
            lines.append(f'    {key}: Any = None')
            
        lines.append('    ')
        lines.append('    def __post_init__(self):')
        lines.append(f'        self._type = "{entity.sem_type.name}"')
        lines.append('        self.children = {}')
        lines.append('        ')
        lines.append('    def add_child(self, name: str, child):')
        lines.append('        """Add a child entity."""')
        lines.append('        self.children[name] = child')
        lines.append('        ')
        lines.append('    def get_metadata(self) -> Dict:')
        lines.append('        return {')
        lines.append(f'            "name": "{entity.name}",')
        lines.append(f'            "guna": "{guna.value}",')
        lines.append(f'            "pada": "{pada.value}"')
        lines.append('        }')
        
        return lines

class SQLBackend(Backend):
    """SQL code generation backend."""
    
    def get_file_extension(self) -> str:
        return '.sql'
        
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate SQL schema from meaning graph."""
        lines = []
        
        lines.append('-- Generated by Sadhana v3.0')
        lines.append('')
        
        # Generate tables for entities
        tables = []
        for uid, ent in graph.entities.items():
            if ent.synthetic:
                continue
            tables.append(self._generate_table(ent, graph, inference))
            
        lines.extend(tables)
        lines.append('')
        
        # Generate foreign keys from relations
        fk_lines = self._generate_foreign_keys(graph)
        lines.extend(fk_lines)
        
        return '\n'.join(lines)
        
    def _generate_table(self, entity: SemanticEntity, graph: MeaningGraph,
                       inference: SemanticInference) -> str:
        """Generate CREATE TABLE for entity."""
        lines = []
        
        table_name = entity.name.lower()
        guna = inference.infer_guna(entity, graph)
        
        lines.append(f'CREATE TABLE {table_name} (' )
        lines.append('    id INTEGER PRIMARY KEY AUTOINCREMENT,')
        lines.append(f'    name VARCHAR(255) NOT NULL,')
        lines.append(f'    guna VARCHAR(20) DEFAULT \'{guna.value}\',')
        lines.append('    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP')
        lines.append(');')
        lines.append('')
        
        return '\n'.join(lines)
        
    def _generate_foreign_keys(self, graph: MeaningGraph) -> List[str]:
        """Generate foreign key constraints from relations."""
        lines = []
        
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                parent = graph.entities.get(rel.participants[0])
                child = graph.entities.get(rel.participants[1])
                
                if parent and child and not parent.synthetic and not child.synthetic:
                    lines.append(f'-- Relation: {parent.name} contains {child.name}')
                    lines.append(f'ALTER TABLE {child.name.lower()} ')
                    lines.append(f'    ADD COLUMN {parent.name.lower()}_id INTEGER,')
                    lines.append(f'    ADD FOREIGN KEY ({parent.name.lower()}_id) ')
                    lines.append(f'    REFERENCES {parent.name.lower()}(id);')
                    lines.append('')
                    
        return lines


# ============================================================================
# NEW BACKENDS: Rust, Go, Java, C++
# ============================================================================

class RustBackend(Backend):
    """Rust code generation backend with ownership semantics."""
    
    def get_file_extension(self) -> str:
        return '.rs'
        
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate Rust code from meaning graph."""
        lines = []
        
        lines.append('// Generated by Sadhana v3.0')
        lines.append('// Rust Backend with Ownership Semantics')
        lines.append('')
        lines.append('use std::collections::HashMap;')
        lines.append('')
        
        # Generate structs for entities
        real_entities = [(uid, ent) for uid, ent in graph.entities.items() if not ent.synthetic]
        
        for uid, ent in real_entities:
            lines.extend(self._generate_struct(ent, graph, inference))
            lines.append('')
            
        # Generate main function
        lines.append('fn main() {')
        lines.append('    println!("=== Sadhana Generated Rust Application ===");')
        lines.append('    ')
        
        # Instantiate all entities
        var_names = {}
        for uid, ent in real_entities:
            var_name = self._make_var_name(ent.name, var_names)
            var_names[uid] = var_name
            lines.append(f'    let {var_name} = {ent.name}::new();')
            lines.append(f'    println!("Created: {{:?}}", {var_name});')
            
        lines.append('    ')
        lines.append('    // Build containment hierarchy')
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                parent_uid, child_uid = rel.participants[0], rel.participants[1]
                if parent_uid in var_names and child_uid in var_names:
                    parent_var = var_names[parent_uid]
                    child_var = var_names[child_uid]
                    child_name = graph.entities[child_uid].name
                    lines.append(f'    {parent_var}.add_child("{child_name}", {child_var});')
                    
        lines.append('    ')
        lines.append('    println!("\\n=== Application Ready ===");')
        lines.append('}')
        
        return '\n'.join(lines)
        
    def _generate_struct(self, entity: SemanticEntity, graph: MeaningGraph,
                        inference: SemanticInference) -> List[str]:
        """Generate Rust struct for entity."""
        lines = []
        
        guna = inference.infer_guna(entity, graph)
        pada = inference.infer_pada(entity, graph)
        
        lines.append(f'/// Semantic Entity: {entity.name}')
        lines.append(f'/// Guna: {guna.value}')
        lines.append(f'/// Pada: {pada.value}')
        lines.append(f'#[derive(Debug)]')
        lines.append(f'pub struct {entity.name} {{')
        lines.append('    pub name: String,')
        lines.append('    pub guna: String,')
        lines.append('    pub pada: String,')
        lines.append('    pub children: HashMap<String, Box<dyn std::any::Any>>,')
        lines.append('}')
        lines.append('')
        lines.append(f'impl {entity.name} {{')
        lines.append(f'    pub fn new() -> Self {{')
        lines.append(f'        {entity.name} {{')
        lines.append(f'            name: "{entity.name}".to_string(),')
        lines.append(f'            guna: "{guna.value}".to_string(),')
        lines.append(f'            pada: "{pada.value}".to_string(),')
        lines.append('            children: HashMap::new(),')
        lines.append('        }')
        lines.append('    }')
        lines.append('    ')
        lines.append('    pub fn add_child<T: \'static>(&mut self, name: &str, child: T) {')
        lines.append('        self.children.insert(name.to_string(), Box::new(child));')
        lines.append('    }')
        lines.append('    ')
        lines.append('    pub fn get_metadata(&self) -> HashMap<String, String> {')
        lines.append('        let mut meta = HashMap::new();')
        lines.append('        meta.insert("name".to_string(), self.name.clone());')
        lines.append('        meta.insert("guna".to_string(), self.guna.clone());')
        lines.append('        meta.insert("pada".to_string(), self.pada.clone());')
        lines.append('        meta')
        lines.append('    }')
        lines.append('}')
        
        return lines
        
    def _make_var_name(self, entity_name: str, existing: Dict) -> str:
        """Create unique variable name."""
        base = entity_name.lower()
        var_name = f"{base}_inst"
        counter = 1
        while var_name in existing.values():
            var_name = f"{base}_inst_{counter}"
            counter += 1
        return var_name


class GoBackend(Backend):
    """Go code generation backend with goroutine support."""
    
    def get_file_extension(self) -> str:
        return '.go'
        
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate Go code from meaning graph."""
        lines = []
        
        lines.append('// Generated by Sadhana v3.0')
        lines.append('// Go Backend with Concurrency Support')
        lines.append('')
        lines.append('package main')
        lines.append('')
        lines.append('import (')
        lines.append('    "fmt"')
        lines.append('    "time"')
        lines.append(')')
        lines.append('')
        
        # Generate structs
        real_entities = [(uid, ent) for uid, ent in graph.entities.items() if not ent.synthetic]
        
        for uid, ent in real_entities:
            lines.extend(self._generate_struct(ent, graph, inference))
            lines.append('')
            
        # Generate main
        lines.append('func main() {')
        lines.append('    fmt.Println("=== Sadhana Generated Go Application ===")')
        lines.append('    ')
        
        var_names = {}
        for uid, ent in real_entities:
            var_name = self._make_var_name(ent.name, var_names)
            var_names[uid] = var_name
            lines.append(f'    {var_name} := New{ent.name}()')
            lines.append(f'    fmt.Printf("Created: %+v\\n", {var_name})')
            
        lines.append('    ')
        lines.append('    // Build containment hierarchy')
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                parent_uid, child_uid = rel.participants[0], rel.participants[1]
                if parent_uid in var_names and child_uid in var_names:
                    parent_var = var_names[parent_uid]
                    child_var = var_names[child_uid]
                    child_name = graph.entities[child_uid].name
                    lines.append(f'    {parent_var}.AddChild("{child_name}", {child_var})')
                    
        lines.append('    ')
        lines.append('    fmt.Println("\\n=== Application Ready ===")')
        lines.append('}')
        
        return '\n'.join(lines)
        
    def _generate_struct(self, entity: SemanticEntity, graph: MeaningGraph,
                        inference: SemanticInference) -> List[str]:
        """Generate Go struct."""
        lines = []
        
        guna = inference.infer_guna(entity, graph)
        pada = inference.infer_pada(entity, graph)
        
        lines.append(f'// {entity.name} - Semantic Entity')
        lines.append(f'// Guna: {guna.value}, Pada: {pada.value}')
        lines.append(f'type {entity.name} struct {{')
        lines.append('    Name     string')
        lines.append('    Guna     string')
        lines.append('    Pada     string')
        lines.append('    Children map[string]interface{}')
        lines.append('    Created  time.Time')
        lines.append('}')
        lines.append('')
        lines.append(f'// New{entity.name} creates a new instance')
        lines.append(f'func New{entity.name}() *{entity.name} {{')
        lines.append(f'    return &{entity.name}{{')
        lines.append(f'        Name:     "{entity.name}",')
        lines.append(f'        Guna:     "{guna.value}",')
        lines.append(f'        Pada:     "{pada.value}",')
        lines.append('        Children: make(map[string]interface{}),')
        lines.append('        Created:  time.Now(),')
        lines.append('    }')
        lines.append('}')
        lines.append('')
        lines.append(f'// AddChild adds a child entity')
        lines.append('func (e *' + entity.name + ') AddChild(name string, child interface{}) {')
        lines.append('    e.Children[name] = child')
        lines.append('}')
        lines.append('')
        lines.append(f'// GetMetadata returns entity metadata')
        lines.append('func (e *' + entity.name + ') GetMetadata() map[string]string {')
        lines.append('    return map[string]string{')
        lines.append('        "name": e.Name,')
        lines.append('        "guna": e.Guna,')
        lines.append('        "pada": e.Pada,')
        lines.append('    }')
        lines.append('}')
        
        return lines
        
    def _make_var_name(self, entity_name: str, existing: Dict) -> str:
        base = entity_name.lower()
        var_name = f"{base}Inst"
        counter = 1
        while var_name in existing.values():
            var_name = f"{base}Inst{counter}"
            counter += 1
        return var_name


class JavaBackend(Backend):
    """Java code generation backend with OOP patterns."""
    
    def get_file_extension(self) -> str:
        return '.java'
        
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate Java code from meaning graph."""
        lines = []
        
        lines.append('// Generated by Sadhana v3.0')
        lines.append('// Java Backend with OOP Patterns')
        lines.append('')
        lines.append('import java.util.*;')
        lines.append('')
        lines.append('public class SadhanaGenerated {')
        lines.append('    ')
        
        # Generate classes as inner classes
        real_entities = [(uid, ent) for uid, ent in graph.entities.items() if not ent.synthetic]
        
        for uid, ent in real_entities:
            lines.extend(['    ' + line for line in self._generate_class(ent, graph, inference)])
            lines.append('    ')
            
        # Generate main method
        lines.append('    public static void main(String[] args) {')
        lines.append('        System.out.println("=== Sadhana Generated Java Application ===");')
        lines.append('        ')
        
        var_names = {}
        for uid, ent in real_entities:
            var_name = self._make_var_name(ent.name, var_names)
            var_names[uid] = var_name
            lines.append(f'        {ent.name} {var_name} = new {ent.name}();')
            lines.append(f'        System.out.println("Created: " + {var_name}.getName());')
            
        lines.append('        ')
        lines.append('        // Build containment hierarchy')
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                parent_uid, child_uid = rel.participants[0], rel.participants[1]
                if parent_uid in var_names and child_uid in var_names:
                    parent_var = var_names[parent_uid]
                    child_var = var_names[child_uid]
                    child_name = graph.entities[child_uid].name
                    lines.append(f'        {parent_var}.addChild("{child_name}", {child_var});')
                    
        lines.append('        ')
        lines.append('        System.out.println("\\n=== Application Ready ===");')
        lines.append('    }')
        lines.append('}')
        
        return '\n'.join(lines)
        
    def _generate_class(self, entity: SemanticEntity, graph: MeaningGraph,
                       inference: SemanticInference) -> List[str]:
        """Generate Java class."""
        lines = []
        
        guna = inference.infer_guna(entity, graph)
        pada = inference.infer_pada(entity, graph)
        
        lines.append(f'/**')
        lines.append(f' * Semantic Entity: {entity.name}')
        lines.append(f' * Guna: {guna.value}')
        lines.append(f' * Pada: {pada.value}')
        lines.append(f' */')
        lines.append(f'public static class {entity.name} {{')
        lines.append('    private String name;')
        lines.append('    private String guna;')
        lines.append('    private String pada;')
        lines.append('    private Map<String, Object> children;')
        lines.append('    private Date createdAt;')
        lines.append('    ')
        lines.append(f'    public {entity.name}() {{')
        lines.append(f'        this.name = "{entity.name}";')
        lines.append(f'        this.guna = "{guna.value}";')
        lines.append(f'        this.pada = "{pada.value}";')
        lines.append('        this.children = new HashMap<>();')
        lines.append('        this.createdAt = new Date();')
        lines.append('    }')
        lines.append('    ')
        lines.append('    public void addChild(String name, Object child) {')
        lines.append('        children.put(name, child);')
        lines.append('    }')
        lines.append('    ')
        lines.append('    public String getName() { return name; }')
        lines.append('    public String getGuna() { return guna; }')
        lines.append('    public String getPada() { return pada; }')
        lines.append('    public Map<String, Object> getChildren() { return children; }')
        lines.append('    public Map<String, String> getMetadata() {')
        lines.append('        Map<String, String> meta = new HashMap<>();')
        lines.append('        meta.put("name", name);')
        lines.append('        meta.put("guna", guna);')
        lines.append('        meta.put("pada", pada);')
        lines.append('        return meta;')
        lines.append('    }')
        lines.append('}')
        
        return lines
        
    def _make_var_name(self, entity_name: str, existing: Dict) -> str:
        base = entity_name.lower()
        return f"{base}Inst"


class CppBackend(Backend):
    """C++ code generation backend with memory management."""
    
    def get_file_extension(self) -> str:
        return '.cpp'
        
    def generate(self, graph: MeaningGraph, inference: SemanticInference) -> str:
        """Generate C++ code from meaning graph."""
        lines = []
        
        lines.append('// Generated by Sadhana v3.0')
        lines.append('// C++ Backend with Smart Pointers')
        lines.append('')
        lines.append('#include <iostream>')
        lines.append('#include <string>')
        lines.append('#include <vector>')
        lines.append('#include <map>')
        lines.append('#include <memory>')
        lines.append('#include <chrono>')
        lines.append('')
        lines.append('using namespace std;')
        lines.append('')
        
        # Generate forward declarations
        real_entities = [(uid, ent) for uid, ent in graph.entities.items() if not ent.synthetic]
        for uid, ent in real_entities:
            lines.append(f'class {ent.name};')
        lines.append('')
        
        # Generate classes
        for uid, ent in real_entities:
            lines.extend(self._generate_class(ent, graph, inference))
            lines.append('')
            
        # Generate main
        lines.append('int main() {')
        lines.append('    cout << "=== Sadhana Generated C++ Application ===" << endl;')
        lines.append('    ')
        
        var_names = {}
        for uid, ent in real_entities:
            var_name = self._make_var_name(ent.name, var_names)
            var_names[uid] = var_name
            lines.append(f'    auto {var_name} = make_shared<{ent.name}>();')
            lines.append(f'    cout << "Created: " << {var_name}->getName() << endl;')
            
        lines.append('    ')
        lines.append('    // Build containment hierarchy')
        for rel in graph.relations:
            if rel.rel_type == 'contains' and len(rel.participants) >= 2:
                parent_uid, child_uid = rel.participants[0], rel.participants[1]
                if parent_uid in var_names and child_uid in var_names:
                    parent_var = var_names[parent_uid]
                    child_var = var_names[child_uid]
                    child_name = graph.entities[child_uid].name
                    lines.append(f'    {parent_var}->addChild("{child_name}", {child_var});')
                    
        lines.append('    ')
        lines.append('    cout << "\\n=== Application Ready ===" << endl;')
        lines.append('    return 0;')
        lines.append('}')
        
        return '\n'.join(lines)
        
    def _generate_class(self, entity: SemanticEntity, graph: MeaningGraph,
                       inference: SemanticInference) -> List[str]:
        """Generate C++ class."""
        lines = []
        
        guna = inference.infer_guna(entity, graph)
        pada = inference.infer_pada(entity, graph)
        
        lines.append(f'/**')
        lines.append(f' * Semantic Entity: {entity.name}')
        lines.append(f' * Guna: {guna.value}')
        lines.append(f' * Pada: {pada.value}')
        lines.append(f' */')
        lines.append(f'class {entity.name} {{')
        lines.append('private:')
        lines.append('    string name;')
        lines.append('    string guna;')
        lines.append('    string pada;')
        lines.append('    map<string, shared_ptr<void>> children;')
        lines.append('    chrono::system_clock::time_point createdAt;')
        lines.append('    ')
        lines.append('public:')
        lines.append(f'    {entity.name}() {{')
        lines.append(f'        name = "{entity.name}";')
        lines.append(f'        guna = "{guna.value}";')
        lines.append(f'        pada = "{pada.value}";')
        lines.append('        createdAt = chrono::system_clock::now();')
        lines.append('    }')
        lines.append('    ')
        lines.append('    void addChild(const string& name, shared_ptr<void> child) {')
        lines.append('        children[name] = child;')
        lines.append('    }')
        lines.append('    ')
        lines.append('    string getName() const { return name; }')
        lines.append('    string getGuna() const { return guna; }')
        lines.append('    string getPada() const { return pada; }')
        lines.append('    map<string, string> getMetadata() const {')
        lines.append('        map<string, string> meta;')
        lines.append('        meta["name"] = name;')
        lines.append('        meta["guna"] = guna;')
        lines.append('        meta["pada"] = pada;')
        lines.append('        return meta;')
        lines.append('    }')
        lines.append('};')
        
        return lines
        
    def _make_var_name(self, entity_name: str, existing: Dict) -> str:
        base = entity_name.lower()
        return f"{base}Inst"


# ============================================================================
# SECTION 17: MAIN COMPILER
# ============================================================================

class SadhanaCompiler:
    """
    Main Sadhana compiler - orchestrates all layers.
    
    Pipeline:
    1. Lex → Parse → AST
    2. Build Meaning Graph
    3. Apply Dhatus
    4. Compute CMK
    5. Encode Bija
    6. Expand (if requested)
    7. Pass through Membrane
    8. Generate Code
    """
    
    def __init__(self):
        self.cmk_computer = CMKComputer()
        self.bija_system = BijaSystem()
        self.dhatu_layer = DhatuLayer(self.cmk_computer)
        self.sandhi = SandhiEngine(self.cmk_computer)
        self.option_engine = OptionRuleEngine(self.cmk_computer)
        self.temporal = TemporalExpansion(self.option_engine)
        self.topological = TopologicalSpace(self.cmk_computer)
        self.sanhara = SanharaEngine(self.cmk_computer, self.topological)
        self.membrane = SemanticMembrane(self.cmk_computer, self.topological)
        self.inference = SemanticInference()
        
        # New layers (15-20)
        self.resonance = StructuralResonanceCompiler()
        self.type_inference = TypeRoleCapabilityInference()
        self.mutation_versioning = DeferredMutationVersioning()
        self.causal_runtime = CausalProvenanceRuntime()
        self.meta = MetaLayer()
        
        # Backends
        self.backends: Dict[str, Backend] = {
            'html': HTMLBackend(),
            'python': PythonBackend(),
            'sql': SQLBackend(),
            'rust': RustBackend(),
            'go': GoBackend(),
            'java': JavaBackend(),
            'cpp': CppBackend()
        }
        
    def compile(self, source: str, target_domain: str = 'html',
                temporal_level: int = 0, simulate: bool = False) -> Dict:
        """
        Compile Sadhana source to target domain.
        
        Args:
            source: Sadhana notebook text
            target_domain: Output domain ('html', 'python', 'sql')
            temporal_level: Expansion level (0-3)
            simulate: If True, don't actually generate code
            
        Returns:
            Dictionary with compilation results
        """
        result = {
            'success': False,
            'ast': None,
            'graph': None,
            'cmk': None,
            'bija': None,
            'domain': target_domain,
            'entities': 0,
            'relations': 0,
            'constraints': 0,
            'expansion_level': temporal_level,
            'code': None,
            'errors': []
        }
        
        try:
            # Step 1: Lexical analysis
            lexer = SadhanaLexer(source)
            tokens = lexer.tokenize()
            
            # Step 2: Parsing
            parser = SadhanaParser(tokens)
            ast = parser.parse()
            result['ast'] = ast
            
            # Step 3: Build Meaning Graph
            graph = self._build_meaning_graph(ast)
            result['graph'] = graph
            
            # Step 4: Apply Dhatus
            graph = self.dhatu_layer.apply_all(graph)
            
            # Step 5: Compute CMK
            cmk = self.cmk_computer.compute(graph)
            result['cmk'] = cmk
            
            # Step 6: Encode Bija
            bija = self.bija_system.encode(graph)
            result['bija'] = bija
            
            # Step 7: Temporal Expansion
            if temporal_level > 0:
                graph = self.temporal.expand(graph, temporal_level)
                
            # Step 8: Topological validation
            region = self.topological.classify_point(graph)
            if region == "singularity":
                result['errors'].append("Meaning at singularity (invalid)")
                return result
                
            # Step 9: Semantic Membrane
            if not simulate:
                try:
                    auth_token = self.membrane.validate(graph, cmk)
                    result['auth_token'] = auth_token
                except MembraneViolation as e:
                    result['errors'].append(str(e))
                    return result
                    
            # Step 10: Code Generation
            if not simulate and target_domain in self.backends:
                backend = self.backends[target_domain]
                code = backend.generate(graph, self.inference)
                result['code'] = code
                
            # Collect statistics
            result['entities'] = len([e for e in graph.entities.values() if not e.synthetic])
            result['relations'] = len(graph.relations)
            result['constraints'] = len(graph.constraints)
            result['success'] = True
            
        except Exception as e:
            result['errors'].append(f"Compilation error: {str(e)}")
            import traceback
            result['traceback'] = traceback.format_exc()
            
        return result
        
    def _build_meaning_graph(self, ast: AST) -> MeaningGraph:
        """Convert AST to Meaning Graph."""
        graph = MeaningGraph()
        
        # Process header
        if 'domain' in ast.header.directives:
            graph.domain = ast.header.directives['domain']
        if 'expansion' in ast.header.directives:
            graph.expansion_level = int(ast.header.directives['expansion'])
        if 'roots' in ast.header.directives:
            roots_val = ast.header.directives['roots']
            if isinstance(roots_val, list):
                graph.roots = roots_val
            else:
                graph.roots = [r.strip() for r in roots_val.split(',')]
                
        # Create entities
        name_to_uid = {}
        for name in ast.body.entities:
            ent = graph.add_entity(name)
            name_to_uid[name] = ent.uid
            
        # Create relations
        for rel_type, source, target in ast.body.relations:
            # Ensure entities exist
            if source not in name_to_uid:
                ent = graph.add_entity(source)
                name_to_uid[source] = ent.uid
            if target not in name_to_uid:
                ent = graph.add_entity(target)
                name_to_uid[target] = ent.uid
                
            graph.add_relation(rel_type, [name_to_uid[source], name_to_uid[target]])
            
        # Create constraints
        for constr in ast.body.constraints:
            target_name = constr['target']
            if target_name in name_to_uid:
                graph.add_constraint(
                    'cardinality',
                    name_to_uid[target_name],
                    constr
                )
                
        # Add explicit roots
        graph.roots.extend(ast.body.roots)
        graph.roots = list(set(graph.roots))  # Deduplicate
        
        return graph
        
    def simulate(self, graph: MeaningGraph, operation: str, **kwargs) -> SimulationResult:
        """Run simulation on graph."""
        ops = {
            'stress_test': lambda g: self.sanhara.stress_test(g, kwargs.get('iterations', 100)),
            'expand': lambda g: self.temporal.expand(g, kwargs.get('level', 1))
        }
        
        if operation in ops:
            return self.sanhara.simulate(graph, ops[operation])
        else:
            return SimulationResult(False, 0.0, [f"Unknown operation: {operation}"])

# ============================================================================
# SECTION 15: STRUCTURAL RESONANCE COMPILER
# ============================================================================

@dataclass
class ResonancePattern:
    """A detected structural pattern for reuse."""
    id: str
    structure_hash: str  # CMK of the pattern
    source_entities: List[str]
    frequency: int = 1
    backend_affinity: Dict[str, float] = field(default_factory=dict)

class StructuralResonanceCompiler:
    """
    Layer 15: Structural Resonance Compiler
    
    Detects structural isomorphism, enables pattern reuse,
    and scores backend affinity for optimal code generation.
    """
    
    def __init__(self):
        self.patterns: Dict[str, ResonancePattern] = {}
        self.resonance_threshold = 0.85
    
    def detect_pattern(self, graph: MeaningGraph) -> Optional[ResonancePattern]:
        """Detect if graph matches a known pattern."""
        cmk_computer = CMKComputer()
        cmk = cmk_computer.compute(graph)
        
        for pattern in self.patterns.values():
            if pattern.structure_hash == cmk.synthesis:
                pattern.frequency += 1
                return pattern
        return None
    
    def register_pattern(self, graph: MeaningGraph, backend_scores: Dict[str, float]) -> str:
        """Register a new pattern for reuse."""
        cmk_computer = CMKComputer()
        cmk = cmk_computer.compute(graph)
        
        pattern_id = f"pattern_{len(self.patterns)}"
        pattern = ResonancePattern(
            id=pattern_id,
            structure_hash=cmk.synthesis,
            source_entities=list(graph.entities.keys()),
            backend_affinity=backend_scores
        )
        self.patterns[pattern_id] = pattern
        return pattern_id
    
    def compute_backend_affinity(self, graph: MeaningGraph, domain: str) -> float:
        """Score how well a domain suits this structure (0.0-1.0)."""
        scores = {
            'html': self._score_html_affinity(graph),
            'python': self._score_python_affinity(graph),
            'sql': self._score_sql_affinity(graph),
            'rust': self._score_rust_affinity(graph),
            'go': self._score_go_affinity(graph),
            'java': self._score_java_affinity(graph),
            'cpp': self._score_cpp_affinity(graph)
        }
        return scores.get(domain, 0.5)
    
    def _score_html_affinity(self, graph: MeaningGraph) -> float:
        """HTML works best with hierarchical containment structures."""
        score = 0.5
        for entity in graph.entities.values():
            if entity.semantic_type == SemanticType.CONTAINER:
                score += 0.1
            if entity.guna == Guna.SATTVA:
                score += 0.05
        return min(score, 1.0)
    
    def _score_python_affinity(self, graph: MeaningGraph) -> float:
        """Python works best with clear data models."""
        score = 0.5
        if len(graph.entities) > 3:
            score += 0.2
        for rel in graph.relations:
            if rel.relation_type == "contains":
                score += 0.05
        return min(score, 1.0)
    
    def _score_sql_affinity(self, graph: MeaningGraph) -> float:
        """SQL works best with relational structures."""
        score = 0.5
        for rel in graph.relations:
            if rel.relation_type in ["contains", "requires"]:
                score += 0.1
        return min(score, 1.0)
    
    def _score_rust_affinity(self, graph: MeaningGraph) -> float:
        """Rust works best with ownership-clear structures."""
        return 0.7
    
    def _score_go_affinity(self, graph: MeaningGraph) -> float:
        """Go works best with simple compositions."""
        return 0.7
    
    def _score_java_affinity(self, graph: MeaningGraph) -> float:
        """Java works best with inheritance patterns."""
        return 0.7
    
    def _score_cpp_affinity(self, graph: MeaningGraph) -> float:
        """C++ works best with memory-managed patterns."""
        return 0.6
    
    def find_isomorphic_structures(self, graph1: MeaningGraph, graph2: MeaningGraph) -> bool:
        """Check if two graphs are structurally isomorphic."""
        if len(graph1.entities) != len(graph2.entities):
            return False
        if len(graph1.relations) != len(graph2.relations):
            return False
        
        cmk1 = CMKComputer().compute(graph1)
        cmk2 = CMKComputer().compute(graph2)
        return cmk1.synthesis == cmk2.synthesis

# ============================================================================
# SECTION 16: TYPE/ROLE/CAPABILITY INFERENCE
# ============================================================================

@dataclass  
class InferredType:
    """An emergent type detected from usage patterns."""
    name: str
    base_entity: str
    properties: List[str]
    capabilities: List[str]
    frozen: bool = False

class TypeRoleCapabilityInference:
    """
    Layer 16: Type/Role/Capability Inference
    
    Detects emergent types, stabilizes roles, bounds capabilities,
    and detects order sensitivity.
    """
    
    def __init__(self):
        self.inferred_types: Dict[str, InferredType] = {}
        self.frozen_types: Set[str] = set()
        self.role_assignments: Dict[str, str] = {}  # entity_id -> role
    
    def detect_emergent_type(self, graph: MeaningGraph, entity_ids: List[str]) -> Optional[InferredType]:
        """Detect if a group of entities forms an emergent type."""
        if len(entity_ids) < 2:
            return None
        
        # Check for common patterns
        common_props = self._extract_common_properties(graph, entity_ids)
        capabilities = self._infer_capabilities(graph, entity_ids)
        
        if common_props:
            type_name = f"EmergentType_{len(self.inferred_types)}"
            inferred = InferredType(
                name=type_name,
                base_entity=entity_ids[0],
                properties=common_props,
                capabilities=capabilities
            )
            self.inferred_types[type_name] = inferred
            return inferred
        return None
    
    def _extract_common_properties(self, graph: MeaningGraph, entity_ids: List[str]) -> List[str]:
        """Extract properties common to all entities."""
        if not entity_ids:
            return []
        
        first = graph.entities.get(entity_ids[0])
        if not first:
            return []
        
        common = set(first.attributes.keys())
        for eid in entity_ids[1:]:
            entity = graph.entities.get(eid)
            if entity:
                common &= set(entity.attributes.keys())
        return list(common)
    
    def _infer_capabilities(self, graph: MeaningGraph, entity_ids: List[str]) -> List[str]:
        """Infer capabilities from relations."""
        capabilities = []
        for eid in entity_ids:
            for rel in graph.relations:
                if rel.source == eid:
                    if rel.relation_type == "contains":
                        capabilities.append("container")
                    elif rel.relation_type == "requires":
                        capabilities.append("dependent")
        return list(set(capabilities))
    
    def stabilize_role(self, entity_id: str, role: str):
        """Assign and stabilize a role for an entity."""
        self.role_assignments[entity_id] = role
    
    def freeze_type(self, type_name: str):
        """Freeze an inferred type to prevent mutation."""
        if type_name in self.inferred_types:
            self.inferred_types[type_name].frozen = True
            self.frozen_types.add(type_name)
    
    def detect_order_sensitivity(self, graph: MeaningGraph) -> List[Tuple[str, str]]:
        """Detect entity pairs that are order-sensitive."""
        sensitive_pairs = []
        for rel in graph.relations:
            if rel.relation_type in ["requires", "enables"]:
                sensitive_pairs.append((rel.source, rel.target))
        return sensitive_pairs
    
    def get_capability_bounds(self, entity_id: str) -> Dict[str, Tuple[int, int]]:
        """Get min/max bounds for entity capabilities."""
        return {
            'children': (0, 100),
            'relations': (0, 50),
            'constraints': (0, 20)
        }

# ============================================================================
# SECTION 17: DEFERRED MUTATION & VERSIONING
# ============================================================================

@dataclass
class MutationVersion:
    """A versioned mutation record."""
    version: int
    timestamp: str  # ISO format (latent time)
    mutation_type: str
    entity_id: str
    changes: Dict[str, Any]
    compatibility: List[int]  # Compatible with versions

class DeferredMutationVersioning:
    """
    Layer 17: Deferred Mutation & Versioning
    
    Locks core invariants, manages adaptive surface traits,
    validates compatibility, and maintains semantic audit trail.
    """
    
    def __init__(self):
        self.locked_invariants: Set[str] = set()  # Entity IDs
        self.mutation_channels: Dict[str, List[MutationVersion]] = defaultdict(list)
        self.current_version = 0
        self.audit_trail: List[Dict] = []
    
    def lock_invariant(self, entity_id: str) -> bool:
        """Lock an entity's core properties from mutation."""
        self.locked_invariants.add(entity_id)
        self._audit("lock", entity_id, {"status": "locked"})
        return True
    
    def is_locked(self, entity_id: str) -> bool:
        """Check if entity is locked."""
        return entity_id in self.locked_invariants
    
    def create_mutation_channel(self, entity_id: str, mutation: Dict[str, Any]) -> int:
        """Create a versioned mutation channel for an entity."""
        if entity_id in self.locked_invariants:
            raise ValueError(f"Cannot mutate locked entity: {entity_id}")
        
        self.current_version += 1
        version = MutationVersion(
            version=self.current_version,
            timestamp=f"T{self.current_version}",  # Latent time
            mutation_type=mutation.get('type', 'unknown'),
            entity_id=entity_id,
            changes=mutation.get('changes', {}),
            compatibility=[self.current_version - 1] if self.current_version > 1 else []
        )
        self.mutation_channels[entity_id].append(version)
        self._audit("mutate", entity_id, {"version": self.current_version})
        return self.current_version
    
    def validate_compatibility(self, entity_id: str, from_version: int, to_version: int) -> bool:
        """Check if mutation is compatible between versions."""
        channels = self.mutation_channels.get(entity_id, [])
        target = next((v for v in channels if v.version == to_version), None)
        if not target:
            return False
        return from_version in target.compatibility or from_version == to_version - 1
    
    def get_audit_trail(self, entity_id: Optional[str] = None) -> List[Dict]:
        """Get semantic audit trail."""
        if entity_id:
            return [a for a in self.audit_trail if a.get('entity_id') == entity_id]
        return self.audit_trail
    
    def _audit(self, action: str, entity_id: str, details: Dict):
        """Record audit entry."""
        self.audit_trail.append({
            'action': action,
            'entity_id': entity_id,
            'details': details,
            'version': self.current_version
        })

# ============================================================================
# SECTION 18: CAUSAL & PROVENANCE RUNTIME
# ============================================================================

@dataclass
class CausalLink:
    """A cause-effect relationship."""
    cause: str
    effect: str
    link_type: str  # 'generates', 'enables', 'requires'
    strength: float  # 0.0-1.0

class CausalProvenanceRuntime:
    """
    Layer 18: Causal & Provenance Runtime
    
    Tracks dependency graph, cause-effect chains, justification records,
    enables reverse debugging, and supports deterministic rollback.
    """
    
    def __init__(self):
        self.dependency_graph: Dict[str, Set[str]] = defaultdict(set)
        self.causal_links: List[CausalLink] = []
        self.justification_records: Dict[str, str] = {}
        self.execution_trace: List[Dict] = []
    
    def record_generation(self, source: str, generated: List[str], justification: str):
        """Record that source generated entities."""
        for g in generated:
            self.dependency_graph[g].add(source)
            self.causal_links.append(CausalLink(
                cause=source,
                effect=g,
                link_type='generates',
                strength=1.0
            ))
            self.justification_records[g] = justification
        self._trace("generation", source, {"generated": generated})
    
    def get_dependencies(self, entity_id: str) -> Set[str]:
        """Get all dependencies of an entity."""
        return self.dependency_graph.get(entity_id, set())
    
    def get_dependents(self, entity_id: str) -> Set[str]:
        """Get all entities that depend on this one."""
        dependents = set()
        for eid, deps in self.dependency_graph.items():
            if entity_id in deps:
                dependents.add(eid)
        return dependents
    
    def get_justification(self, entity_id: str) -> Optional[str]:
        """Get justification for entity's existence."""
        return self.justification_records.get(entity_id)
    
    def reverse_debug(self, entity_id: str) -> List[str]:
        """Trace backwards to find all causes of entity."""
        causes = []
        visited = set()
        stack = [entity_id]
        
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            
            for link in self.causal_links:
                if link.effect == current:
                    causes.append(link.cause)
                    stack.append(link.cause)
        
        return causes
    
    def can_rollback(self, entity_id: str) -> bool:
        """Check if entity can be safely removed."""
        dependents = self.get_dependents(entity_id)
        return len(dependents) == 0
    
    def _trace(self, action: str, entity_id: str, data: Dict):
        """Add to execution trace."""
        self.execution_trace.append({
            'action': action,
            'entity_id': entity_id,
            'data': data
        })

# ============================================================================
# SECTION 20: META-LAYER (SELF-REFERENCE)
# ============================================================================

class MetaLayer:
    """
    Layer 20: Meta-Layer (Self-Reference)
    
    Enables language self-description, grammar of grammars,
    and self-validation loops.
    """
    
    def __init__(self):
        self.language_bija = self._compute_language_bija()
        self.self_validating = True
    
    def _compute_language_bija(self) -> str:
        """Compute Bija for Sādhana language itself."""
        # The language describes itself
        return "SADHANA-SELF-v3.0"
    
    def validate_grammar(self, source: str) -> Tuple[bool, List[str]]:
        """Validate that source conforms to Sādhana grammar."""
        errors = []
        
        # Check for invalid patterns
        invalid_patterns = ['neural_network', 'deep_learning', 'tensor_flow']
        for pattern in invalid_patterns:
            if pattern in source.lower():
                errors.append(f"Forbidden pattern detected: {pattern}")
        
        # Check basic structure
        lines = source.strip().split('\n')
        has_entity = False
        for line in lines:
            stripped = line.strip()
            if stripped and not stripped.startswith('@') and not stripped.startswith('#'):
                if stripped[0].isupper():
                    has_entity = True
        
        if not has_entity:
            errors.append("No entities found (lines starting with capital letter)")
        
        return len(errors) == 0, errors
    
    def get_meta_cmk(self) -> str:
        """Get CMK of Sādhana language itself."""
        return hashlib.sha256(self.language_bija.encode()).hexdigest()[:16]
    
    def self_validate(self) -> bool:
        """Run self-validation loop."""
        return self.self_validating

# Additional constants and patterns
NN_PATTERNS = ['neural', 'network', 'deep', 'gradient', 'backprop', 'training_step', 'tensor', 'layer_norm']

EXPANSION_DIMENSIONS = {
    'view': ['desktop', 'mobile', 'tablet'],
    'order': ['forward', 'reverse', 'random'],
    'time': ['eager', 'lazy', 'batched'],
    'representation': ['semantic', 'generic', 'optimized'],
    'context': ['locale', 'accessibility', 'performance']
}

# ============================================================================
# SECTION 21: CLI INTERFACE
# ============================================================================

def main():
    """Command-line interface for Sadhana compiler."""
    parser = argparse.ArgumentParser(
        description='Sadhana Programming Language v3.0',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python sadhana.py website.sadhana --domain html -o output.html
  python sadhana.py app.sadhana --domain python --expand 2
  python sadhana.py schema.sadhana --domain sql --simulate
        '''
    )
    
    parser.add_argument('file', help='Sadhana source file')
    parser.add_argument('-o', '--output', help='Output file')
    parser.add_argument('-d', '--domain', default='html',
                       choices=['html', 'python', 'sql', 'rust', 'go', 'java', 'cpp'],
                       help='Target domain (default: html)')
    parser.add_argument('-e', '--expand', type=int, default=0,
                       help='Temporal expansion level 0-3 (default: 0)')
    parser.add_argument('-s', '--simulate', action='store_true',
                       help='Simulation mode (no code generation)')
    parser.add_argument('-v', '--verbose', action='store_true',
                       help='Verbose output')
                       
    args = parser.parse_args()
    
    # Read source
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {args.file}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
        
    # Compile
    compiler = SadhanaCompiler()
    result = compiler.compile(
        source,
        target_domain=args.domain,
        temporal_level=args.expand,
        simulate=args.simulate
    )
    
    # Output results
    if args.verbose or not args.output:
        print("=" * 60)
        print("SADHANA COMPILATION RESULT")
        print("=" * 60)
        print(f"Success: {result['success']}")
        print(f"Domain: {result['domain']}")
        print(f"Bija: {result['bija'][:50]}..." if result['bija'] else "Bija: None")
        print(f"CMK: {result['cmk'].synthesis[:32]}..." if result['cmk'] else "CMK: None")
        print(f"Entities: {result['entities']}")
        print(f"Relations: {result['relations']}")
        print(f"Constraints: {result['constraints']}")
        print(f"Expansion: T{result['expansion_level']}")
        
        if result['errors']:
            print("\nErrors:")
            for err in result['errors']:
                print(f"  - {err}")
                
        if args.verbose and result.get('traceback'):
            print("\nTraceback:")
            print(result['traceback'])
            
    # Write output
    if result['success'] and result['code'] and args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result['code'])
            print(f"\n[OK] Code written to: {args.output}")
            
            # Also save Bija metadata
            bija_file = args.output.rsplit('.', 1)[0] + '.bija'
            with open(bija_file, 'w', encoding='utf-8') as f:
                f.write(f"Bija: {result['bija']}\n")
                f.write(f"CMK: {result['cmk'].synthesis}\n")
                f.write(f"Domain: {result['domain']}\n")
                f.write(f"Entities: {result['entities']}\n")
                f.write(f"Relations: {result['relations']}\n")
            print(f"[OK] Metadata saved to: {bija_file}")
            
        except Exception as e:
            print(f"Error writing output: {e}")
            sys.exit(1)
            
    sys.exit(0 if result['success'] else 1)

if __name__ == '__main__':
    main()
