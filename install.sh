#!/bin/bash

# MCP Installer Script
# This script installs Stitch MCP and NotebookLM MCP with the same configuration

set -e  # Exit on error

echo "🚀 MCP Installer - Starting installation..."
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if running on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo -e "${RED}❌ This script is designed for macOS only.${NC}"
    exit 1
fi

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
echo -e "${BLUE}📋 Checking prerequisites...${NC}"

if ! command_exists python3; then
    echo -e "${RED}❌ Python3 is not installed. Please install Python3 first.${NC}"
    exit 1
fi

if ! command_exists uv; then
    echo -e "${BLUE}📦 Installing uv (Python package manager)...${NC}"
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

# Create necessary directories
echo -e "${BLUE}📁 Creating directories...${NC}"
mkdir -p "$HOME/.gemini/antigravity"

# Download Stitch proxy script
echo -e "${BLUE}⬇️  Downloading Stitch MCP proxy...${NC}"
curl -fsSL https://raw.githubusercontent.com/tskim81/mcp-installer/main/configs/stitch_proxy.py -o "$HOME/.gemini/antigravity/stitch_proxy.py"

# Install NotebookLM MCP
echo -e "${BLUE}📦 Installing NotebookLM MCP...${NC}"
uv tool install notebooklm-mcp-server

# Download MCP config
echo -e "${BLUE}⬇️  Downloading MCP configuration...${NC}"
curl -fsSL https://raw.githubusercontent.com/tskim81/mcp-installer/main/configs/mcp_config.json -o "$HOME/.gemini/antigravity/mcp_config.json"

echo ""
echo -e "${GREEN}✅ Installation complete!${NC}"
echo ""
echo -e "${BLUE}📝 Installed components:${NC}"
echo "  • Stitch MCP proxy: $HOME/.gemini/antigravity/stitch_proxy.py"
echo "  • NotebookLM MCP: $HOME/.local/share/uv/tools/notebooklm-mcp-server/bin/notebooklm-mcp"
echo "  • MCP Config: $HOME/.gemini/antigravity/mcp_config.json"
echo ""
echo -e "${GREEN}🎉 You can now use Stitch MCP and NotebookLM MCP!${NC}"
