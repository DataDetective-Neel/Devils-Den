# Getting Started with OpenEnv Course

## Project Structure

```
openenv-course/
├── README.md                    # Main course overview
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore file
├── venv/                        # Virtual environment (already set up!)
├── module-1/                    # Why OpenEnv?
│   ├── README.md
│   └── notebook.ipynb
├── module-2/                    # Using Existing Environments
│   ├── README.md
│   └── notebook.ipynb
├── module-3/                    # Deploying Environments
│   ├── README.md
│   └── notebook.ipynb
├── module-4/                    # Building Your Own Environment
│   ├── README.md
│   └── notebook.ipynb
├── module-5/                    # Training with OpenEnv + TRL
│   ├── README.md
│   └── notebook.ipynb
└── scripts/                     # Helper scripts
    ├── setup.py                 # Automated setup
    ├── setup.sh                 # Bash setup script
    └── verify.py                # Verify structure
```

## Quick Start

### 1. Activate the Virtual Environment

The virtual environment is already created and dependencies are installed!

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 2. Start Jupyter

```bash
jupyter notebook
```

### 3. Begin with Module 1

Navigate to `module-1/notebook.ipynb` and start learning!

## Module Overview

| Module | Topic | Duration | Key Concepts |
|--------|-------|----------|--------------|
| 1 | Why OpenEnv? | 45-60 min | RL loop, OpenEnv architecture, 3-method interface |
| 2 | Using Existing Environments | 45-60 min | Environment Hub, type-safe models, writing policies |
| 3 | Deploying Environments | 45-60 min | Local dev, Docker, HF Spaces deployment |
| 4 | Building Your Own Environment | 45-60 min | 3-component pattern, scaffolding, custom logic |
| 5 | Training with OpenEnv + TRL | 45-60 min | GRPO, reward functions, LLM training |

## Prerequisites

- Python 3.10+ ✓
- Basic Python knowledge
- Familiarity with Hugging Face ecosystem (helpful)
- No RL experience required

## Hardware Requirements

- **Modules 1-4:** Any computer (CPU only)
- **Module 5:** A100 40GB GPU recommended (Google Colab Pro or similar)

## Getting Help

If you encounter any issues:

1. Check the module README for concepts
2. Review the notebook comments
3. Ensure your virtual environment is activated
4. Check that all dependencies are installed:
   ```bash
   pip list
   ```

## Next Steps

1. Read the main [README.md](../README.md)
2. Start with [Module 1](../module-1/README.md)
3. Work through each module in order
4. Complete the exercises in the notebooks
5. Build your own environment!

## What You'll Learn

By the end of this course, you'll be able to:

- ✓ Connect to and use OpenEnv environments
- ✓ Write policies for RL tasks
- ✓ Deploy environments locally and to the cloud
- ✓ Build custom RL environments from scratch
- ✓ Train LLMs using GRPO and environment feedback

## Resources

- [OpenEnv GitHub](https://github.com/meta-pytorch/OpenEnv)
- [Environment Hub Collection](https://huggingface.co/collections/openenv/environment-hub)
- [TRL Documentation](https://huggingface.co/docs/trl)
- [Hugging Face Hub](https://huggingface.co)

---

**Ready to get started?** Open `module-1/notebook.ipynb` and dive in!
