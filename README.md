# 🚀 Git-to-B2B Changelog Generator

A smart Python automation tool that bridges the gap between engineering updates and B2B marketing[cite: 1]. It automatically transforms technical Git commit logs into executive-ready, ROI-focused product announcements using Google's `gemini-2.5-flash` model[cite: 1].

---

## 📌 Project Overview

### 🏷️ Project Name
Git-to-B2B Changelog Generator[cite: 1]

### 💡 What It Does
Extracts raw GitHub commits and turns technical code changes into clear, compelling B2B updates tailored for stakeholders, clients, and marketing teams[cite: 1].

### 🚨 Problem It Solves
Engineering teams release features constantly, but enterprise clients often miss their true value because technical updates are filled with jargon[cite: 1]. This tool automates the translation process, saving hours of manual rewriting while making sure every update highlights business impact[cite: 1, 2].

---

## 🎯 STAR Overview

* 🏢 **Situation:** B2B companies ship features rapidly, but marketing teams struggle to translate technical code logs into enterprise-ready messaging[cite: 1].
* 🎯 **Task:** Automate the pipeline to convert raw technical commits into value-driven product updates for executive buyers[cite: 1].
* ⚡ **Action:** Built a Python backend using `PyGithub` for commit fetching and `gemini-2.5-flash` to extract and structure ROI-focused content[cite: 1].
* 📈 **Result:** Cut changelog creation time from hours to seconds while delivering accurate, strategic announcements[cite: 1, 2].

---

## ✨ Key Features

* 📡 **Automated Commit Fetching:** Instantly fetches the latest commits from any public GitHub repository[cite: 1, 2].
* 🧠 **Value-Driven AI Translation:** Uses Gemini 2.5 Flash to emphasize real-world business impact and customer benefits instead of raw code syntax[cite: 1, 2].
* 📊 **Executive-Ready Output:** Generates structured announcements complete with headlines, key business highlights, technical summaries, and clear calls-to-action[cite: 1, 2].

---

## 🛠️ Tech Stack

* 🐍 **Language:** Python 3.9+[cite: 2]
* 🤖 **AI Engine:** Google GenAI SDK (`gemini-2.5-flash`)[cite: 2]
* 🐙 **GitHub API:** PyGithub[cite: 2]

---

## 🚀 Getting Started

### 1. 📥 Installation
Clone the repository and install dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/git-to-b2b-changelog.git](https://github.com/YOUR_USERNAME/git-to-b2b-changelog.git)
cd git-to-b2b-changelog
pip install google-genai PyGithub