# 🚀 Git-to-B2B Changelog Generator

A specialized Python automation tool designed to bridge the gap between engineering updates and B2B marketing. It extracts raw git commit logs using PyGithub and transforms them into high-converting, executive-ready product announcements using Google's gemini-2.5-flash model.

---

## 📋 Overview

* 🏷️ **Project Name:** Git-to-B2B Changelog Generator
* 💡 **What It Does:** Automates the extraction of raw GitHub commit logs and translates technical development updates into polished, value-focused B2B changelogs and executive product announcements.
* 🚨 **Problems It Solves:** Bridges the communication gap between engineering and marketing teams, eliminates manual translation of dense code commits into business value, and ensures enterprise stakeholders receive clear ROI-focused product updates instantly.

---

## 📌 Problem & Solution (STAR Framework)

* 🏢 *Situation:* B2B software companies ship updates constantly, but critical features remain invisible to enterprise clients because non-technical marketing teams struggle to translate dense engineering jargon into business value.
* 🎯 *Task:* Build an automated AI pipeline that continuously ingests raw technical commit logs and translates them into structured, value-driven B2B posts for executive buyers and stakeholders.
* ⚡ *Action:* Developed a Python backend leveraging PyGithub for commit extraction and integrated Google's gemini-2.5-flash via the google-genai SDK to parse, categorize, and format technical updates into ROI-focused content.
* 📈 *Result:* Reduced B2B product changelog and social content creation time from hours to seconds while maintaining high technical accuracy and strategic business messaging.

---

## ✨ Key Features

* 📦 *Automated Data Extraction:* Seamlessly fetches recent commits from any public GitHub repository via PyGithub.
* 🧠 *Value-Oriented AI Processing:* Leverages Gemini 2.5 Flash to automatically extract business impact, ROI, and user benefits over pure code syntax.
* 📄 *Structured Output Generation:* Formats outputs into clean headlines, strategic business impact highlights, engineering updates, and clear calls-to-action (CTAs).

---

## 🛠️ Tech Stack & Dependencies

* 🐍 *Language:* Python 3.9+
* 🤖 *AI Engine:* Google GenAI SDK (gemini-2.5-flash)
* 🐙 *API Integration:* PyGithub (GitHub REST API Wrapper)

---

## 🚀 Getting Started

### 1. 📥 Installation
Clone the repository and install the required packages:
```bash
git clone [https://github.com/YOUR_USERNAME/git-to-b2b-changelog.git](https://github.com/YOUR_USERNAME/git-to-b2b-changelog.git)
cd git-to-b2b-changelog
pip install google-genai PyGithub