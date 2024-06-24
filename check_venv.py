import sys

if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    print("Virtual environment is active.")
else:
    print("Virtual environment is NOT active.")
    sys.exit(1)  # Exit with a non-zero status to fail the step
