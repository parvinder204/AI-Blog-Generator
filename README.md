# 🧠 AI Blog Generator

An intelligent, SEO-friendly blog content generator built using **Flask**, **OpenAI**, and **Tailwind CSS**. This web application allows users to enter a prompt and receive a fully generated blog article within seconds — ideal for marketers, bloggers, and content creators.

---

## 🚀 Features

- 🔥 Generates human-like blog content using OpenAI
- 🎯 SEO-optimized writing style prompt
- 📐 Fully responsive UI with Tailwind CSS
- 🖱️ Simple user interface with auto-resizing inputs
- 📦 Easy integration and customizable prompt logic


## 🛠️ Tech Stack

| Technology    | Role                          |
|---------------|-------------------------------|
| Flask         | Python backend & routing      |
| OpenAI        | AI content generation         |
| Tailwind CSS  | Responsive frontend styling   |
| HTML + JS     | UI and frontend logic         |


## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-blog-generator.git
cd ai-blog-generator
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-openai-api-key
```

Or export it directly:

```bash
export OPENAI_API_KEY=your-openai-api-key
```

### 5. Run the Flask App

```bash
python main.py
```

Visit `http://localhost:5000` in your browser.

---


## ✅ To-Do / Improvements

- [ ] Add login/authentication
- [ ] Generate full blog with headers, images, etc.
- [ ] Export as PDF or copy-to-clipboard
- [ ] Deploy on Vercel or Render

---

## 🙌 Credits

Built by [Parvinder Singh].

---

## 📄 License

This project is licensed under the MIT License.
