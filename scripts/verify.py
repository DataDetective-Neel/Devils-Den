#!/usr/bin/env python3
"""
Verification script to check that all modules are correctly set up.
"""

import sys
from pathlib import Path


def check_file(path: Path, description: str) -> bool:
    """Check if a file exists."""
    if path.exists():
        print(f"✓ {description}: {path}")
        return True
    else:
        print(f"✗ {description}: {path} (missing)")
        return False


def check_directory(path: Path, description: str) -> bool:
    """Check if a directory exists."""
    if path.is_dir():
        print(f"✓ {description}: {path}")
        return True
    else:
        print(f"✗ {description}: {path} (missing)")
        return False


def main():
    """Main verification function."""
    print("="*60)
    print("OpenEnv Course Structure Verification")
    print("="*60)
    
    project_root = Path(__file__).parent.parent
    all_checks_passed = True
    
    # Check main files
    print("\nMain Files:")
    print("-"*60)
    all_checks_passed &= check_file(project_root / "README.md", "Main README")
    all_checks_passed &= check_file(project_root / "requirements.txt", "Requirements")
    
    # Check modules
    for module_num in range(1, 6):
        module_name = f"module-{module_num}"
        print(f"\n{module_name.upper()}:")
        print("-"*60)
        
        module_path = project_root / module_name
        all_checks_passed &= check_directory(module_path, "Module directory")
        all_checks_passed &= check_file(module_path / "README.md", "README")
        all_checks_passed &= check_file(module_path / "notebook.ipynb", "Notebook")
    
    # Check scripts directory
    print("\nScripts:")
    print("-"*60)
    scripts_path = project_root / "scripts"
    all_checks_passed &= check_directory(scripts_path, "Scripts directory")
    all_checks_passed &= check_file(scripts_path / "setup.py", "Setup script")
    all_checks_passed &= check_file(scripts_path / "setup.sh", "Bash setup script")
    
    # Summary
    print("\n" + "="*60)
    if all_checks_passed:
        print("✓ All checks passed!")
        print("="*60)
        print("\nYou're ready to start the course!")
        print("\nRun: python scripts/setup.py")
        print("Or:  bash scripts/setup.sh")
        return 0
    else:
        print("✗ Some checks failed")
        print("="*60)
        print("\nPlease ensure all files are present before starting.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
