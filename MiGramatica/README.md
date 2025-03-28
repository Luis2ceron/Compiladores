# For Loop Analysis with ANTLR4

## Project Overview
This project demonstrates the implementation of Listener and Visitor patterns using ANTLR4 to analyze and simulate for loops in a custom grammar.

## Prerequisites
- Python 3.8+
- ANTLR4
- antlr4-python3-runtime

## Project Structure
- `MiGramatica.g4`: ANTLR grammar definition
- `MyListener.py`: Listener implementation for for loop detection
- `EvalVisitor.py`: Visitor implementation for for loop simulation
- `test_listener.py`: Unit tests for Listener
- `test_visitor.py`: Unit tests for Visitor

## Setup and Generation
1. Generate ANTLR Parser:
```bash
antlr4 -Dlanguage=Python3 MiGramatica.g4
```

## Running Tests
```bash
python3 -m unittest test_listener.py
python3 -m unittest test_visitor.py
```

## Features
- Detect for loop structures
- Simulate for loop execution
- Track variable states during loop iterations