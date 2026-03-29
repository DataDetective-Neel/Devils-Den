# Hugging Face Token Setup Guide

## Why You Need a Token

A Hugging Face token is required for:
- **Module 3:** Deploying environments to HF Spaces
- **Module 4:** Pushing your custom environments
- **Module 5:** Downloading models for training
- Accessing private models or datasets

## Step-by-Step Setup

### 1. Create a Hugging Face Account

If you don't have one already:
- Go to https://huggingface.co/join
- Sign up with email or GitHub

### 2. Generate an Access Token

1. Visit: https://huggingface.co/settings/tokens
2. Click **"New token"**
3. Configure the token:
   - **Name:** `OpenEnv Course` (or any name you prefer)
   - **Type:** Select **"Write"** (allows reading and writing)
   - **Scopes:** Leave defaults (repo read/write)
4. Click **"Generate a token"**
5. **IMPORTANT:** Copy the token immediately! You won't see it again.

### 3. Save Your Token (Choose One Method)

#### Method A: Login via CLI (Recommended)

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Login to Hugging Face
huggingface-cli login

# Paste your token when prompted
# Choose 'y' to add token to git credential helper
```

#### Method B: Use .env File

1. Copy the example file:
   ```bash
   copy .env.example .env  # Windows
   # cp .env.example .env  # Linux/Mac
   ```

2. Edit `.env` and replace `your_token_here` with your actual token:
   ```
   HF_TOKEN=hf_YourActualTokenHere
   ```

3. Load in notebooks:
   ```python
   from dotenv import load_dotenv
   import os
   
   load_dotenv()
   hf_token = os.getenv('HF_TOKEN')
   ```

#### Method C: Set Environment Variable

**Windows PowerShell:**
```powershell
$env:HF_TOKEN = "hf_YourActualTokenHere"
```

**Windows CMD:**
```cmd
set HF_TOKEN=hf_YourActualTokenHere
```

**Linux/Mac:**
```bash
export HF_TOKEN="hf_YourActualTokenHere"
```

### 4. Verify Authentication

Test your token works:

```bash
# Activate virtual environment
venv\Scripts\activate

# Test with Python
python -c "from huggingface_hub import whoami; print(whoami())"
```

You should see your username and account info!

## When You Need the Token

### Module 3: Deploying Environments
```bash
# Login first
huggingface-cli login

# Then deploy
cd my-environment
openenv push --repo-id username/my-env
```

### Module 5: Training
```python
from transformers import AutoModelForCausalLM

# Token loaded automatically if you used 'huggingface-cli login'
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-1.5B-Instruct",
    token=True  # Uses stored token
)
```

## Security Best Practices

✓ **DO:**
- Keep your token secret
- Use `.env` files (already in `.gitignore`)
- Use write tokens only when needed
- Regenerate tokens if compromised

✗ **DON'T:**
- Commit tokens to git
- Share tokens publicly
- Hardcode tokens in notebooks
- Use the same token for everything

## Token Scopes

| Scope | What You Can Do | Needed For |
|-------|-----------------|------------|
| **Read** | Download public/private models | Module 5 (if using private models) |
| **Write** | Upload models, create repos, push to Spaces | Modules 3, 4, 5 |
| **Manage** | Delete repos, manage org permissions | Not needed for course |

For this course, **Write** scope is recommended.

## Troubleshooting

### "Invalid token" error
- Check you copied the entire token (starts with `hf_`)
- Ensure no extra spaces
- Try generating a new token

### "Permission denied" error
- Make sure you're using a **Write** token, not Read-only
- Check you're authenticated: `huggingface-cli whoami`

### Token not found
- Re-run `huggingface-cli login`
- Check `.env` file exists and is in project root
- Verify environment variable is set: `echo $HF_TOKEN`

## Need Help?

- Hugging Face Docs: https://huggingface.co/docs/hub/security-tokens
- Course README: [README.md](README.md)
- Getting Started: [GETTING_STARTED.md](GETTING_STARTED.md)

---

**Ready?** Get your token from https://huggingface.co/settings/tokens and continue with Module 1!
