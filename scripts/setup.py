#!/usr/bin/env python3
"""
Setup script for OpenEnv course.
Creates virtual environment and installs all dependencies.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, check=True):
    """Run a shell command and print output."""
    print(f"Running: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}", file=sys.stderr)
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr, file=sys.stderr)
        return False


def main():
    """Main setup function."""
    print("="*60)
    print("OpenEnv Course Setup")
    print("="*60)
    
    # Check Python version
    if sys.version_info < (3, 10):
        print("Error: Python 3.10+ is required")
        sys.exit(1)
    
    print(f"\nPython version: {sys.version}")
    
    # Get project root
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print(f"\nProject root: {project_root}")
    
    # Create virtual environment
    print("\n" + "="*60)
    print("Creating virtual environment...")
    print("="*60)
    
    venv_path = project_root / "venv"
    
    if venv_path.exists():
        print(f"Virtual environment already exists at {venv_path}")
        response = input("Recreate? (y/N): ").strip().lower()
        if response == 'y':
            print("Removing existing venv...")
            import shutil
            shutil.rmtree(venv_path)
        else:
            print("Using existing venv")
    
    if not venv_path.exists():
        if not run_command([sys.executable, "-m", "venv", str(venv_path)]):
            print("Failed to create virtual environment")
            sys.exit(1)
    
    # Determine pip path
    if sys.platform == "win32":
        pip_path = venv_path / "Scripts" / "pip.exe"
        python_path = venv_path / "Scripts" / "python.exe"
    else:
        pip_path = venv_path / "bin" / "pip"
        python_path = venv_path / "bin" / "python"
    
    # Upgrade pip
    print("\n" + "="*60)
    print("Upgrading pip...")
    print("="*60)
    
    if not run_command([str(python_path), "-m", "pip", "install", "--upgrade", "pip"]):
        print("Warning: Failed to upgrade pip")
    
    # Install requirements
    print("\n" + "="*60)
    print("Installing dependencies...")
    print("="*60)
    
    requirements_file = project_root / "requirements.txt"
    if not requirements_file.exists():
        print(f"Error: {requirements_file} not found")
        sys.exit(1)
    
    if not run_command([str(pip_path), "install", "-r", str(requirements_file)]):
        print("Failed to install dependencies")
        sys.exit(1)
    
    # Success message
    print("\n" + "="*60)
    print("Setup Complete!")
    print("="*60)
    print("\nTo activate the virtual environment:")
    
    if sys.platform == "win32":
        print(f"  {venv_path}\\Scripts\\activate")
    else:
        print(f"  source {venv_path}/bin/activate")
    
    print("\nTo run Jupyter notebooks:")
    print("  jupyter notebook")
    
    print("\nTo start a module:")
    print("  cd module-1")
    print("  jupyter notebook notebook.ipynb")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    main()
