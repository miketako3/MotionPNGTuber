$ErrorActionPreference = "Stop"

# Local build helper for Windows
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
  Write-Error "uv is not installed. See README.md for setup." 
  exit 1
}

uv sync --frozen --preview-features extra-build-dependencies
uv pip install pyinstaller==6.10.0
uv run pyinstaller MotionPNGTuber.spec
