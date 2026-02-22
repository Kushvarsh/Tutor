📘 LLM Math Tutor using LangChain + Groq

An AI-powered Math Tutor built using LangChain, Groq LLM, and Output Parsers to generate structured, step-by-step solutions to mathematical problems.

This project demonstrates how to build a reliable LLM application using Prompt Engineering and Structured Output Parsing without using agents or RAG.

🚀 Project Overview

Large Language Models (LLMs) generate powerful responses, but their outputs are often unstructured and inconsistent. In real-world applications, especially in education and automation systems, we need responses in a predictable and structured format.

This project solves that problem by:

Designing strong system prompts

Enforcing structured JSON output

Validating responses using Output Parsers

Displaying results in a clean Streamlit interface

The result is a math tutor that not only solves problems but explains them step-by-step in a structured format.

🎯 Objective

The main objectives of this project are:

1.To control LLM output using structured schemas

2.To generate step-by-step mathematical explanations

3.To ensure consistent JSON responses

4.To build an interactive AI-powered educational tool

🧠 How the System Works
1. User Input

   The user enters a mathematical question in the Streamlit interface.

2. Prompt Engineering

   A carefully designed system prompt instructs the LLM to:

     Solve the problem step-by-step

     Return the answer strictly in JSON format

     Follow a predefined response schema

3. Output Parsing

   Using PydanticOutputParser, the application:

   Defines the expected response structure

   Validates model output

   Ensures structured and clean data

4. Response Display

   The structured response is displayed as:

   Problem

   Step-by-step solution

   Final answer

🏗️ Tech Stack

1.Python

2.LangChain

3.Groq LLM

4.Pydantic

5.Streamlit

6.python-dotenv

📂 Project Structure

-LLM-Math-Tutor/

-app.py — Streamlit user interface

-Tutor.py — LLM logic, prompt design, and output parser

-requirements.txt — Project dependencies

-.env — API key configuration

README.md — Project documentation
