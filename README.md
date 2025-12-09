# AI Workforce OS

<p align="center">
  <strong>The Operating System for Human-AI Organizations</strong>
</p>

<p align="center">
  <a href="https://aiworkforceos.org">Website</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#installation">Installation</a> •
  <a href="https://huggingface.co/collections/ekharitonov/ai-workforce-os-recommended-models">Models</a> •
  <a href="https://t.me/pathoflumina">Community</a>
</p>

---

## What is AI Workforce OS?

**AI Workforce OS** is an open-source framework for designing organizations where humans and AI agents collaborate as a unified workforce.

As AI agents become capable of executing complex tasks, organizations face new challenges:

- 🏗️ How to structure hybrid human-AI teams?
- ⚖️ Who is accountable when AI agents make decisions?
- 📋 How to divide work between humans and machines?
- 📊 How to measure productivity of a hybrid workforce?

AI Workforce OS provides the architecture, governance models, and tools to answer these questions.

## Core Components

| Component | Description |
|-----------|-------------|
| **Organizational Architecture** | Structures for hybrid teams (2-5 humans managing 50-100 agents) |
| **Governance & Accountability** | Decision frameworks, escalation patterns, trust tiers |
| **Task Allocation** | Models for dividing work (Type A vs Type B tasks) |
| **Economics & Metrics** | ROI measurement, productivity tracking, cost models |

## Quick Start

### Run in Google Colab (Free, No Setup)

The fastest way to try AI Workforce OS:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ekharitonov/aiworkforceos/blob/main/examples/colab/AI_Workforce_OS_Basic_Crew.ipynb)

### Installation
```bash
# Clone the repository
git clone https://github.com/ekharitonov/aiworkforceos.git
cd aiworkforceos

# Install dependencies
pip install -r requirements.txt

# Set up environment
cp .env.example .env
# Edit .env with your configuration
```

### Recommended Models

All models are **Apache 2.0** licensed — free for commercial use.

| RAM | Model | Performance | Command |
|-----|-------|-------------|---------|
| 8GB | Qwen2.5-3B | Fast, good quality | `ollama pull qwen2.5:3b` |
| 16GB | Qwen2.5-7B | Balanced | `ollama pull qwen2.5:7b` |
| 32GB+ | Qwen2.5-14B | Best quality | `ollama pull qwen2.5:14b` |

> 📚 See full model list: [Hugging Face Collection](https://huggingface.co/collections/ekharitonov/ai-workforce-os-recommended-models)

## Example Use Cases

- **Customer Support Teams**: 3 humans + 20 AI agents handling tier 1-2 support
- **Content Production**: 2 editors + 15 AI writers producing 100+ articles/week
- **Data Analysis**: 1 analyst + 10 AI agents processing reports 24/7
- **Software Development**: 5 developers + 50 AI coding agents

## Project Status

🚧 **Active Development** — This project is in early stages. Expect frequent updates.

- ✅ Core framework
- ✅ Basic examples
- 🔄 Documentation (in progress)
- 📅 Advanced patterns (planned)

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Resources

- 🌐 **Website:** [aiworkforceos.org](https://aiworkforceos.org)
- 📖 **Documentation:** [docs.aiworkforceos.org](https://docs.aiworkforceos.org) *(coming soon)*
- 🤗 **Models:** [Hugging Face Collection](https://huggingface.co/collections/ekharitonov/ai-workforce-os-recommended-models)
- 💬 **Telegram Community:** [@pathoflumina](https://t.me/pathoflumina)
- 🔬 **Research:** [IEEE Collabratec Workspace](https://ieee-collabratec.ieee.org/app/workspaces/10597/AI-Workforce-OS/)

## Citation

If you use AI Workforce OS in your research, please cite:
```bibtex
@software{aiworkforceos2024,
  author = {Kharitonov, Eugene},
  title = {AI Workforce OS: The Operating System for Human-AI Organizations},
  year = {2025},
  url = {https://github.com/ekharitonov/aiworkforceos}
}
```

## License

MIT License — Free for everyone, including commercial use.

## Author

**Eugene Kharitonov**
- LinkedIn: [linkedin.com/in/ekharitonov](https://linkedin.com/in/ekharitonov)
- Telegram: [@pathoflumina](https://t.me/pathoflumina)
- GitHub: [@ekharitonov](https://github.com/ekharitonov)

---

<p align="center">
  <sub>Built for the future of work 🚀</sub>
</p>