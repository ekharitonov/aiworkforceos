# 🤖 Mini Content Agency - Demo

## Overview

This is a working prototype of an AI-powered content agency demonstrating the **AI Workforce OS** framework.

**Team Structure:** 2 Humans + 5 AI Agents

### Human Roles:
- **CEO (You)** - Set tasks, approve results
- **Editor** - Quality control, final approval

### AI Agent Roles:
1. **Research Analyst** 🔬 - Gathers information and data
2. **Content Writer** ✍️ - Creates articles and content
3. **SEO Specialist** 🎯 - Optimizes for search engines
4. **Social Media Manager** 📱 - Creates social posts
5. **QA Checker** ✅ - Quality assurance and error checking

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Get your API key at: https://platform.openai.com

### 3. Run the UI

```bash
python simple_ui.py
```

Open in browser: http://localhost:7860

## Available Workflows

### 📝 Create Article
**Agents:** Research Analyst → Content Writer → SEO Specialist → QA Checker

**Input:**
- Topic
- Target audience
- Word count

**Output:** Complete, optimized, quality-checked article

**Time:** ~5-10 minutes

---

### 📱 Social Media Campaign
**Agents:** Research Analyst → Social Media Manager → QA Checker

**Input:**
- Campaign topic
- Target platforms

**Output:** Platform-specific posts ready to publish

**Time:** ~3-5 minutes

---

### 🎯 Optimize Content
**Agents:** SEO Specialist → Content Writer → QA Checker

**Input:**
- Existing content

**Output:** SEO-optimized version with improvements

**Time:** ~3-5 minutes

## Cost Estimates

Using GPT-3.5-turbo:
- **Article Creation:** ~$0.10-0.15
- **Social Campaign:** ~$0.05-0.08
- **Content Optimization:** ~$0.08-0.12

Using local models (Ollama):
- **All workflows:** FREE (runs on your computer)

## Architecture

### Role Hierarchy

```
CEO (Human)
    ↓
Editor (Human)
    ↓
    ├─ Research Analyst (AI)
    ├─ Content Writer (AI) 
    ├─ SEO Specialist (AI)
    ├─ Social Media Manager (AI)
    └─ QA Checker (AI)
```

### Workflow Example: Article Creation

```
1. Research Analyst
   ↓ (research findings)
2. Content Writer
   ↓ (draft article)
3. SEO Specialist
   ↓ (optimized version)
4. QA Checker
   ↓ (final approved article)
5. Editor (Human) reviews
```

## Files Structure

```
demo_company/
├── requirements.txt       # Dependencies
├── roles.py              # AI agent role definitions
├── workflow.py           # Task orchestration
├── simple_ui.py          # Gradio web interface
├── .env                  # API keys (create this)
└── README.md            # This file
```

## Using Local Models (Advanced)

Want to run for FREE without OpenAI? Use Ollama:

### 1. Install Ollama

```bash
# macOS/Linux
curl -fsSL https://ollama.com/install.sh | sh

# Or download from: https://ollama.com
```

### 2. Pull a Model

```bash
# Recommended models:
ollama pull qwen2.5:7b        # 16GB RAM
ollama pull qwen2.5:3b        # 8GB RAM
```

### 3. Update Code

In `simple_ui.py`, replace the `get_llm()` function:

```python
def get_llm():
    from langchain_community.llms import Ollama
    return Ollama(model="qwen2.5:7b")
```

## Customization

### Add New Agent

In `roles.py`:

```python
@staticmethod
def your_new_role(llm: Optional[object] = None) -> Agent:
    return Agent(
        role='Your Role Name',
        goal='What this agent does',
        backstory='Agent background and expertise',
        llm=llm,
        verbose=True
    )
```

### Create New Workflow

In `workflow.py`:

```python
def your_workflow(self, input_params):
    # Define tasks
    task1 = Task(...)
    task2 = Task(...)
    
    # Create crew
    crew = Crew(agents=[...], tasks=[...])
    
    # Run
    return crew.kickoff()
```

## Production Deployment

For production use:

1. **Scale up:** Add more agents for parallel processing
2. **Add monitoring:** Track task completion, costs, errors
3. **Human oversight:** Add approval steps for critical tasks
4. **Quality gates:** Implement scoring thresholds
5. **Version control:** Track agent performance over time

## Troubleshooting

### "Please set OPENAI_API_KEY"
- Create `.env` file with your API key
- Restart the application

### "Agency not initialized"
- Click "Initialize Agency" button in the UI
- Check that your API key is valid

### Slow performance
- Using GPT-4? Switch to GPT-3.5-turbo
- Consider using local models with Ollama

### High costs
- Reduce word counts
- Use GPT-3.5-turbo instead of GPT-4
- Switch to free local models

## Next Steps

1. **Try all workflows** to understand agent collaboration
2. **Customize roles** to fit your specific needs
3. **Create new workflows** for your use cases
4. **Scale up** by adding more specialized agents
5. **Measure ROI** by tracking time and cost savings

## Learn More

- 🌐 **Website:** [aiworkforceos.org](https://aiworkforceos.org)
- 💬 **Community:** [Telegram](https://t.me/pathoflumina)
- 🤗 **Models:** [Hugging Face Collection](https://huggingface.co/collections/ekharitonov/ai-workforce-os-recommended-models)
- 📚 **GitHub:** [ekharitonov/aiworkforceos](https://github.com/ekharitonov/aiworkforceos)

---

**Built with AI Workforce OS** | MIT License
