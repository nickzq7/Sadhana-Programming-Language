# SADHANA Programming Language v1.0 (Experimental)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0--experimental-orange.svg)](VERSION)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18846465.svg)](https://doi.org/10.5281/zenodo.18846465)

> **"Where Meaning Precedes Structure, and Order Does Not Define Truth"**

> **Research Status**: This is an **experimental AGI alignment framework** 
> implementing formal semantic constraints for AI safety. While the 
> code generation features are functional, the AGI safety mechanisms 
> (Layer 13-20) are theoretical research prototypes. This is v1.0 - 
> the foundation for future AGI-integrated development.

> **Open Source**: This project is open source under the MIT License. 
> The `sadhana.py` compiler is included in this repository - no external 
> dependencies required beyond Python 3.8+. Use it freely in personal, 
> academic, or commercial projects.

**Sadhana** (Sanskrit: साधना) is an **experimental meaning-first programming framework** designed for **AGI alignment research**. It combines 2,500-year-old Sanskrit linguistic principles from Panini's *Ashtadhyayi* with modern compiler construction to create a paradigm for **safe, verifiable AI systems**. While functional for multi-target code generation today, its architecture is designed as a foundation for future AGI-integrated development environments.

---

## Table of Contents

- [What Makes Sadhana Unique?](#what-makes-sadhana-unique)
- [Core Philosophy](#core-philosophy)
- [Quick Start (5 Minutes)](#quick-start-5-minutes)
- [The Sanskrit Connection](#the-sanskrit-connection)
- [20-Layer Architecture](#20-layer-architecture)
- [Language Syntax Guide](#language-syntax-guide)
- [Code Examples](#code-examples)
- [Multi-Target Backends](#multi-target-backends)
- [Novelty & Research Contributions](#novelty--research-contributions)
- [About the Author](#about-the-author)
- [License](#license)

---

## What Makes Sadhana Unique?

| Feature | Traditional Languages | **Sadhana** |
|---------|---------------------|-------------|
| **Syntax** | Order-dependent, rigid grammar | **Order-free**, notebook-style |
| **Abstraction** | Syntax -> Semantics | **Semantics -> Syntax** |
| **Time** | Embedded in execution | **Latent parameter** (T0->T3 expansion) |
| **Meaning** | Derived from code | **Primary**, code derived from meaning |
| **Philosophy** | Western formal logic | **Sankhya philosophy** (Guna & Pada) |
| **Neural Nets** | Often dependent | **Formally excluded** from core |

### Key Innovations

1. **Meaning-First Programming** - Write what you mean, not how to do it
2. **AGI Alignment Architecture** - Built-in safety constraints for future AI integration
3. **Order-Independence** - Statements can appear in any order
4. **Time-Latent Expansion** - Time is a parameter, not embedded
5. **Semantic Membrane** - Execution firewall blocks unsafe meanings (AGI safety)
6. **Sanhara Engine** - Non-committal simulation for safe AGI reasoning
7. **7 Multi-Target Backends** - Generate HTML, Python, SQL, Rust, Go, Java, C++

---

## Core Philosophy

Sadhana is built on **5 Core Axioms** that fundamentally differentiate it from conventional programming:

### The 5 Core Axioms

```
Axiom 1: Meaning precedes structure
Axiom 2: Order does not define meaning  
Axiom 3: Time is latent (parameter of expansion)
Axiom 4: Finite grammar, infinite structures
Axiom 5: No neural networks in core (formal exclusion)
```

### The 8 Dhatus (Semantic Laws)

Derived from Sanskrit grammatical principles, these laws govern all transformations:

| Dhatu | Law | Description |
|-------|-----|-------------|
| 1 | **Identity Preservation** | Entities maintain identity across all transformations |
| 2 | **Constraint Conservation** | Constraints are never silently modified |
| 3 | **Non-Contradiction** | No entity may have contradictory properties |
| 4 | **Reconstruction Completeness** | Original meaning must be reconstructible |
| 5 | **Mutation Containment** | Mutations are local and tracked |
| 6 | **Semantic Closure** | Valid meanings produce valid meanings |
| 7 | **Drift Elimination** | CMK must remain invariant across transformations |
| 8 | **Impossible-State Pruning** | Invalid configurations pruned before execution |

---

## Quick Start (5 Minutes)

### Installation

```bash
# Clone the repository
git clone https://github.com/nickzq7/sadhana.git
cd sadhana

# The compiler (sadhana.py) is INCLUDED in the repo!
# No pip install needed - just run directly with Python

# Verify Python 3.8+ is installed
python --version

# Check sadhana.py is present
ls sadhana.py  # Linux/Mac
# or
dir sadhana.py  # Windows
```

**What's Included:**
- ✅ `sadhana.py` - The complete compiler (3,587 lines, pure Python)
- ✅ `README.md` - This documentation
- ✅ No external dependencies required!
- ✅ Works on Windows, Mac, and Linux

### Your First Sadhana Program (WORKING EXAMPLE)

Create a file called `hello.sadhana`:

```sadhana
@domain: html
@title: My First Sadhana Page

# STEP 1: Declare all entities (one per line, Capitalized)
Header
Navigation
Hero
Footer

# STEP 2: Define relationships
# Format: Parent contains Child
Header contains Navigation
Header contains Hero
Body contains Header
Body contains Footer

# NOTE: Constraints are OPTIONAL - remove if unsure!
# The example below is commented out because it requires exactly 2 Navigation entities
# Constraint: Header must have exactly 2 Navigation
```

**IMPORTANT RULES FOR BEGINNERS:**
1. **Entity names** must be Capitalized (Header, not header)
2. **One entity per line** when declaring
3. **Relations** use lowercase keywords: `contains`, `requires`, `enables`, `depends`
4. **Constraints are OPTIONAL** - if used, they MUST be satisfiable
5. **Order does NOT matter** - declare entities and relations in any order

### Compile and Run

```bash
# ALWAYS use -v (verbose) flag to see what's happening
python sadhana.py hello.sadhana -o hello.html -v

# Success output will show:
# - Success: True
# - Bija: HTMEHead... (compressed meaning)
# - CMK: hash... (meaning fingerprint)
# - [OK] Code written to: hello.html

# Generate Python instead
python sadhana.py hello.sadhana -o hello.py --domain python -v

# Generate SQL schema
python sadhana.py hello.sadhana -o hello.sql --domain sql -v
```

### Screenshot: Successful Compilation

Here's what successful compilation looks like in your terminal:

#### HTML Backend Output:
```
============================================================
SADHANA COMPILATION RESULT
============================================================
Success: True
Domain: html
Bija: HTMEAppSMEFooFtSMEHeaHdSMEMainSMRc(App,HeaHd)...
CMK: 855fbf84210843d1f0f85fda6134732e...
Entities: 4
Relations: 3
Constraints: 0
Expansion: T0

[OK] Code written to: demo.html
[OK] Metadata saved to: demo.bija
```

#### Python Backend Output (Same .sadhana file!):
```
============================================================
SADHANA COMPILATION RESULT
============================================================
Success: True
Domain: python
Bija: HTMEAppSMEFooFtSMEHeaHdSMEMainSMRc(App,HeaHd)...
CMK: 855fbf84210843d1f0f85fda6134732e...
Entities: 4
Relations: 3
Constraints: 0
Expansion: T0

[OK] Code written to: demo.py
[OK] Metadata saved to: demo.bija
```

**Notice:** The same `.sadhana` file produces the same **Bija** and **CMK** across all backends - the meaning is preserved, only the output format changes!

### What Each Field Means:

```
Success: True          <-- Compilation successful!
Domain: html           <-- Target backend used
Bija: HTMEApp...       <-- Compressed semantic grammar
CMK: 855fbf84...       <-- Meaning fingerprint (invariant hash)
Entities: 4            <-- Number of entities in your code
Relations: 3           <-- Number of relationships defined
Constraints: 0         <-- Number of constraints (0 = no validation)
Expansion: T0          <-- Temporal level (T0 = minimal)
[OK] Code written...   <-- Output files generated
```

---

### Screenshot: Generated Output Files

After successful compilation, you'll have these files:

```bash
$ ls -la
-rw-r--r-- 1 user user  141200 Jan 01 12:00 sadhana.py      # Compiler
-rw-r--r-- 1 user user     245 Jan 01 12:00 demo.sadhana     # Your code
-rw-r--r-- 1 user user    1856 Jan 01 12:00 demo.html        # Generated HTML
-rw-r--r-- 1 user user    2104 Jan 01 12:00 demo.py          # Generated Python
-rw-r--r-- 1 user user     312 Jan 01 12:00 demo.bija        # Meaning metadata
```

#### Generated HTML (view in browser):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Sadhana Generated</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        .entity-app { background-color: hsl(45, 80%, 90%); ... }
        .entity-header { background-color: hsl(45, 80%, 90%); ... }
    </style>
</head>
<body>
    <div class="entity-app guna-sattva">
        <span class="label">App</span>
        <header class="entity-header guna-sattva">
            <span class="label">Header</span>
        </header>
        <main class="entity-main guna-sattva">
            <span class="label">Main</span>
        </main>
        <footer class="entity-footer guna-sattva">
            <span class="label">Footer</span>
        </footer>
    </div>
</body>
</html>
```

#### Generated Python (run with `python demo.py`):
```python
@dataclass
class App:
    """Semantic Entity: App, Guna: sattva, Pada: madhyaloka"""
    children: Dict[str, Any] = field(default_factory=dict)
    
    def add_child(self, name: str, child):
        self.children[name] = child

# ... Header, Main, Footer classes ...

def main():
    app_inst = App()
    header_inst = Header()
    main_inst = Main()
    footer_inst = Footer()
    
    app_inst.add_child("Header", header_inst)
    app_inst.add_child("Main", main_inst)
    app_inst.add_child("Footer", footer_inst)
    
    print("=== Application Ready ===")
    return {"App": app_inst, "Header": header_inst, ...}

if __name__ == '__main__':
    result = main()
```

#### Generated Bija Metadata (demo.bija):
```
Bija: HTMEAppSMEFooFtSMEHeaHdSMEMainSMRc(App,HeaHd)Rc(App,Main)Rc(App,FooFt)
CMK: 855fbf84210843d1f0f85fda6134732e
Domain: html
Entities: 4
Relations: 3
```

### Screenshot: Compilation Failure (What Errors Look Like)

If there's a problem, you'll see this instead:

```
============================================================
SADHANA COMPILATION RESULT
============================================================
Success: False                <-- PROBLEM!
Domain: html
Bija: HTMEHead...
CMK: ...
Entities: 4
Relations: 3
Constraints: 1
Expansion: T0

Errors:
  - Constraint violated: cardinality on Header_abc123
     <-- This tells you what to fix!

[NO output file generated]
```

**Visual Comparison:**

| ✅ Success | ❌ Failure |
|-----------|-----------|
| `Success: True` | `Success: False` |
| `[OK] Code written...` | `[NO output file generated]` |
| Files created | No files created |
| Ready to use | Needs fixing |

**Fix:** Check the [Troubleshooting Guide](#troubleshooting-guide) below!

---

## The Sanskrit Connection

### Panini's Influence on Computer Science

> *"Panini's grammar is one of the greatest monuments of human intelligence."* - **Leonard Bloomfield** (1927)

Sadhana draws deep inspiration from **Panini's Ashtadhyayi** (5th century BCE), the world's first formal system for describing a natural language:

| Panini's Concept | Sadhana Implementation |
|-----------------|----------------------|
| **Shiva Sutras** (Phonological rules) | Semantic Root Taxonomy (400+ roots) |
| **Gunas** (Sattva, Rajas, Tamas) | Visual/Lay classification system |
| **Sandhi** (Euphonic combination) | Sandhi Engine (composition gate) |
| **Sutra** (Aphoristic rule) | Option-Rule Engine |
| **Prakriya** (Derivational process) | Temporal Expansion (T0->T3) |
| **Vyakarana** (Grammar/Analysis) | Meaning Graph & CMK computation |

### The Three Gunas in Programming

From **Sankhya Philosophy**, Sadhana adopts the **Guna** system for classifying entities:

```
+----------------------------------------------------------+
|  SATTVA (Sattva Guna) - Illumination, Harmony           |
|  +-- Color: Gold/White                                   |
|  +-- Quality: Purity, knowledge, clarity                 |
|  +-- UI Mapping: Headers, titles, logos, hero sections   |
|  +-- Code Aspect: Public APIs, documentation             |
+----------------------------------------------------------+
|  RAJAS (Rajas Guna) - Activity, Passion                 |
|  +-- Color: Orange/Red                                   |
|  +-- Quality: Movement, action, desire                   |
|  +-- UI Mapping: Buttons, navigation, controls           |
|  +-- Code Aspect: Functions, methods, actions            |
+----------------------------------------------------------+
|  TAMAS (Tamas Guna) - Inertia, Darkness                 |
|  +-- Color: Dark/Black                                   |
|  +-- Quality: Stability, foundation, rest                |
|  +-- UI Mapping: Footers, backgrounds, shadows           |
|  +-- Code Aspect: Private methods, infrastructure        |
+----------------------------------------------------------+
```

### The Three Padas (Spatial Orientation)

```
    URDHVALOKA (Upper World)
    +-- Position: Top
    +-- Order: -1, -2, -3...
    +-- Element: header, nav, hero
         
    MADHYALOKA (Middle World) <- Default
    +-- Position: Center/Fill
    +-- Flex: 1 (expand to fill)
    +-- Element: main, content, body
         
    ADHOLOKA (Lower World)
    +-- Position: Bottom
    +-- Order: 999, 1000...
    +-- Element: footer, bottom-bar
```

---

## 20-Layer Architecture

Sadhana implements a **20-layer semantic computing framework**, each layer building upon the previous:

```
+----------------------------------------------------------------+
| LAYER 20: Meta-Layer (Self-Reference)                          |
|         +-- Grammar of grammars, self-validation                |
+----------------------------------------------------------------+
| LAYER 19: Execution Backends (Multi-Target)                    |
|         +-- HTML, Python, SQL, Rust, Go, Java, C++             |
+----------------------------------------------------------------+
| LAYER 18: Causal & Provenance Runtime                          |
|         +-- Dependency tracking, reverse debugging              |
+----------------------------------------------------------------+
| LAYER 17: Deferred Mutation & Versioning                       |
|         +-- Lock invariants, mutation channels                  |
+----------------------------------------------------------------+
| LAYER 16: Type/Role/Capability Inference                       |
|         +-- Emergent type detection, role stabilization         |
+----------------------------------------------------------------+
| LAYER 15: Structural Resonance Compiler                        |
|         +-- Pattern detection, backend affinity scoring         |
+----------------------------------------------------------------+
| LAYER 14: Semantic Membrane (Execution Firewall) *            |
|         +-- Blocks imaginary/unsafe meanings                    |
+----------------------------------------------------------------+
| LAYER 13: Sanhara Engine (Non-Committal Simulation) *         |
|         +-- Test scenarios, measure semantic debt               |
+----------------------------------------------------------------+
| LAYER 12: Topological Meaning Space                            |
|         +-- Meaning manifold, singularity detection             |
+----------------------------------------------------------------+
| LAYER 11: Temporal-Structural Expansion (Kala)                 |
|         +-- T0->T1->T2->T3 expansion pipeline                      |
+----------------------------------------------------------------+
| LAYER 10: Option-Rule Engine (Gated Decompression)            |
|         +-- Quantum-gate-like conditional rules                 |
+----------------------------------------------------------------+
| LAYER 9:  Sandhi Engine (Composition Gate) *                  |
|         +-- Mandatory composition: >=2 meanings + >=1 root      |
+----------------------------------------------------------------+
| LAYER 8:  Global Root Operators                                |
|         +-- Coherence, Composition, Imagination, etc.          |
+----------------------------------------------------------------+
| LAYER 7:  Bija Layer (Meta-Compression) *                     |
|         +-- Reversible semantic grammar encoding                |
+----------------------------------------------------------------+
| LAYER 6:  Semantic Reduction                                   |
|         +-- Meaning compression algorithms                      |
+----------------------------------------------------------------+
| LAYER 5:  Canonical Meaning Kernel (CMK) *                    |
|         +-- Invariant fingerprint: 5-part hash                  |
+----------------------------------------------------------------+
| LAYER 4:  Meaning Graph Layer (Hypergraph) *                  |
|         +-- Entities + Relations + Constraints                  |
+----------------------------------------------------------------+
| LAYER 3:  Semantic Primitives                                  |
|         +-- Guna & Pada classification                          |
+----------------------------------------------------------------+
| LAYER 2:  Dhatu Layer (8 Mandatory Semantic Laws) *           |
|         +-- Identity, Constraints, Non-Contradiction...        |
+----------------------------------------------------------------+
| LAYER 1:  Ontological Foundation                               |
|         +-- Entity, Container, Interface, Function types       |
+----------------------------------------------------------------+
| LAYER 0:  Axiomatic Layer (5 Core Axioms)                     |
|         +-- Meaning-first, Order-free, Time-latent...          |
+----------------------------------------------------------------+
```

### * Key Innovation Layers

| Layer | Innovation | Novel Concept |
|-------|-----------|---------------|
| **5** | **CMK (Canonical Meaning Kernel)** | Invariant 5-part hash that survives all transformations |
| **7** | **Bija System** | Sanskrit-inspired semantic grammar encoding (NOT a hash) |
| **9** | **Sandhi Engine** | Mandatory composition gate requiring >=2 meanings + >=1 root |
| **13** | **Sanhara Engine** | Non-committal simulation with semantic debt measurement |
| **14** | **Semantic Membrane** | Execution firewall blocking imaginary meanings |

---

## Language Syntax Guide

### 1. Directives (Header Configuration)

Directives start with `@` and go at the **TOP** of your file.

#### Required Directives:

```sadhana
@domain: html      # REQUIRED - Target output language
                  # Options: html, python, sql, rust, go, java, cpp

@title: My App     # RECOMMENDED - Name of your application
```

#### Optional Directives:

```sadhana
@expansion: 2      # Temporal expansion level (0-3)
                  # 0 = minimal (default)
                  # 1 = add skeleton structures
                  # 2 = add Guna/Pada variants  
                  # 3 = full archetype expansion
```

#### Complete Example:

```sadhana
# === HEADER (directives first!) ===
@domain: python
@title: My Task Manager
@expansion: 1

# === BODY (entities and relations) ===
App
Task

App contains Task
```

#### Changing Domain = Different Output:

**File: `universal.sadhana`:**
```sadhana
@domain: html      # Change this to: python, sql, rust, go, java, cpp
@title: My App

Container
Item

Container contains Item
```

**Compile to all backends:**
```bash
# Same .sadhana file, 7 different outputs!
python sadhana.py universal.sadhana -o out.html --domain html
python sadhana.py universal.sadhana -o out.py --domain python
python sadhana.py universal.sadhana -o out.sql --domain sql
python sadhana.py universal.sadhana -o out.rs --domain rust
python sadhana.py universal.sadhana -o out.go --domain go
python sadhana.py universal.sadhana -o out.java --domain java
python sadhana.py universal.sadhana -o out.cpp --domain cpp
```

### 2. Entity Declaration

Entities are **Capitalized names** (PascalCase by convention).

#### Basic Syntax:
```sadhana
# One entity per line
Header
Navigation
Button
Footer
```

#### Naming Rules:
```sadhana
# ✅ CORRECT - Capitalized
Header
MainContent
UserProfile
AuthService

# ❌ WRONG - lowercase
header          # ERROR!
mainContent     # ERROR!
user_profile    # ERROR!
```

#### Auto-Detected Guna (Quality) by Name:
```sadhana
# These become SATTVA (illumination, harmony)
Header          # detected by "Header"
Hero            # detected by "Hero"
Logo            # detected by "Logo"
Title           # detected by "Title"

# These become RAJAS (activity, passion)
Button          # detected by "Button"
Navigation      # detected by "Nav"
Action          # detected by "Action"
Link            # detected by "Link"

# These become TAMAS (stability, foundation)
Footer          # detected by "Footer"
Background      # detected by "Background"
Shadow          # detected by "Shadow"
Base            # detected by "Base"
```

**Note:** Guna detection is automatic based on keyword matching. You don't need to specify it!

### 3. Relations

Define how entities connect. **Order does NOT matter!**

#### Valid Relation Keywords:

| Relation | Meaning | Backend Mapping |
|----------|---------|-----------------|
| `contains` | Parent-child containment | HTML: nested elements<br>Python: class composition<br>SQL: foreign key |
| `requires` | Dependency needed | All: constructor injection |
| `enables` | Capability activation | All: method calls |
| `depends` | Soft dependency | All: reference |
| `extends` | Inheritance | Python/Java: class extends<br>Others: composition |
| `implements` | Interface fulfillment | Java: implements<br>Others: abstract base |

#### Syntax:
```sadhana
# Format: Entity relation Entity
# Both entities MUST be declared first!

# ✅ CORRECT
Header
Nav
Header contains Nav

# ❌ WRONG - Nav not declared!
Header contains Nav
Nav
```

#### Examples by Backend:

```sadhana
# Universal example (works for ALL backends)
App
Database
Service

App contains Service      # HTML: <app><service></service></app>
                          # Python: App.service = Service()
                          # SQL: service.app_id foreign key

Service requires Database # HTML: data-requires="database"
                          # Python: Service.__init__(self, db)
                          # SQL: service.database_id foreign key
```

#### Order Independence:
```sadhana
# These are IDENTICAL - Sadhana doesn't care about order!

# Version A
A contains B
B contains C

# Version B  
B contains C
A contains B

# Version C
C
B
A
A contains B
B contains C

# All produce the SAME CMK (meaning fingerprint)!
```

### 4. Constraints (IMPORTANT - READ CAREFULLY)

Constraints **validate** your structure. If violated, compilation **FAILS** (Semantic Membrane blocks execution).

#### How Constraints Work

```sadhana
# This constraint counts children with EXACT NAME MATCH
Constraint: Header must have exactly 2 Navigation

# Meaning: Header must contain EXACTLY 2 children named "Navigation"
# NOT 2 children total, but 2 named "Navigation"
```

#### WRONG Example (Will Fail):
```sadhana
Header
Nav1
Nav2
Hero

Header contains Nav1
Header contains Nav2
Header contains Hero

# ❌ ERROR! Header has 0 children named "Navigation"
# It has Nav1 and Nav2, not "Navigation"
Constraint: Header must have exactly 2 Navigation
```

#### CORRECT Example (Will Pass):
```sadhana
Header
Navigation
Navigation  # Same name = same type
Hero

Header contains Navigation
Header contains Navigation  # First Navigation child
Header contains Hero

# ✅ SUCCESS! Header has exactly 2 children named "Navigation"
Constraint: Header must have exactly 2 Navigation
```

#### Valid Constraint Patterns:

```sadhana
# Exact count
Constraint: Container must have exactly 3 Item

# Minimum count
Constraint: Page must have at least 1 Footer

# Maximum count  
Constraint: Sidebar must have at most 5 Widget

# One child
Constraint: Header must have exactly one Logo
```

#### BEGINNER TIP:
**Skip constraints until you're comfortable!** They are optional. Start with just entities and relations:

```sadhana
@domain: html
@title: Simple Page

Header
Nav
Main
Footer

Header contains Nav
Body contains Header
Body contains Main
Body contains Footer
# No constraints = no validation errors!
```

### 5. Roots Declaration (Optional)

Roots are **semantic operators** that guide code generation style.

#### Syntax (NO colon!):
```sadhana
# ✅ CORRECT - no colon, space-separated
Roots Composition Coherence

# ❌ WRONG - don't use colons or commas
Roots: Composition, Coherence
```

#### Available Global Roots:

| Root | Effect | When to Use |
|------|--------|-------------|
| `Composition` | Build structures from parts | Default - always safe |
| `Coherence` | Ensure consistency | When structure must be unified |
| `Normalization` | Standardize forms | Database schemas |
| `Abstraction` | Generalize patterns | Framework design |
| `Analogy` | Pattern transfer | Converting between domains |
| `Equivalence` | Identify sameness | Merging similar entities |
| `Imagination` | **FORBIDDEN** | Never use - blocked by Semantic Membrane |

#### Example:
```sadhana
@domain: sql
@title: Database Schema

Customer
Order

Customer contains Order

# Use these roots for database design
Roots Composition Normalization
```

**Note:** Roots are optional! If unsure, just use `Roots Composition` or skip entirely.

---

## Code Examples

### COMPLETE BEGINNER'S GUIDE

#### BEFORE YOU START - The Golden Rules of Sadhana

```
RULE 1: Entities are Capitalized (Header, not header)
RULE 2: Keywords are lowercase (contains, not Contains)
RULE 3: Constraints MUST match your relations exactly
RULE 4: Use -v flag ALWAYS to see errors
RULE 5: When in doubt, remove constraints first
```

---

### Example 1: Universal App Structure (Works with ALL Backends)

**File: `app.sadhana`** - One file, compiles to HTML, Python, SQL, Rust, Go, Java, and C++!

```sadhana
@domain: html
@title: Task Manager Application

# ============================================================
# UNIVERSAL ENTITY DECLARATIONS
# These work across ALL backends (HTML, Python, SQL, etc.)
# ============================================================

# Main Application Container
Application

# UI Layer (becomes HTML elements, Python classes, SQL tables)
Dashboard
TaskList
TaskItem
UserProfile

# Data Layer (becomes database tables, class properties)
Database
User
Task

# Control Layer (becomes methods, functions, APIs)
AuthService
TaskManager

# ============================================================
# RELATIONSHIPS (hierarchy and dependencies)
# Format: Entity relation Entity
# Valid relations: contains, requires, enables, depends, extends, implements
# ============================================================

# Application hierarchy
Application contains Dashboard
Application contains AuthService
Dashboard contains TaskList
Dashboard contains UserProfile
TaskList contains TaskItem

# Data hierarchy
Database contains User
Database contains Task

# Service dependencies
AuthService requires Database
TaskManager requires Database
TaskManager enables TaskList
User enables TaskItem

# ============================================================
# CONSTRAINTS (OPTIONAL - remove if causing errors)
# Format: Constraint: Target must have [quantifier] [Count] [EntityType]
# Valid quantifiers: exactly, at least, at most
# ============================================================

# This constraint says: TaskList must have minimum 1 TaskItem
# Constraint: TaskList must have at least 1 TaskItem

# This constraint says: Application must have exactly 1 Database
# Constraint: Application must have exactly 1 Database

# ============================================================
# ROOTS (semantic operators - OPTIONAL)
# These guide code generation style
# ============================================================
Roots Composition Coherence
```

#### Compile to ALL 7 Backends:

```bash
# 1. HTML/CSS (for web UI)
python sadhana.py app.sadhana -o app.html --domain html -v

# 2. Python (for backend logic)
python sadhana.py app.sadhana -o app.py --domain python -v

# 3. SQL (for database schema)
python sadhana.py app.sadhana -o app.sql --domain sql -v

# 4. Rust (for systems programming)
python sadhana.py app.sadhana -o app.rs --domain rust -v

# 5. Go (for microservices)
python sadhana.py app.sadhana -o app.go --domain go -v

# 6. Java (for enterprise)
python sadhana.py app.sadhana -o app.java --domain java -v

# 7. C++ (for high-performance)
python sadhana.py app.sadhana -o app.cpp --domain cpp -v
```

**All 7 files generated from ONE .sadhana source!**

---

### Example 2: Database Schema (SQL Backend)

**File: `ecommerce.sadhana`**

```sadhana
@domain: sql
@title: E-Commerce Database Schema

# STEP 1: Declare entities (becomes SQL tables)
Customer
Order
Product
Category
OrderItem
Payment

# STEP 2: Define relationships (becomes foreign keys)
# "contains" = parent-child (foreign key in child table)
Customer contains Order
Order contains OrderItem

# "requires" = dependency relationship
Order requires Payment
Product requires Category

# NOTE: These constraints are commented out because they would fail
# with the current simple example. Uncomment only if you have
# the matching entity names!

# Constraint: Order must have at least 1 OrderItem
# Constraint: Product must have exactly 1 Category
```

**Compile:**
```bash
python sadhana.py ecommerce.sadhana -o schema.sql --domain sql -v
```

**Generated Output:** Creates SQL tables with proper foreign key relationships!

**Generated SQL (excerpt):**
```sql
-- Generated by Sadhana v1.0

CREATE TABLE customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    guna VARCHAR(20) DEFAULT 'sattva',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL,
    guna VARCHAR(20) DEFAULT 'rajas',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Relation: customer contains order
ALTER TABLE order 
    ADD COLUMN customer_id INTEGER,
    ADD FOREIGN KEY (customer_id) 
    REFERENCES customer(id);
```

---

### Example 3: Python Application

**File: `taskapp.sadhana`**

```sadhana
@domain: python
@title: Task Management App

# Entities become Python classes
Application
TaskManager
Task
User
AuthService
Database

# Relations become class compositions and dependencies
Application contains TaskManager
Application contains AuthService
TaskManager contains Task
TaskManager requires Database
AuthService requires Database
User enables Task
```

**Compile:**
```bash
python sadhana.py taskapp.sadhana -o taskapp.py --domain python -v
```

**Run the generated Python:**
```bash
python taskapp.py
```

**Output:**
```
=== Sadhana Generated Application ===
  Created: Application = <__main__.Application object>
  Created: TaskManager = <__main__.TaskManager object>
  ...
```

---

### Example 4: Temporal Expansion Demo (T0 -> T3)

**File: `expand.sadhana`**

```sadhana
@domain: html
@title: Expansion Demo

# Simple structure that expands
Container
Child

Container contains Child
```

**Compile with different expansion levels:**

```bash
# T0: Seed (basic structure only)
python sadhana.py expand.sadhana -o t0.html -e 0 -v
# Output: 2 entities

# T1: Fundamental (adds skeleton entities)
python sadhana.py expand.sadhana -o t1.html -e 1 -v
# Output: ~10+ entities (adds Structure containers)

# T2: Variation (adds Guna x Pada combinations)
python sadhana.py expand.sadhana -o t2.html -e 2 -v
# Output: ~20+ entities (Sattva/Madhyaloka variants, etc.)

# T3: Full expansion (adds archetypes)
python sadhana.py expand.sadhana -o t3.html -e 3 -v
# Output: ~50+ entities (with archetype instantiations)
```

**What is Temporal Expansion?**
- **T0**: Your original meaning (compressed)
- **T1**: Add structural skeletons (implementation details)
- **T2**: Add quality variants (Sattva/Rajas/Tamas combinations)
- **T3**: Full archetype expansion (complete variant space)

---

### Example 5: Simulation Mode (Testing Without Output)

Test your meaning without generating code:

```bash
python sadhana.py app.sadhana --simulate -v
```

This validates:
- [x] Topological validity (no circular containment)
- [x] Constraint satisfaction
- [x] CMK preservation
- [x] Semantic Membrane checks

**Use this to debug before generating actual code!**

---

## Troubleshooting Guide

### Common Errors and Solutions

#### Error 1: "Constraint violated: cardinality"

**Problem:** Your constraint doesn't match your relations.

**Example that FAILS:**
```sadhana
Header
Nav

Header contains Nav

# ❌ WRONG: Header has 1 "Nav", not "Navigation"
Constraint: Header must have exactly 1 Navigation
```

**Fix:**
```sadhana
Header
Navigation

Header contains Navigation

# ✅ CORRECT: Name matches exactly
Constraint: Header must have exactly 1 Navigation
```

**OR:** Remove the constraint entirely!

---

#### Error 2: "Parser error at Lx:y: Expected NAME"

**Problem:** Syntax error in your .sadhana file.

**Common causes:**
1. Using lowercase for entity names (`header` instead of `Header`)
2. Missing entity declarations before using in relations
3. Wrong relation keywords

**Fix:**
```sadhana
# ❌ WRONG
header          # must be Header
nav             # must be Nav
header nav      # missing 'contains'

# ✅ CORRECT
Header
Nav
Header contains Nav
```

---

#### Error 3: "No entities found"

**Problem:** File is empty or all lines are comments.

**Fix:** Ensure you have actual entity declarations:
```sadhana
# This file has NO entities (all comments or blank)
# Header
# Nav

# ✅ CORRECT - uncomment:
Header
Nav
```

---

#### Error 4: "Execution blocked: Forbidden root detected"

**Problem:** You used `Imagination` root which is forbidden.

**Fix:** Use valid roots only:
```sadhana
# ❌ FORBIDDEN
Roots: Imagination

# ✅ ALLOWED
Roots: Composition Coherence
```

---

#### Error 5: "Success: False" but no error message shown

**Problem:** You forgot the `-v` (verbose) flag.

**Fix:** Always use `-v`:
```bash
# ❌ No error details
python sadhana.py app.sadhana -o app.html

# ✅ Full error details
python sadhana.py app.sadhana -o app.html -v
```

---

### Quick Debugging Checklist

Before asking for help, check:

- [ ] Using `-v` flag to see full output?
- [ ] Entity names are Capitalized?
- [ ] Relation keywords are lowercase (`contains`, not `Contains`)?
- [ ] Constraint names match entity names exactly?
- [ ] No `Imagination` in Roots?
- [ ] File is saved and not empty?
- [ ] Python 3.8+ installed?

---

### Minimal Working Example (Copy-Paste This)

If nothing works, start with this guaranteed working file:

**`test.sadhana`:**
```sadhana
@domain: html
@title: Test Page

Header
Main
Footer

Body contains Header
Body contains Main
Body contains Footer
```

**Compile:**
```bash
python sadhana.py test.sadhana -o test.html -v
```

**Expected Output:**
```
Success: True
Entities: 3
Relations: 3
[OK] Code written to: test.html
```

---

## Multi-Target Backends

Sadhana generates code for **7 different target languages**:

| Backend | Extension | Best For | Command |
|---------|-----------|----------|---------|
| **HTML/CSS** | `.html` | Web interfaces, UI prototypes | `--domain html` |
| **Python** | `.py` | Data models, application structure | `--domain python` |
| **SQL** | `.sql` | Database schemas | `--domain sql` |
| **Rust** | `.rs` | Systems programming, ownership semantics | `--domain rust` |
| **Go** | `.go` | Concurrent services, simple compositions | `--domain go` |
| **Java** | `.java` | Enterprise OOP patterns | `--domain java` |
| **C++** | `.cpp` | Memory-managed systems | `--domain cpp` |

### Backend Affinity Scoring

The Structural Resonance Compiler (Layer 15) scores how well a structure fits each backend:

```
HTML:   +0.1 for each Container entity
        +0.05 for each Sattva entity
        Optimal for: Hierarchical UI structures

Python: +0.2 if entities > 3
        +0.05 for each "contains" relation
        Optimal for: Data models, clear hierarchies

SQL:    +0.1 for each "contains"/"requires" relation
        Optimal for: Relational data structures
```

---

## Novelty & Research Contributions

### 1. Meaning-First Programming Paradigm

> **Problem:** Traditional programming forces developers to think in syntax and execution order, losing semantic intent in implementation details.
>
> **Solution:** Sadhana separates *meaning specification* from *structural implementation*. You declare what exists and how they relate; the compiler determines optimal representation.

### 2. The CMK (Canonical Meaning Kernel)

A **5-part invariant hash** that survives all transformations:

```python
CMK = {
    structure:   "Entity topology hash",      # What exists
    behavior:    "Relation pattern hash",     # How they connect
    constraints: "Constraint core hash",      # Rules governing
    role:        "Semantic role signature",   # Domain + roots
    synthesis:   "Master hash"                # Combined invariant
}
```

**Key Property:** Any valid transformation must preserve the CMK. If CMK changes, the transformation is invalid.

### 3. Bija System - Semantic Grammar Encoding

Unlike hashes (one-way), **Bija** is a **reversible semantic grammar**:

```
Example Bija: HTMEHeadSATMENaviRAJMEFootTAM

Breakdown:
- HTM          : Domain prefix (HTML)
- EHeadSATM    : Entity "Header", Sattva Guna, Madhyaloka
- ENaviRAJM    : Entity "Navigation", Rajas Guna, Madhyaloka
- EFootTAM     : Entity "Footer", Tamas Guna, Madhyaloka
```

**Properties:**
- Variable length (not fixed like hashes)
- Reversible to meaning skeleton
- CMK collision detection
- Compression ratio: ~10:1 vs full graph

---

#### How to Decode Bija (Python API)

You can programmatically decode Bija strings back to meaning skeletons:

```python
from sadhana import BijaSystem, MeaningGraph

# Create Bija system
bija_system = BijaSystem()

# Example: Encode a meaning graph to Bija
graph = MeaningGraph()
graph.domain = "html"
header = graph.add_entity("Header")
nav = graph.add_entity("Nav")
graph.add_relation("contains", [header.uid, nav.uid])

# Encode to Bija
bija = bija_system.encode(graph)
print(f"Bija: {bija}")
# Output: HTMEHeaHdSMENavNvSMERc(HeaHd,NavNv)

# Decode back to skeleton
skeleton = bija_system.decode_to_skeleton(bija)
print(f"Domain: {skeleton['domain']}")
print(f"Entities: {[e['code'] for e in skeleton['entities']]}")
print(f"Relations: {[r['code'] for r in skeleton['relations']]}")
```

**Decoding Output Format:**
```python
{
    'domain': 'html',           # Extracted from HTM prefix
    'entities': [
        {'code': 'HeaHdSM', 'type': 'entity'},    # Header, Sattva, Madhyaloka
        {'code': 'NavNvSM', 'type': 'entity'}     # Nav, default Guna/Pada
    ],
    'relations': [
        {'code': 'Rc(HeaHd,NavNv)'}  # contains relation between Header and Nav
    ],
    'constraints': []
}
```

**Bija Grammar Tokens:**

| Token | Meaning | Example |
|-------|---------|---------|
| `HTM` | HTML domain | `HTM...` |
| `PYT` | Python domain | `PYT...` |
| `SQL` | SQL domain | `SQL...` |
| `E` | Entity start | `EHeaHd...` |
| `S/A/T` | Guna (Sattva/Rajas/Tamas) | `EHeadSATM` |
| `U/M/D` | Pada (Urdhvaloka/Madhyaloka/Adholoka) | `EHeadSATM` |
| `R` | Relation | `Rc(...)` |
| `c/r/e/d/x/i` | Relation type | `Rc` = contains, `Rr` = requires |
| `C` | Constraint | `C[...]` |

**Command Line Decoding:**

```bash
# After compilation, a .bija file is automatically created
python sadhana.py app.sadhana -o app.html -v

# View the Bija file
cat app.bija
# Bija: HTMEAppSMESer...
# CMK: a3f7c2b8d9e1f4a5...
```

**Use Cases for Decoding:**
1. **Version Control**: Compare meaning structures without full code diff
2. **Semantic Search**: Find similar architectures by Bija patterns
3. **Verification**: Ensure transmitted meaning wasn't corrupted
4. **Translation**: Convert Bija to other semantic representations

### 4. Sandhi Engine - Mandatory Composition

Prevents invalid meaning merges through strict rules:

```
To compose meanings through Sandhi:
1. Must have >= 2 input meanings
2. Must specify >= 1 Global Root
3. No implicit merge allowed
4. Constraints must harmonize
5. CMK lineage must be tracked
```

### 5. Sanhara Engine - Non-Committal Simulation

**Quantum-computing-inspired** simulation without commitment:

```python
# Fork the meaning graph
fork = graph.copy()

# Apply operation to fork
result = operation(fork)

# Measure semantic debt
debt = measure_cmk_drift(graph, fork)

# If debt acceptable, merge; else discard
if debt < threshold:
    commit(fork)
else:
    discard(fork)  # Original unchanged
```

**Applications:**
- A/B testing structures
- Refactoring safety checks
- Constraint validation
- Optimization exploration

### 6. Semantic Membrane - Execution Firewall

Blocks execution if:
- [ ] Meaning is imaginary (contains "Imagination" root)
- [ ] Meaning is abstract but uninstantiated
- [ ] Constraints are violated
- [ ] Forbidden roots present
- [ ] CMK mismatch detected

```sadhana
# This will be BLOCKED:
Roots: Imagination  # NEVER executes
Entity: Unicorn
```

### 7. Temporal Expansion (Kala)

Time as a **parameter** rather than embedded state:

| Level | Name | Structures | Description |
|-------|------|------------|-------------|
| T0 | Seed | Original | Compressed meaning |
| T1 | Fundamental | +64 | Add structural skeletons |
| T2 | Variation | +128 | Guna x Pada combinations |
| T3 | Full | +256 | Archetype instantiations |

### 8. Order-Independence through Meaning Graphs

Sadhana uses **hypergraphs** where:
- Nodes = Semantic entities
- Hyperedges = Relations (connect any number of entities)
- **No inherent ordering** - topology defines structure

```sadhana
# These are IDENTICAL in meaning:
A contains B
B requires C

# Same as:
B requires C
A contains B

# Same as:
# (Any permutation produces same CMK)
```

### 9. Sanskrit-Inspired Formal System

First programming language to systematically apply:
- **Panini's rule-based grammar** (Ashtadhyayi)
- **Sankhya's Guna theory** for classification
- **Nyaya's logic** for constraint validation
- **Vedanta's non-duality** in meaning preservation

### 10. Neural Network Exclusion

**Explicitly designed WITHOUT neural networks** in core:

```python
# Forbidden patterns (blocked by Meta-Layer):
NN_PATTERNS = [
    'neural', 'network', 'deep', 'gradient', 
    'backprop', 'training_step', 'tensor', 'layer_norm'
]
```

**Rationale:** AGI research needs formal, verifiable foundations. Neural networks are powerful but opaque; Sadhana provides a **transparent, mathematically rigorous** alternative for structural reasoning.

---

## About the Author

**Manish Parihar** is a researcher and developer exploring the intersection of:
- Ancient Indian Linguistics & Philosophy
- Artificial General Intelligence
- Programming Language Design
- Computational Semantics

### Connect With Me

[![GitHub](https://img.shields.io/badge/GitHub-nickzq7-black?style=flat-square&logo=github)](https://github.com/nickzq7)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Manish%20Parihar-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/manish-parihar-899b5b23a/)
[![Blog](https://img.shields.io/badge/Blog-manishkparihar-orange?style=flat-square&logo=blogger)](https://manishkparihar.blogspot.com/)
[![YouTube](https://img.shields.io/badge/YouTube-@ProgramDr-red?style=flat-square&logo=youtube)](https://www.youtube.com/@ProgramDr)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0002--1900--8945-green?style=flat-square)](https://orcid.org/0009-0002-1900-8945)

### Research Interests

- Semantic Computing Frameworks
- Sanskrit & Paninian Grammar in CS
- Constraint-Based Code Generation
- Meaning-First Programming Paradigms
- AGI Architecture Design

---

## Further Reading

### Sanskrit & Linguistics
- [Panini's Ashtadhyayi](https://en.wikipedia.org/wiki/Ashtadhyayi) - The world's first formal grammar
- [Sankhya Philosophy](https://en.wikipedia.org/wiki/Samkhya) - Dualistic realism, Guna theory
- [Bhagavad Gita Chapter 14](https://www.holy-bhagavad-gita.org/chapter/14) - The three Gunas

### Programming Language Theory
- [Constraint Programming](https://en.wikipedia.org/wiki/Constraint_programming)
- [Hypergraph Data Models](https://en.wikipedia.org/wiki/Hypergraph)
- [Formal Language Theory](https://en.wikipedia.org/wiki/Formal_language)

### Code Generation & AGI
- [Fifth-Generation Programming](https://en.wikipedia.org/wiki/Fifth-generation_programming_language)
- [Generative Grammar (Chomsky)](https://en.wikipedia.org/wiki/Generative_grammar)
- [Code Generation for AGI](https://blog.apiad.net/p/llm-code-generation)

---

## Contributing

Contributions welcome! Areas of interest:

- Additional backends (TypeScript, Swift, Kotlin, etc.)
- Documentation improvements
- Test cases and examples
- IDE support (syntax highlighting)
- Research collaborations

Please ensure contributions respect the **core axioms** - especially the **no neural networks in core** principle.

**Repository Structure:**
```
sadhana/
├── sadhana.py          # Main compiler (single file, ~3,600 lines)
├── README.md           # This documentation
└── examples/           # Example .sadhana files (optional)
```

The entire compiler is in **one file** (`sadhana.py`) for easy distribution and understanding. No build process needed!

---

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024-2026 Manish Parihar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

**You are free to:**
- ✅ Use in personal projects
- ✅ Use in commercial applications  
- ✅ Modify and distribute
- ✅ Include in proprietary software
- ✅ Sublicense to others

**Requirements:**
- Include the original copyright notice
- Include the MIT license text

This is open source software. Use it anywhere, for anything, without asking permission!

---

## Acknowledgments

- **Maharshi Panini** (5th c. BCE) - For the Ashtadhyayi, the world's first formal system
- **Kapila Muni** - For Sankhya philosophy and the Guna theory
- **Sri Krishna** - For teaching the Gunas in the Bhagavad Gita
- **Noam Chomsky** - For generative grammar and formal language theory
- **Leonard Bloomfield** - For recognizing Panini's genius

---

## Conclusion

> *"The Supreme Lord said: The three Gunas - Sattva, Rajas, and Tamas - born of Prakriti, bind the imperishable soul to the body."* - **Bhagavad Gita 14.5**

Sadhana is more than a programming language-it is a **philosophical framework** for computation. By returning to the wisdom of ancient Indian linguistics while pushing the boundaries of modern code generation, we create a tool that thinks about software the way humans think about meaning: **holistically, relationally, and semantically**.

**Idea - Manish Kumar Parihar**
**Research - Manish Kumar Parihar**
**Assembler - Manish Kumar Parihar**
**Reasoning - Manish Kumar Parihar**
**Quality Check - Manish Kumar Parihar**
**Study - Manish Kumar Parihar**
**Framework Design - Manish Kumar Parihar**
**Coder - AI(75%) + Online Reference (10%) + Manish Kumar Parihar (15%)**




**Welcome to the future of programming. Welcome to Sadhana.**

---

<p align="center">
  <strong>SADHANA - The Path to Meaningful Code</strong>
</p>

<p align="center">
  Made with love by <a href="https://github.com/nickzq7">Manish Parihar</a>
</p>
